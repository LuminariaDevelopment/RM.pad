import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
from kmk.modules.layers import Layers
from kmk.modules.encoder import RotaryEncoder
from kmk.extensions.RGB import RGB
from kmk.extensions.midi import Midi

keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)
keyboard.col_pins = (board.GP29, board.GP06, board.GP07)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
macros = Macros()
media = MediaKeys()
midi = Midi()
keyboard.modules.append(layers)
keyboard.modules.append(macros)
keyboard.extensions.append(media)
keyboard.extensions.append(midi)

rgb = RGB(
    pixel_pin=board.GP0,
    num_pixels=3,
    val_default=150,
)
keyboard.extensions.append(rgb)

DEEP_BLUE = (0, 119, 255)
SKY_BLUE = (152, 216, 255)
WHITE = (255, 255, 255)

encoder = RotaryEncoder()
encoder.pins = ((board.GP03, board.GP04, None, False),)
encoder.map = (
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
    ((KC.PGUP, KC.PGDN, KC.HOME),),
    ((KC.MIDI_CC(1), KC.MIDI_CC(2), KC.NO),),
)
keyboard.modules.append(encoder)

class LayerColorKey:
    def __init__(self):
        self.current_layer = 0
    
    def toggle(self, *args):
        self.current_layer = (self.current_layer + 1) % 3
        if self.current_layer == 0:
            rgb.set_rgb_fill(DEEP_BLUE)
            keyboard.active_layers = [0]
        elif self.current_layer == 1:
            rgb.set_rgb_fill(SKY_BLUE)
            keyboard.active_layers = [1]
        else:
            rgb.set_rgb_fill(WHITE)
            keyboard.active_layers = [2]

lc_key = LayerColorKey()

keyboard.keymap = [
    [
        KC.LWIN(KC.R), KC.LCTRL(KC.T), KC.LCTRL(KC.L),
        KC.LWIN(KC.D), KC.LALT(KC.F4), KC.LWIN(KC.UP),
        KC.ANY(lc_key.toggle), KC.MACRO("ggs"), KC.LWIN(KC.L),
    ],
    [
        KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT, KC.MEDIA_PREV,
        KC.RGB_TOG, KC.RGB_ANI, KC.RGB_MODE_PLAIN,
        KC.ANY(lc_key.toggle), KC.NO, KC.RESET,
    ],
    [
        KC.MIDI_NOTE(60), KC.MIDI_NOTE(62), KC.MIDI_NOTE(64),
        KC.MIDI_NOTE(65), KC.MIDI_NOTE(67), KC.MIDI_NOTE(69),
        KC.ANY(lc_key.toggle), KC.MIDI_NOTE(71), KC.MIDI_NOTE(72),
    ]
]

if __name__ == '__main__':
    rgb.set_rgb_fill(DEEP_BLUE)
    keyboard.go()