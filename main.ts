radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        edubitTrafficLightBit.setLed(LedColor.Red, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.On))
        basic.pause(500)
        edubitTrafficLightBit.setLed(LedColor.Red, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.Off))
    } else if (receivedNumber == 2) {
        edubitTrafficLightBit.setLed(LedColor.Yellow, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.On))
        basic.pause(500)
        edubitTrafficLightBit.setLed(LedColor.Yellow, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.Off))
    } else if (receivedNumber == 3) {
        edubitTrafficLightBit.setLed(LedColor.Green, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.On))
        basic.pause(500)
        edubitTrafficLightBit.setLed(LedColor.Green, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.Off))
    } else if (receivedNumber == 4) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    edubitTrafficLightBit.setLed(LedColor.Red, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.On))
    basic.pause(500)
    edubitTrafficLightBit.setLed(LedColor.Red, edubitTrafficLightBit.digitalStatePicker(DigitalIoState.Off))
})
radio.setGroup(1)
basic.showIcon(IconNames.Heart)
