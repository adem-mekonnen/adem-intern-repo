# Code Formatting & Style Guides

## 1. Why Code Formatting Matters
Consistent code formatting is vital for team collaboration. It ensures that the codebase is readable by everyone and prevents "diff noise" in Pull Requests where simple spacing changes hide actual logic changes. It allows developers to focus on the code's functionality rather than its appearance.

## 2. Airbnb JavaScript Style Guide Takeaways
I reviewed the Airbnb guide and implemented these key takeaways:
* **Prefer const/let over var:** To avoid issues with variable hoisting and scoping.
* **Semicolons:** Always required to prevent ambiguity in JavaScript's automatic semicolon insertion.
* **Trailing Commas:** Used in multiline objects and arrays to make git diffs cleaner when adding new items.

## 3. Environment Setup (ESLint & Prettier)
I installed the necessary developer dependencies using the following command:

```bash
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier eslint-config-airbnb-base
ESLint Configuration (.eslintrc.json)
code
JSON
{
  "extends": ["airbnb-base", "plugin:prettier/recommended"],
  "env": {
    "node": true,
    "es2021": true
  },
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  },
  "rules": {}
}
Prettier Configuration (.prettierrc)
code
JSON
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
4. Real Linter Results & Fixes
I ran the linter on my local math.js file to detect style and logic issues.
Command run: npx eslint math.js
Initial Results:
The linter detected 12 problems (11 errors, 1 warning). Specific errors included:
prettier/prettier: Flagged functions written on a single line that needed to be expanded to blocks.
no-unused-vars: Flagged functions like add and subtract that were defined but not exported.
Logic Error Spotted: The linter flagged line 4:24 where my divide function was incorrectly using * instead of /.
The Fix:
I ran npx eslint math.js --fix which automatically resolved the indentation and semicolons.
I manually corrected the divide function to use the proper division operator.
I added module.exports to the bottom of the file to resolve the unused variable errors.
5. Reflection on Readability
Using a linter and formatter made a significant difference. Before formatting, the inconsistent indentation and one-line functions made the code feel cramped. Now, the code has a predictable structure following the Airbnb standard, which makes it much easier to scan for logic errors. It feels professional and is much easier to maintain.
