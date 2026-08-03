from pywinauto.application import Application
import time

# Start Calculator
app = Application(backend="uia").start("calc.exe")
dlg = app.window(title="Calculator")

# Wait for it to be ready
dlg.wait('visible', timeout=10)
print("Calculator is open. Locking screen in 2 seconds...")
time.sleep(2)

# Try to click '5'
dlg.child_window(auto_id="num5Button").click()
print("Test Finished!")
