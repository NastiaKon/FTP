import os


def default_path(name):  # функция для создания папки
    if name == 'admin':
        pathway = '/'.join(os.getcwd().split('/')[0:-1]) + '/users_directory'
        return pathway
    cwd = '/'.join(os.getcwd().split('/')[0:-1]) + '/users_directory'  # находим путь к папке users_directory
    pathway = os.path.join(cwd, name)  # указываем путь к папке с названием юзера
    if os.path.isdir(f'../users_directory/{name}') is False:  # создаем директорию для юзера, если она не создана
        os.mkdir(f'{pathway}')
    else:
        print(f"Стандартная директория уже создана - {pathway}")  # предупреждаем, что она создана, если создана
    return pathway  # возвращаем путь к созданной папке