import requests
from bs4 import BeautifulSoup

from config.config_university_project import ConfigUniversityProject
from helper.logger_helper import LoggerSimple
from helper.reader_helper import store_jsons_perline_in_file

logger = LoggerSimple(name=__name__).logger


def get_content_request(url='https://diemthi.tuyensinh247.com/diem-chuan.html'):
    return requests.get(url).content


def extract_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    universities_data = []
    for e_li in soup.select('#benchmarking > li'):
        e_a = e_li.find('a')
        url = 'https://diemthi.tuyensinh247.com' + e_a.get('href') if e_a.get('href') != '' else None
        university_code = e_a.find('strong').get_text()
        university_name = e_a.get_text().split('-')[-1].strip()
        # logger.info(name)
        university_obj = {
            'url': url,
            'university_code': university_code,
            'university_name': university_name
        }
        universities_data.append(university_obj)
    return universities_data


if __name__ == '__main__':
    # folder_data_base = '/bee_university'

    url = 'https://diemthi.tuyensinh247.com/diem-chuan.html'
    content_html = get_content_request(url=url)
    universities_data = extract_content(html=content_html)
    logger.info(universities_data)
    file_university_path = ConfigUniversityProject().file_university_path
    # store file university.gz
    store_jsons_perline_in_file(jsons_obj=universities_data, file_output_path=file_university_path)
    logger.info(f'stored data in {file_university_path}')
