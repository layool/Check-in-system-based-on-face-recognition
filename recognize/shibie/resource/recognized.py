# 摄像头实时人脸识别
# Real-time face recognition

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Dlib_face_recognition_from_camera

# Created at 2018-05-11
# Updated at 2019-04-09
import scipy.spatial.distance as dist
from xpinyin import Pinyin
pin = Pinyin()
import time
import csv
localtime = time.asctime( time.localtime(time.time()) )
timef=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
path = "data/load/name.csv"
classpath = "data/signin/%s.csv"%(timef)

#import time
from sklearn.metrics.pairwise import cosine_similarity
import dlib          # 人脸处理的库 Dlib
import numpy as np   # 数据处理的库 numpy
import cv2           # 图像处理的库 OpenCv
import pandas as pd  # 数据处理的库 Pandas

# 人脸识别模型，提取128D的特征矢量
# face recognition model, the object maps human faces into 128D vectors
# Refer this tutorial: http://dlib.net/python/index.html#dlib.face_recognition_model_v1
facerec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('data/data_dlib/shape_predictor_68_face_landmarks.dat')#----------------------------------------10.17
number = []

def rune():
    # 计算两个128D向量间的欧式距离
    # compute the e-distance between two 128D features
    def return_euclidean_distance(feature_1, feature_2):
        #print(feature_1)
        feature_1 = np.array(feature_1)
        feature_2 = np.array(feature_2)
        dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
        return dist

    # 计算两个128D向量间的余弦相似度
    def cosplay(vector1,vector2):
        '''print("npppppp-------------", vector1)
        print("npppppp",np.dot(vector1,vector2))'''
        op7 = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * (np.linalg.norm(vector2)))
        #print(op7)
        return op7

    # 计算切比雪夫距离
    def qiebixuefu(vector1,vector2):
        v1 = np.mat(vector1)
        v2 = np.mat(vector2)
        temp=abs(v1 - v2).max()
        return temp


    # 计算jaccard距离
    def jaccardnum(vector1,vector2):
        a= [round(i,1) for i in vector1]
        b=[round(i,1) for i in vector2]
        vec1 = np.array(a)
        vec2 = np.array(b)
        d = float(dist.pdist(np.array([vec1, vec2]), "jaccard"))
        return d





    # 处理存放所有人脸特征的 csv
    path_features_known_csv = "data/load/features_all.csv"
    csv_rd = pd.read_csv(path_features_known_csv, header=None)
    #print("Fa",csv_rd)
    # 用来存放所有录入人脸特征的数组
    # the array to save the features of faces in the database
    features_known_arr = []

    # 读取已知人脸数据
    # print known faces
    for i in range(csv_rd.shape[0]):
        features_someone_arr = []
        for j in range(0, len(csv_rd.ix[i, :])):
            features_someone_arr.append(csv_rd.ix[i, :][j])
        features_known_arr.append(features_someone_arr)
    '''print("Faces1111：",features_known_arr)
    print("Faces in Database：", len(features_known_arr))'''
    '''# Dlib 检测器和预测器
    # The detector and predictor will be used
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('data/data_dlib/shape_predictor_68_face_landmarks.dat')#----------------------------------------10.17'''

    # 创建 cv2 摄像头对象
    # cv2.VideoCapture(0) to use the default camera of PC,
    # and you can use local video name by use cv2.VideoCapture(filename)
    cap = cv2.VideoCapture(0)

    # cap.set(propId, value)
    # 设置视频参数，propId 设置的视频参数，value 设置的参数值
    cap.set(3, 480)
    tuples = []
    for i in range(100):
        tuples.append(0)
    lists = []
    # cap.isOpened() 返回 true/false 检查初始化是否成功
    # when the camera is open
    while cap.isOpened():
        #QApplication.processEvents()  # 防止gui假死
        flag, img_rd = cap.read()
        kk = cv2.waitKey(1)

        #imgYcc = cv2.cvtColor(img_rd, cv2.COLOR_BGR2YCR_CB)
        # 取灰度
        img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)

        # 人脸数 faces
        faces = detector(img_gray, 0)

        # 待会要写的字体 font to write later
        font = cv2.FONT_HERSHEY_COMPLEX

        # 存储当前摄像头中捕获到的所有人脸的坐标/名字
        # the list to save the positions and names of current faces captured
        pos_namelist = []
        name_namelist = []

        # 按下 q 键退出
        # press 'q' to exit
        if kk == ord('q'):
            break
        else:
            # 检测到人脸 when face detected
            if len(faces) != 0:
                # 获取当前捕获到的图像的所有人脸的特征，存储到 features_cap_arr
                # get the features captured and save into features_cap_arr
                features_cap_arr = []
                #t7 = time.time()
                for i in range(len(faces)):
                    shape = predictor(img_rd, faces[i])
                    features_cap_arr.append(facerec.compute_face_descriptor(img_rd, shape))
                # 遍历捕获到的图像中所有的人脸
                # traversal all the faces in the database
                #t8 = time.time()
                #print(t8 - t7)
                for k in range(len(faces)):
                    #print("##### camera person", k+1, "#####")
                    # 让人名跟随在矩形框的下方
                    # 确定人名的位置坐标
                    # 先默认所有人不认识，是 unknown
                    # set the default names of faces with "unknown"
                    name_namelist.append("unknown")

                    # 每个捕获人脸的名字坐标 the positions of faces captured
                    pos_namelist.append(tuple([faces[k].left(), int(faces[k].bottom() + (faces[k].bottom() - faces[k].top())/4)]))

                    # 对于某张人脸，遍历所有存储的人脸特征
                    # for every faces detected, compare the faces in the database
                    e_distance_list = []
                    cosplay_list=[]
                    qiebixuefu_list=[]
                    jaccard_list=[]
                    for i in range(len(features_known_arr)):
                        # 如果 person_X 数据不为空
                        if str(features_known_arr[i][0]) != '0.0':
                            #print("with person", str(i + 1), "欧氏距离: ", end='')
                            #t1=time.time()
                            e_distance_tmp = return_euclidean_distance(features_cap_arr[k], features_known_arr[i])
                            #t2 = time.time()
                            xiangsidu=cosplay(features_cap_arr[k], features_known_arr[i])

                            qie=qiebixuefu(features_cap_arr[k], features_known_arr[i])
                            #t3 = time.time()
                            jie=jaccardnum(features_cap_arr[k], features_known_arr[i])
                            #print("ghh",t2-t1)
                            #print("mmm",t3-t2)

                            #print(e_distance_tmp)
                            #print("余弦相似度",xiangsidu)
                            e_distance_list.append(e_distance_tmp)
                            cosplay_list.append(xiangsidu)
                            qiebixuefu_list.append(qie)
                            jaccard_list.append(jie)

                        else:
                            # 空数据 person_X
                            e_distance_list.append(999999999)
                            cosplay_list.append(0)
                            qiebixuefu_list.append(999999999)
                            jaccard_list.append(1)

                    # Find the one with minimum e distance
                    similar_person_num = e_distance_list.index(min(e_distance_list))
                    with open(path, "r") as f:
                        csv_read = csv.reader(f)

                        for line in csv_read:
                            lists.append(line)
                        #print(lists)
                    countff=int(similar_person_num)
                    #print(countff)

                    #similar_cosplay_num = cosplay_list.index(max(cosplay_list))
                    #print("121212",similar_person_num)
                    print(e_distance_list)
                    print(cosplay_list)
                    print(qiebixuefu_list)
                    print(jaccard_list)
                    #print("Minimum e distance with person", int(similar_person_num)+1)
                    #print("index",cosplay_list[similar_person_num])
                    if min(e_distance_list) <=0.40 and cosplay_list[similar_person_num]>=0.96 and qiebixuefu_list[similar_person_num]<=0.12 :
                        # 在这里修改 person_1, person_2 ... 的名字
                        # 可以在这里改称 Jack, Tom and others
                        # Here you can modify the names shown on the camera
                        #name_namelist[k] = "Person " + str(countff + 1)
                        tuples[countff]=tuples[countff]+1
                        print(tuples[countff])
                        if(tuples[countff]>=5):
                            tempt = lists[countff]
                            print(tempt)
                            if countff in number:
                                #print("ifififiififiifif")
                                break
                            else:
                                number.append(countff)
                                #print("elseelseelseelse")
                                with open(classpath, 'a+', newline="") as f:
                                    csv_write = csv.writer(f)
                                    csv_write.writerow(tempt)
                            #name_namelist[k] = "Person " + str(int(similar_cosplay_num) + 1)
                            print("May be person "+str(tempt[0]))
                            #print("May be person " + str(int(similar_cosplay_num) + 1))
                        else:
                            break
                    else:
                        print("Unknown person")

                    # 矩形框
                    # draw rectangle
                    for kk, d in enumerate(faces):
                        # 绘制矩形框
                        cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)
                    #print('\n')
                #name = pin.get_pinyin(str(tempt[0]))
                # 在人脸框下面写人脸名字
                # write names under rectangle
                #print("111111",name_namelist)
                '''for i in range(len(faces)):
                    print("22222222222",name_namelist[i])
                    cv2.putText(img_rd,name_namelist[i],pos_namelist[i], font, 0.8, (0, 255, 255), 1, cv2.LINE_AA)'''

        #print("Faces in camera now:", name_namelist, "\n")

        cv2.putText(img_rd, "Press 'q': Quit", (20, 450), font, 0.8, (84, 255, 159), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Face Recognition", (20, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 100), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

        # 窗口显示 show with opencv
        cv2.imshow("camera", img_rd)

    # 释放摄像头 release camera
    cap.release()

    # 删除建立的窗口 delete all the windows
    cv2.destroyAllWindows()
	
	
if __name__ == "__main__":
	rune()


