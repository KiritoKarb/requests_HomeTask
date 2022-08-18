import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        _splited_file_path = file_path.split('/')
        file_name = _splited_file_path[-1]
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content_Type': 'aplication/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        '''
        В пути указана папка, в которую я решил добавить файл, У вас этой папки не будет.
        Для корректной работы программы нужно изменить "path" на "{}" в "params", но у меня так все сработало =)
        '''
        params = {'path': 'HT_for_Netology/{}' .format(file_name), 'overwrite': 'true'}
        page = requests.get(url, params=params, headers=headers).json()
        href = page.get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
