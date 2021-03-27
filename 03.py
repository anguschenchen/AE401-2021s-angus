# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:57:10 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time 
mc = Minecraft.create()

x, y, z=mc.player.getTilePos()
mc.setBlock(x+1, y, z,169)
mc.setBlock(x+1, y, z-1,169)
mc.setBlock(x+1, y, z+1,169)
mc.setBlock(x, y, z+1,169)
mc.setBlock(x, y, z-1,169)
mc.setBlock(x-1, y, z,169)
mc.setBlock(x-1, y, z-1,169)
mc.setBlock(x-1, y, z+1,169)


x, y, z = mc.player.getTilePos()

mc.setBlocks(x, y ,z, x+15, y, z+10, 57)
x, y, z = mc.player.getTilePos()
mc.setBlocks(x+3, y, z, x+13, y+10, z+10, 169 )
mc.setBlocks(x+4, y+1, z+1, x-12, y+9, z+9, 0)