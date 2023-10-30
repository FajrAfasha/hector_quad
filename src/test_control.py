import rospy

from hector_uav_msgs.srv import EnableMotors
from hector_uav_msgs.msg import Altimeter
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


cmd_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

kz = 2.0
zd = 4

#def callback_takeoff(msg):
#   z = msg.altitude
#
#   u_z = kz * (zd - z)
#
#   cmd_msg = Twist()
#   cmd_msg.linear.z = u_z
#   cmd_pub.publish(cmd_msg)

def callback_takeoff_2(msg):
    z = msg.pose.pose.position.z 
    u_z = kz * (zd - z)

    cmd_msg = Twist()
    cmd_msg.linear.z = u_z
    cmd_pub.publish(cmd_msg)

def main():
    rospy.init_node("test_control")

    #1 Enable motors
    rospy.wait_for_service("/enable_motors")
    foo2call = rospy.ServiceProxy("/enable_motors", EnableMotors)
    if foo2call(True):
        print("Motors started")

    
    #2 a) Get altitude data
    #  b) Compute control action u_z = kz x (z*-z)
    #rospy.Subscriber("/altimeter", Altimeter, callback_takeoff)


    rospy.Subscriber("/ground_truth/state", Odometry, callback_takeoff_2)


    rospy.spin()

if __name__ =="__main__":
    main()
    