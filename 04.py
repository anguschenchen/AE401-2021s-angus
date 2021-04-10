# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:00:33 2021

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    mc = Minecraft.create()
    x , y, z=mc.player.getTilePos()
    a = mc.getBlock(x, y-1,z)
    b = mc.getBlock(x+5,y-1,z)
    c = mc.getBlock(x-5,y-1,z)
    d = mc.getBlock(x,y-1,z+5)
    e = mc.getBlock(x,y-1,z-5)
    f = mc.getBlock(x,y-5,z-5)
    if a ==8 or a ==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9 or e==8 or e==9 or f==8 or f==9:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,174)
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()   
x,y,z=mc.player.getTilePos()    
a=0
while a<20:
    mc.setBlocks(x+30,y-1,z,x-30,y-20,z,19)
    z=z+5
    a=a+1