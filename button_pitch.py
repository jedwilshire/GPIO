from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
button = Button('BOARD37')
exit_button = Button('BOARD33')
tb = TonalBuzzer('BOARD12')
a4 = Tone('A4')
b4 = Tone('B4')
while not exit_button.is_pressed:
    if button.is_pressed:
        tb.play(a4)
        sleep(1)
        tb.play(b4)
        sleep(1)
        tb.stop()
    else:
        tb.stop()