# 从人脸图像文件中提取人脸特征存入 CSV
# Features extraction from images and save into features_all.csv

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Dlib_face_recognition_from_camera
# Mail:     coneypo@foxmail.com

# Created at 2018-05-11
# Updated at 2019-04-04

from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QApplication
import cv2
import os
import dlib
from skimage import io
import csv
import numpy as np
import shutil
from PyQt5.QtWidgets import *
# 要读取人脸图像文件的路径
path_images_from_camera = "data/load/data_faces_from_camera/"

path = "data/load/"
'''# Dlib 正向人脸检测器
detector = dlib.get_frontal_face_detector()

# Dlib 人脸预测器
predictor = dlib.shape_predictor("data/data_dlib/shape_predictor_68_face_landmarks.dat")#=---------------------------10.17

# Dlib 人脸识别模型
# Face recognition model, the object maps human faces into 128D vectors
face_rec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")'''

def del_file(path):
    filelist=[]
    filelist=os.listdir(path)                #列出该目录下的所有文件名
    for f in filelist:
        filepath = os.path.join(path, f )   #将文件名映射成绝对路劲
        if os.path.isfile(filepath):            #判断该文件是否为文件或者文件夹
            os.remove(filepath)                 #若为文件，则直接删除
            print(str(filepath)+" removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
            print("dir "+str(filepath)+" removed!")
    #shutil.rmtree(path,True)                 #最后删除img总文件夹
    print("删除成功")

def removeku():
    if os.path.isdir(path):
        del_file(path)
    else:
        pass
class ProgressBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ProgressBar')
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QPushButton('Start', self)
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(40, 80)

        self.button.clicked.connect(self.onStart)
        self.timer = QBasicTimer()
        self.step = 0

    def onStart(self):
        '''if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')'''
        #else:
        self.timer.start(1, self)
        #self.button.setText('Stop')

    def timerEvent(self, event):
        if self.step== 1:
            self.timer.stop()
            self.pbar.reset()
            self.step=0
            self.close()
            return
        self.step = self.step + 1
        # Dlib 正向人脸检测器
        detector = dlib.get_frontal_face_detector()

        # Dlib 人脸预测器
        predictor = dlib.shape_predictor("data/data_dlib/shape_predictor_68_face_landmarks.dat")

        # Dlib 人脸识别模型
        # Face recognition model, the object maps human faces into 128D vectors
        face_rec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")


        # 返回单张图像的 128D 特征
        def return_128d_features(path_img):
            img_rd = io.imread(path_img)
            img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
            faces = detector(img_gray, 1)
            print("%-40s %-20s" % ("检测到人脸的图像 / image with faces detected:", path_img), '\n')
            # 因为有可能截下来的人脸再去检测，检测不出来人脸了
            # 所以要确保是 检测到人脸的人脸图像 拿去算特征

            if len(faces) != 0:
                shape = predictor(img_gray, faces[0])
                face_descriptor = face_rec.compute_face_descriptor(img_gray, shape)
            else:
                face_descriptor = 0
                print("no face")

            return face_descriptor


        # 将文件夹中照片特征提取出来, 写入 CSV
        def return_features_mean_personX(person,person_cnt,path_faces_personX):
            features_list_personX = []
            personcount=(person)/(person_cnt)
            print(personcount)
            photos_list = os.listdir(path_faces_personX)
            if photos_list:
                for i in range(len(photos_list)):
                    print(len(photos_list))
                    #print(i/len(photos_list)*100)
                    #self.pbar.emit(str(i/len(photos_list)))
                    QApplication.processEvents()#防止gui假死
                    ff=int(personcount*100+i/len(photos_list)*100/person_cnt)
                    self.pbar.setValue(ff)
                    #print(ff)
                    # 调用return_128d_features()得到128d特征
                    #print("%-40s %-20s" % ("正在读的人脸图像 / image to read:", path_faces_personX + "/" + photos_list[i]))
                    features_128d = return_128d_features(path_faces_personX + "/" + photos_list[i])
                    #  print(features_128d)
                    # 遇到没有检测出人脸的图片跳过
                    if features_128d == 0:
                        i += 1
                    else:
                        features_list_personX.append(features_128d)
            else:
                print("文件夹内图像文件为空 / Warning: No images in " + path_faces_personX + '/', '\n')

            # 计算 128D 特征的均值
            # personX 的 N 张图像 x 128D -> 1 x 128D
            if features_list_personX:
                features_mean_personX = np.array(features_list_personX).mean(axis=0)
            else:
                features_mean_personX = '0'
            return features_mean_personX

        # 获取已录入的最后一个人脸序号 / get the num of latest person
        person_list = os.listdir("data/load/data_faces_from_camera/")
        person_num_list = []
        for person in person_list:
            person_num_list.append(int(person.split('_')[-1]))
        person_cnt = max(person_num_list)

        with open("data/load/features_all.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for person in range(person_cnt):
                #print("121212",str(int((person+1)/(person_cnt+1))))
                #self._signal.emit(str(int((person+1)/(person_cnt+1))))
                # Get the mean/average features of face/personX, it will be a list with a length of 128D
                print(path_images_from_camera + "person_"+str(person+1))
                features_mean_personX = return_features_mean_personX(person,person_cnt,path_images_from_camera + "person_"+str(person+1))
                writer.writerow(features_mean_personX)
                print("特征均值 / The mean of features:", list(features_mean_personX))
                print('\n')

            print("所有录入人脸数据存入 / Save all the features of faces registered into: data/load/features_all.csv")
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    qb = ProgressBar()
    qb.show()
    sys.exit(app.exec_())