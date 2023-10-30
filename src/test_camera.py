import rospy

from sensor_msgs.msg import Image



def callback_foo(data):
    print(data.shape)



def main():
    rospy.init_node("test_camera_node")
    sub = rospy.Subscriber(/cam_1/camera/image, Image, callback_foo)

if  __name__=="__main__":
    main()