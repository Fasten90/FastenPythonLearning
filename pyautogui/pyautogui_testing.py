# https://automatetheboringstuff.com/chapter18/

import pyautogui
import subprocess
from time import sleep


width, height = pyautogui.size()



# Start on new thread
subp = subprocess.Popen(['calc.exe'])

sleep(2)

calc_1_location = pyautogui.locateOnScreen('calc.exe_1.png')
calc_2_location = pyautogui.locateOnScreen('calc.exe_2.png')

mouse_speed = 0.25

# Top left corner
#pyautogui.moveTo(windows_real_start_x, windows_real_start_y, duration=mouse_speed)

print(calc_1_location)
print(calc_2_location)
button_width = calc_2_location[0] - calc_1_location[0]

width_button = calc_1_location[2]
height_button = calc_1_location[3]

number_1_x = calc_1_location[0]
number_1_y = calc_1_location[1]

pyautogui.moveTo(number_1_x, number_1_y)

sleep(1)

pyautogui.moveRel(int(width_button/2), int(height_button/2))

sleep(1)

# Click to the 'Calc - 1 number'
pyautogui.click(button='left')

sleep(1)

# Go got 3 buttons right, for 'Calc + button'
pyautogui.moveRel(button_width*3, 0, duration=mouse_speed)

sleep(1)

pyautogui.click(button='left')

sleep(1)

# Go back to 'Calc - 1 number button'
pyautogui.moveRel(button_width*(-3), 0, duration=mouse_speed)

sleep(1)

pyautogui.click(button='left')

sleep(1)

# Go to 'Calc equation '=' sign'
pyautogui.moveRel(button_width*3, height_button, duration=mouse_speed)

sleep(1)

pyautogui.click(button='left')

#pyautogui.typewrite()


subp.terminate()


