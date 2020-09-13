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