# -*- coding: utf-8 -*-x, y, z = 
"""
Created on Sat Apr 24 10:15:12 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random




x, y, z =mc.player.getPos()


mc.setSign(x, y ,z , 63, 0,"This","is","so","boring")


while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x,  hit.pos.y, hit.pos.z
        block = mc.getBlock(x, y ,z)
        print("the block id is:" + str(block))
        
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x,  hit.pos.y, hit.pos.z
        block = mc.getBlock(x, y ,z)
        mc.postToChat("the block id is:" + str(block))
        
        
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x,  hit.pos.y, hit.pos.z
        mc.setBlocks(x,y,z,x+2,y+2,z+2,57)
    
pos=mc.player.getTilePos()
while True:
    x = pos.x + random.uniform(20 ,-20)
    z = pos.z + random.uniform(20 , -20)
    y = pos.y +10
    mc.spawnEntity(x,y,z,50)
    time.sleep(0.1)
    
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x, y, z = hit.pos.x,  hit.pos.y, hit.pos.z
        mc.createExplosion(x,y,z)
        
        
        
        
        
        
        
        
        
        
        