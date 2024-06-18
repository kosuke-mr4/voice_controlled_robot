import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32, Bool

class RobotController:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("voice_pitch", Float32, self.pitch_callback)
        rospy.Subscriber("voice_volume", Float32, self.volume_callback)
        rospy.Subscriber("is_speaking", Bool, self.is_speaking_callback)

        self.pitch = 0.0
        self.volume = 0.0
        self.is_speaking = False

    def pitch_callback(self, msg):
        self.pitch = msg.data

    def volume_callback(self, msg):
        self.volume = msg.data

    def is_speaking_callback(self, msg):
        self.is_speaking = msg.data

    def control_robot(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.is_speaking:
                cmd_vel = Twist()
                cmd_vel.linear.x = self.volume * 0.3
                cmd_vel.angular.z = 0.0
                # if(cmd_vel.linear.x  > 1.0):
                #     cmd_vel.linear.x = 1.0
                # if(cmd_vel.angular.z > 1.0):
                #     cmd_vel.angular.z = 1.0
                self.cmd_vel_pub.publish(cmd_vel)
            else:
                cmd_vel = Twist()
                cmd_vel.linear.x = 0.0
                cmd_vel.angular.z = 0.5
                self.cmd_vel_pub.publish(cmd_vel)
            rate.sleep()
