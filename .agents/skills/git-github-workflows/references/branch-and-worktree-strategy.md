# Branch & Worktree Strategy Guide

## Branch Lifecycle

1. **Keep Branches Short-Lived**:
   - Merge branches within 1–3 days to prevent diverging too far from `main` and minimize integration debt.
2. **Never Commit Directly to Main**:
   - Protect `main` / `master` with branch protection rules requiring status checks and code reviews.
3. **Always Rebase, Don't Blind-Merge**:
   - Rebase feature branches onto latest `origin/main` before opening PRs to preserve a linear history:
     ```bash
     git checkout feat/my-feature
     git fetch origin
     git rebase origin/main
     ```

## Git Worktree for High-Productivity Context Switching

When you need to fix an urgent bug without disturbing your ongoing uncommitted work, do not rely on fragile `git stash`. Use `git worktree`:

### 1. Create a parallel workspace directory
```bash
# Creates a new directory at ../hotfix-login linked to hotfix/login-crash branch
git worktree add -b hotfix/login-crash ../hotfix-login main
```

### 2. Work in the new worktree
```bash
cd ../hotfix-login
# Make changes, run tests, commit
git commit -m "fix(auth): prevent null crash during login"
git push origin hotfix/login-crash
```

### 3. Cleanup worktree when finished
```bash
cd ../my-main-project
git worktree remove ../hotfix-login
```
