import rospy
from voice_controlled_robot.voice_analyzer import VoiceAnalyzer
from voice_controlled_robot.robot_controller import RobotController
import threading

if __name__ == "__main__":
    rospy.init_node("voice_controlled_robot_node", anonymous=True)

    voice_analyzer = VoiceAnalyzer()
    robot_controller = RobotController()

    voice_thread = threading.Thread(target=voice_analyzer.analyze_voice)
    robot_thread = threading.Thread(target=robot_controller.control_robot)

    voice_thread.start()
    robot_thread.start()

    rospy.spin()
