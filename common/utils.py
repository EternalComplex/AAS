import cv2
import pyautogui
import win32con
import win32gui

import common.constant as constant


def start_confirm(cnt, interval):
    """
    程序运行确认窗口
    :return: OK | Cancel
    """
    return pyautogui.confirm(text=f'脚本运行{cnt}次, 结束后间隔{interval}秒再次运行, 确认启动吗？', title='AAS', buttons=['OK', 'Cancel'])


def error_confirm():
    """
    程序出现错误的提示窗口
    :return:
    """
    return pyautogui.confirm(text='找不到目标窗口，请打开软件', title='AAS', buttons=['OK'])


def runs_confirm():
    """
    程序运行次数选择窗口
    :return:
    """
    return pyautogui.confirm(text='请选择脚本运行次数.', title='AAS', buttons=[1, 5, 10, 999])


def interval_confirm():
    """
    程序运行间隔选择窗口
    :return:
    """
    return pyautogui.confirm(text='请选择脚本运行间隔时间.', title='AAS', buttons=[120, 180, 240, 300])


def into_software():
    """
    进入软件的主界面
    :return:
    """
    try:
        h = win32gui.FindWindow(None, constant.WINDOW_NAME)
        win32gui.SetForegroundWindow(h)
        if win32gui.IsIconic(h):
            win32gui.ShowWindow(h, win32con.SW_SHOWMAXIMIZED)
    except:
        error_confirm()


def get_xy(img_model_path):
    """
    确定目标点击坐标
    :param img_model_path: 模板图片路径
    :return: 返回目标点击位置的中心坐标
    """
    # 将屏幕截图保存
    pyautogui.screenshot().save(constant.SCREENSHOT_PATH)

    # 读取图像
    img = cv2.imread(constant.SCREENSHOT_PATH)
    img_terminal = cv2.imread(img_model_path)  # 图像模板

    # 进行模板匹配
    res = pyautogui.locateCenterOnScreen(img_model_path)

    return res


def get_xys(img_model_path):
    """
        确定所有[去解决]坐标
        :param img_model_path: 模板图片路径
        :return: 返回坐标列表
        """
    # 将屏幕截图保存
    pyautogui.screenshot().save(constant.SCREENSHOT_PATH)

    # 读取图像
    img = cv2.imread(constant.SCREENSHOT_PATH)
    img_terminal = cv2.imread(img_model_path)  # 图像模板

    # 进行模板匹配
    res = list(pyautogui.locateAllOnScreen(img_model_path))

    return res


