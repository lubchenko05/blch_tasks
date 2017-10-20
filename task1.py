from os import listdir, access, R_OK, getcwd
from os.path import isfile, getctime, join as os_join
import hashlib


'''
Task:
Твій комп'ютер потрапив до рук твого колеги, який вирішив пожартувати та скопіював багато файлів до випадкових
директорій по всій файловій системі. Тим більше дублікати збережені з абсолютно рандомними незручними іменами.
 Наприклад - "this_something _like.txt"
Напишіть функцію, яка повертає масив усіх файлів-дублікатів. Щоб точно зрозуміти, що два файли є точними дублікатами
 поверніть масив масивів, де перший елемент файл-клон, другий - оригінальний файл.
 Наприклад: [ ['/tmp/I_like_banana.mpg', '/home/parker/my_banana.mpg'], ['/home/trololol.mov',
  '/etc/apache2/httpd.conf'] ]
'''


def get_copies(path):
    # List of dirs if found in dir some dirs just add it to list
    dirs = [path, ]
    # Add files using format {md5: [[path1,path2], date]}
    files = {}
    # Loop that using for get files from all directories
    for _dir in dirs:
        try:
            items = [os_join(_dir, i) for i in listdir(_dir)]
        except FileNotFoundError:
            print('Wrong path: %s' % _dir)
            continue
        # Check if item is file - add it to dictionary or if item is directory - add it to dirs.
        for item in items:
            if isfile(item):
                if not access(item, R_OK):  # Check permissions for data reading.
                    print('Access error: %s' % _dir)
                    break
                try:
                    with open(item, 'rb') as file_to_check:
                        data = file_to_check.read()
                        md5_returned = hashlib.md5(data).hexdigest()  # get md5 file sum
                    if md5_returned:
                        # Get file creation time (used for identification witch file is original file)
                        date = getctime(item)
                        # Check if file was not exist - just add it to dictionary/
                        if md5_returned in files:
                            # If file exist check original date in dict, and if this file created before - insert it on
                            # first position, else in the end of list.
                            f = files[md5_returned]
                            if f[1] > date:
                                f[0].insert(0, item)
                                f[1] = date
                            else:
                                f[0].append(item)
                        else:
                            files[md5_returned] = [[item, ], date]
                except OSError:  # I got it when i try to read system files.
                    print('Data read error: %s' % item)
                    continue
            else:
                dirs.append(item)
    # Return result with a user-specified format.
    result = []
    [[[result.append([item[0], z]) for z in item[1:]] for item in v[:1]] for k, v in files.items() if len(v) > 1]
    return result

if __name__ == '__main__':
    print(get_copies(os_join(getcwd(), 'test_dir')))  # For testing
