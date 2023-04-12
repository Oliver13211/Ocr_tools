import easyocr
import pyttsx3
import random
import easygui
import time
import sys

engine = pyttsx3.init()


def ocr1(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    return result


def ocr2(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    s = dict()
    u = list()
    for i in result:
        s[i] = False
    while True:
        o = random.choice(result)
        if not s[o]:
            pyttsx3.speak(o)
            s[o] = True
            if easygui.buttonbox('好了吗？', 'ocr模块', ['好了', '还没有']) == '好了':
                continue
            else:
                time.sleep(8)
            for x in s:
                if s[x]:
                    u.append(x)
            if u == result:
                sys.exit()
        else:
            continue


if __name__ == '__main__':
    ocr1('E:\\1.png')
    ocr2('E:\\1.png')
