import rospy
from std_msgs.msg import Float32, Bool
import time
import asyncio
from websockets.server import serve
import json

class VoiceAnalyzer:
    def __init__(self):
        self.pitch_pub = rospy.Publisher("voice_pitch", Float32, queue_size=10)
        self.volume_pub = rospy.Publisher("voice_volume", Float32, queue_size=10)
        self.is_speaking_pub = rospy.Publisher("is_speaking", Bool, queue_size=10)
        

    async def echo(self, websocket):
        async for message in websocket:
            data = json.loads(message) 
            print(data)   
            self.volume_pub.publish(Float32(data['volume']))
            self.pitch_pub.publish(Float32(data['frequency']))
            self.is_speaking_pub.publish(Bool(data['volume'] > 5.0))

    async def main(self):
        async with serve(self.echo, "0.0.0.0", 5002):
            await asyncio.Future()  # run forever

    def analyze_voice(self):
        while not rospy.is_shutdown():
            asyncio.run(self.main())