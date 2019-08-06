import pigpio
from time import sleep

pi = pigpio.pi()

r = [17, 0]
g = [22, 0]
b = [24, 255]

# Start with Blue 255
pi.set_PWM_dutycycle(b[0], b[1])

while(1):
  for i in range(255):
    r[1] += 1
    b[1] -= 1

    pi.set_PWM_dutycycle(r[0], r[1])
    pi.set_PWM_dutycycle(b[0], b[1])

    sleep(0.02)
  
  for i in range(255):
    g[1] += 1
    r[1] -= 1

    pi.set_PWM_dutycycle(g[0], g[1])
    pi.set_PWM_dutycycle(r[0], r[1])

    sleep(0.02)
  
  for i in range(255):
    b[1] += 1
    g[1] -= 1

    pi.set_PWM_dutycycle(b[0], b[1])
    pi.set_PWM_dutycycle(g[0], g[1])

    sleep(0.02)

