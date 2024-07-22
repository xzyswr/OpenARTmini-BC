# 导入包
#from pyb import LED
import pyb, machine
import sensor, image, time, math
import os, tf
import seekfree

#thresholds1_black = [(0, 60, -15, 7, -19, 18)]
thresholds1_black = [(47, 100, -14, 25, -14, 17)]
thresholds = [(65, 100, -59, 105, -30, 60)]

def Camera_Init():
    sensor.reset() #初始化感光元件
    sensor.set_pixformat(sensor.RGB565) #设置为RGB565色彩空间
    sensor.set_framesize(sensor.QVGA) #设置图像的大小
    sensor.set_auto_gain(False) #自动增益关闭
    sensor.set_auto_whitebal(False) #自动白平衡关闭
    sensor.set_auto_exposure(False, exposure_us = 1200) #自动曝光关闭
    sensor.skip_frames(time = 100) #等待200ms使感光元件稳定

Camera_Init() #初始化摄像头
# 捡取
all_blob = [] # 保存所有色块
while(1):
    img = sensor.snapshot()
    blobs = img.find_blobs(
                [thresholds1_black[0]],
                invert=False, # 反转
                x_stride = 20,
                y_stride = 20,
                pixels_threshold=1000,
                area_threshold=1000,
                merge=False,
                )
    if not blobs:
        print("无目标")
    else:
          for blob in blobs:
                if blob.w()<120 and blob.w()>60 and blob.h()<120 and blob.h()>60  :
                     img.draw_rectangle((blob.x(),blob.y(),blob.w(),blob.h()),color=(0,255,0),thickness=2)
