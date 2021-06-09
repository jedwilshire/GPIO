from gpiozero import DistanceSensor, Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
ds = DistanceSensor(echo = 'BOARD32', trigger = 'BOARD36')
button = Button('BOARD33')
tb = TonalBuzzer('BOARD12')
while not button.is_pressed:
    dist = ds.distance * 300
    #print('Distance:', dist)
    tone = Tone(dist + 250)
    tb.play(tone)
    sleep(.01)
tb.stop()