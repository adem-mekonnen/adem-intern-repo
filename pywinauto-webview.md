# Automating WebViews Inside the Windows App

## Research & Learning
Focus Bear uses **WebView2** to display its user interface. This requires a "Hybrid" automation strategy. I learned that while Pywinauto sees the application window, it cannot see the buttons inside the HTML content. To solve this, we connect Selenium to the application's remote debugging port (usually 9222).

## Reflection

### How do you detect WebView components in a Windows app?
Using **inspect.exe** or **Accessibility Insights**, a WebView usually appears as a `Pane` or `Document` control type with a ClassName like `Chrome_WidgetWin_1` or `WebView2Host`. Inside the app's dev environment, we can also use `Ctrl + Shift + I` to open standard browser DevTools if enabled.

### What is the difference between testing native Windows UI and WebViews?
*   **Native UI:** Elements are identified by `AutomationId` or `Name`. We use the Windows Accessibility tree.
*   **WebViews:** Elements are identified by `CSS Selectors`, `XPath`, or `ID`. We use the DOM (Document Object Model).
*   **Difference:** Native testing is about interacting with the OS; WebView testing is about interacting with HTML/JavaScript.

### How do Pywinauto (native) and Selenium (WebView via DevTools) work together?
They work as a "Double Team." Pywinauto handles the "Container" actions (moving the window, resizing, interacting with native title bars or system tray icons). Selenium handles the "Content" actions (filling out forms, clicking web buttons, and verifying text inside the UI). They communicate via a Shared Debugging Port.

### What challenges might arise when automating WebViews?
*   **Context Switching:** You have to manage two different drivers, which can make the code complex.
*   **Port Conflicts:** If the debugging port (9222) is already in use by another app or Chrome instance, the test will fail to connect.
*   **Synchronization:** You have to ensure that Pywinauto has opened the window fully before Selenium tries to connect to the WebView inside it, otherwise, the connection will be refused.
