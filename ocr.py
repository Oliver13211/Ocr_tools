import easyocr


def ocr(photo):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(photo, detail=0)
    return result


