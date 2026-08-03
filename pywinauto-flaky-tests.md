# Handling Flaky Tests & Improving Stability

## Research: Common Causes of Flakiness
I researched why tests fail non-deterministically. The most common causes are:
* **Race Conditions:** The script tries to interact with a button before the app has finished its "opening" animation.
* **Environmental Lag:** The computer slows down (CPU spike), causing the app to take 5 seconds to load instead of the usual 1 second.
* **Pop-ups:** Unexpected system notifications or "Update Available" dialogues blocking the UI.

## Reflection

### How do implicit waits help prevent timing-related test failures?
Implicit waits (or global timing settings in Pywinauto) provide a "buffer." They tell the library to automatically wait a fraction of a second before every action. This smooths out small inconsistencies in how fast the UI renders.

### When should explicit waits be used instead of implicit waits?
Explicit waits (`wait('visible')`) should be used for major events, like waiting for a window to open, a network request to finish, or a long animation to complete. They are better than implicit waits because they allow for a long timeout (e.g., 10-20 seconds) without slowing down every other simple action in the script.

### How does retry logic help with test stability, and when should it be avoided?
Retry logic (like `WaitUntilPasses`) helps when an action might fail momentarily—for example, if a button is visible but not yet "clickable" because an animation is playing. However, it should be avoided if it "masks" a real bug. If a button takes 5 tries to click every single time, that might be a performance bug that needs fixing, not a flaky test.

### What strategies can prevent flaky tests in large test suites?
1. **Clean State:** Ensure the app is reset to a "factory" state before every test.
2. **Headless Testing (where possible):** Reduces the impact of OS UI glitches.
3. **Screenshot on Failure:** Capturing exactly what the screen looked like helps determine if a failure was a real bug or a timing fluke.
4. **Independent Tests:** Tests should not depend on the result of a previous test; if Test A fails, Test B should still be able to run.
