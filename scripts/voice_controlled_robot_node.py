#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import rospy
from voice_controlled_robot.voice_analyzer import VoiceAnalyzer
from voice_controlled_robot.robot_controller import RobotController

if __name__ == "__main__":
    rospy.init_node("voice_controlled_robot_node", anonymous=True)

    voice_analyzer = VoiceAnalyzer()
    robot_controller = RobotController()

    rospy.spin()
