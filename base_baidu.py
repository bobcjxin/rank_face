# -*- coding: UTF-8 -*-
# 百度人脸识别：https://ai.baidu.com/ai-doc/FACE/ek37c1qiz#%E4%BA%BA%E8%84%B8%E6%A3%80%E6%B5%8B
from aip import AipFace

from config import BAIDU_ID, BAIDU_KEY, BAIDU_SECRET_KEY

'''
百度人脸识别
优点：可免费使用，个人账户的限制为2QPS,企业账户的限制为10QPS
'''

""" 你的 APPID AK SK """
APP_ID = BAIDU_ID
API_KEY = BAIDU_KEY
SECRET_KEY = BAIDU_SECRET_KEY

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

"""
image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"

imageType = "BASE64"

# 调用人脸检测
client.detect(image, imageType)


# 如果有可选参数
options = dict()
options["face_field"] = "age"
options["max_face_num"] = 2
options["face_type"] = "LIVE"
options["liveness_control"] = "LOW"

# 带参数调用人脸检测
client.detect(image, imageType, options)
"""

if __name__ == "__main__":
    url = "https://smartracing.oss-cn-hangzhou.aliyuncs.com/shared/images/profiles/full/1571196895035.jpg"
    options = {
        "face_field": "age,beauty,expression,face_shape,emotion"
    }
    res = client.detect(url, "URL", options)
    face = res['result']['face_list'][0]

    expression = {"none": "不笑", "smile": "微笑", "laugh": "大笑"}
    face_shape = {"square":" 正方形", "triangle": "三角形", "oval": "椭圆", "heart": "心形", "round": "圆形"}
    emotion = {"angry": "愤怒", "disgust": "厌恶", "fear": "恐惧", "happy": "高兴", "sad": "伤心", "surprise": "惊讶", "neutral": "无情绪"}

    print(f"检测年龄：{face['age']},颜值：{face['beauty']},表情：{expression.get(face['expression']['type'])},脸型：{face_shape.get(face['face_shape']['type'])}, 情绪:{emotion.get(face['emotion']['type'])}")

