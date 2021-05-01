# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:20:28 2021

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

x,y,z = mc.player.getTilePos()
for i in range(0, 30):
    for j in range(3):
        mc.setBlock(x+i+j,y-1,z+i, 1)
#   mc.setBlocks(x+i+1, y-1 ,z+i,x+i , y-1, z+i+1,1)
#  first way
#   mc.setBlock(x+i, y-1 ,z+i,1)
#   mc.setBlock(x+i+1, y-1 ,z+i,1)
#   mc.setBlock(x+i, y-1 ,z+i+1,1)      
        
# second way
#   mc.setBlocks(x+i+1, y-1 ,z+i,x+i , y-1, z+i+1,1)
        
x,y,z = mc.player.getTilePos()
mc.setBlocks(x-1, y+3, z-1,x+1,y+5, z+1, 20 )
mc.setBlocks(x, y, z, x,y+3,z, 17)