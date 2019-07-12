#   Copyright (c) 2019 BeeCost Team <beecost.com@gmail.com>. All Rights Reserved
#   BeeCost Project can not be copied and/or distributed without the express permission of @tuantmtb
from config.config_university_project import ConfigUniversityProject
from helper.logger_helper import LoggerSimple
from helper.reader_helper import load_jsonl_from_gz, store_jsons_perline_in_file

logger = LoggerSimple(name=__name__).logger


def statistic_count_diemchuan(universities_diemchuan_data):
    count = 0
    for university_diemchuan in universities_diemchuan_data:
        count += len(
            [diemchuan for diemchuan in university_diemchuan.get('diemchuan_datas') if diemchuan.get('year') == 2018])
        logger.info(
            [diemchuan for diemchuan in university_diemchuan.get('diemchuan_datas') if diemchuan.get('year') == 2018])
    logger.info(count)


if __name__ == '__main__':
    file_university_diemchuan_path = ConfigUniversityProject().file_university_diemchuan_path
    universities_diemchuan_data = load_jsonl_from_gz(file_university_diemchuan_path)
    # statistic_count_diemchuan(universities_diemchuan_data)
    majors = set()
    for university_diemchuan in universities_diemchuan_data:
        for diemchuan in university_diemchuan.get('diemchuan_datas'):
            majors.add(diemchuan.get('major_name'))
    logger.info(list(majors))
    file_major_path = ConfigUniversityProject().file_major_path
    store_jsons_perline_in_file(jsons_obj=list(majors), file_output_path=file_major_path)
    logger.info(f'major statistic: {file_major_path}')