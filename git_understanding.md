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
*   **Repo & PR:** facebook/react - PR #28385
*   **What changed:** This PR improved "Hydration" error messages. When the server-rendered HTML doesn't match the client-rendered HTML, the app now gives a much more detailed error message telling the developer exactly which tag caused the problem.
*   **Reviewer Discussion:** Senior developers (like Sebastian Markbåge) discussed the specific wording of the error. They wanted to make sure the message was helpful for beginners but didn't make the library's file size too large. 
*   **Handling of Changes:** The author had to change several lines of code because a reviewer noticed that the new error message didn't account for "Text Nodes" correctly. After the author pushed a fix, the PR was approved with an "LGTM" (Looks Good To Me).
*   **Learning:** I learned that code review in big teams isn't just about finding "bugs"—it's about "Developer Experience" (DX). They spent a lot of time talking about how to make the error message easy to understand.

## Writing Meaningful Commit Messages - Evidence

### Open-Source Research
**Repository Reviewed:** [facebook/react](https://github.com/facebook/react/commits/main)

*   **Good Commit Example:** `5167b5f` - "Fix useSyncExternalStore re-render loop when state is updated in effect"
    *   **Why:** It uses the imperative mood ("Fix"), names the specific area affected, and explains the specific bug (re-render loop).
*   **Weak Commit Example:** `e8f2a1b` - "Update"
    *   **Why:** It gives zero context. A reader has to open the code changes to have any idea what was updated.

### My Real Commits (Proof of Work)
I performed three commits in this repository to demonstrate different styles. Here is my `git log --oneline` output:

30016d4 Merge branch 'main' of https://github.com/adem-mekonnen/adem-intern-repo
c2028f0 chore: add whitespace to README for git practice
74fc9c7 I went into the README file and added a second space at the bottom because the bot told me I needed to make three commits and I had nothing to commit so I'm adding this long message to show what a bad overly detailed commit looks like
3bb4c64 fixed stuff

---

### Reflections (Updated)
*   **What makes a good commit message?** A good message uses the imperative mood, stays under 50 characters for the summary, and explains the "why" rather than just the "what."
*   **How does it help collaboration?** It makes the project history searchable. Teammates can use `git log` to understand the evolution of the code without reading every line of code.
*   **How can poor messages cause issues?** Vague messages like "fixed stuff" create a "dark age" in the project history. If a bug is found later, it's impossible to know which commit caused it without manual investigation, which slows down the whole team.

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
I created a conflict by editing the same lines in `math.js` on two different branches. On the `main` branch, I added a `power` function using `Math.pow()`. On the `conflict-demo` branch, I added the same function using the `**` operator. When I ran `git merge conflict-demo`, Git stopped because it couldn't automatically choose between the two different implementations of the same function.

**How I resolved it using my Desktop Client (VS Code):**
Instead of using the terminal, I used **Visual Studio Code** to resolve the conflict visually:
*   **What I saw:** In the **Source Control** tab (left sidebar), `math.js` appeared under **"Merge Changes"** with a red "!" icon. When I opened the file, the conflict was highlighted with a blue background for the "Current Change" (main) and a green background for the "Incoming Change" (conflict-demo).
*   **Actions taken:** Above the highlighted code, VS Code provided four options: *Accept Current Change*, *Accept Incoming Change*, *Accept Both*, and *Compare Changes*. 
*   **Resolution:** I clicked **"Accept Current Change"** to keep the `Math.pow` version. 
*   **Completing the merge:** After selecting the code, I clicked the **"+" (plus icon)** next to the file in the sidebar to "Stage" the resolution. Finally, I typed a message and clicked the blue **"Commit"** button in VS Code to finalize the merge.

**What I learned:**
I learned that merge conflicts are a safety tool that prevents accidental data loss. Using a desktop client like VS Code is much more efficient than the terminal because it allows you to see the two versions side-by-side and choose the correct one with a single click.
# Git Concepts: Staging vs. Committing

## Research: The Difference
* **Staging (`git add`):** Think of this as the "Loading Dock." You are choosing which changes you want to include in your next save. It allows you to review your work before making it permanent.
* **Committing (`git commit`):** This is the "Warehouse." Once you commit, you are creating a permanent snapshot (a version) of your project in the history. Each commit has a unique ID and a message describing the change.

## Reflection

### What is the difference between staging and committing?
Staging is an intermediate step where you prepare your files. Committing is the final step that saves those prepared files into the project's history.

### Why does Git separate these two steps?
Git separates them to give developers "granular control." For example, if I fix three different bugs in three different files, I can stage and commit them one by one so that the history is clean and easy to read, rather than having one giant "messy" commit.

### When would you want to stage changes without committing?
I would stage changes when I have finished one part of a task but want to keep working on another part before I save the whole "version." It acts as a way to "bookmark" my progress.

## Practical Experiment
In my experiments using the GitHub interface:
1. I modified the file.
2. The interface automatically staged the changes when I started typing the commit message.
3. Clicking "Commit changes" performed both the staging and the committing.
