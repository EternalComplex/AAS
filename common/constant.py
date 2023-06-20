import os
import sys

"""
常量类
"""
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
# 屏幕截图
SCREENSHOT_PATH = BASE_DIR + '\\tb\\template\\screenshot.png'
# 窗口名称
WINDOW_NAME = '蜂鸟舆情'
# [去解决]图标
EXCEPTION_PATH = BASE_DIR + '\\tb\\template\\exception.png'
# [手动处理]图标
MANUAL_PROCESS_PATH = BASE_DIR + '\\tb\\template\\manual_process.png'
# [刷新]图标
REFRESH_PATH = BASE_DIR + '\\tb\\template\\refresh.png'
# [滑块]图标
SLIDER_PATH = BASE_DIR + '\\tb\\template\\slider.png'
# [处理完成]图标
PROCESS_COMPLETED_PATH = BASE_DIR + '\\tb\\template\\process_completed.png'
