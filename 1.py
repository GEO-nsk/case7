import os

MENU = ('1. Просмотр каталога\n'
        '2. На уровень вверх\n'
        '3. На уровень вниз\n'
        '4. Количество файлов и каталогов\n'
        '5. Размер текущего каталога\n'
        '6. Поиск файла\n'
        '7. Выход из программы\n')

def acceptCommand():
    '''

    The function asks from user function

    '''
    num_command = int(input('Seleсt item from menu: '))
    if 0 < num_command < 8:
        return num_command
    else:
        return 'Error! please try again.'

def runCommand(command):
    '''

    The function runs selected feature

    '''
    if command == 1:
        return showDir()
    if command == 2:
        return moveUp()
    if command == 3:
        path = os.getcwd()
        return moveDown(path)
    if command == 4:
        path = os.getcwd()
        return print(countFiles(path))
    if command == 5:
        path = os.getcwd()
        return print(get_total_size(path))
    if command == 6:
        target = str(input('Enter the string that should be included \
in the file name: '))
        path = str(input('Specify the path to the directory where we \
are starting the search: '))
        return print(findFiles(target, path))
    if command == 7:
        return 7

def moveUp():
    '''

    The function moves uoy to rhe root directory

    '''
    os.chdir('../')

def moveDown(path):
    '''

    The function moves you to the selected directory

    '''
    s = os.listdir(path)
    for itr in s:
        if os.path.isdir(path + '\\' + itr):
            print(itr)
    currentDir = os.getcwd()
    newDir = str(input('enter name of directory: '))
    rootDir = currentDir + '\\' + newDir
    os.chdir(rootDir)

def showDir():
    '''

    The function shows files in the directory

    '''
    Dir_now = (os.listdir())
    print('files in the directory: ')
    for itr in Dir_now:
        print('- ' + itr)

def countFiles(path):
    '''

    The function shows number of files in the directory

    '''

    cnt = 0

    for itr in os.listdir(path):
        new_path = path + '\\' + itr
        if os.path.isfile(new_path):
            cnt += 1
        if os.path.isdir(new_path):
            cnt += 1
        if os.path.isdir(new_path):
            cnt += countFiles(new_path)
    return cnt
def findFiles(target, path):
    '''The function generates a list of file paths whose name contains
    the "target" parameter.

    Parameters:
    target - name of the required file
    path - path to the directory where the function start the search

    '''
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if target in file:
                file_list.append(os.path.join(root, file))
    if file_list:
        return file_list
    else:
        return "The file was not found."

def get_total_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print('Работа программы завершена.')
            break


main()
