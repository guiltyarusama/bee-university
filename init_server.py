import os
import sys

folder_root_path = '/bee'
folder_python_path = folder_root_path + '/git/bee-university'

print('folder_python_path:', folder_python_path)

os.putenv('PYTHONPATH', folder_python_path)
os.putenv('folder_root_path', folder_root_path)

os.system('bash')
