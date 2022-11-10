import cv2
import numpy as np
import matplotlib.pyplot as plt
path='/home/addtion_storage/huangtao/tomato_detect_rotate/split/images/0027__1__312___312.jpg'
annpath=path.replace('images','labelTxt').replace('jpg','txt')
img=cv2.imread(path)

with open(annpath,'r') as f:
    ann=f.readlines()
for each in ann:
    each=each.strip()
    axis=[float(i) for i in each.split(' ')[:8]]
    label=each.split(' ')[8]
    area1 = np.array([[axis[0], axis[1]], [axis[2], axis[3]], [axis[4], axis[5]], [axis[6], axis[7]]], dtype=np.int32)
    #cv2.fillPoly(img, [area1], (2, 255, 255))
    cv2.polylines(img, [area1], True, (98, 9, 11), 3)
plt.imshow(img[:,:,::-1])
plt.show()