import pyaudio
import numpy as np
import rospy
from std_msgs.msg import Float32, Bool


class VoiceAnalyzer:
    def __init__(self):
        # rospy.init_node("voice_analyzer", anonymous=True)
        self.pitch_pub = rospy.Publisher("voice_pitch", Float32, queue_size=10)
        self.volume_pub = rospy.Publisher("voice_volume", Float32, queue_size=10)
        self.is_speaking_pub = rospy.Publisher("is_speaking", Bool, queue_size=10)

        self.chunk = 1024
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )

    def analyze_voice(self):
        while not rospy.is_shutdown():
            data = self.stream.read(self.chunk)
            audio_data = np.frombuffer(data, dtype=np.float32)

            pitch = self.get_pitch(audio_data)
            volume = self.get_volume(audio_data)
            is_speaking = self.is_speaking(volume)

            self.pitch_pub.publish(pitch)
            self.volume_pub.publish(volume)
            self.is_speaking_pub.publish(is_speaking)

    def get_pitch(self, audio_data):
        # ピッチ解析の処理を実装（例: librosaやpyinを使用）
        # 簡単な例として、音声データの平均値を返す
        return np.mean(audio_data)

    def get_volume(self, audio_data):
        volume = np.max(np.abs(audio_data))
        return volume

    def is_speaking(self, volume, threshold=0.01):
        return volume > threshold
