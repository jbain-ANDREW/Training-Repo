#!/usr/bin/env python3
"""
Fetch GitHub Issues — Training-Repo

Fetches all GitHub issues (open and closed) with complete details and writes to JSON.
Claude can then read the JSON and suggest fixes.

Usage:
    python fetch_issues.py

Requirements:
    - PyGithub: pip install PyGithub
    - GitHub Personal Access Token in GITHUB_TOKEN env var
      (get from https://github.com/settings/tokens → Personal access tokens)

Output:
    - issues.json (all issues with full details)
    - issues_summary.md (markdown summary for easy reading)
"""

import os
import json
from datetime import datetime
from github import Github, GithubException

# Configuration
REPO_OWNER = "jbain-ANDREW"
REPO_NAME = "Training-Repo"
OUTPUT_FILE = "issues.json"
SUMMARY_FILE = "issues_summary.md"

def get_github_client():
    """Create GitHub client from GITHUB_TOKEN env var."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError(
            "GITHUB_TOKEN not found. Set it:\n"
            "  PowerShell: $env:GITHUB_TOKEN = 'ghp_...'\n"
            "  Bash: export GITHUB_TOKEN='ghp_...'\n\n"
            "Get token at: https://github.com/settings/tokens"
        )
    return Github(token)

def fetch_issues():
    """Fetch all issues (open + closed) with full details."""
    gh = get_github_client()
    repo = gh.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
    
    print(f"Fetching issues from {REPO_OWNER}/{REPO_NAME}...")
    
    all_issues = []
    
    # Get both open and closed issues
    for state in ["open", "closed"]:
        print(f"  Fetching {state} issues...")
        issues = repo.get_issues(state=state)
        
        for issue in issues:
            issue_data = {
                "number": issue.number,
                "title": issue.title,
                "state": issue.state,
                "body": issue.body,
                "url": issue.html_url,
                "created_at": issue.created_at.isoformat(),
                "updated_at": issue.updated_at.isoformat(),
                "closed_at": issue.closed_at.isoformat() if issue.closed_at else None,
                "assignee": issue.assignee.login if issue.assignee else None,
                "labels": [label.name for label in issue.labels],
                "comments": issue.comments,
                "comments_list": []
            }
            
            # Fetch all comments for this issue
            if issue.comments > 0:
                for comment in issue.get_comments():
                    issue_data["comments_list"].append({
                        "author": comment.user.login,
                        "body": comment.body,
                        "created_at": comment.created_at.isoformat(),
                    })
            
            all_issues.append(issue_data)
            print(f"    #{issue.number}: {issue.title[:60]}")
    
    return all_issues

def save_to_json(issues):
    """Save issues to JSON file."""
    with open(OUTPUT_FILE, "w") as f:
        json.dump(issues, f, indent=2)
    print(f"\n✓ Saved {len(issues)} issues to {OUTPUT_FILE}")

def save_to_markdown(issues):
    """Save issues summary to markdown file."""
    open_count = sum(1 for i in issues if i["state"] == "open")
    closed_count = len(issues) - open_count
    
    md_lines = [
        "# Training-Repo GitHub Issues",
        f"\nFetched: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\n**Summary:** {open_count} open · {closed_count} closed · {len(issues)} total\n",
        "---\n",
    ]
    
    # Open issues first
    if open_count > 0:
        md_lines.append("## 🔴 Open Issues\n")
        for issue in sorted([i for i in issues if i["state"] == "open"], key=lambda x: x["number"]):
            md_lines.extend(_format_issue_md(issue))
        md_lines.append("\n")
    
    # Closed issues
    if closed_count > 0:
        md_lines.append("## ✅ Closed Issues\n")
        for issue in sorted([i for i in issues if i["state"] == "closed"], key=lambda x: x["number"]):
            md_lines.extend(_format_issue_md(issue))
    
    with open(SUMMARY_FILE, "w") as f:
        f.write("\n".join(md_lines))
    print(f"✓ Saved markdown summary to {SUMMARY_FILE}")

def _format_issue_md(issue):
    """Format a single issue as markdown."""
    lines = [
        f"### #{issue['number']}: {issue['title']}",
        f"- **State:** {issue['state'].upper()}",
        f"- **Assignee:** {issue['assignee'] or '(unassigned)'}",
        f"- **Labels:** {', '.join(issue['labels']) if issue['labels'] else '(none)'}",
        f"- **Created:** {issue['created_at']}",
        f"- **Comments:** {issue['comments']}",
        f"- **URL:** {issue['url']}",
    ]
    
    if issue["body"]:
        lines.append(f"\n**Description:**\n```\n{issue['body']}\n```")
    
    if issue["comments_list"]:
        lines.append(f"\n**Comments ({len(issue['comments_list'])}):**")
        for comment in issue["comments_list"]:
            lines.append(f"- **{comment['author']}** ({comment['created_at']}): {comment['body'][:100]}...")
    
    lines.append("")
    return lines

def main():
    """Fetch issues and save to files."""
    try:
        issues = fetch_issues()
        save_to_json(issues)
        save_to_markdown(issues)
        print(f"\n✅ Done! Read the JSON or markdown summary, then ask Claude to help fix the issues.")
    except GithubException as e:
        print(f"❌ GitHub error: {e}")
    except ValueError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
