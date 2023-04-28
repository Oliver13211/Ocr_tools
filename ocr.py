import easyocr
import pyttsx3

engine = pyttsx3.init()


def ocr(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    return result


