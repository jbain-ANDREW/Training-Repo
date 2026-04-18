# ECE GitHub Training Repo

Welcome! This repository is your hands-on introduction to Git and GitHub.

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

### 3. Do the Exercise

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
