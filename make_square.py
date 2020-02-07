import rospy
from geometry_msgs.msg import Twist
from math import radians

# constant for speed 
LIN_SPEED = 0.2
ROT_SPEED = radians(90)


class MakeSquare:

    def __init__(self):
        # Initialize
        rospy.init_node('MakeSquare', anonymous=False)

        # What to do you ctrl + c (call shutdown function written below)
        rospy.on_shutdown(self.shutdown)

    def run(self):
        TurnLeft()
        time.sleep(5)
        GoForwardAndBump()

    def shutdown(self):
       
       # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
        # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
        # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(5)


if __name__ == '__main__':
    try:
        robot = MakeSquare()
        robot.run()
    except Exception, err:
        rospy.loginfo("TurnLeft node terminated.")
        print err
