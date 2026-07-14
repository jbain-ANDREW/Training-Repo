# Python & GitHub Setup

GitHub is how the software world shares and manages code. This repo teaches you the core workflow — clone, branch, commit, pull request — by having you build something real that gets published to the web.

## What You Will Learn

- Setting up VS Code with Git
- Cloning a repository
- Creating a branch
- Making and committing changes
- Opening a Pull Request

## Getting Started

### 1. Install the Tools

- **Git**: https://git-scm.com/downloads
- **VS Code**: https://code.visualstudio.com/

Inside VS Code, install the extension **GitHub Pull Requests** (search in the Extensions panel).

### 2. Clone This Repo

Open a terminal in VS Code (`Ctrl+`` `) and run:

```bash
git clone https://github.com/jbain-ANDREW/Training-Repo.git
cd Training-Repo
```

### 3. Confirm You Have Push Access

You can clone and read this repo without any special access, but **pushing requires write (collaborator) access**. Confirm before you get to the push step, or you will hit a 403 error.

To check: try running `git push` on a test branch, or look for your GitHub username in the repo's collaborator list. If you are not listed or the push fails, file a GitHub Issue:

1. Go to [github.com/jbain-ANDREW/Training-Repo/issues](https://github.com/jbain-ANDREW/Training-Repo/issues)
2. Open a new issue titled **"Access request — \<your GitHub username\>"**
3. Include your GitHub username in the body

Issues are reviewed regularly and access is granted so you can see other students' progress as the archive grows.

### 4. Do the Exercise

See the [GitHub Pages site](https://jbain-ANDREW.github.io/Training-Repo) for full exercise instructions.

The short version:

```bash
# Create your own branch (use your real name)
git checkout -b firstname-lastname

# Copy the template
cp exercises/splash-page/template.html docs/splash-pages/firstname-lastname.html

# Edit the file in VS Code, then commit
git add docs/splash-pages/firstname-lastname.html
git commit -m "Add splash page: Firstname Lastname"
git push origin firstname-lastname
```

Then open a Pull Request on GitHub. Once it's reviewed and merged, your page will appear in the archive.

## Rules

- Only add or edit files inside `docs/splash-pages/` — nothing else.
- One file per student, named `firstname-lastname.html`.
- Changes outside `docs/splash-pages/` will not be accepted.

## Assets / Screenshots

Screenshots and images used in the docs live in `assets/images/`.

| File | Path | Notes |
|---|---|---|
| `Screenshot 2026-04-26 154405.jpg` | `assets/images/` | Currently loose in repo root — move here |

**Naming convention for new screenshots:** `topic-description.png`, e.g. `github-clone-dialog.png`, `vscode-extensions-panel.png`.

Save new screenshots to:
```
assets/images/your-filename.png
```
