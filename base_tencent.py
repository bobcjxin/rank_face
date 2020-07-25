# -*- coding: UTF-8 -*-
# 腾讯人脸识别：https://ai.qq.com/doc/detectface.shtml#1-%E6%8E%A5%E5%8F%A3%E6%8F%8F%E8%BF%B0
import base64
import hashlib
import random
import requests
import string
import time
from urllib.parse import urlencode

from config import TC_ID, TC_KEY

'''
腾讯人脸识别
优点：
缺点：签名是真的难搞，检测内容好像也没有百度多
'''

APP_ID = TC_ID
APP_KEY = TC_KEY


def get_params(img):
    time_stamp = str(int(time.time()))
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    params = {
        'app_id': APP_ID,
        'image': img,
        'mode': '0',
        'time_stamp': time_stamp,
        'nonce_str': nonce_str
    }

    sort_dict = sorted(params.items(), key=lambda item: item[0], reverse=False)
    sort_dict.append(('app_key', APP_KEY))
    rawtext = urlencode(sort_dict).encode()
    sha = hashlib.md5()
    sha.update(rawtext)
    md5text = sha.hexdigest().upper()
    params['sign'] = md5text
    return params


def main(img):
    '''
    #用python系统读取方法
    f = open('c:/girl.jpg','rb')
    img = base64.b64encode(f.read())   #得到API可以识别的字符串
     '''
    #用opencv读入图片
    # frame=cv2.imread('e:/python/dlib/r3.jpg')
    # nparry_encode = cv2.imencode('.jpg', frame)[1]
    # data_encode = np.array(nparry_encode)
    # img = base64.b64encode(data_encode)    #得到API可以识别的字符串

    params = get_params(img)

    url = "https://api.ai.qq.com/fcgi-bin/face/face_detectface"  # 人脸分析
    res = requests.post(url, params).json()

    face = res['data']['face_list'][0]
    print(f"检测年龄{face['age']}, 颜值{face['beauty']}, 心情愉悦值:{face['expression']}")


if __name__ == "__main__":
    with open("face.jpg", "rb") as f:
        image = base64.b64encode(f.read())

    main(image)
