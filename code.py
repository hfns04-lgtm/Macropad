import time
import displayio  # type: ignore
import terminalio
import usb_hid
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Macro labels group
macro_group = displayio.Group()
macro_labels = []
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    lbl = label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                      anchored_position=((macropad.display.width - 1) * x / 2,
                                         macropad.display.height - 1 - (3 - y) * 12),
                      anchor_point=(x / 2, 1.0))
    macro_labels.append(lbl)
    macro_group.append(lbl)

rect = Rect(0, 0, macropad.display.width, 13, fill=0xFFFFFF)
macro_group.append(rect)
macro_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                               anchored_position=(macropad.display.width // 2, 0),
                               anchor_point=(0.5, 0.0)))

root_group = displayio.Group()
root_group.append(macro_group)
macropad.display.root_group = root_group
mouse = Mouse(usb_hid.devices)

# Hardcoded macro groups
apps = [
    {
        'name': '',
        'macros': [
            (0x000000, '      O', ['Kushkush024!', {'tone': 131}]),
            (0x000000, '', ['Kushkush024!', {'tone': 131}]),
            (0x000000, 'O      ', ['Kushkush024!', {'tone': 131}]),
            (0x000000, '', ['2004119180743', {'tone': 131}]),
            (0x000000, '_', ['2004119180743', {'tone': 131}]),
            (0x000000, '', ['2004119180743', {'tone': 131}]),
            (0x000000, '', ['2004119180743', {'tone': 131}]),
            (0x000000, '', ['2004119180743', {'tone': 131}]),
            (0x000000, '', ['2004119180743', {'tone': 131}]),
            (0x000000, 'SLEEP', [Keycode.WINDOWS, 'x', -Keycode.WINDOWS, 0.5, 'g', 0.5, 's', {'tone': 131}]),
            (0x000000, '  RESTART', [Keycode.WINDOWS, 'x', -Keycode.WINDOWS, 0.5, 'g', 0.5, 'r', {'tone': 131}]),
            (0x000000, 'OFF', [Keycode.WINDOWS, 'x', -Keycode.WINDOWS, 0.5, 'g', 0.5, 'a', {'tone': 131}]),
        ]
    },
    {
        'name': '=+=+=+=+=[ HOME 0]=+=+=+=+=',
        'macros': [
            (0x000000, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, Keycode.LEFT_ALT, 'm', {'tone': 131}]),
            (0x000000, 'TaskMng', [Keycode.WINDOWS, Keycode.R, -Keycode.R, -Keycode.WINDOWS, 0.3, 'taskmgr', Keycode.ENTER, -Keycode.ENTER, {'tone': 131}]),
            (0x000000, 'Deafen', [Keycode.CONTROL, Keycode.SHIFT, '.', {'tone': 131}]),
            (0x000000, 'VOL+', [[ConsumerControlCode.VOLUME_INCREMENT]], 0.1, {'tone': 131}),
            (0x000000, 'VOL 0', [[ConsumerControlCode.MUTE]], {'tone': 131}),
            (0x000000, 'VOL-', [[ConsumerControlCode.VOLUME_DECREMENT]], 0.1, {'tone': 131}),
            (0x000000, 'Ttours', [Keycode.CONTROL, Keycode.SHIFT, 'i', Keycode.F12, -Keycode.F12, -Keycode.SHIFT, -Keycode.CONTROL, {'tone': 131}]),
            (0x000000, 'winG', [Keycode.WINDOWS, 'g', {'tone': 131}]),
            (0x000000, 'Clip', [Keycode.CONTROL, Keycode.SHIFT, ']', {'tone': 131}]),
            (0x000000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK], {'tone': 131}]),
            (0x000000, '||/>', [[ConsumerControlCode.PLAY_PAUSE], {'tone': 131}]),
            (0x000000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK], {'tone': 131}]),
        ]
    },
    {
        'name': '=+=+=+=+=[ HOME 1 ]=+=+=+=+=',
        'macros': [
            (0x000000, 'ver', [{'move_x': -1920, 'move_y': 0, 'steps': 1, 'step_delay': 0}, Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, -Keycode.LEFT_ALT, -Keycode.CONTROL, {'tone': 131}]),
            (0x000000, 'hor', [{'move_x': -1920, 'move_y': 0, 'steps': 1, 'step_delay': 0}, Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.LEFT_ARROW, -Keycode.LEFT_ARROW, -Keycode.LEFT_ALT, -Keycode.CONTROL, {'tone': 131}]),
            (0x000000, 'disp2 on', [Keycode.WINDOWS, 'r', -Keycode.WINDOWS, 0.3, 'powershell Start-ScheduledTask -TaskName "poopoofartnigga2"', Keycode.ENTER, -Keycode.ENTER, {'tone': 131}]),
            (0x000000, 'disp2 off', [Keycode.WINDOWS, Keycode.R, -Keycode.R, -Keycode.WINDOWS, 0.4, 'schtasks /run /tn "poopoofartnigga3"', Keycode.ENTER, -Keycode.ENTER, {'tone': 131}]),
            (0x000000, 'audrly', [Keycode.WINDOWS, Keycode.R, -Keycode.R, -Keycode.WINDOWS, 0.4, 'schtasks /run /tn "auduorelay"', Keycode.ENTER, -Keycode.ENTER, {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
        ]
    },
    {
        'name': '=+=+=+=+=[ SPAM ]=+=+=+=+=',
        'macros': [
            (0x000000, 'Balls', [Keycode.ENTER, 0.5, 'Balls', Keycode.ENTER, {'tone': 131}]),
            (0x000000, 'Quiros', [Keycode.ENTER, 0.5, 'Adrian Quiros Salazar', Keycode.ENTER, {'tone': 131}]),
            (0x000000, 'lastmsg', [1.0, Keycode.UP_ARROW, -Keycode.UP_ARROW, Keycode.ENTER, -Keycode.ENTER], 4.4),
            (0x000000, 'lmfast', [1.0, Keycode.UP_ARROW, -Keycode.UP_ARROW, Keycode.ENTER, -Keycode.ENTER], 2.4),
            (0x000000, 'lmslow', [1.0, Keycode.UP_ARROW, -Keycode.UP_ARROW, Keycode.ENTER, -Keycode.ENTER], 7.4),
            (0x000000, 'c', ['C', {'tone': 131}],0.03),
(0x000000, 'ChatLoop', [
    {'move_x': -10000, 'move_y': -10000, 'steps': 1, 'step_delay': 0},
    {'move_x': 100, 'move_y': 1355, 'steps': 1, 'step_delay': 0},
    {'buttons': 1}, {'buttons': -1},
    2.0,
    {'move_x': -10000, 'move_y': -10000, 'steps': 1, 'step_delay': 0},
    {'move_x': 100, 'move_y': 1855, 'steps': 1, 'step_delay': 0},
    {'buttons': 1}, {'buttons': -1},
    2.0
], 2.0),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, '', ['', {'tone': 131}]),
            (0x000000, 'alt', [Keycode.WINDOWS, 'r', -Keycode.WINDOWS, 0.3, 'powershell Start-ScheduledTask -TaskName "altspam2"', Keycode.ENTER, -Keycode.ENTER, {'tone': 131}]),
        ]
    },

]

class App:
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        macro_group[13].text = self.name
        rect.fill = 0xFFFFFF if self.name else 0x000000
        for i in range(12):
            if i < len(self.macros):
                macropad.pixels[i] = self.macros[i][0]
                macro_labels[i].text = self.macros[i][1]
            else:
                macropad.pixels[i] = 0
                macro_labels[i].text = ''
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

app_objects = [App(app) for app in apps]
last_position = macropad.encoder
app_index = 0
app_objects[app_index].switch()

# State for toggling loops and last fired time
loop_enabled = [False] * 12
last_fired = [0.0] * 12

def run_macro_sequence(seq):
    for item in seq:
        if isinstance(item, int):
            if item >= 0:
                macropad.keyboard.press(item)
            else:
                macropad.keyboard.release(-item)

        elif isinstance(item, float):
            time.sleep(item)

        elif isinstance(item, str):
            macropad.keyboard_layout.write(item)

        elif isinstance(item, list):
            for code in item:
                if isinstance(code, int):
                    macropad.consumer_control.press(code)
                    macropad.consumer_control.release()
                elif isinstance(code, float):
                    time.sleep(code)

        elif isinstance(item, dict):
            # Mouse move
            if 'move_x' in item or 'move_y' in item:
                steps = item.get('steps', 1)
                delay = item.get('step_delay', 0.01)
                dx = item.get('move_x', 0) // steps
                dy = item.get('move_y', 0) // steps
                for _ in range(steps):
                    macropad.mouse.move(dx, dy)
                    time.sleep(delay)

            # Mouse buttons
            if 'buttons' in item:
                if item['buttons'] >= 0:
                    macropad.mouse.press(item['buttons'])
                else:
                    macropad.mouse.release(-item['buttons'])

            # Scroll or fine move
            if 'x' in item or 'y' in item or 'wheel' in item:
                macropad.mouse.move(item.get('x', 0), item.get('y', 0), item.get('wheel', 0))

            # Tone
            if 'tone' in item:
                macropad.stop_tone()
                if item['tone'] > 0:
                    macropad.start_tone(item['tone'])
                time.sleep(0.2)
                macropad.stop_tone()

            # Audio file
            if 'play' in item:
                macropad.play_file(item['play'])


while True:
    # Handle encoder page turning
    position = macropad.encoder
    if position != last_position:
        last_position = position
        app_index = position % len(app_objects)
        app_objects[app_index].switch()
        # Reset loops on app switch if you want
        loop_enabled = [False] * 12

    event = macropad.keys.events.get()
    now = time.monotonic()

    if event:
        key = event.key_number
        if key >= len(app_objects[app_index].macros):
            continue

        macro = app_objects[app_index].macros[key]
        color, label_txt, seq, *maybe_interval = macro
        interval = maybe_interval[0] if maybe_interval else None

        if event.pressed:
            if interval is not None:
                # Toggle loop on/off
                loop_enabled[key] = not loop_enabled[key]
                macropad.pixels[key] = 0xFFFFFF if loop_enabled[key] else color
                macropad.pixels.show()
                if not loop_enabled[key]:
                    last_fired[key] = 0  # Reset timer when stopped
            else:
                macropad.pixels[key] = 0xFFFFFF           # flash white
                macropad.pixels.show()
                run_macro_sequence(seq)                   # do the macro
                macropad.pixels[key] = color              # restore original color
                macropad.pixels.show()

        elif event.released:
            # Optionally reset pixel color if not looping
            if not loop_enabled[key]:
                macropad.pixels[key] = color
                macropad.pixels.show()

    # Run looping macros if enabled and enough time passed
    for i, macro in enumerate(app_objects[app_index].macros):
        color, label_txt, seq, *maybe_interval = macro
        interval = maybe_interval[0] if maybe_interval else None
        if interval is not None and loop_enabled[i]:
            if now - last_fired[i] >= interval:
                last_fired[i] = now
                run_macro_sequence(seq)