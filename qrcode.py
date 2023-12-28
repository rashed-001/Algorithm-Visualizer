# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 00:16:18 2022

@author: Rashedul Alam
"""


import qrcode
data="msg"
img=qrcode.make(data=data)
img.save("scmg.png")
