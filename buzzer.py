from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer('BOARD12')
buzzer.on()
sleep(1)
buzzer.off()