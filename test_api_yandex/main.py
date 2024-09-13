import yadisk
import requests

Client_ID = "98ada8bdd6ac411aa2fb3eaaf8af778d"

ya_token = ""  # необходимо поставить свой токен

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
test_headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {ya_token}'}


class NewFolderLibrary:
    """Создаем папку на Яндекс диске через библиотеку Yadisk[sync_defaults]"""

    def __init__(self, token, path):
        """указываем основные параметры,и срауз отправляем команды на проверку токена и создание папки"""
        self.path = path
        self.client = yadisk.Client(token=token)

    def check_token(self):
        """команда на проверку валидности токена"""
        try:
            with self.client:
                token_validity = self.client.check_token()
                if token_validity is True:
                    return "Токен валиден"
                else:
                    return "Ошибка! Токен не подошел"
        except ConnectionError:
            return "Ошибка! Неудалось установить соединение"

    def create_folder(self):
        """Создаем папку"""
        try:
            with self.client:
                self.client.mkdir(self.path)
                return f"папка создана успешно"
        except yadisk.exceptions.DirectoryExistsError:
            return "Ошибка! Такая папка уже существует"


class NewFolderRequest:
    """Создаем папку на Яндекс диске через Requests"""

    def __init__(self, headers, path):
        """определяем основные параметры, и отправляем команду на создание папки """
        self.headers = headers
        self.params = {"path": path}
        self.url = "https://cloud-api.yandex.net/v1/disk/resources?"

    def create_folder(self):
        """команда на создание папки"""
        response = requests.put(url=self.url, headers=self.headers, params=self.params)
        if response.status_code == 201:
            return "Папка создана успешно"
        elif response.status_code == 400:
            return "Ошибка! Неверный запрос"
        elif response.status_code == 401:
            return "Ошибка! Проверьте идентификатор/токен"
        elif response.status_code == 409:
            return "Ошибка! Такая папка уже существует"


if __name__ == "__main__":
    pass
