import random
import sys
import time
import tb.tb_handle_api as tb
import common.utils as utils


if __name__ == '__main__':
    cnt = int(utils.runs_confirm())
    interval = int(utils.interval_confirm())
    check = utils.start_confirm(cnt, interval)
    if check == 'OK':
        index = 1
        while index <= cnt:
            print(f'第{index}次异常处理开始...')
            tb.handle_exception()
            print(f'第{index}次异常处理结束...')
            index += 1
            for i in range(interval, 0):
                print(f'执行倒计时：{i}s')
                time.sleep(1)
    else:
        sys.exit(0)
