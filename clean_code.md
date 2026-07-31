# Understanding Clean Code Principles

*Note: This is a practice example written to demonstrate the concept, not taken from a live project.*

## The Five Principles

**Simplicity** – Code should do what's needed in the most straightforward way possible. Avoid clever one-liners or unnecessary abstraction layers that make the code harder to follow than a plain, direct solution would.

**Readability** – Code is read far more often than it's written. It should be understandable at a glance, using clear names, consistent structure, and logical flow, so another developer (or future you) doesn't have to decode it.

**Maintainability** – Code should be easy to modify, extend, or debug later without a large risk of breaking something else. This comes from small functions, clear naming, low duplication, and good structure.

**Consistency** – Following agreed style guides and project conventions (naming, formatting, file structure) means the codebase feels like it was written by one person, even with multiple contributors, which reduces friction and confusion.

**Efficiency** – Code should perform well, but performance shouldn't be chased prematurely at the cost of clarity. Optimize the parts that actually matter (measured, not guessed), and keep everything else simple and readable.

## Example: Messy Code

```javascript
function p(d) {
  let r = [];
  for (let i = 0; i < d.length; i++) {
    if (d[i].s === 'a' && d[i].t > 0) {
      let x = d[i].t;
      if (x > 100) {
        x = x * 0.9;
      }
      r.push({ n: d[i].n, total: x });
    }
  }
  return r;
}
```

### Why this is difficult to read
- The function name `p` and parameter `d` give no indication of what the function does or what data it operates on.
- Variables like `r`, `i`, `x`, `s`, `t`, and `n` are meaningless abbreviations — a reader has to trace through the logic just to guess what each one represents.
- Magic values (`'a'`, `100`, `0.9`) are unexplained — there's no way to know `'a'` means "active" or that `0.9` represents a 10% discount without reverse-engineering the intent.
- The function mixes multiple responsibilities at once — filtering records, applying a discount calculation, and building a result object — all inside one loop with no separation.

## Cleaned-Up Rewrite

```javascript
const ACTIVE_STATUS = 'active';
const DISCOUNT_THRESHOLD = 100;
const DISCOUNT_RATE = 0.9;

function isEligibleForDiscount(record) {
  return record.status === ACTIVE_STATUS && record.total > 0;
}

function applyDiscount(total) {
  return total > DISCOUNT_THRESHOLD ? total * DISCOUNT_RATE : total;
}

function getDiscountedTotals(records) {
  return records
    .filter(isEligibleForDiscount)
    .map((record) => ({
      name: record.name,
      total: applyDiscount(record.total),
    }));
}
```

### Why the rewrite is cleaner
- **Simplicity:** Using `.filter()` and `.map()` replaces the manual loop and nested conditionals with a straightforward pipeline that reads top-to-bottom.
- **Readability:** Renaming `p`, `d`, `r`, `i`, `x`, `s`, `t`, `n` to `getDiscountedTotals`, `records`, `isEligibleForDiscount`, `applyDiscount`, `total`, `status`, `name` makes the function's purpose obvious without needing to trace the logic.
- **Maintainability:** Splitting the logic into `isEligibleForDiscount` and `applyDiscount` means each rule can be changed independently — e.g. adjusting the discount rate only touches one small function.
- **Consistency:** Named constants (`ACTIVE_STATUS`, `DISCOUNT_THRESHOLD`, `DISCOUNT_RATE`) replace magic values, so the same meaning is used everywhere these values appear instead of unexplained literals scattered through the code.
- **Efficiency:** The rewrite performs the same work as the original (single pass filtering and mapping) — clarity was improved without adding unnecessary overhead.

# Naming Variables & Functions

*Note: This is a practice example written to demonstrate the concept, not taken from a live project.*

## Research: Best Practices
- **Be descriptive, not clever:** `daysSinceLastLogin` beats `d` or `dsll`.
- **Use intention-revealing names:** a name should answer *what it holds* or *what it does* without needing a comment.
- **Functions = verbs, variables = nouns:** `calculateTotal()`, `isValid`, `userList` — not `data`, `handle`, `temp`.
- **Avoid ambiguous abbreviations:** `usr`, `cnt`, `mgr` save keystrokes but cost readability later.
- **Be consistent:** don't mix `getUser` and `fetchCustomer` for the same kind of operation.
- **Booleans should read like yes/no questions:** `isActive`, `hasPermission`, `canEdit`.

## Code Refactoring Example

### Before (Unclear Names)
```javascript
function calc(a, b, t) {
  let x = a * b;
  if (t === 1) {
    x = x * 0.9;
  }
  return x;
}
```

### After (Clear, Intention-Revealing Names)
```javascript
function calculatePrice(unitPrice, quantity, isDiscounted) {
  let total = unitPrice * quantity;
  if (isDiscounted) {
    total = total * 0.9; // apply 10% discount
  }
  return total;
}
```

### Renames and Why They Helped
- **Function: `calc` → `calculatePrice`** — `calc` gave no indication of what was being calculated. `calculatePrice` immediately tells a reader what the function produces.
- **Variable: `a` → `unitPrice`** — `a` could have meant anything. `unitPrice` makes clear it's a per-unit cost being multiplied.
- **Variable: `b` → `quantity`** — same issue as above; `quantity` makes the multiplication (`unitPrice * quantity`) self-explanatory without needing to trace how the function is called.
- **Variable: `t` → `isDiscounted`** — `t` was a magic flag compared against the literal `1`, forcing the reader to guess what `1` meant. `isDiscounted` reads as a yes/no question and removes the need to decode a magic number.
- **Variable: `x` → `total`** — `x` is a placeholder name with no meaning. `total` matches what the value actually represents as it's built up and returned.

## Reflections

