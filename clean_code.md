# Handling Errors & Edge Cases (Practice Example)

## Research: Strategies for Robust Code
* **Guard Clauses:** These are checks at the beginning of a function that return early if a condition is not met. This prevents deeply nested "if" statements and keeps the main logic flat and readable.
* **Input Validation:** Checking that data entering a function is the correct type (e.g., ensuring a score is a number, not a string) before the code tries to process it.
* **Graceful Failure:** Ensuring that if an error happens, the app returns a helpful message or safe fallback instead of crashing or throwing a fatal error.

## Code Refactoring Example

### ❌ Original Function (No Error Handling)
This function crashes if the `user` object is missing or if the `score` is not a valid number.
```javascript
function updateHighScore(user, score) {
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }
}
function updateHighScore(user, score) {
  // 1. Guard clause: reject if user object is missing or malformed
  if (!user || typeof user !== 'object') {
    return "Error: invalid user provided.";
  }

  // 2. Guard clause: reject if score isn't a valid number
  if (typeof score !== 'number' || isNaN(score)) {
    return "Error: score must be a valid number.";
  }

  // 3. Handle missing property edge case: Default highScore to 0
  if (typeof user.highScore !== 'number') {
    user.highScore = 0;
  }

  // Core Logic
  if (score > user.highScore) {
    user.highScore = score;
    return "New record!";
  }

  return "Score did not beat the current record.";
}
