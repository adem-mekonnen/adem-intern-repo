# Advanced Git Commands Reflection

## 1. git checkout main -- <file>
*   **What it does:** This command restores a specific file to match its version on the `main` branch (or any other branch you specify) without affecting any other files or changes in your current working directory.
*   **When to use it:** Use this when you have accidentally broken or deleted logic in a single file on your feature branch and want to reset just that one file back to a known-working state from the main branch without losing the rest of your work.
*   **What surprised me:** I was surprised at how "surgical" it is. It doesn't reset the whole branch, only the specific file path I provided. In my test on `file-restore-test`, it successfully restored `math.js` while leaving other edits active.

## 2. git cherry-pick <commit>
*   **What it does:** It takes the changes from a single, specific commit from another branch and applies them directly onto your current branch as a new commit.
*   **When to use it:** Use this when a colleague has fixed a critical bug on a different branch, and you need that specific fix immediately in your own work without merging their entire (possibly unfinished) branch.
*   **What surprised me:** I learned that cherry-picking behaves like a merge; if the file has changed on both branches, it can trigger a real merge conflict that requires manual resolution, which I experienced during my hands-on test.

## 3. git log
*   **What it does:** It displays the commit history of the repository, including author, date, and messages. Using flags like `--oneline --graph --all` provides a visual map of the project's evolution.
*   **When to use it:** I would use this to understand the "story" of the code and find specific commit hashes for `git bisect` or `git cherry-pick`. It is essential for understanding who changed what and when, which helps in team collaboration.
*   **What surprised me:** The `--graph` view was a huge help. It turned a list of text into a visual map that showed exactly where my feature branches diverged from and merged back into the main history.

## 4. git blame <file>
*   **What it does:** It shows a line-by-line history of a file, identifying exactly which commit and author last modified every single line of code.
*   **When to use it:** This is the best tool for debugging. When I find a suspicious line of code, I use `git blame` to see the original commit message. This gives me the context of *why* that line was written that way and who to talk to about it.
*   **What surprised me:** It surprised me how well `git blame` and `git bisect` work together. `git blame` pointed me to the exact same "buggy" commit (`d427c3b`) that I found earlier using the binary search method.
