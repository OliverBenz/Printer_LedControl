import pigpio
from time import sleep
import requests
import json

pi = pigpio.pi()

# Get print status
# Read expected time remaining
# Make new call when 2/3 of expected time remaining are done
# if ETR < 2 sec -> wait 2 sec
# if ETC > 5h -> wait 1h

def getValues():
  return json.loads(requests.get('http://127.0.0.1:3004/api/job').json())

# pi.set_PWM_dutycycle(r[0], r[1])
# red - 17
# green - 22
# blue - 24

def updateLight(red, green, blue):
  pi.set_PWM_dutycycle(17, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(24, blue)

# TODO: Check if colors look good over camera
# 255 might be too bright
def changeLight(status):
  if status == "Offline":
    # No light
    updateLight(0, 0, 0)

  if status == "Error" or status == "Cancelling":
    # Red light
    updateLight(255, 0, 0)

  if status == "Printing":
    # White light
    updateLight(120, 120, 120)

  if status == "Pausing" or status == "Paused":
    # Yellow light
    updateLight(255, 255, 0)

  if status == "Operational":
    # Green light
    updateLight(0, 255, 0)


if __name__ == "__main__":
  status = ""
  r = getValues()
  # BUG: What is timeremainvalue if print is done? Wait some time if print is done
  # TODO: If print is done -> check for changed status every 5min??

  # If status hasn't changed -> Wait 2/3 of expected time remaining
  # 2sec < ETR < 5h 
  time = 0
  if r["state"] == status:
    if r["progress"]["printTimeLeft"] < 2:
      time = 2
    elif r["progress"]["printTimeLeft"] > 18000:
      time = 3600
    else:
      time = (2/3) * r["progress"]["printTimeLeft"]

    sleep(time)

  else:
    status = r["state"]
    changeLight(status)