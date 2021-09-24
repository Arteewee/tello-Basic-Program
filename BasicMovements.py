from djitellopy import tello
# library tello
from time import sleep
# delay for each commands

me = tello.Tello()
me.connect()
# connect tello for control ip and everything
print(me.get_battery())
# menunjukan baterai yang tersisa di drone
me.takeoff()
#  take off drone
me.send_rc_control(0,50,0,0)
#  left right velocity, forward backward, up and down velocity , yaw (rotate)
sleep(2)
# bakal bergerak ke depan dengan kecepatan 50 dan selama 2 detik dan bakal alnding
me.send_rc_control(0,0,0,50)
sleep(2)
me.send_rc_control(0,0,0,0)
me.land()

