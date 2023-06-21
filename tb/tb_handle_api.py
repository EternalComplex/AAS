import random
import time
import pyautogui
import common.constant as constant
import common.utils as utils


def handle_exception():
    """
    淘宝的滑块异常处理
    :return:
    """
    # TODO 进入软件主界面
    utils.into_software()

    # TODO 捕捉[去解决]操作的坐标
    p1 = utils.get_xys(constant.EXCEPTION_PATH)
    print(f'捕获到的[去解决]坐标：{p1}')

    # TODO 对[去解决]逐个处理
    for p in p1:
        print(f'点击[去解决]：{p}')
        pyautogui.moveTo(p.left + int(p.width / 2), p.top + int(p.height / 2), duration=0.35)
        pyautogui.click()
        time.sleep(4)

        # TODO 判断是否存在[滑块]
        p4 = utils.get_xy(constant.SLIDER_PATH)
        if p4 is not None:
            # TODO 点击[手动处理]
            p2 = utils.get_xy(constant.MANUAL_PROCESS_1_PATH)
            if p2 is None:
                p2 = utils.get_xy(constant.MANUAL_PROCESS_2_PATH)
            if p2 is not None:
                print(f'点击[手动处理]：{p2}：{p2}')
                pyautogui.moveTo(p2[0], p2[1], duration=0.35)
                pyautogui.click()
                time.sleep(4)

                # TODO 点击[刷新]
                p3 = utils.get_xy(constant.REFRESH_PATH)
                print(f'点击[刷新]：{p3}')
                pyautogui.moveTo(p3[0], p3[1], duration=0.35)
                pyautogui.click()
                time.sleep(2)
                pyautogui.click()
                time.sleep(random.randint(7, 10))

                # TODO 拖拽[滑块]
                print(f'拖拽[滑块]：{p4}')
                pyautogui.moveTo(p4[0], p4[1], duration=0.45)
                pyautogui.mouseDown()
                pyautogui.moveRel(random.randint(90, 100), random.randint(5, 10), duration=0.20)
                pyautogui.mouseUp()
                time.sleep(1)
                pyautogui.moveTo(p4[0], p4[1], duration=0.45)
                pyautogui.mouseDown()
                pyautogui.moveRel(random.randint(95, 110), random.randint(5, 10), duration=0.25)
                pyautogui.moveRel(random.randint(95, 110), random.randint(-10, -5), duration=0.20)
                pyautogui.moveRel(random.randint(95, 100), random.randint(5, 10), duration=0.15)
                pyautogui.mouseUp()
                time.sleep(5)

                # TODO 点击[处理完成]
                p5 = utils.get_xy(constant.PROCESS_COMPLETED_1_PATH)
                if p5 is None:
                    p5 = utils.get_xy(constant.PROCESS_COMPLETED_2_PATH)
                print(f'[处理完成]坐标：{p5}')
                pyautogui.moveTo(p5[0], p5[1], duration=0.35)
                pyautogui.click()
                pyautogui.moveRel(100, 100, duration=0.35)
                pyautogui.click()
                time.sleep(4)

        # TODO 重新进入软件主界面
        utils.into_software()
        time.sleep(4)
