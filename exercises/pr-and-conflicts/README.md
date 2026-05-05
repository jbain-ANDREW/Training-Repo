# Pull Requests and Merge Conflicts Lab

Two-part exercise for ECE — Build With AI.

**Full instructions and concept explanation on the course site:**
[pr-lab.html](https://jbain-ANDREW.github.io/Training-Repo/pr-lab.html)

---

## Part 1 — Open a Pull Request

Add your name to `shared-file.py` using the standard branch → commit → PR workflow.

1. Create your branch:
   ```
   git checkout -b firstname-lastname
   ```
2. Open `exercises/pr-and-conflicts/shared-file.py`
3. Add one line to the `participants` list — your name and one word that describes you:
   ```python
   "Firstname Lastname : one_word",
   ```
4. Commit:
   ```
   git add exercises/pr-and-conflicts/shared-file.py
   git commit -m "Add Firstname Lastname to participants"
   ```
5. Push:
   ```
   git push origin firstname-lastname
   ```
6. Go to GitHub and open a Pull Request — base: `main`, compare: `firstname-lastname`

---

## Part 2 — Resolve a Merge Conflict

The `conflict-setup` branch has a different `motto` line than `main`.
Merging creates a conflict you need to resolve by hand.

1. Check out the conflict branch:
   ```
   git checkout conflict-setup
   ```
2. Merge main into it:
   ```
   git merge main
   ```
   Git will report a conflict in `shared-file.py`.
3. Open `exercises/pr-and-conflicts/shared-file.py` — look for the `<<<<<<<` markers
4. Decide which motto to keep (or write a new one), then remove all conflict markers
5. Save the file, then:
   ```
   git add exercises/pr-and-conflicts/shared-file.py
   git commit -m "Resolve motto conflict"
   git push origin conflict-setup
   ```
6. Open a Pull Request on GitHub — base: `main`, compare: `conflict-setup`

---

See `INSTRUCTOR.md` in this folder for setup and reset instructions.
