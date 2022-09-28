#!/usr/bin/env python
import rospy
import time
import simple_tello
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def main():
  t1 = simple_tello.Tello_drone()
  
  while t1.state.is_flying == False: 
    t1.controler.takeoff()
  
  while t1.state.fly_mode != 6:
    print("wait...")
  
  t1.controler.flip(0)
  
  while t1.state.fly_mode != 6:
    print("wait...") 
    
  while t1.state.is_flying == True:
    t1.controler.land() 

  
if __name__ == "__main__":
  rospy.init_node("run_tello", anonymous=True)
  main()
