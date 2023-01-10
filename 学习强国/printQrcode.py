import base64
import pyqrcode
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
from io import BytesIO

def printQrcode(base64Str):
    # 1.解码Base64字符串
    img_data = base64.b64decode(base64Str)

    # 2.将节码结果转为字节流
    byte_stream = BytesIO(img_data)

    # 3.打开字节流得到图片对象
    img = Image.open(byte_stream)

    img = ImageEnhance.Brightness(img).enhance(2.0)  #增加亮度
    img = ImageEnhance.Contrast(img).enhance(4.0)  #增加对比度


    # img.show()  # 播放图片，供测试用


    barcodes = pyzbar.decode(img)

    # 5.打印解析结果
    url=barcodes[0].data.decode("utf-8")
    code = pyqrcode.create(url)
    code.svg("uca-url.svg", scale=8)
    code.eps("uca-url.eps", scale=2)

    print("用学习强国扫码登录，如未安装扫码下载:")
    print(code.terminal(quiet_zone=1))
    print("或者网页访问该链接：")
    print(url)

