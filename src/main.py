from modules.hand_tracking import HandDetector
from modules.piano_key import PianoKey
from modules.piano import Piano
from screeninfo import get_monitors
import cv2 as cv
import logging as log
import math
import os
import sys
sys.path.append("..")


def main():
    log.basicConfig(format='[ %(levelname)s ] %(message)s',
                    level=log.INFO, stream=sys.stdout)

    # инициализация значений
    cap = cv.VideoCapture(0)
    detector = HandDetector()

    success, img = cap.read()

    monitor = get_monitors()
    #m_width = monitor[0].width
    #m_height = monitor[0].height
    m_width, m_height = img.shape[:2]

    # генерация клавиш и пианино
    XX = 50
    #piano = Piano(10, 10, int(m_width/1.5), int(m_height/3))
    piano = Piano(XX, 0, int(m_width), int(m_height/3))
    spath = os.path.abspath('') + '\\sounds\\sound_4'

    piano.generator_7(spath)
    cond = 15
    # работа нейросети
    while cap.isOpened():
        success, img = cap.read()
        img = cv.flip(img, 1)
        #img = cv.resize(img, (int(m_width/1.5), int(m_height/1.5)),
        #                interpolation=cv.INTER_AREA)
        left_points, right_points = detector.findPosition(img, True)

        fingers = []
        zone = piano.keys[0].height

        hashs = piano.keys[0].width
        pressed = {}
        for key in piano.keys:
            pressed[key] = False

        if left_points:
            for i in range(len(left_points)):
                if left_points[i][2] < zone and left_points[i][0] % 4 == 0:
                    fingers.append((left_points[i], left_points[i-1]))
        if right_points:
            for i in range(len(left_points)):
                if right_points[i][2] < zone and right_points[i][0] % 4 == 0:
                    fingers.append((right_points[i], right_points[i-1]))

        if fingers:
            for finger in fingers:
                hh = (finger[0][1]-XX)//hashs # one calc instead of 3
                if -1 < hh < 7:
                    if finger[0][2] > finger[1][2] or math.sqrt((finger[0][1]-finger[1][1])**2 + (finger[0][2]-finger[1][2])**2) < cond:
                        piano.keys[hh].press()
                        pressed[hh] = True

        for key in piano.keys:
            if not pressed[key]:
                piano.keys[key].unpress()

        # отрисовка
        img = piano.draw(img)
        cv.imshow("Image", img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    sys.exit(main() or 0)
