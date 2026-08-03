# Integrating Pywinauto Tests into CI/CD

## Research: GUI Testing in the Pipeline
I researched how automated E2E tests fit into the software development lifecycle. In a professional environment, these tests run automatically every time a developer creates a "Pull Request." This ensures that new code doesn't break existing Windows functionality.

## Reflection

### How does running tests in CI/CD help maintain application stability?
CI/CD acts as a safety net. By running the full Pywinauto suite on every code change, we ensure that critical features (like the distraction blocker or the routine timer) are never broken by accident. It prevents "Regression Bugs" from reaching the actual users.

### What are the challenges of running GUI-based tests (Pywinauto) in CI/CD?
The biggest challenge is that Pywinauto requires a **Graphical User Interface (GUI)** to function. Standard CI servers are often "headless" (no screen). To fix this, we have to use Windows-based runners and ensure they are logged into a desktop session, otherwise, the script will fail because it can't find a "Window Handle."

### How can flaky tests be handled in a CI/CD environment?
*   **Auto-Retry:** The CI pipeline can be set to "Retry on Failure" up to 3 times before reporting a bug.
*   **Artifacts:** We configure the CI to save **Screenshots** or **Video Recordings** of the test run so we can see exactly what went wrong on the server.
*   **Environment Parity:** Ensuring the CI server has the exact same Windows version and screen resolution as a user's machine.

### What would be the next steps to fully integrate Focus Bear’s tests?
The next step would be to create a `.github/workflows/e2e-tests.yml` file. This would tell GitHub to:
1. Spin up a Windows Virtual Machine.
2. Install Python and Pywinauto.
3. Launch the Focus Bear app.
4. Run the test suite and upload the results.
