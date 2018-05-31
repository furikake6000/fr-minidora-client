import cv2
import time
import random
from minidora import Minidora
from minidora.servo_motor import ServoMotorData

m = Minidora(self_host='0.0.0.0', minidora_host='minidora-v0-yayoi.local')

if __name__ == "__main__":
    while(True):
        smdata = ServoMotorData()
        smdata.arm.left = 1.0
        smdata.arm.right = 1.0
        smdata.head.roll = 0.0
        m.move_servo_motor(smdata)
        time.sleep(10.0)