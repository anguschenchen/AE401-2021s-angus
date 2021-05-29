# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:52:41 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


def buildPyramid(x, y, z):
    base = 10
    height = base//2 + 1
    for i in range(height):
        x1 = x + i
        
        y1 = y + i
        
        z1 = z + i
        
        x2 = x + base - i 
        
        z2 = x + base - i
        
        mc.setBlocks( x1, y1, z1, x2, y1, z2, 20)


x, y, z = mc.player.getTilePos()

buildPyramid( x, y, z)



