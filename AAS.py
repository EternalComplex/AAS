import random
import sys
import time
import tb.tb_handle_api as tb
import common.utils as utils


if __name__ == '__main__':
    check = utils.start_confirm()
    if check == 'OK':
        cnt = 1
        while True:
            print(f'第{cnt}次异常处理')
            tb.handle_exception()
            print(f'第{cnt}次异常处理结束')
            cnt += 1
            time.sleep(240)
    else:
        sys.exit(0)
