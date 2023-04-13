import easyocr
import pyttsx3
import random
import easygui
import time

engine = pyttsx3.init()


def ocr1(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    return result


def ocr2(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    random.shuffle(result)
    for i in result:
        pyttsx3.speak(i)
        op = easygui.buttonbox('好了吗？','ocr模块',['好了','还没好'])
        if op == '好了':
            pass
        else:
            time.sleep(10)


        easygui.msgbox('使用完毕','ocr主程序','结束')

if __name__ == '__main__':
    ocr1('E:\\1.png')
    ocr2('E:\\1.png')
