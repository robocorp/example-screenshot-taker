from datetime import datetime
from time import sleep
from pathlib import Path
import os
from sys import platform, exit

import pyautogui

# from pygetwindow import PyGetWindowException

IS_WIN = True if platform.lower() == "win32" else False

OUTPUT_DIR = f"screenshots_{int(datetime.timestamp(datetime.utcnow()))}"
FILE_NAME_TEMPLATE = f"{OUTPUT_DIR}/robocorp_recording_"
TRACK_TARGET_APP = False  # At this moment it is harcoded False, so the target app tracking does not work anyway.
TARGET_APP = "microsoft edge"


def _target_app_visible(title: str):
    if not title:
        return False
    parts = title.split("-")
    return parts[-1].lstrip().rstrip().lower() == TARGET_APP


def _check_output_sanity():
    return not Path(OUTPUT_DIR).exists()


def _take_screenshot(file_name):
    if IS_WIN and TRACK_TARGET_APP:
        if pyautogui.getActiveWindow() is not None and _target_app_visible(pyautogui.getActiveWindow().title):
            pyautogui.screenshot(file_name)
    else:
        pyautogui.screenshot(file_name)


def screenshot_task():
    init_time = datetime.utcnow()
    loop_break_init_time = datetime.utcnow()
    init_filename_index = 0

    try:
        if not _check_output_sanity():
            print("The output directory exists. Please FIRST empty it AND THEN delete it")
            exit(-1)
        
        os.mkdir(OUTPUT_DIR)
        print(f"The robot is taking screenshots in every 5 seconds now. And saving them in {OUTPUT_DIR}. Press Ctrl-C to stop",
              flush=True)
            
        while True:
            now_time = datetime.utcnow()

            loop_break_diff = now_time - loop_break_init_time
            if int(loop_break_diff.total_seconds()) >= 10800:
                # If the code is running more than 3 hours then break anyway.
                break
            
            diff = now_time - init_time
            if int(diff.total_seconds()) % 5 == 0:
                _take_screenshot(f"{FILE_NAME_TEMPLATE}{init_filename_index}.png")
                init_filename_index += 1
                init_time = now_time
                sleep(1)
    except KeyboardInterrupt:
        print("You closed the app")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    screenshot_task()