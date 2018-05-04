import datetime
import pynput
import os
from mss import mss


class ScreenCapture:
    def __init__(self):
        if os.path.isdir('Captures') is False:
            os.mkdir('Captures')
        self.count = 0
        self.start_filename = "TODO start_filename"
        self.mouse = pynput.mouse
        self.keyboard = pynput.keyboard
        with self.mouse.Listener(on_click=self.on_click) as listener:
            listener.join()
        with self.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.count += 1
            self.screen_capture()
            print('pressed at {} with {}'.format((x, y), button))
        self.keyboard.Controller().press(key=self.keyboard.Key.esc)

    def on_press(self, key):
        print(key)
        if key is not self.keyboard.Key.esc:
            self.screen_capture()
            self.keyboard.Controller().press(self.keyboard.Key.esc)

    def on_release(self, key):
        print(key)
        self.keyboard.Controller().press(key=self.keyboard.Key.esc)

    def screen_capture(self):
        date = datetime.datetime.now()
        filename = date.year + date.month + date.day + date.hour + date.minute + date.second
        with mss() as sct:
            if os.path.isfile(f'Captures\{self.start_filename}{filename}.png'):
                sct.shot(mon=-1, output=f'Captures/{self.start_filename}{filename}.png')
            else:
                sct.shot(mon=-1, output=f'Captures/{self.start_filename}{filename}{self.count}.png')
        print(f'Não Salvo {self.count}')
