from subprocess import call
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
m = PyMouse()
x_dim, y_dim = m.screen_size()


# init minimize the execution window
k.press_key('Command')
k.tap_key('h')
k.release_key('Command')
time.sleep(2)
m.click(x_dim/2, y_dim/2, 1)


# 301 - 770
for page in range(301, 770):
    m.click(154, 112, 1)
    time.sleep(0.1)
    k.tap_key('delete', n=3)
    time.sleep(0.1)
    k.type_string(str(page))
    time.sleep(0.1)
    k.tap_key('return')
    time.sleep(2)

    call(["screencapture", "-R523,128,608,757", "page_" + str(page) + ".png"])
