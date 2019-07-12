#  Copyright (c) 2019 BeeCost Team <beecost.com@gmail.com>. All Rights Reserved
#  BeeCost Project can not be copied and/or distributed without the express permission of @tuantmtb

import json

from helper.datetime_helper import get_date_current, get_date_time_current
from helper.encode_json_helper import default_encode
from helper.logger_helper import LoggerSimple
from helper.reader_helper import store_gz, store_file

logger = LoggerSimple(name=__name__).logger


def write_log(set_file_name, data, id=None, gzip_mode=True, folder_output_log_tracker='/bee/data/log'):
    try:
        if id is None:
            data_log = json.dumps(data, ensure_ascii=False, default=default_encode) + '\n'
        else:
            data_log = str(id) + ' ' + json.dumps(data, ensure_ascii=False, default=default_encode) + '\n'
        # print(data_log)

        if gzip_mode is True:
            file_output_path = folder_output_log_tracker + '/' + get_date_current() + '/' + set_file_name + '/' + get_date_time_current() + '.gz'
            store_gz(content=data_log, file_output_path=file_output_path, is_append=True)
        else:
            file_output_path = folder_output_log_tracker + '/' + get_date_current() + '/' + set_file_name + '/' + get_date_time_current() + '.txt'
            store_file(data_log, file_output_path)
    except Exception as e:
        logger.error(e)
