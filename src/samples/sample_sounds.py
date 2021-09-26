import os
import sys
import time
sys.path.append("..")
from modules.piano_key import PianoKey

def main():
    path = os.path.abspath('') + '\\sounds\\sound_4'
    a = PianoKey(0, 0, 100, 100, 'C4', path, 1000, 1000)
    b = PianoKey(0, 0, 100, 100, 'D4', path, 1000, 1000)
    c = PianoKey(0, 0, 100, 100, 'E4', path, 1000, 1000)
    d = PianoKey(0, 0, 100, 100, 'F4', path, 1000, 1000)
    e = PianoKey(0, 0, 100, 100, 'G4', path, 1000, 1000)
    f = PianoKey(0, 0, 100, 100, 'A4', path, 1000, 1000)
    k = PianoKey(0, 0, 100, 100, 'B4', path, 1000, 1000)

    for i in range(3):
        print('Now play C4')
        a.play_sound()
        time.sleep(0.3)
        print('Now play D4')
        b.play_sound()
        time.sleep(0.3)
        print('Now play E4')
        c.play_sound()
        time.sleep(0.3)
        print('Now play F4')
        d.play_sound()
        time.sleep(0.3)
        print('Now play G4')
        e.play_sound()
        time.sleep(0.3)
        print('Now play A4')
        f.play_sound()
        time.sleep(0.3)
        print('Now play B4')
        k.play_sound()
        time.sleep(0.3)


if __name__ == '__main__':
    sys.exit(main() or 0)
