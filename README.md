# Albion Seller

An automated script for selling items in Albion Online. This script automates the process of clicking through inventory items and selling them at the market.

## Features

- **Auto-detects screen resolution**: Automatically adapts to your screen size
- **Auto-scales coordinates**: Adjusts mouse positions based on your resolution (originally designed for 2560x1440)
- **Customizable inventory rows**: Input the number of rows in your inventory
- **Automated selling workflow**: Clicks through each item and sells it

## Requirements

- Python 3.x
- pyautogui

## Installation

1. Install the required dependency:
```bash
pip install pyautogui
```

## Usage

1. Run the script:
```bash
python AlbionSeller.py
```

2. When prompted, enter the number of rows in your inventory

3. The script will automatically:
   - Detect your screen resolution
   - Scale the coordinates accordingly
   - Click through each inventory item
   - Sell each item at the market

## How It Works

The script uses pyautogui to automate mouse movements and clicks. It:
- Detects your current screen resolution
- Calculates scaling factors based on the original 2560x1440 resolution
- Scales all coordinates to match your screen size
- Iterates through your inventory (rows × 4 columns)
- Performs the selling sequence for each item

## Important Notes

- Make sure Albion Online is martketplace is open and positioned it correctly before running
- The script assumes a 4-column inventory layout
- Coordinates may need adjustment if the game UI changes
- Use at your own risk - automation may violate game terms of service

Run like this ✅ : <img width="539" height="486" alt="image" src="https://github.com/user-attachments/assets/84be44fe-1cea-4f00-b0ba-2bc23d7f6580" />



Not like THIS ✖️ : <img width="794" height="425" alt="image" src="https://github.com/user-attachments/assets/682eaa46-8c84-4cce-bbe3-a5efb62ab1e6" />


## License

This project is open source and available for educational purposes.
