class ConfigUniversityProject:

    def __init__(self, *args, **kwargs):
        self.folder_data_base = kwargs.get('folder_data_base', '/bee_university')

    @property
    def folder_output_path(self):
        return self.folder_data_base + '/crawler/common'

    @property
    def file_university_path(self):
        return self.folder_output_path + '/university.gz'

    @property
    def file_university_diemchuan_path(self):
        return self.folder_output_path + '/university_diemchuan.gz'

    @property
    def file_major_path(self):
        return self.folder_output_path + '/major.gz'
