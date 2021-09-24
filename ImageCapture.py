from djitellopy import tello
# library tello
import cv2
# delay for each commands

me = tello.Tello()
me.connect()
# connect tello for control ip and everything
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)