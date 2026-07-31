# Handling Errors & Edge Cases

## Research: Strategies for Robust Code
* **Guard Clauses:** These are checks at the beginning of a function that return early if a condition isn't met. This prevents deeply nested "if" statements and makes the code cleaner.
* **Input Validation:** Checking that the data entering a function is correct (e.g., making sure a number isn't a string or that a required field isn't empty).
* **Graceful Failure:** Ensuring that if an error happens, the app shows a helpful message instead of crashing.

## Code Refactoring Example

### ❌ Original Function (No Error Handling)
This function will crash if the `user` object is missing or if the `score` is not a number.
```javascript
function updateHighScore(user, score) {
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }
}
---

# Commenting & Documentation

## Research: Best Practices
* **Explain the "Why," not the "What":** Code tells you *what* is happening. Comments should tell you *why* it is happening (e.g., "Retrying because the API is unstable").
* **Self-Documenting Code:** Use clear variable and function names so you don't need a comment to explain them.
* **Keep it updated:** An outdated comment is worse than no comment at all.

## Code Example: Bad vs. Good Comments

### ❌ Poorly Commented Code
```javascript
// Function to add two numbers
function add(a, b) {
  let c = a + b; // add a and b and store in c
  return c; // return the result
}
---

# Refactoring Code for Simplicity

## Research: Refactoring Techniques
* **Extract Method:** If a function is too long, break parts of it into smaller, named functions.
* **Simplify Boolean Expressions:** Instead of complex `if (a == true && b == false)`, use clear logic.
* **Remove Dead Code:** Delete variables or functions that are never used.
* **Replace Loop with Pipeline:** Using modern methods like `.filter()` or `.map()` instead of manual `for` loops.

## Code Example: Over-engineered vs. Simple

### ❌ Over-engineered Code
This code is too long and manually tracks a counter to find active users.
```javascript
function getActiveUsers(users) {
  let activeList = [];
  for (let i = 0; i < users.length; i++) {
    if (users[i].status === 'active') {
      if (users[i].age > 18) {
        activeList.push(users[i]);
      }
    }
  }
  return activeList;
}

## Avoiding Code Duplication

**Issues with duplicated code:**
- Repeated logic meant any bug fix or rule change had to be made in multiple places, increasing the risk of missing one and introducing inconsistent behavior.
- Duplication made the code harder to read — it wasn't obvious at a glance that two blocks were meant to represent the same rule.
- It increased the size of the codebase without adding value, making review and testing slower.

**How refactoring improved maintainability:**
- Extracting the shared logic into a single function/helper means the rule now lives in one place — future changes only need to happen once.
- The code is more readable: the intent (e.g. "eligibility check") is named explicitly instead of implied by repeated conditions.
- Testing is simpler since the shared logic can be tested once in isolation, rather than verifying the same behavior in every place it's duplicated.
# Before — one big function doing several jobs
def process_order(order):
    # validate
    if not order.items:
        raise ValueError("Order has no items")
    if order.total <= 0:
        raise ValueError("Invalid total")
    
    # calculate discount
    discount = 0
    if order.total > 100:
        discount = order.total * 0.1
    final_total = order.total - discount
    
    # send confirmation
    print(f"Sending email to {order.customer_email}")
    print(f"Order confirmed: {final_total}")
    
    return final_total

# After — broken into focused functions
def validate_order(order):
    if not order.items:
        raise ValueError("Order has no items")
    if order.total <= 0:
        raise ValueError("Invalid total")

def calculate_discount(total):
    return total * 0.1 if total > 100 else 0

def send_confirmation(order, final_total):
    print(f"Sending email to {order.customer_email}")
    print(f"Order confirmed: {final_total}")

def process_order(order):
    validate_order(order)
    discount = calculate_discount(order.total)
    final_total = order.total - discount
    send_confirmation(order, final_total)
    return final_total
## Writing Small, Focused Functions

**Why breaking down functions is beneficial:**
- Small functions are easier to read and understand — each one answers a single, clear question about what it does.
- They're easier to test in isolation, since each function has a narrow, predictable responsibility rather than mixed concerns.
- They're easier to reuse — a focused function like `calculate_discount()` can be called elsewhere without dragging along unrelated logic.
- Debugging is faster: when something breaks, a well-named small function narrows down where to look.

**How refactoring improved the structure of the code:**
- Splitting the large function into `validate_order`, `calculate_discount`, and `send_confirmation` made the responsibilities explicit instead of buried inside one long block.
- The main `process_order` function now reads almost like a summary of the steps, which makes the overall flow easier to follow.
- Future changes are more contained — e.g. changing the discount rule only touches `calculate_discount`, without risk of breaking validation or notification logic.
## Naming Variables & Functions

**What makes a good variable or function name:**
- It clearly describes the purpose or content without needing a comment to explain it.
- Functions are named as actions (verbs), variables as things (nouns), and booleans read like questions (e.g. `isValid`).
- Names are consistent across the codebase so similar operations aren't described differently in different places.

**Issues from poorly named variables:**
- Code becomes hard to read and understand without extra context or comments.
- Increases the chance of bugs, since it's easy to misuse a variable when its purpose isn't clear.
- Slows down onboarding and code review, since readers have to reverse-engineer intent from usage instead of the name itself.
- Misleading names (e.g. a plural name for a single value) can cause confusion or outright errors.

**How refactoring improved readability:**
- Renaming `calc`, `a`, `b`, `t`, and `x` to `calculate_price`, `unit_price`, `quantity`, `is_discounted`, and `total` made the function's purpose obvious at a glance.
- Anyone reading the refactored code can understand what it does without stepping through the logic line by line.
- It reduced the need for comments, since the names themselves now communicate intent.
## Code Formatting & Style Guides

**Why code formatting is important:**
- Consistent formatting makes code easier to read and reduces mental overhead when switching between files or contributors.
- It keeps git diffs focused on actual logic changes rather than formatting noise.
- It reduces bugs — linters catch issues like unused variables or accidental loose equality before they cause problems.
- It removes subjective debate over style, since the rules are enforced automatically rather than argued case by case.

**Issues the linter detected:**
- [Fill in with your actual results, e.g.: unused variables, inconsistent quote usage, missing semicolons, use of `var` instead of `const`/`let`, loose equality checks]

**Did formatting make the code easier to read:**
- Yes — after running Prettier and fixing ESLint warnings, indentation and spacing became consistent throughout, and the Airbnb rules around naming and structure made the code easier to scan.
## Understanding Clean Code Principles

**Simplicity** – Code should do what's needed in the most straightforward way possible. Avoid clever one-liners or unnecessary abstraction layers that make the code harder to follow than a plain, direct solution would.

**Readability** – Code is read far more often than it's written. It should be understandable at a glance, using clear names, consistent structure, and logical flow, so another developer (or future you) doesn't have to decode it.

**Maintainability** – Code should be easy to modify, extend, or debug later without a large risk of breaking something else. This comes from small functions, clear naming, low duplication, and good structure.

**Consistency** – Following agreed style guides and project conventions (naming, formatting, file structure) means the codebase feels like it was written by one person, even with multiple contributors, which reduces friction and confusion.

**Efficiency** – Code should perform well, but performance shouldn't be chased prematurely at the cost of clarity. Optimize the parts that actually matter (measured, not guessed), and keep everything else simple and readable.
