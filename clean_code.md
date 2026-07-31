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
