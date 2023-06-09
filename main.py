import ocr
from easygui import msgbox, fileopenbox
from tkinter import *
import ctypes
import pyttsx3
from time import sleep
import re

zh_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0"
engine = pyttsx3.init()
engine.setProperty('voice', zh_voice_id)
volume = engine.getProperty('volume')
# noinspection PyTypeChecker
engine.setProperty('volume', volume + 10.0)
engine.runAndWait()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

window = Tk()
window.tk.call('tk', 'scaling', ScaleFactor / 100)
window.title('ocr工具箱')
window.geometry('800x600')
op1 = None


def btn1_command():
    msgbox('''感谢您使用本工具
本工具由年少无知的小学生Oliver开发，因学业压力较大，不能及时更新。有意见请发邮件至邮箱：2995306790@qq.com，可能不会回复，请谅解。

感谢大家的支持！

Oliver  版本号：2.4.0''', '关于')


def btn5_command():
    global op1
    op1 = fileopenbox('请选择文件')
    print(op1)
    str(op1)
    if op1 is None:
        msgbox('你没有选择文件，请重新选择')
    else:
        lbl2.configure(text=f'选择的图片是：{op1}')
        lbl2.place(x=0, y=0)


def btn3_command():
    global op1
    if op1 is None:
        msgbox('你没有选择文件')
    else:
        ocr_result = ocr.ocr_fuc(op1)
        u = list()
        for r in ocr_result:
            u.append(r.get('text'))
        s = 0
        s_list = []
        # print(ocr_result)
        for i in u:
            if re.search(r"\s", i):
                item = i.split()
                s_list = s_list + item
            else:
                s_list.append(i)

        for i in s_list:
            s += 1
            engine.say(i)
            lbl1.configure(text=f'正在播报第{s}个词语，总共有{str(len(s_list))}个词语')
            lbl1.update()
            engine.runAndWait()
            sleep(20)


def btn4_command():
    lbl1.configure(text='识别结果显示区')
    lbl1.update()


btn1 = Button(window, text='关于', font=('微软雅黑Light', 20), bg='red', fg='white', command=btn1_command)
btn3 = Button(window, text='报听写', font=('微软雅黑', 20), command=btn3_command, bg='yellow')
lbl1 = Label(window, text='识别结果显示区', font=('微软雅黑', 14))
btn4 = Button(window, text='清除', font=('微软雅黑', 20), command=btn4_command, bg='violet', fg='white')
lbl2 = Label(window, text='', font=('微软雅黑Light', 14))
btn5 = Button(window, text='选择图片', font=('微软雅黑', 20), bg='blue', fg='white', command=btn5_command)


def btn2_command():
    global op1
    if op1 is None:
        msgbox('你没有选择文件')
    else:
        lbl1.configure(text='正在识别中')
        ocr_result = ocr.ocr_fuc(op1)
        o = []
        for c in ocr_result:
            o.append(c.get('text'))

        lbl1.configure(text=f'''识别结果如下：
        {o}''')


btn2 = Button(window, text='提取图中文字', font=('微软雅黑', 20), command=btn2_command, bg='yellow')


class Ocr_tools:
    @staticmethod
    def main():
        btn1.place(x=700, y=0)
        btn2.place(x=580, y=300)
        btn3.place(x=670, y=450)
        btn4.place(x=700, y=100)
        btn5.place(x=650, y=200)
        lbl1.place(x=0, y=0, height=400, width=500)
        window.mainloop()


m = Ocr_tools()

m.main()
