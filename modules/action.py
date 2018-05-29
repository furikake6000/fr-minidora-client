# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Action(object):
    def __init__(self):
        pass

    @abstractmethod
    def activate(self):
        # Called when action activated
        pass
    
    @abstractmethod
    def update(self):
        # Called every frame while action is activated
        pass

    @abstractmethod
    def deactivate(self):
        # Called when action deactivated
        pass