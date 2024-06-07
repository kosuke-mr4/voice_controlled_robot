# WIP:voice_controlled_robot

2024 roboken demo programming contest / team 9

## todo
```
- gazeboのモデルが動かない
- トピックが生えてないことの修正
- 拾った音声の処理ロジックの調整
- 実機検証用がまだできていない
```

## idea
```
- はじめに声の高さの範囲を取得する
- 自己位置推定
- ビジュアルを良くする
```

## requirement
```
ros # installed at yamasemi
```

## install
```
pip3 install -r requirements.txt
```

### gazebo
```
roslaunch voice_controlled_robot voice_controlled_robot_gazebo.launch
```