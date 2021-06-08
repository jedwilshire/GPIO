from gpiozero.tones import Tone
from gpiozero import TonalBuzzer
from time import sleep
A = Tone('A4')
B = Tone('B4')
C = Tone('C5')
D = Tone('D5')
E = Tone('E5')
F = Tone('F5')


notes = [A, B, C, B, A, A, B, C, E, B, C, A, D]
lengths = [.25, .25, 0.5, 0.5, 0.5, .25, .25, .25, .25, .25, .25, .5, 1.0]
tb = TonalBuzzer('BOARD12')
for i in range(len(notes)):
    tb.play(notes[i])
    sleep(lengths[i])
tb.stop()
    