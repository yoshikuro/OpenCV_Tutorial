# ROS-OpenCV_Tutorial/opencv_only
#### 目的：ひとまずPythonでOpenCVを使えるようにする
### ファイル構成
```
ROS-OpenCV_Tutorial/
├ sample1.py  画像の読み込み/表示
├ sample2.py  画像をグレースケールにする
├ sample3.py  画像から特定の色を抽出する
└ img/  プログラム内で使用される画像を格納しているフォルダ
```
***
### sample1.py

***
### sample2.py
sample1.pyのプログラムに、色空間を変換する関数を追加している

```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色空間をBGRからグレースケールに変換
```

OpenCVの関数`cvtColor()`は、入力された画像の色空間を変換する <br>
`imread()`関数では、読み込んだ画像の色がBGR(B：青、G：緑、R：赤)で表現されるが、色の抽出などがやりづらかったりする <br>
`cvtColor()`によって、色空間を後で扱いやすい形に変換することができる <br>
第一引数は変換する画像、第二引数には変換する前後の色空間によって読み替える <br>
第二引数でよく使いそうなものは以下 <br>
|コード|変換内容|
|---|---|
|cv2.COLOR_BGR2RGB|BGR -> RGB|
|cv2.COLOR_BGR2GRAY|BGR -> グレースケール|
|cv2.COLOR_BGR2HSV|BGR -> HSV|
|cv2.COLOR_HSV2BGR|HSV -> BGR|

そのほかのものは、リンクを参照 <br>
<https://docs.opencv.org/3.4.0/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0>
