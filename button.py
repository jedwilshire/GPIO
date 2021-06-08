from gpiozero import Button, Buzzer
buzz_button = Button('BOARD37')
exit_button = Button('BOARD33')
buzzer = Buzzer('BOARD12')
while not exit_button.is_pressed:
    if buzz_button.is_pressed:
        buzzer.on()
    else:
        buzzer.off()