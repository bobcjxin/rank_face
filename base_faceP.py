# -*- coding: UTF-8 -*-
# face+识别：https://console.faceplusplus.com.cn/documents/4888373
import base64
import requests

from config import FP_KEY, FP_SECRET
'''
Face+人脸识别
优点：接入方便，提供男女视角评分, 免费使用没有并发上限(但也不保证并发)
'''

API_KEY = FP_KEY
API_SECRET = FP_SECRET


def main(img):
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    data = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "image_base64": img,
        "return_attributes": "age,beauty"
    }
    res = requests.post(url, data=data).json()
    face = res['faces'][0]["attributes"]
    print(f'年龄：{face["age"]["value"]}，女性视角颜值：{face["beauty"]["female_score"]}，男性视角颜值：{face["beauty"]["male_score"]}')


if __name__ == "__main__":
    with open("face.jpg", "rb") as f:
        image = base64.b64encode(f.read())

    main(image)
