import ocr
from easygui import msgbox, fileopenbox
from tkinter import *
import ctypes
import pyttsx3
from time import sleep

zh_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0"
engine = pyttsx3.init()
engine.setProperty('voice', zh_voice_id)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 10.0)
engine.runAndWait()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

window = Tk()
window.tk.call('tk', 'scaling', ScaleFactor / 100)
window.title('ocr工具箱')
window.geometry('800x600')


def btn1_command():
    msgbox('''感谢您使用本工具
本工具由年少无知的小学生Oliver开发，因学业压力较大，不能及时更新。有意见请发邮件至邮箱：2995306790@qq.com，可能不会回复，请谅解。
感谢python的开发团队和Guido Van Rossum，感谢easygui、pyttsx3的开发者，也感谢兔子喝咖啡给我了灵感。

感谢大家的支持！

Oliver  版本号：2.0.0''', '关于')


def btn3_command():
    op2 = fileopenbox('请选择文件')
    ocr_result = ocr.ocr(op2)
    s = 0
    # print(ocr_result)
    for i in ocr_result:
        s += 1
        engine.say(i)
        lbl1.configure(text=f'正在播报第{s}个词语，总共有{str(len(ocr_result))}个词语')
        lbl1.update()
        engine.runAndWait()
        sleep(5)



def btn4_command():
    lbl1.configure(text='识别结果显示区')
    lbl1.update()


btn1 = Button(window, text='关于', font=('微软雅黑Light', 20), bg='red', fg='white', command=btn1_command)
btn3 = Button(window, text='报听写', font=('微软雅黑', 20), command=btn3_command, bg='yellow')
lbl1 = Label(window, text='识别结果显示区',  font=('微软雅黑', 14))
btn4 = Button(window, text='清除', font=('微软雅黑', 20), command=btn4_command, bg='violet', fg='white')


def btn2_command():
    op1 = fileopenbox('请选择文件')
    if op1 == None:
        msgbox('你没有选择文件，请重新选择')
    lbl1.configure(text='正在识别中')
    ocr_result = ocr.ocr(op1)
    lbl1.configure(text=f'''识别结果如下：
{ocr_result}''')


btn2 = Button(window, text='提取图中文字', font=('微软雅黑', 20), command=btn2_command, bg='yellow')


class Ocr_tools:
    @staticmethod
    def main():
        btn1.place(x=700, y=0)
        btn2.place(x=580, y=250)
        btn3.place(x=670, y=450)
        btn4.place(x=700, y=100)
        lbl1.place(x=0, y=0, height=400, width=500)
        window.mainloop()


m = Ocr_tools()

m.main()
