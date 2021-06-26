# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 09:57:42 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
from random import randrange

for i in range(10):
    x, y, z = mc.player.getTilePos()
    x = x+i
    for j in range(10):
        r = randrange(0,16)
        z = z+1
        mc.setBlock(x, y, z, 35, r)


r = randrange(1,16)
while True:
    hits = mc.events.pullBlockHits()
    if len(hits)>0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == r:
            mc.postToChat("congrates you found it")
            mc.setBlock(hit.pos,57)
            break
        elif data<r:
            mc.postToChat("the id is lower then the block id")
        elif data>r:
            mc.postToChat("the id is higher then the block id")
            
            
            
            
def linearSearch():
    for i in range (1000001):
        if i==r:
            return i
    
def binarySearch():
    low = 0
    high = 100000000
    
    while low>=high:
        mid = (low + high)//2
        
        if mid>r:
            high = mid-1
        elif mid<r:
            low = mid+1
        else:
            return mid
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            