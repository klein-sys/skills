---
name: git-github-workflows
description: >-
  Use this skill when staging, committing, branching, rebasing, opening pull requests, or resolving merge
  conflicts in Git and GitHub. Enforces conventional commit messages, atomic commit hygiene, safe rebase
  practices, git worktrees, and PR readiness reviews.
---

# Git & GitHub Workflows

This skill guides you through production-grade version control practices. It ensures clean, bisectable commit histories, predictable release management via Conventional Commits, safe branch coordination, and polished GitHub Pull Requests.

---

## When to Activate This Skill

- When creating branches or switching contexts across tasks.
- When staging changes, writing commit messages, or squashing WIP commits.
- When synchronizing with upstream branches (`git rebase` / `git merge`) and resolving conflicts.
- When opening or updating Pull Requests (PRs) and generating release notes.
- When managing multiple concurrent feature branches without stashing chaos (using `git worktree`).

---

## Core Version Control Workflow

```
[Create Feature Branch / Worktree]
               │
               ▼
   [Atomic Implementation Loop]
               │
               ▼
[Atomic Conventional Commits]
               │
               ▼
[Rebase onto Upstream main]
               │
               ▼
[Pre-PR Self-Review & Verification]
               │
               ▼
 [Publish PR with Semantic Summary]
```

### 1. Branch Strategy & Worktree Isolation
- **Branch Naming**: Use prefixed kebab-case:
  - `feat/user-authentication`
  - `fix/token-expiration-race`
  - `refactor/extract-database-client`
  - `docs/api-getting-started`
- **Worktree for Parallel Tasks**:
  Instead of stash thrashing, create an isolated worktree:
  ```bash
  git worktree add ../my-feature-branch feat/my-feature
  ```
  See [Branch & Worktree Strategy](./references/branch-and-worktree-strategy.md).

### 2. Atomic Commits & Hygiene
- **One Conceptual Change Per Commit**:
  - Never bundle unrelated formatting, dependency updates, and feature changes into a single commit.
  - Keep commits small, self-contained, and buildable (every commit should compile and pass tests).
- **Stage Precisely**:
  - Review diffs before staging: `git diff`
  - Stage selectively: `git add -p` or specific file paths. Never use blind `git add .` without checking untracked files.

### 3. Conventional Commit Standard
Every commit message must follow the Conventional Commits specification:
```
<type>(<optional scope>): <imperative description>

[optional body explaining rationale, trade-offs, and context]

[optional footer: Closes #123, BREAKING CHANGE: ...]
```
Allowed types: `feat`, `fix`, `refactor`, `test`, `docs`, `perf`, `chore`, `ci`, `build`.
See [Conventional Commits Reference](./references/conventional-commits.md).

### 4. Synchronization & Safe Rebasing
- Synchronize with the main development branch regularly:
  ```bash
  git fetch origin
  git rebase origin/main
  ```
- **Conflict Resolution Protocol**:
  1. Inspect status: `git status`.
  2. Resolve conflicts in files deliberately; check for accidental loss of either branch's logic.
  3. Run tests immediately after resolving conflicts to verify functionality.
  4. Continue rebase: `git rebase --continue`.
  5. Never use `--force` on shared protected branches (`main`, `master`, `release`). Use `--force-with-lease` only on your personal feature branch if rebased.

### 5. Pull Request Preparation & Polish
Before opening a PR, execute the pre-PR verification:
- `git status` is clean.
- All unit and integration tests pass.
- Linter and formatter pass without warnings.
- Fill out the PR template with clear context, testing steps, and screenshots if UI changes were made.
See [PR Template & Checklist](./examples/pr-template-and-checklist.md).

---

## References & Guides

- [Conventional Commits Cheat Sheet](./references/conventional-commits.md)
- [Branching & Worktree Strategy Guide](./references/branch-and-worktree-strategy.md)
- [Pull Request Template & Review Checklist](./examples/pr-template-and-checklist.md)

---

## Verification Checklist

Before pushing or requesting review:

- [ ] Commit history is linear, clean, and free of "WIP", "temp", or accidental merge commits.
- [ ] No secrets, `.env` files, temporary artifacts, or large binary files are tracked.
- [ ] Every commit message follows the `type(scope): imperative summary` syntax.
- [ ] Branch is rebased cleanly onto the target base branch with no merge conflicts.
- [ ] PR description clearly explains the *Why*, *What*, and *How to Test*.
