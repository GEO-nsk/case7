import os

MENU = ('1. Просмотр каталога\n'
        '2. На уровень вверх\n'
        '3. На уровень вниз\n'
        '4. Количество файлов и каталогов\n'
        '5. Размер текущего каталога\n'
        '6. Поиск файла\n'
        '7. Выход из программы\n')

def acceptCommand():
    num_command = int(input('Выберите пункт меню: '))
    if 0 < num_command < 8:
        return num_command
    else:
        return 'Ошибка! Такой команды нет'

def runCommand(command):
    if command == 1:
        return showDir()
    if command == 2:
        return moveUp()
    if command == 3:
        return moveDown()
    if command == 4:
        path = os.getcwd()
        return print(countFiles(path))
    if command == 5:
        return 5
    if command == 6:
        target = str(input('Enter the string that should be included \
in the file name: '))
        path = str(input('Specify the path to the directory where we \
are starting the search: '))
        return print(findFiles(target, path))
    if command == 7:
        return 7

def moveUp():
    os.chdir('../')

def moveDown():
    s = os.listdir()
    for itr in s:
        if os.path.isdir:
            print(itr)
    currentDir = os.getcwd()
    newDir = str(input('Введите имя нужного каталога: '))
    rootDir = currentDir + '\\' + newDir
    os.chdir(rootDir)

def showDir():
    Dir_now = (os.listdir())
    print('Файлы в этом каталоге: ')
    for itr in Dir_now:
        print('- ' + itr)

def countFiles(path):
    count = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            count += 1
        elif os.path.isdir(item_path):
            count += countFiles(item_path)  # Рекурсивный вызов для подпапки
    return count

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
