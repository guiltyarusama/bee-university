#  Copyright (c) 2019 BeeCost Team <beecost.com@gmail.com>. All Rights Reserved
#  BeeCost Project can not be copied and/or distributed without the express permission of @tuantmtb
import os
import sys

from helper.logger_helper import LoggerSimple

logger = LoggerSimple(name=__name__).logger


def show_error_info(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logger.error(f'{exc_type}, {fname}, {exc_tb.tb_lineno}')
