FROM ros_python

# ワークディレクトリを作成
WORKDIR /catkin_ws/src/voice_controlled_robot

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3-pip \
    portaudio19-dev \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-xacro \
    cmake \
    && apt-get clean


# Pythonの依存関係をインストール
COPY requirements.txt /catkin_ws/src/voice_controlled_robot/
RUN pip3 install -r /catkin_ws/src/voice_controlled_robot/requirements.txt

# ソースコードをコピー
COPY . /catkin_ws/src/voice_controlled_robot/

# ROSのセットアップスクリプトを実行して環境をセットアップ
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
                  cd /catkin_ws && \
                  catkin_make"


# # ROSノードを起動するエントリーポイント
# CMD ["roslaunch", "voice_controlled_robot", "voice_controlled_robot_gazebo.launch"]