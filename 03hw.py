# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:19:37 2021

@author: -
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x , y, z=mc.player.getTilePos()
mc.setBlocks(x+5, y, z, x+7, y+2, z, 35,1)
mc.setBlocks(x+5, y-1,z+1, x+7 , y-1 , z+3, 35)
mc.setBlocks(x+8, y, z+1, x+8 , y+2, z+3, 35, 5)
mc.setBlocks(x+5, y, z+4, x+7, y+2, z+4, 35,14)
mc.setBlocks(x+5, y+3,z+1, x+7 , y+3 , z+3, 35,4)
mc.setBlocks(x+4, y, z+1, x+4 , y+2, z+3, 35, 3)