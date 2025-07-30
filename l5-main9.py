import random
import time

import tkinter as tk
from tkinter import messagebox 
from tkinter import simpledialog
import webbrowser

import sys
import subprocess

#Not have to type in the taskbar
def callback(url):
    webbrowser.open_new_tab(url)

# Function to create a Tkinter message box
def show_info(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, message)
    root.destroy()

def show_prompt(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = simpledialog.askstring(title, message)
    root.destroy()
    return result

def show_alert(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning(title, message)
    root.destroy()

def show_confirmation(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result

def check_requirements():
    try:
        import pyautogui
        import pytesseract
        return True
    except ImportError:
        return False
    
def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
        return False
    return True

def ter_read(name):
    name = pytes.image_to_string(pic, output_type=Output.DICT)
    extracted_string = name['text']
    print(extracted_string)
    extracted_string = str(extracted_string).replace('\n', '').replace(' -', ' ').replace('- ', ' ').replace(' - ', ' ').replace('-', ' ').replace(":","").replace("L","l").replace("  "," ")
    
    if extracted_string == "":
        time.sleep(1)

    return extracted_string
string = ""

show_info('Welcome', 'This program will automatically type text from the keybr.com website. \n'
'It will take a screenshot of the text and use OCR to extract it. \n')

while True:
    if not check_requirements():
        show_alert('Missing requirements', 'Pyautogui or Pytesseract Not Found\n')
        if show_confirmation('Install', 'Install requirements? \n'):
            install_package("pyautogui")
            install_package("pytesseract")
            if not check_requirements():
                show_alert('Error', 'Failed to install required packages. Please install them manually.')
                show_info('Instructions', 'Go to https://pypi.org/project/pyautogui/ and https://pypi.org/project/pytesseract/ to install the packages. \n'
                'After installation, run the program again.')
            break
        else:
            if show_confirmation('Quit', 'No installations are done, quit? \n'):
                show_info('Goodbye', 'You have chosen to exit the program. Goodbye!')
                exit()
            else:
                continue
    else:
        break

import pyautogui as pag
import pytesseract as pytes
from pytesseract import Output
pytes.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

screen = pag.size()
print(screen)
pag.click(screen.height, 0)


url = "https://www.keybr.com"
webbrowser.open(url)

while True:
    while True:
        in_type = show_prompt("Input", "Type how many times you want to run the code: \n")
        if in_type is None:
            if not show_confirmation('Confirmation', 'You have not entered a number. Continue? \n'):
                show_info('Goodbye', 'You have chosen to exit the program. Goodbye!')
                exit()
            else:
                continue
        try:
            in_type = int(in_type)
            if in_type <= 0:
                show_alert("Error", "You have entered a number less than or equal to 0. Please enter a number greater than 0: \n".upper())
                continue
            elif in_type > 50:
                if not show_confirmation("Really?", "Are you sure? May take a long time.: \n".upper()):
                    continue
            break
        except ValueError:
            show_alert("Error", "You have not entered a valid number. Please enter a valid number: \n".upper())
            continue

    show_info('Tip', 'Change your typing to English QWERTY. \n'
    'Move your mouse to any corners of the screen to stop the program.\n')

    screen = pag.size()
    print(screen)

    while in_type > 0:
        in_type -= 1
        while True:
            words_list = []

            random_number = random.uniform(0.035, 0.05) # Random typing interval to minimize detection
            pag.press('enter')

            time.sleep(2)
            pag.press('enter')
            pag.click(512, 500) #Teleport the mouse to screenshot
            screenshot = pag.screenshot(region=(325, 325, 750, 100))
            screenshot.save(r'keybr_screenshot.png')
            pic = r'keybr_screenshot.png'
            
            while True: #Check if the text was right
                for i in range(3):
                    words = ter_read(f"data-{i}")
                    words_list.append(words)
                
                if words_list[0] != words_list[1] != words_list[2]:
                    continue
                elif words_list[0] == words_list[1] == words_list[2]:
                    final_data = words_list[0]
                    break
                elif (words_list[0] != words_list[1] or words_list[0] != words_list[2]) and words_list[1] == words_list[2]:
                    final_data = words_list[2]
                    break
                elif (words_list[1] != words_list[2] or words_list[1] != words_list[0]) and words_list[0] == words_list[2]:
                    final_data = words_list[0]
                    break
                elif (words_list[2] != words_list[0] or words_list[2] != words_list[1]) and words_list[0] == words_list[1]:
                    final_data = words_list[1]
                    break
            
            print(f"{final_data}\n")

            pag.write(final_data, interval=random_number)
            random_number = random.uniform(0.035, 0.05) # Random typing interval to minimize detection
            break
        
    if not show_confirmation('Completed typing!', 'Do you want to proceed?'):
        show_info('Goodbye', 'You have chosen to exit the program. Goodbye!')
        exit()
    else:
        continue
