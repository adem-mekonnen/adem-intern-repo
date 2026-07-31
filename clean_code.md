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
