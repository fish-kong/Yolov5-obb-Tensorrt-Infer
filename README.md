# yolov5_for_oriented_object_detection

The Pytorch implementation is [yolov5_obb](https://github.com/hukaixuan19970627/yolov5_obb )

actually ,This repo is based on [yolov5](https://github.com/ultralytics/yolov5/tree/v6.0/)  and only used at Linux PC (partial dependency install hardly at windows PC)

## How to Run, yolov5s as example
1.train your datasets in {yolov5_obb} 
generate .pt at {yolov5_obb/runs/exp[?]/weights/best.pt} 

2. generate .wts from {yolov5_obb/runs/exp[?]/weights/best.pt} 

```
cp gen_wts.py {yolov5_obb}
python gen_wts.py -w runs/train/exp[]/weights/best.pt -o yolov5s.wts
// a file 'yolov5s.wts' will be generated.
```

3. build **tensorrt engine **

```
cd {yolov5_obb_tensorrt_cpp}
// update CLASS_NUM/Inputsize in yololayer.h 
// caution:CLASS_NUM= your classes +180(180 for angle classes)
mkdir build
cd build
cp {yolov5_obb}/yolov5s.wts ../yolov5s.wts
cmake ..
make
sudo ./yolov5_gen -s [.wts] [.engine] [n/s/m/l/x]  // serialize model to plan file
// For example yolov5s
sudo ./yolov5_gen -s ../yolov5s.wts ../yolov5s.engine s
```

4. use **tensorr engine**
```
sudo ./yolov5_use ../yolov5s.engine ../images/test.jpg
```
![image](https://github.com/fish-kong/Yolov5-obb-Tensorrt-Infer/blob/main/yolov5_obb_tensorrt_cpp/result.jpg)

