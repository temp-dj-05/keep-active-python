# import pyautogui
# import time

# def keep_mouse_active():
#     try:
#         while True:
#             # Move the mouse in a small square pattern
#             pyautogui.moveRel(10, 0, duration=0.25)  # Move right
#             pyautogui.moveRel(0, 10, duration=0.25)  # Move down
#             pyautogui.moveRel(-10, 0, duration=0.25) # Move left
#             pyautogui.moveRel(0, -10, duration=0.25) # Move up
#             time.sleep(180)  # Pause for 1 second

#     except pyautogui.FailSafeException:
#         print("Fail-safe triggered from moving the mouse to a corner.")
#     except KeyboardInterrupt:
#         print("Script stopped by user.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     keep_mouse_active()


import pyautogui
import time

def move_mouse_continuously(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.moveRel(10, 0, duration=0.25)  # Move right
        pyautogui.moveRel(0, 10, duration=0.25)  # Move down
        pyautogui.moveRel(-10, 0, duration=0.25) # Move left
        pyautogui.moveRel(0, -10, duration=0.25) # Move up
        time.sleep(1)  # Small pause between movements

def keep_mouse_active():
    try:
        print("Mouse moving script started. Press Ctrl+C to stop.")
        while True:
            print("Moving mouse for 5 minutes...")
            move_mouse_continuously(300)  # Move for 5 minutes (300 seconds)

            print("Pausing for 2 minutes...")
            time.sleep(120)  # Pause for 2 minutes (120 seconds)

    except pyautogui.FailSafeException:
        print("Fail-safe triggered from moving the mouse to a corner.")
    except KeyboardInterrupt:
        print("Script stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    keep_mouse_active()
