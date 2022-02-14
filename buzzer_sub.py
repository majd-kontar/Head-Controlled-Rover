#!//home/pi/Desktop/Gaze/bin/python3                                                                                                                                                                                                         
import rospy
import buzzer
from std_msgs.msg import Float64



def callback(data):
    rospy.loginfo("Receiving Ultrasonic Sensor Data")
    buzz=buzzer.Buzzer(26)
    if data.data < 15.0:
        buzz.turn_on()
    else:
        buzz.turn_off()
    
def receive_message():
    rospy.init_node('buzze_sub_py',anonymous=True)
    # Node is subscribing to the video_frames topic
    rospy.Subscriber('ultrasonic_pub', Float64, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    receive_message()