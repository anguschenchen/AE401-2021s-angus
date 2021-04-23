# -*- coding: utf-8 -*-/
"""
Created on Fri Apr 23 18:25:45 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x, y, z=mc.player.getTilePos()
    a = mc.getBlock(x, y-1,z)
    if a == 2:
        mc.setBlock(x, y, z, 8)