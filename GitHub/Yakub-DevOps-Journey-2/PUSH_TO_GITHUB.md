# Pushing this repo to github.com/paragonadey

Run these from the unzipped `yaco-devops-journey/` folder.

## 1. Create the empty repo on GitHub

Go to https://github.com/new and create a repository named **yaco-devops-journey** under
the **paragonadey** account. Do **not** tick "Add a README", "Add .gitignore" or
"Choose a license" — this repo already has them and an initialised repo causes a
merge conflict on the first push.

## 2. Check nothing secret is about to be committed

Do this BEFORE the first commit, not after.

```bash
cat .gitignore                       # confirm it exists and is not empty
grep -rIiE "AKIA[0-9A-Z]{16}|password *= *[\"'][^\"'{$]|BEGIN RSA PRIVATE KEY" . || echo "clean"
```

**Expected:** the word `clean`. If anything else prints, remove it before continuing.

## 3. Initialise and push

```bash
git init
git branch -M main
git add .
git status                           # READ THIS. No .pem, .env, .tfstate or kubeconfig.
git commit -m "Initial commit: 60-day DevOps journey scaffold"
git remote add origin https://github.com/paragonadey/yaco-devops-journey.git
git push -u origin main
```

**What `git status` before committing does:** shows exactly what is staged.
**Why:** it is the last cheap moment to catch a secret. After `git push`, a leaked
credential is compromised and must be rotated, not just deleted.

## 4. If the push is rejected

`Updates were rejected because the remote contains work that you do not have locally` means
the GitHub repo was created with a README. Either delete and recreate it empty, or:

```bash
git pull --rebase origin main
git push -u origin main
```

## 5. Authentication

GitHub no longer accepts account passwords over HTTPS. Use either:

- **A personal access token** — github.com → Settings → Developer settings → Personal
  access tokens → Fine-grained tokens. Give it `Contents: Read and write` on this one repo
  only. Paste it when git prompts for a password. Do not paste it into any file.
- **SSH** — `ssh-keygen -t ed25519 -C "your@email"`, add the `.pub` key to GitHub, then use
  `git remote set-url origin git@github.com:paragonadey/yaco-devops-journey.git`.

## 6. Daily habit from here

```bash
git add .
git commit -m "Week 1 Day 3: ELB hands-on, target group health check fix"
git push
```

Commit messages that say what changed and why beat "update" every time. A recruiter
scrolling your commit history is reading a diary of how you think.
