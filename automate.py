import pyautogui as screen
import string
import random

pos = screen.position()
print(pos)
textx = 921 
texty = 966
screen.FAILSAFE=False
sendx = 1848
sendy = 967
screen.moveTo(textx,texty, duration = 0.01) 
for i in range(1):
     message = "divesh is "+''.join(random.  choices(string.ascii_lowercase, k=10))
     screen.moveTo(textx,texty, duration = 0.000001)   
     screen.click(textx,texty,1,0.000001,'left')
     screen.typewrite(message,0.000001)
     screen.moveTo(sendx,sendy, duration = 0.000001)   
     screen.click(sendx,sendy,1,0.000001,'left')
