# OpenCV_Tutorial
PythonでOpenCVを使用した画像処理を行いたい人向けのサンプルコード <br>
どこかの大学のどこかの研究室でもしかするともしかするかもしれない <br>

## 使用環境
Virtual Box
* OS  :  Ubuntu 20.04.4 LTS(64-bit)
* メインメモリ  :  8192MB
* ビデオメモリ  :  64MB
* ストレージ    :  50GB

ROS
* Virsion  :  noetic

## 事前準備
* Virtual BoxでLinux環境を作る
* ROSのインストールをする <br>
  →インストール手順は、以下のサイトから可能 <br>
  <http://wiki.ros.org/noetic/Installation/Ubuntu>

### 1. パッケージを作成
   Ubuntu上で、ターミナルを起動(Ctrl + Alt + T)

### 2. 必要なドライバなどをインスト―ル
  今回必要となるものは以下の通り。
  
  |対象|種類|説明|
  |----|----|----|
  |usb_cam|ROSパッケージ|USBカメラをキャプチャするパッケージ|
  |image_view|ROSパッケージ|キャプチャした画像を表示させる|
  |guvciview|アプリ|Linuxデスクトップ用のWebカメラアプリケーション|
  |terminator|ターミナルソフト|ターミナルの分割、画面切り替えができる|

```
$ sudo apt install ros-noetic-usb-cam
$ sudo apt install ros-noetic-image-view
$ sudo apt install guvciview
$ sudo apt-get install terminator
```

### 3. 本リポジトリのクローン <br>
<catkin_ws> と書かれているものは、各自の作成したワークスペースに置き換えて考える
```
$ cd <catkin_ws>/src
$ git clone https://github.com/yoshikuro/opencv_tutorial.git
```

### 4. パッケージのビルド <br>
  クローンしたパッケージは、ビルドをすることで使用可能になる
```
$ cd <catkin_ws>
$ catkin build
$ source devel/setup.bash
```

### 5. USBカメラの接続
  1. USBカメラをPCに接続する
  2. Virtual Boxのタブにあるデバイスから、USBをクリック
  3. PCに接続したカメラを選択する
  4. ターミナルでUSBカメラが接続されていることを確認する<br>
  `$ ls /dev/video*`<br>
    接続されている場合、`/dev/video0`が表示される(番号は接続されているカメラの数によって変わる)

### 6. 動作確認
  実際に動作可能かを確認する <br>
  3つのターミナルを開き、以下を実行する
  
 ```
 $ roscore
 ```
 
 ```
 $ rosrun usb_cam usb_cam_node
 ```
 
 ```
 $ rosrun image_view image_view image:=/usb_cam/image_raw
 ```

 また、roslaunchを使用することで、上3つの実行がひとつのターミナルで完結する <br>
 起動するノード(rosrunで動かすやつ)が増えて、困難に感じたときはlaunchファイルを作ると便利 <br>
 ```
 $ roslaunch usb_cam usb_cam-test.launch
 ```
 
 ### 7. エラーなど動作しないとき
 #### rosrun usb_cam usb_cam_node の起動時にエラーが表示される (VIDIOC_STREAMON　error 5, Input/output error)
  1. Virtual BoxのUSB設定が、デフォルトの1.1になっている <br>
  Ubuntuを一度閉じ、Virtual Boxマネージャの設定からUSB設定を3.0にする <br>
  USB設定に2.0、3.0がない場合は、Virtual BoxのサイトからダウンロードしたExtention Packをインストールする <br>
  <https://www.virtualbox.org/wiki/Download_Old_Builds> <br>
  ※Virtual Boxのバージョンを確認し、ダウンロードするものを一致させること
  
 ### 8. 参考になるサイト
 * ROS launchファイルの使い方 <br>
   <https://kazuyamashi.github.io/ros_lecture/ros_launch.html>
