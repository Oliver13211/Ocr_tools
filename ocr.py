from cnocr import CnOcr

ocr = CnOcr()


def ocr_fuc(photo):
    result = ocr.ocr(photo)
    return result


if __name__ == '__main__':
    demo = ocr_fuc("D:\\User\\oliver\\Desktop\\1.jpg")
    print(f"{demo}")