**What makes a good variable or function name?**
A good name clearly describes the purpose or content of what it represents, without needing a comment to explain it. Functions are named as actions (verbs, like `calculatePrice`), variables as things (nouns, like `unitPrice` or `total`), and booleans read like yes/no questions (like `isDiscounted`). Good names are also consistent across the codebase, so the same kind of operation isn't described differently in different places.

**What issues can arise from poorly named variables?**
Poor names make code hard to read and force the reader to trace through logic just to figure out what a value represents, as with `a`, `b`, `t`, and `x` in the example above. They increase the risk of bugs, since it's easy to misuse a variable when its purpose isn't obvious. They also slow down code review and onboarding, since reviewers have to reverse-engineer intent instead of reading it directly from the name, and magic values compared against unclear flags (like `t === 1`) hide meaning that only the original author knew.

**How did refactoring improve code readability?**
Renaming `calc` to `calculatePrice` and `a`, `b`, `t`, `x` to `unitPrice`, `quantity`, `isDiscounted`, and `total` made the function's purpose and internal logic clear at a glance, with no need to step through it line by line to understand what it does. It also removed the need for an explanatory comment, since the names themselves now communicate intent — the discount check reads as a plain English condition instead of a comparison against an unexplained number.

# Handling Errors & Edge Cases

*Note: This is a practice example written to demonstrate the concept, not taken from a live project.*

## Research: Strategies for Robust Code
- **Guard Clauses:** Checks at the beginning of a function that return early if a condition isn't met. This avoids deeply nested "if" statements and keeps the main logic flat and readable.
- **Input Validation:** Checking that data entering a function is correct (e.g., making sure a number isn't a string, or a required field isn't empty) before acting on it.
- **Graceful Failure:** Ensuring that if an error happens, the app returns a helpful message or safe fallback instead of crashing.

## Code Refactoring Example

### Original Function (No Error Handling)
This function crashes if `user` is missing, if `user.highScore` doesn't exist yet, or if `score` isn't a valid number.

```javascript
function updateHighScore(user, score) {
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }
}
```

### Refactored Function (With Guard Clauses & Validation)

```javascript
function updateHighScore(user, score) {
  // Guard clause: reject if user object is missing or malformed
  if (!user || typeof user !== 'object') {
    return "Error: invalid user provided.";
  }

  // Guard clause: reject if score isn't a valid number
  if (typeof score !== 'number' || isNaN(score)) {
    return "Error: score must be a valid number.";
  }

  // Default highScore to 0 if it doesn't exist yet
  if (typeof user.highScore !== 'number') {
    user.highScore = 0;
  }

  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }

  return "Score did not beat the current record.";
}
```

## Reflections

**What was wrong with the original function?**
The original function assumed `user` would always be a valid object and that `user.highScore` would already exist as a number. It also assumed `score` would always be a valid number. If any of these assumptions failed — e.g. `user` was `undefined`, `user.highScore` was missing, or `score` was a string — the function would either crash or silently produce incorrect results (e.g. comparing a number to `undefined`).

**How did the refactor improve reliability?**
The refactored version validates its inputs before doing any work. It checks that `user` is a valid object, that `score` is a genuine number, and it safely defaults `highScore` to `0` if it hasn't been set yet. Instead of crashing or failing silently, the function now returns a clear, descriptive message for every failure case, so the caller always knows exactly what went wrong.

**Which guard clauses or validation checks did you add?**
- A guard clause rejecting a missing or non-object `user`.
- A guard clause rejecting a `score` that isn't a valid number (using `typeof` and `isNaN`).
- A default-value check that sets `user.highScore` to `0` if it isn't already a number, preventing a broken comparison against `undefined`.

# Commenting & Documentation

*Note: This is a practice example written to demonstrate the concept, not taken from a live project.*

## Research: Best Practices
- **Explain the "Why," not the "What":** Code already shows *what* is happening. Good comments explain *why* it's happening — e.g. "Retrying because the API is unstable" — context that isn't obvious from the code alone.
- **Self-Documenting Code:** Use clear variable and function names so the code explains itself without needing a comment to translate it.
- **Keep it updated:** An outdated comment that no longer matches the code is worse than no comment at all, since it actively misleads the reader.
- **Avoid noise comments:** Don't comment on things that are already obvious from the code (e.g. `i++; // increment i`).

## Code Example: Bad vs. Good Comments

### Poorly Commented Code
```javascript
// Function to add two numbers
function add(a, b) {
  let c = a + b; // add a and b and store in c
  return c; // return the result
}
```
Every comment here just restates what the code already says line by line — it adds no real information.

### Improved Version
```javascript
function add(a, b) {
  return a + b;
}
```
The function is simple enough that clear naming (`add`, `a`, `b`) makes it fully self-explanatory — no comments are needed at all. If this function were more complex (e.g. handling rounding rules or currency conversion), a comment would be worth adding to explain *why* a particular approach was chosen, not to restate the arithmetic itself.

## Reflections

**When should you add comments?**
Comments are worth adding when they explain *why* something is done a certain way — non-obvious business logic, a workaround for a bug or limitation, or reasoning that isn't visible from the code itself (e.g. "Retrying 3 times because the payment API occasionally times out"). They're also useful for documenting public function signatures, expected inputs/outputs, or edge cases a future developer wouldn't otherwise anticipate.

**When should you avoid comments and instead improve the code?**
Comments should be avoided when they simply restate what the code already says (e.g. `// add a and b`), since these add clutter and go stale as the code changes. In these cases, the better fix is to make the code self-documenting — clearer variable and function names, smaller focused functions, and simpler logic — so it doesn't need translation in the first place. If a comment is needed just to explain what a poorly named variable or overly complex line does, that's usually a sign the code itself should be refactored instead.

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