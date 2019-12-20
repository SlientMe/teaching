import cv2, os
import numpy as np


def read_data(path, sz=None):
    pr_img = []  # 图像列表
    pr_flg = []  # 对应标签
    pr_count = 0  # 初始化检测到的人数
    for dirname, dirnames, filenames in os.walk(path):  # 遍历当前程序目录
        for subdirname in dirnames:  # 遍历程序文件夹下的各个目录
            subject_path = os.path.join(dirname, subdirname)
            print(subject_path)
            for filename in os.listdir(subject_path):  # 遍历文件夹下文件
                try:
                    filepath = os.path.join(subject_path, filename)
                    im = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # 读取文件夹下PGM文件
                    if im.shape != (200, 200):  # 判断像素是否200
                        im = cv2.resize(im, (200, 200))
                    pr_img.append(np.asarray(im, dtype=np.uint8))  # 添加图像
                    pr_flg.append(pr_count)  # 添加标签
                except:
                    print("io error")
            pr_count += 1  # 另一个人的标签
    return [pr_img, pr_flg]


def face_rec():
    names = ['lemon', 'star']
    [pics, flags] = read_data(os.getcwd() + '/demo/')
    flags = np.asarray(flags, dtype=np.int32)  # 转为NUMPY的ARRAY
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(pics), np.asarray(flags))
    face_cascade = cv2.CascadeClassifier('default.xml')
    img = cv2.imread('WechatIMG10.jpg')
    while True:
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi = gray[x:x + w, y:y + h]
            try:
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                params = model.predict(roi)  # predict（）返回一个元祖格式值 （标签，系数）
                cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)
            except:
                continue
        cv2.imshow("abc", img)
        k = cv2.waitKey(1)
        if k == 32:  # press 'SPACE' to quit
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_rec()