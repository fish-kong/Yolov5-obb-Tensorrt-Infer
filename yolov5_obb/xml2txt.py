# *_* coding : UTF-8 *_*
# 功能描述   ：把旋转框 cx,cy,w,h,angle，转换成四点坐标x1,y1,x2,y2,x3,y3,x4,y4,class,difficulty

import os
import xml.etree.ElementTree as ET
import math

label=['tomato']
def edit_xml(xml_file):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    print(xml_file)
    tree = ET.parse(xml_file)
    f=open(xml_file.replace('xml','txt').replace('anns','labelTxt'),'w')
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        obj_type = obj.find('type')
        type = obj_type.text
        
        if type == 'bndbox':
            obj_bnd = obj.find('bndbox')
            obj_xmin = obj_bnd.find('xmin')
            obj_ymin = obj_bnd.find('ymin')
            obj_xmax = obj_bnd.find('xmax')
            obj_ymax = obj_bnd.find('ymax')
            xmin = float(obj_xmin.text)
            ymin = float(obj_ymin.text)
            xmax = float(obj_xmax.text)
            ymax = float(obj_ymax.text)
            obj_bnd.remove(obj_xmin)  # 删除节点
            obj_bnd.remove(obj_ymin)
            obj_bnd.remove(obj_xmax)
            obj_bnd.remove(obj_ymax)
            x0 = xmin
            y0 = ymin
            x1 = xmax
            y1 = ymin
            x2 = xmin
            y2 = ymax
            x3 = xmax
            y3 = ymax
        elif type == 'robndbox':
            obj_bnd = obj.find('robndbox')
            obj_bnd.tag = 'bndbox'   # 修改节点名
            obj_cx = obj_bnd.find('cx')
            obj_cy = obj_bnd.find('cy')
            obj_w = obj_bnd.find('w')
            obj_h = obj_bnd.find('h')
            obj_angle = obj_bnd.find('angle')
            cx = float(obj_cx.text)
            cy = float(obj_cy.text)
            w = float(obj_w.text)
            h = float(obj_h.text)
            angle = float(obj_angle.text)

            x0, y0 = rotatePoint(cx, cy, cx - w / 2, cy - h / 2, -angle)
            x1, y1 = rotatePoint(cx, cy, cx + w / 2, cy - h / 2, -angle)
            x2, y2 = rotatePoint(cx, cy, cx + w / 2, cy + h / 2, -angle)
            x3, y3 = rotatePoint(cx, cy, cx - w / 2, cy + h / 2, -angle)
        classes=int(obj.find('name').text)
        axis=list([str(x0),str(y0),str(x1), str(y1),str(x2), str(y2),str(x3), str(y3),label[classes],'0'])
        bb = " ".join(axis)
        f.writelines(bb)
        f.writelines("\n")
    f.close()
# 转换成四点坐标
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc;
    yoff = yp - yc;
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return int(xc + pResx), int(yc + pResy)

if __name__ == '__main__':
    for path in os.listdir('anns/'):
        edit_xml('anns/'+path)
