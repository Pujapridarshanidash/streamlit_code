import os
import time

def digital_clock():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        current_time = time.strftime("%H:%M:%S")

        print("=== Digital Clock ===\n")
        print(current_time.center(30))
        print("\nPress CTRL+C to stop")

        time.sleep(1)

digital_clock()