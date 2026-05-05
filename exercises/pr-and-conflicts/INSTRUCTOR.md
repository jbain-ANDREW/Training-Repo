# Instructor Guide — Pull Requests and Merge Conflicts Lab

## One-time setup (do this before running the lab for the first time)

`shared-file.py` is already on `main` with the instructor participant entry.
You just need to create and push the `conflict-setup` branch:

```
cd Training-Repo
git checkout main
git checkout -b conflict-setup
```

Edit `exercises/pr-and-conflicts/shared-file.py` — change the motto line to:
```python
motto = "if it compiles, ship it"
```

Commit and push:
```
git add exercises/pr-and-conflicts/shared-file.py
git commit -m "conflict-setup: alternative motto for Part 2"
git push origin conflict-setup
```

Return to main:
```
git checkout main
```

The repo now has two branches with diverging `motto` lines — the conflict is ready.

---

## Running Part 1

Students branch from `main`, add their name to `participants`, push, and open a PR.
Each PR is independent — merge them in any order once the format looks right.

If two students submit at the same time and GitHub shows a merge conflict in the PR
(because both added to the end of the list), have each student pull and rebase:
```
git checkout firstname-lastname
git pull origin main --rebase
git push origin firstname-lastname --force-with-lease
```

---

## Running Part 2

Students check out `conflict-setup` locally, run `git merge main`, and resolve the
`motto` conflict in `shared-file.py`. Each student can either:

**Option A (shared branch):** All students work on `conflict-setup` itself. Simple,
but they may see each other's in-progress states.

**Option B (individual branches, recommended):** Each student creates their own branch
off `conflict-setup`:
```
git checkout -b firstname-lastname-conflict origin/conflict-setup
git merge main
```
They resolve the conflict, push their branch, and open a PR targeting `conflict-setup`
(not `main`). Keeps each student's work isolated.

---

## Resetting between class sections

The `participants` list grows across runs. Before a new section, trim it back to
just the instructor line:

```
git checkout main
```

Edit `shared-file.py` — remove all student entries, leave only:
```python
participants = [
    "James Bain  : builder",        # instructor
]
```

Commit and push:
```
git add exercises/pr-and-conflicts/shared-file.py
git commit -m "Reset participants for new section"
git push origin main
```

The `conflict-setup` branch does not need to be reset — it only has the motto change,
which students resolve locally each time.

---

## Doing the lab yourself (instructor demo)

You can fully participate in Part 1 — just add a second entry after the instructor
placeholder (or use a different name). The PR you open will be live on GitHub and
can serve as an example for students to see what a real PR looks like.

For Part 2, checking out `conflict-setup` and merging `main` (after a few student
PRs have been merged) will show a genuine multi-entry conflict, making it a richer
demo than what any individual student sees.
