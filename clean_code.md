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
