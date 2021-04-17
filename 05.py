# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:18:00 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x, y ,z = mc.player.getTilePos()
blockType = int(input("Put in block ID"))

mc.setBlock(x, y ,z, blockType)