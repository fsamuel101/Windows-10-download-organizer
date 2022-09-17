import collections
import os
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'mkb']
EXT_IMGS = ['png', 'jpg', 'jpeg', 'gif', 'svg']
EXT_DOCS = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']
EXT_JS = ['txt']

# create a download organizer folder
path = os.path.expanduser('~\Desktop\Download Organizer')

if not os.path.exists(path):
    os.makedirs(path)

# Step 1  create a diretories where we want to store the files
BASE_PATH = os.path.expanduser('~\Desktop\Download Organizer')
DEST_DIRS = ['Music', 'Video', 'Photos', 'Documents', 'Application', 'Compressed', 'Javascript-Notes', 'Others']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# step 2  - map files from downloads folder based o their file extension

DOWNLOADS_PATH = os.path.expanduser('~\Downloads')
file_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    file_ext = file_name.split('.')[-1]
    file_mapping[file_ext].append(file_name)

pprint(file_mapping)

# step 3  move all the files given to  the target directory
for f_ext, f_list in file_mapping.items():

    if f_ext in EXT_AUDIO:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Video', file))

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Photos', file))

    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Documents', file))

    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Application', file))

    elif f_ext in EXT_INSTL:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Compressed', file))

    elif f_ext in EXT_JS:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Javascript-Notes', file))

    else:
        for file in f_list:
            os.renames(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Others', file))


print("DONE")
