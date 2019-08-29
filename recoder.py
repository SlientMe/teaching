from pynput import keyboard


def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key):
    key_name = get_key_name(key)


def on_release(key):
    key_name = get_key_name(key)
    if key_name in keys:
        key_stat[key_name] = key_stat[key_name] + 1

    if key_name == 'Key.page_down':
        fp = open('key_stat.xyz', 'w')
        for key in keys:
            fp.write('%s: %i\n' % (key, key_stat[key]))
        return False


key_stat = {}
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', 'Key.esc', 'Key.tab',
        'Key.caps_lock', 'Key.shift', 'Key.ctrl', 'Key.alt', 'Key.cmd', 'Key.space', 'Key.alt_r', 'Key.cmd_r',
        'Key.enter', 'Key.shift_r', 'Key.backspace', 'Key.up', 'Key.down', 'Key.left', 'Key.right', 'Key.ctrl_r', ',',
        '.', '/', ';', '\'', '\\', ']', '[', '=', '-']
for key in keys:
    key_stat[key] = 0
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()