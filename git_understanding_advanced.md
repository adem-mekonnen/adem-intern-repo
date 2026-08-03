# Advanced Git Commands Reflection

## 1. git checkout main -- <file>
*   **What it does:** Restores a specific file to match its version on the `main` branch without affecting other changes in the working directory.
*   **Real Project Use Case:** If I break a configuration file that was working on `main`, I can "reset" just that file without losing my other progress on the branch.
*   **What surprised me:** It is extremely "surgical"—it only touches the file I specify, nothing else.

## 2. git cherry-pick <commit>
*   **What it does:** Applies the changes from one specific commit onto the current branch.
*   **Real Project Use Case:** If a teammate fixes a bug on another branch, I can "cherry-pick" just that fix into my branch without merging their whole (possibly unfinished) branch.
*   **What surprised me:** It can cause merge conflicts just like a normal merge if the files have diverged significantly.

## 3. git log
*   **What it does:** Displays the commit history. Using `--oneline --graph --all` shows a visual map of all branches.
*   **Real Project Use Case:** Essential for understanding the "story" of the code and finding commit hashes for debugging or cherry-picking.
*   **What surprised me:** The `--graph` view makes a complex branching history very easy to see visually.

## 4. git blame <file>
*   **What it does:** Shows line-by-line which commit and author last modified each part of a file.
*   **Real Project Use Case:** The best tool for finding "Why" a specific line was written and who to talk to if that line has a bug.
*   **What surprised me:** It perfectly confirmed the same "buggy" commit that I found earlier using `git bisect`.
