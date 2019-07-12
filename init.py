import logging
import os
import sys

folder_root_path = '/Volumes/WORK/wp/startup/meowbees'
folder_python_path = folder_root_path + '/git/bee-university'

print('folder_python_path:', folder_python_path)

os.putenv('PYTHONPATH', folder_python_path)
os.putenv('folder_root_path', folder_root_path)
os.putenv('folder_root_path', folder_root_path)



# logging.basicConfig(stream=sys.stdout, level=logging.INFO)

os.system('bash')
