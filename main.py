from pywinauto.application import Application

class chatTool():
    def __init__(self):
        self.app = None

    def start(self):
        # 常用方式一：连接已有微信进程（进程号在 任务管理器-详细信息 可以查看）
        # app = Application(backend='uia').connect(process=8948)
        # 常用方式二：启动微信进程 （注意路径中特殊字符的转义，/和\，不注意有时会出错）
        self.app = Application(backend="uia").start(r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')

    def stop(self):
        self.app.kill()

def chat():
    pass

print("start")
ct = chatTool()
ct.start()
ct.stop()