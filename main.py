import pigpio
from time import sleep
import requests
import json

pi = pigpio.pi()

# pi.set_PWM_dutycycle(r[0], r[1])
# red - 17
# green - 22
# blue - 24

class Light:
  def __init__(self, pRed, pGreen, pBlue):
    self.red = 0
    self.green = 0
    self.blue = 0

    self.portRed = pRed
    self.portGreen = pGreen
    self.portBlue = pBlue

  def setColor(self, r, g, b):
    self.red = r
    self.green = g
    self.blue = b
  
  def updateLights(self):
    pi.set_PWM_dutycycle(self.portRed, self.red)
    pi.set_PWM_dutycycle(self.portGreen), self.green)
    pi.set_PWM_dutycycle(self.portBlue, self.blue)
  
  def changeColor(self, status):
    if status == "Offline":
      self.setColor(0, 0, 0)       # Off
    
    elif status == "Error" or status == "Cancelling":
      self.setColor(255, 0, 0)     # Red

    elif status == "Printing":
      self.setColor(120, 120, 120) # White

    elif status == "Pausing" or status == "Paused":
      self.setColor(255, 255, 0)   # Yellow

    elif status == "Operational":
      self.setColor(0, 255, 0)     # Green

    self.updateLights()


if __name__ == "__main__":
  Light light(17, 22, 24);
  prev_status = ""

  while True:
    r = json.loads(requests.get('http://127.0.0.1:3004/api/job').json())

    # If status hasn't changed -> Wait 2/3 of expected time remaining
    # 2sec < ETR < 5h 
    time = 0
    if r["state"] == prev_status:
      if r["progress"]["printTimeLeft"] < 2:
        time = 2
      elif r["progress"]["printTimeLeft"] > 18000:
        time = 3600
      else:
        time = (2/3) * r["progress"]["printTimeLeft"]

      sleep(time)

    else:  # Update lighting
      prev_status = r["state"]
      light.changeColor(status)
