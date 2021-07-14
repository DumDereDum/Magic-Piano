import sys
import os
import numpy as np
import time
import cv2
from playsound import playsound


class PianoKey:
    left = None
    right = None
    height = None
    width = None
    note = None
    sound = None
    middle = None
    pressed = None
    color = None

    # note - нота (пример "E1"), sound - путь до звукового файла
    # x1 x2 y1 y2 - координаты в пикселях если не переданы размеры image,
    #    иначе - координаты в зависимости от размеров image

    def __init__(self, x1, y1, x2, y2, note, sound, image_height=None, image_width=None):
        if image_height:
            self.left = (x1 * image_width, y1 * image_height)
            self.right = (x2 * image_width, y2 * image_height)
            self.height = (y2-y1) * image_height
            self.width = (x2-x1) * image_width
        else:
            self.left = (x1, y1)
            self.right = (x2, y2)
            self.height = y2-y1
            self.width = x2-x1
        self.note = note
        self.sound = sound
        self.middle = (x2-x1, y2-y1)
        self.pressed = False
        self.color = (255, 255, 255)  # format BGR

    def play_sound(self):
        # играем звук
        path = self.sound + '\\' + self.note + '.mp3'
        playsound(path)
        # time.sleep(0.3)

    def press(self):
        if self.pressed:
            return
        else:
            self.color = (100, 40, 20)
            self.pressed = True

    def unpress(self):
        self.pressed = False
        self.color = (255, 255, 255)

    def draw_key(self, img):
        x, y = self.left
        cv2.rectangle(img, self.left, self.right, self.color, cv2.LINE_4)
        cv2.putText(img, self.note, (x+20, int(y+self.height*0.1)),
                    cv2.FONT_HERSHEY_PLAIN, int(self.height*0.03), (0, 0, 0), 3)
        return img
