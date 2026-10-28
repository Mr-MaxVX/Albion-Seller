import pyautogui

COLUMNS = 4
Gate = True

# Auto-detect screen resolution
screen_width, screen_height = pyautogui.size()
print(f"Detected screen resolution: {screen_width}x{screen_height}")

# Original resolution the coordinates were designed for
original_width = 2560
original_height = 1440

# Calculate scaling factors
scale_x = screen_width / original_width
scale_y = screen_height / original_height
print(f"Scaling factors: X={scale_x:.2f}, Y={scale_y:.2f}")

# Scale coordinates
def scale_coords(x, y):
    return int(x * scale_x), int(y * scale_y)

while(Gate == True):
    try:
        Rows = int(input("What is the number of rows in your inventory?"))
        Gate = False
    except ValueError:
        print("The entered vlaue is not numeric please try again...")
        Gate = True
        continue

for i in range(0, Rows*COLUMNS):
    
    ## in scope
    pyautogui.moveTo(*scale_coords(1285, 418))
    pyautogui.click()
    
    ## Click Item
    pyautogui.moveTo(*scale_coords(1707, 576))
    pyautogui.click()
    

    ## Decrease the price
    pyautogui.moveTo(*scale_coords(1104, 841))
    pyautogui.click()
    
    ## Sell the item
    pyautogui.moveTo(*scale_coords(1539, 971))
    pyautogui.click()
    

print("Finish")


