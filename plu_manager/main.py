import csv
import pyautogui
import subprocess
import keyboard
import time
import ctypes

FILE_NAME = "1234.xls"

COLUMNS = [
    "Hotkey", "Name", "LFCode", "Code", "Barcode Type", "Unit Price", "Unit Weight",
    "Unit Amount", "Department", "PT Weight", "Shelf Time", "Pack Type", "Tare", "Error(%)",
    "Message1", "Message2", "Label", "Discount/Table", "Account", "sPluFieldTitle20",
    "Account", "Recommend days", "nutrition", "Ice(%)"
]

def get_position(name):
    screen_width, screen_height = pyautogui.size()
    if screen_width == 1920 and screen_height == 1080:
        return {
            "confirm_file": (396, 68),
            "send": (825, 563)
        }.get(name)
    elif screen_width == 1024 and screen_height == 768:
        return {
            "confirm_file": (319, 60),
            "send": (404, 400)
        }.get(name)
    elif screen_width == 1366 and screen_height == 768:
        return {
            "confirm_file": (315, 56),
            "send": (569, 401)
        }.get(name)
    else:
        msg = f"⚠️ Unknown screen resolution: {screen_width}x{screen_height}"
        print(msg)
        ctypes.windll.user32.MessageBoxW(0, msg, "Screen Resolution Error", 0)
        return (0, 0)

def save_to_file(items):
    try:
        with open(FILE_NAME, "w", encoding="utf-16", newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(COLUMNS)
            for item in items:
                row = [
                    item["weight_code"], item["title"], item["weight_code"], item["weight_code"],
                    7, item["sale_cost"], 4, 0, 0, 0, 0, "Normal", 0, 5,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                ]
                writer.writerow(row)
        print("✅ File saved successfully:", FILE_NAME)
        return True
    except Exception as e:
        print("❌ Error saving file:", e)
        ctypes.windll.user32.MessageBoxW(0, f"Error saving file:\n{e}", "File Error", 0)
        return False

def run_bot(file_path):
    try:
        blocked_keys = ['esc', 'ctrl', 'alt', 'win', 'tab', 'shift', 'enter',
                        'backspace', 'delete', 'up', 'down', 'left', 'right']
        for key in blocked_keys:
            keyboard.block_key(key)

        pyautogui.FAILSAFE = False

        program_path = r"RLS1000\RTPLU.exe"
        subprocess.Popen(program_path)
        time.sleep(5)

        pyautogui.hotkey('alt', 'f')
        time.sleep(2)
        pyautogui.hotkey('alt', 'f')
        time.sleep(2)

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(3)

        pyautogui.click(*get_position("confirm_file"))
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(3)

        pyautogui.click(*get_position("send"))
        pyautogui.press('enter')
        pyautogui.press('enter')

        pyautogui.hotkey('alt', 'f4')
        keyboard.unhook_all()
        print("🟢 Bot completed. PLU Manager closed.")
        return True
    except Exception as e:
        print("❌ Bot error:", e)
        ctypes.windll.user32.MessageBoxW(0, f"Bot error:\n{e}", "Bot Error", 0)
        return False

def show_alert(message, title="Info"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

# 👉 Main function to call from outside
def run(items: list):
    if not items:
        print("❌ No items provided.")
        show_alert("No items provided.", "Error ❌")
        return

    if save_to_file(items):
        if run_bot(FILE_NAME):
            show_alert("Finished successfully!", "Done ✅")
        else:
            show_alert("Bot failed to run.", "Error ❌")
    else:
        show_alert("Failed to save file.", "Error ❌")
