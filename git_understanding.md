# Git Understanding

## Pull Requests

**Why PRs are important in a team workflow:**
- They create a review checkpoint before code reaches the main branch, catching bugs, design issues, or style violations early.
- They document the reasoning behind a change, which is useful for future reference.
- They allow CI/CD checks (tests, linters, builds) to run automatically before anything is merged.
- They support async collaboration — reviewers can weigh in without blocking the author's progress.

**What makes a well-structured PR:**
- A clear, descriptive title that summarizes the change.
- A description that explains what changed and why, not just what files were touched.
- A link to the related issue for context.
- Small, focused scope — one logical change per PR rather than bundling unrelated work.
- Passing CI checks before requesting review.

**What I learned from reviewing an open-source PR:**
[Fill in based on the actual PR you reviewed — e.g., which repo/PR number, what the change was, how the description explained the "why," what feedback reviewers left, and how the author responded to it.]

## Writing Meaningful Commit Messages

*Note: This is a practice example written to demonstrate the concept.*

### Research: Best Practices for Commit Messages
- **Use the imperative mood:** write "Fix login bug" not "Fixed login bug" or "Fixes login bug" — this matches how Git itself describes commits (e.g. "Merge branch...").
- **Keep the summary line short:** aim for under ~50 characters for the first line, with more detail in the body if needed.
- **Explain the "why," not just the "what":** the diff already shows what changed; the message should explain the reasoning or context behind the change.
- **One logical change per commit:** avoid bundling unrelated fixes into a single commit, since it makes history harder to search and revert cleanly.
- **Reference related issues:** e.g. "Fixes #42" so the commit is traceable to the task it resolves.

