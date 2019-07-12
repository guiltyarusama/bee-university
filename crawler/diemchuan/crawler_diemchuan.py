import requests
from bs4 import BeautifulSoup

from config.config_university_project import ConfigUniversityProject
from helper.error_helper import show_error_info
from helper.logger_helper import LoggerSimple
from helper.multithread_helper import multithread_helper
from helper.reader_helper import load_jsonl_from_gz, store_jsons_perline_in_file

logger = LoggerSimple(name=__name__).logger


def extract_data_diemchuan(url_diemchuan, university_meta, year=None):
    if year is None:
        diemchuan_datas = []

        for year in [2018, 2017, 2016, 2015, 2014]:
            try:
                url_with_year = f'{url_diemchuan}?y={year}'
                logger.info(f'prepare extract {url_with_year}')
                response = requests.get(url_with_year)
                if response.status_code == 200:
                    html = response.content
                    soup = BeautifulSoup(html, 'html.parser')
                    for e_tr in soup.select('table > .bg_white'):
                        e_tds = e_tr.select('td')
                        major_code = e_tds[1].get_text()
                        major_name = e_tds[2].get_text()
                        subject_groups = [subject_group.strip() for subject_group in e_tds[3].get_text().split(',')]
                        point = e_tds[4].get_text()
                        note = e_tds[5].get_text()
                        for subject_group in subject_groups:
                            diemchuan_obj = {
                                'major_code': major_code,
                                'major_name': major_name,
                                'subject_group': subject_group,
                                'point': point,
                                'note': note,
                                'year': year
                            }
                            logger.info(diemchuan_obj)
                            diemchuan_datas.append(diemchuan_obj)
                else:
                    logger.info(f'{response.status_code} - {url_with_year}')


            except Exception as e:
                logger.error(e)
                show_error_info(e)

        return {'diemchuan_datas': diemchuan_datas, 'university_meta': university_meta}
    return None


def method_univerisy_data(university_obj):
    university_diemchuan_data = extract_data_diemchuan(
        url_diemchuan=university_obj.get('url'),
        university_meta=university_obj
    )
    return university_diemchuan_data


if __name__ == '__main__':
    file_university_path = ConfigUniversityProject().file_university_path
    universities = load_jsonl_from_gz(file_university_path)

    # logger.info(universities)
    universities_diemchuan_data = multithread_helper(items=universities, method=method_univerisy_data,
                                                     timeout_concurrent_by_second=360, debug=False,
                                                     max_workers=20)
    file_university_diemchuan_path = ConfigUniversityProject().file_university_diemchuan_path
    store_jsons_perline_in_file(jsons_obj=universities_diemchuan_data, file_output_path=file_university_diemchuan_path)
    logger.info(f'stored file_university_diemchuan_path: {file_university_diemchuan_path}')
