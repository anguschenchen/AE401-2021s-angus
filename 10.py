# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:56:49 2021

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from time import sleep
import random


x, y, z = mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,5)
    if r == 1:
        mc.setBlocks(x, y, z, x+4, y, z, 1)
        x += 4
    elif r == 2:
        mc.setBlocks(x, y, z, x-4, y, z, 1)
        x -= 4
    elif r == 3:
        mc.setBlocks(x, y, z, x, y, z+4, 1)
        z += 4
    elif r == 4:
        mc.setBlocks(x, y, z, x, y, z-4, 1)
        z -= 4

        
while True:
    mc.executeCommand('time add 50')
    sleep(0.5)
        

    