import ocr
from easygui import *


class Ocr_tools:
    @staticmethod
    def main():
        op = buttonbox('欢迎使用ocr工具箱，请选择你要使用的功能', 'ocr主程序', ['提取图片文字', '报听写'])
        if op == '提取图片文字':
            op2 = fileopenbox('请选择图片', '文件资源管理器')
            msgbox(f'识别结果如下：\n{ocr.ocr1(op2)}')
        else:
            op2 = fileopenbox('请选择图片', '文件资源管理器')
            ocr.ocr2(op2)


m = Ocr_tools()


try:
    m.main()
except Exception as e:
    msgbox(
        f'发生了问题，请不要再选择选项或选择文件的时候关闭窗口。如果没有非法的操作但仍然看到此窗口，请将：{e}发给我',
        '错误报告', '好的')

msgbox("""感谢您使用本工具
本工具由年少无知的小学生Oliver开发，因学业压力较大，不能及时更新。有意见请发邮件至邮箱：2995306790@qq.com，可能不会回复，请谅解。
感谢python的开发团队和Guido Van Rossum，感谢easygui、pyttsx3的开发者，也感谢兔子喝咖啡给我了灵感。
由于这是初版，还不够完善。若无法运行，请更换环境然后重试。

感谢大家的支持！

Oliver  版本号：1.0.0""", '自述', '结束')
