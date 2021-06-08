#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# License: https://github.com/rm-hull/luma.led_matrix/blob/master/LICENSE.rst
# Github link: https://github.com/rm-hull/luma.led_matrix/

# Import all the modules 
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

  

# cascaded = Number of cascaded MAX7219 LED matrices, default=1
# block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
# rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   

# create matrix device
serial = spi(device=1,  gpio=noop())
device = max7219(serial, rotate= 3)

   
show_message(device, "Hello!", fill="white")
show_message(device, "Hello!", fill="white", font=proportional(SINCLAIR_FONT), scroll_delay=0.1)
show_message(device, "Hello!", fill="white", font=proportional(TINY_FONT), scroll_delay=0.1)
show_message(device, "Hello!", fill="white", font=proportional(CP437_FONT), scroll_delay=0.3)


  

