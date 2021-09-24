from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("d"): yv = speed
    elif kp.getKey("a"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]


while True :
    val = getKeyboardInput()
    me.send_rc_control(val[0], val[1], val[2], val[3])
    sleep(0.05)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)