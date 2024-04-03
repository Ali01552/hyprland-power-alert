import psutil
import subprocess
import time

subprocess.run(["notify-send", f"Running Power-Alert-System"], check=True)


def send_notification(percent):
    subprocess.run(["notify-send", f"Battery low: {percent}%"], check=True)

def force_sleep():
    subprocess.run(["systemctl", "suspend"], check=True)

while True:
	battery = psutil.sensors_battery()
	percent = int(battery.percent)

	if percent <= 20 and not battery.power_plugged:
		send_notification(percent)

	if percent <= 5 and not battery.power_plugged:
		force_sleep()
	
	time.sleep(60) # check every 60 seconds

subprocess.run(["notify-send", f"Power Alert System is down"], check=True)
