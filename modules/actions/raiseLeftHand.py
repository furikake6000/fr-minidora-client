# -*- coding: utf-8 -*-
import random
from minidora import Minidora
from minidora.servo_motor import ServoMotorData

from .action import Action

class RaiseLeftHand(Action):
    def __init__(self):
        super().__init__()
        self.m = Minidora(self_host='0.0.0.0', minidora_host='minidora-v0-yayoi.local')

    def activate(self):
        # Called when action activated
        super().activate()

        smdata = ServoMotorData()
        smdata.arm.left = 1.0
        self.m.move_servo_motor(smdata)
    
    def update(self):
        # Called every frame while action is activated
        super().update()

    def deactivate(self):
        # Called when action deactivated
        super().deactivate()

        smdata = ServoMotorData()
        smdata.arm.left = 0.0
        self.m.move_servo_motor(smdata)
