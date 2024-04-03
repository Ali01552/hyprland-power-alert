# hyprland-power-alert
This simple Python script monitors your battery level and sends notifications when it gets low. If the battery level reaches a critically low level, it will force your system to sleep to prevent data loss.

## Features

- Sends notifications when battery level is low
- Forces system to sleep when battery level is critically low
- Runs continuously in the background

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ali01552/hyprland-power-alert.git
   sudo pacman -S python-psutil notify-send  # Arch Linux
   ```
2. Run the app on startup

## Testing in Hyprland

This script has been tested in Arch Linux with Hyprland and works as expected.
