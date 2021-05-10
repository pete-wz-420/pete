from time import sleep
from gpiozero import *
from yeelight import Bulb
bulb = Bulb("192.168.1.69")

pir = MotionSensor(12)

while True:

    pir.wait_for_motion()
    bulb.set_rgb(255,0,0)
    bulb.set_rgb(0,0,255)
    bulb.set_rgb(255, 0, 0)
    bulb.set_rgb(0, 0, 255)
    sleep(5)