### Analyzing Open-Source Commit Histories
Looking through the commit history of [React](https://github.com/facebook/react/commits) or [Node.js](https://github.com/nodejs/node/commits), a clear pattern shows up:
- **Good commits** have a short, specific summary line (e.g. "Fix memory leak in useEffect cleanup") followed by a body explaining the root cause and the fix.
- **Weak commits** (less common in these well-maintained projects, but still occasionally visible) are vague, like "update" or "fix" with no further context, making it hard to understand what changed or why without opening the full diff.

### Three Commits with Different Message Styles

**1. Vague commit message:**
```bash
git commit -m "fixed stuff"
```
This tells a future reader nothing about what was fixed, why it broke, or what area of the code was touched.

**2. Overly detailed commit message:**
```bash
git commit -m "Changed the calculateDiscount function in pricing.js to fix a bug where the discount percentage was being applied twice when the user had both a loyalty discount and a seasonal promotion active at the same time, which was causing the final total to be incorrect for users checking out during the summer sale, discovered after a customer support ticket reported an unexpectedly low total on their order confirmation email"
```
This has too much detail crammed into a single line — it should be split into a short summary line plus a body, rather than one long run-on sentence.

**3. Well-structured commit message:**
```bash
git commit -m "Fix double discount application in calculateDiscount

Loyalty and seasonal discounts were both being applied
multiplicatively instead of choosing the larger of the two,
causing incorrect totals for users with both active.

Fixes #57"
```
This follows best practice: a short imperative summary line, a body explaining the root cause and reasoning, and a reference to the related issue.

### Reflections

**What makes a good commit message?**
A good commit message has a short, imperative summary line (e.g. "Fix double discount application") that clearly states what changed, optionally followed by a body that explains *why* the change was needed — the reasoning, root cause, or context that isn't obvious from the diff alone. It stays focused on one logical change and references related issues when applicable.

**How does a clear commit message help in team collaboration?**
Clear commit messages let teammates understand the history of a project without having to read every line of every diff. They make it much faster to find when and why a specific change was made (e.g. using `git log` or `git blame`), which is especially valuable during debugging, code review, or when writing release notes. They also make it easier to decide whether a specific commit is safe to revert or cherry-pick.

**How can poor commit messages cause issues later?**
Vague messages like "fixed stuff" or "update" leave no record of what problem was being solved, forcing anyone investigating a bug later to dig through the full diff or ask the original author (who may not remember either). This slows down debugging, makes `git blame` far less useful, and can lead to duplicated effort if someone doesn't realize an issue was already addressed in a past commit. Overly detailed one-line messages, on the other hand, become hard to scan in `git log`, defeating the purpose of a quick, readable history.

## Understanding `git bisect`

**What does `git bisect` do?**
`git bisect` uses binary search across commit history to find the exact commit that introduced a bug. You mark one commit as "good" (before the bug existed) and another as "bad" (where the bug is present), and Git checks out commits in between, narrowing the search by half each time based on whether the bug is present, until it identifies the precise commit responsible.

**When would you use it in a real-world debugging situation?**
It's most useful when a bug is discovered well after it was introduced, and it isn't obvious which of many commits caused it — for example, a regression found in production that could have come from any of dozens of merges over the past few weeks. Rather than manually checking out and testing each commit in order, `git bisect` finds the source in a handful of steps.

**How does it compare to manually reviewing commits?**
Manually reviewing commits means checking them one at a time, which is linear — with 100 commits, you might need to check up to 100 of them. `git bisect`'s binary search only needs about log₂(100) ≈ 7 steps to find the same commit, since each test eliminates half of the remaining possibilities. This makes it dramatically faster for large histories, and it also removes guesswork, since you're following a systematic process instead of guessing which commit "looks suspicious."

**Hands-on test:**
I created a series of 5 commits in a test branch, where the 4th commit introduced a deliberate bug (a `divide` function that multiplied instead of dividing). Using `git bisect start`, marking the first commit as good and the last as bad, Git correctly identified the exact commit that introduced the bug after only 2-3 test steps, confirming how the binary search narrows down the culprit efficiently.
## Understanding `git bisect`

**What does `git bisect` do?**
`git bisect` uses binary search across commit history to find the exact commit that introduced a bug. You mark one commit as "good" (before the bug existed) and another as "bad" (where the bug is present), and Git checks out commits in between, narrowing the search by half each time based on whether the bug is present, until it identifies the precise commit responsible.

**When would you use it in a real-world debugging situation?**
It's most useful when a bug is discovered well after it was introduced, and it isn't obvious which of many commits caused it — for example, a regression found in production that could have come from any of dozens of merges over the past few weeks. Rather than manually checking out and testing each commit in order, `git bisect` finds the source in a handful of steps.

**How does it compare to manually reviewing commits?**
Manually reviewing commits means checking them one at a time, which is linear — with 100 commits, you might need to check up to 100 of them. `git bisect`'s binary search only needs about log₂(n) steps to find the same commit, since each test eliminates half of the remaining possibilities. This makes it dramatically faster for large histories and removes guesswork, since you're following a systematic process instead of guessing which commit "looks suspicious."

**Hands-on test:**
I created 5 commits on a test branch (`bisect-practice`), where the 4th commit (`d427c3b`, "Add divide function") introduced a deliberate bug — a `divide` function that multiplied instead of dividing. Using `git bisect start`, marking `ce7c1a3` (a later commit) as bad and `9caaaf7` (the first commit) as good, Git checked out `ada9a05` ("Add multiply function") first. Since the bug wasn't present at that point, I marked it good. Git then checked out `d427c3b`, which contained the bug, so I marked it bad — and Git correctly reported:
## Advanced Git Commands & When to Use Them

### `git checkout main -- <file>`
**What it does:** Restores a specific file to match its version on another branch (e.g. `main`), without affecting any other files or the rest of your working directory.
**When to use it:** Useful when you've made unwanted changes to a single file and want to discard just that file's edits without resetting your entire branch.
**Test result:** On a test branch (`file-restore-test`), I made an edit to `math.js`, committed it, then ran `git checkout main -- math.js`. This restored `math.js` to `main`'s version, discarding my test edit while leaving the rest of the branch untouched — confirmed with `git status` showing the file staged as modified.

### `git cherry-pick <commit>`
**What it does:** Applies the changes from one specific commit onto your current branch, without merging the entire source branch.
**When to use it:** Useful when a specific fix or feature was committed on another branch, but you need just that one change on `main` immediately, without pulling in unrelated work.
**Test result:** I cherry-picked commit `d427c3b` ("Add divide function") from `bisect-practice` onto `main`. Since `main`'s `math.js` had diverged (from an earlier test edit), this caused a real merge conflict, requiring manual resolution with `<<<<<<<`/`=======`/`>>>>>>>` markers. After resolving and staging the file, `git cherry-pick --continue` reported the commit was "now empty," since my manual resolution already matched the intended result — I closed it out with `git cherry-pick --skip`.

### `git log`
**What it does:** Displays commit history, including author, date, and message. With `--oneline --graph --all`, it shows a compact, visual timeline across all branches.
**Test result:** Running `git log --oneline --graph --all` clearly showed `file-restore-test` branching off `main` at commit `9de3c37` and never merging back, while `bisect-practice`'s commits were already part of `main`'s linear history from an earlier merge. This made the actual shape of my branching work visible at a glance, rather than something I had to infer.

### `git blame <file>`
**What it does:** Shows, line by line, which commit last modified each line of a file, along with the author and date.
**Test result:** Running `git blame math.js` showed each function traced to the exact commit that introduced it — e.g. line 4 (the buggy `divide` function) correctly pointed to commit `d427c3b`, matching what `git bisect` had already identified as the source of the bug.

### What surprised me while testing these commands
- `git checkout main -- <file>` is more surgical than I expected — it only touches the specified file, leaving all other changes in the working directory untouched.
- Cherry-picking a commit that touches a file already modified independently on the target branch caused a real merge conflict, not a clean apply — cherry-pick behaves exactly like a merge when it comes to conflicting diffs.
- After manually resolving that conflict, Git reported the cherry-picked commit was "now empty," since my resolution already matched the intended end state — a good reminder that Git cares about the resulting diff, not just replaying a commit's exact steps.
- `git blame` lined up exactly with what `git bisect` had already found, which was a satisfying confirmation that both tools were pointing to the same root cause from two different angles.
## Merge Conflicts & Conflict Resolution

**What caused the conflict?**
I created a branch (`conflict-demo`) and added a `power` function to `math.js`. Then, without merging, I switched back to `main` and added a different implementation of the same `power` function directly on `main` (using `Math.pow` instead of the `**` operator). When I ran `git merge conflict-demo`, Git couldn't automatically reconcile the two versions since both added content at the same location in the file, producing a real merge conflict marked with `<<<<<<< HEAD`, `=======`, and `>>>>>>> conflict-demo`.

**How did I resolve it?**
I opened the conflicted file and reviewed both versions side by side. I chose to keep the `Math.pow`-based implementation from `main`, removed the conflict markers and the alternate version, staged the resolved file with `git add math.js`, and completed the merge with `git commit -m "Resolve merge conflict in power function"`.

**What did I learn?**
A merge conflict isn't an error — it's Git correctly recognizing that two branches changed the same lines and it can't guess which version was intended. Resolving one means actually reading both versions and making a deliberate choice, rather than blindly accepting one side. This connects to what I saw with `git cherry-pick` in the previous issue — cherry-picking a commit onto a diverged branch triggered the exact same conflict-resolution mechanism as a normal merge, which showed me these aren't separate concepts but the same underlying process in Git.
## Branching & Team Collaboration

**Why is pushing directly to `main` problematic?**
Pushing directly to `main` means unreviewed, untested code lands immediately in the branch everyone else builds from and deploys. There's no checkpoint to catch bugs, style issues, or design problems before they affect the whole team. It also removes the paper trail a Pull Request creates — a record of what changed, why, and who approved it — which makes it harder to understand the project's history later.

**How do branches help with reviewing code?**
Branches isolate work-in-progress from the stable `main` branch, so changes can be reviewed, discussed, and tested via a Pull Request before merging. This gives reviewers a clear, contained diff to evaluate, lets CI checks run against the proposed change specifically, and means `main` stays deployable at all times since nothing lands there without going through review first.

**What happens if two people edit the same file on different branches?**
If their changes touch different parts of the file, Git can usually merge them automatically without any conflict. But if they both modify the same lines, Git can't automatically decide which version is correct, resulting in a merge conflict — I saw this directly in a previous exercise, where two branches both added a `power` function to `math.js` with different implementations, and merging required manually resolving the conflict by choosing which version (or combination) to keep.

**Hands-on test:**
I created a branch (`branching-demo`), added a small comment to `math.js`, and committed it. Switching back to `main` confirmed the change wasn't present there — the commit existed only on the branch until merged, demonstrating exactly why branches let you experiment or develop safely without affecting the shared `main` branch.
