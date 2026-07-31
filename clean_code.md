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
