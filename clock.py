from board import I2C
from adafruit_ht16k33.segments import Seg7x4
from time import strftime
from gpiozero import Button
i2c = I2C()
display = Seg7x4(i2c, address=0x70)
button = Button('BOARD33')
while not button.is_pressed:
    display.print(strftime('%M') + ":" + strftime('%S'))
display.fill(0)