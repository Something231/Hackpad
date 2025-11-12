#note this is just the example code but modified.
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rotary import RotaryEncoder
from kmk.modules.neopixel import NeoPixel


keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1, board.GP27]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

leds = NeoPixel(
    pin=board.GP6,
    n=2,
    bpp=3,
    brightness=0.4
)
keyboard.modules.append(leds)

leds.pixels[0] = (255, 141, 162)
leds.pixels[1] = (240, 255, 141)

keyboard.keymap = [
    [KC.MACRO("No"), KC.MACRO("Yes"), KC.MACRO("Hello"), KC.MACRO("Goodbye"), KC.E],
]

encoder = RotaryEncoder(
    pin1=board.GP29,
    pin2=board.GP28,
    clockwise_key=KC.VOLUME_UP,
    counter_clockwise_key=KC.VOLUME_DOWN
)
keyboard.modules.append(encoder)


if __name__ == '__main__':
    keyboard.go()