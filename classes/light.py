import pigpio

# pi.set_PWM_dutycycle(r[0], r[1])
# red - 17
# green - 22
# blue - 24


class Light:
  def __init__(self, p_red, p_green, p_blue):
    self.red = 0
    self.green = 0
    self.blue = 0

    self.portRed = p_red
    self.portGreen = p_green
    self.portBlue = p_blue

    self.pi = pigpio.pi()

  def set_color(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
  
  def update_lights(self):
    self.pi.set_PWM_dutycycle(self.portRed, self.red)
    self.pi.set_PWM_dutycycle(self.portGreen, self.green)
    self.pi.set_PWM_dutycycle(self.portBlue, self.blue)
  
  def change_color(self, status):
    if status == "Offline":
      self.set_color(0, 0, 0)       # Off
    
    elif status in ["Error", "Cancelling"]:
      self.set_color(255, 0, 0)     # Red

    elif status == "Printing":
      self.set_color(120, 120, 120) # White

    elif status in ["Pausing", "Paused"]:
      self.set_color(255, 255, 0)   # Yellow

    elif status == "Operational":
      self.set_color(0, 255, 0)     # Green

    self.update_lights()
