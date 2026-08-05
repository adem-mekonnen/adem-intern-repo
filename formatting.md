# Code Formatting & Style Guides

## Research
I reviewed the Airbnb JavaScript style guide (github.com/airbnb/javascript), focusing on the sections covering variable declarations (`const`/`let` over `var`), semicolon usage, and consistent spacing around operators.

## Setup
Installed ESLint and Prettier with:
```bash
npm install --save-dev eslint prettier eslint-config-airbnb-base eslint-plugin-import eslint-config-prettier eslint-plugin-prettier
```

Created `.eslintrc.json`:
```json
{
  "extends": ["airbnb-base", "plugin:prettier/recommended"],
  "env": {
    "node": true,
    "es2021": true
  },
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  }
}
```

Created `.prettierrc`:
```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2
}
```

## Linter Results
I created `src/example.js` with intentionally messy code and ran `npx eslint src/example.js`. The initial pass surfaced 9 errors and 1 warning:
- `no-var`: flagged `var x = 10`, recommending `let`/`const` instead.
- `no-unused-vars`: flagged that `x` was declared but never used.
- `prefer-const`: flagged that `y` was never reassigned and should use `const` instead of `let`.
- `no-console`: warned about a `console.log` statement.
- Several `prettier/prettier` errors flagged missing semicolons, inconsistent spacing (e.g. `a+b` instead of `a + b`), and Windows-style CRLF line endings clashing with Prettier's expected LF format.

Running `npx eslint src/example.js --fix` automatically resolved 8 of the 9 errors — spacing, semicolons, and the `var`/`let` → `const` conversions. After a second `--fix` pass to resolve a missing trailing newline flagged by Prettier, only one issue remained: the unused `x` variable, which was removed manually since ESLint won't guess what to do with unused code.

Final linted file:
```javascript
function calc(a, b) {
  const y = a + b;
  return y;
}
console.log(calc(1, 2));
```

Running `npx eslint src/example.js` one final time returned **1 warning, 0 errors** — the `no-console` warning, which was kept intentionally since this file is a demo script meant to show output. In production code this would typically be removed or replaced with a proper logger.

## Reflections

**Why is code formatting important?**
Running the linter on my own code showed me firsthand that formatting isn't just cosmetic — it caught a real unused variable and a `let` that should have been `const`, alongside pure style issues like spacing and semicolons. Consistent formatting keeps a codebase readable across contributors and keeps git diffs focused on logic changes instead of style noise.

**What issues did the linter detect?**
It detected a `var` that should have been `const`, an unused variable, a `let` that should have been `const` since it was never reassigned, a `console.log` statement, missing semicolons, inconsistent operator spacing, and CRLF line endings clashing with Prettier's LF default (a side effect of developing on Windows).

**Did formatting the code make it easier to read?**
Yes — after `--fix`, spacing and semicolons were normalized automatically, and correcting `let` to `const` made the code's intent clearer by showing which values never change. Manually removing the unused variable also cleaned up dead code that the linter flagged but couldn't safely delete on its own.
