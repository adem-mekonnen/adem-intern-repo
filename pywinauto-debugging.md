# Debugging & Handling Common Test Failures

## Research: Debugging Strategies
I learned that debugging E2E tests requires a different approach than debugging standard code. Because tests interact with a live UI, we must account for the "Environment" (OS speed, network lag, and UI animations).

## Reflection

### What are the most common reasons for E2E test failures?
*   **Timing Issues:** The script tries to click an element before it has finished loading or animating.
*   **Dynamic IDs:** Some apps generate new IDs every time they start, making the script unable to find the button it used last time.
*   **Context Loss:** In hybrid apps like Focus Bear, the Selenium driver might lose its connection to the WebView if the window refreshes or closes unexpectedly.

### How do you determine if a test is flaky?
A test is flaky if it gives different results (passes and fails) on the exact same code without any changes being made. If it fails in the CI/CD pipeline but passes on my local machine, that is a major sign of flakiness due to environment differences.

### What strategies can you use to improve test reliability?
*   **Explicit Waits:** Using `.wait('visible')` or `.wait('ready')` instead of hard-coded `time.sleep()`.
*   **Retry Logic:** Wrapping unstable actions (like network-dependent button clicks) in a loop that tries 3-5 times before giving up.
*   **State Reset:** Ensuring the app is in the exact same starting position (e.g., logged out, home screen open) before every test run.

### How can logging and screenshots help with debugging test failures?
Since automated tests often run on a "Headless" server (where there is no monitor), screenshots are the only way to see what the app looked like at the exact moment of failure. Logs provide a "paper trail" that tells us exactly which line of code was running and which element the script was looking for when it crashed.
