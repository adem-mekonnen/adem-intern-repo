# Code Formatting & Style Guides

## 1. Why Consistent Code Style Matters
Consistent code style is essential for team collaboration. It ensures that the codebase looks like it was written by a single person, which makes it much easier to read and maintain. It also prevents "diff noise" in Pull Requests, where simple formatting changes (like spaces or quotes) hide the actual logic changes.

## 2. Airbnb JavaScript Style Guide Review
I reviewed the Airbnb guide and focused on two main rules:
* **References:** Always use `const` or `let` and avoid `var` to prevent variable hoisting and scope issues.
* **Semicolons:** Airbnb strictly requires semicolons to avoid issues with JavaScript's Automatic Semicolon Insertion (ASI).

## 3. Environment Setup (ESLint & Prettier)
I installed the necessary tools using the following command:
```bash
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier
