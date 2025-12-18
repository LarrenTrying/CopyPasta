import pyperclip
import pyautogui
import keyboard
import time

TYPING_SPEED = 0.08
CHECK_INTERVAL = 0.005

print("F8 → start typing clipboard")
print("F9 → stop typing instantly")

def interruptible_sleep(duration):
    start = time.time()
    while time.time() - start < duration:
        if keyboard.is_pressed('f9'):
            return False
        time.sleep(CHECK_INTERVAL)
    return True

def type_clipboard():
    text = pyperclip.paste()
    if not text:
        return

    
    time.sleep(0.15)

    for char in text:
        
        if keyboard.is_pressed('f9'):
            print("Typing stopped.")
            break

        pyautogui.write(char)

        if not interruptible_sleep(TYPING_SPEED):
            print("Typing stopped.")
            break

keyboard.add_hotkey('f8', type_clipboard)

keyboard.wait()

