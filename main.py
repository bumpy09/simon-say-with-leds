def on_button_pressed_a():
    radio.send_number(1)
    edubitTrafficLightBit.set_led(LedColor.RED,
        edubitTrafficLightBit.digital_state_picker(DigitalIoState.ON))
    basic.pause(500)
    edubitTrafficLightBit.set_led(LedColor.RED,
        edubitTrafficLightBit.digital_state_picker(DigitalIoState.OFF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        edubitTrafficLightBit.set_led(LedColor.RED,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.ON))
        basic.pause(500)
        edubitTrafficLightBit.set_led(LedColor.RED,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.OFF))
    elif receivedNumber == 2:
        edubitTrafficLightBit.set_led(LedColor.YELLOW,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.ON))
        basic.pause(500)
        edubitTrafficLightBit.set_led(LedColor.YELLOW,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.OFF))
    elif receivedNumber == 3:
        edubitTrafficLightBit.set_led(LedColor.GREEN,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.ON))
        basic.pause(500)
        edubitTrafficLightBit.set_led(LedColor.GREEN,
            edubitTrafficLightBit.digital_state_picker(DigitalIoState.OFF))
    elif False:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
radio.on_received_number(on_received_number)

radio.set_group(1)
basic.show_icon(IconNames.HEART)