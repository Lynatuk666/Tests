import pytest
import main as m

ya_ne_token = "adasda"
test_ne_headers = {"Content-Type": "no"}
test_headers_no_token = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {ya_ne_token}'}


def test_new_folder_library():
    assert m.NewFolderLibrary(m.ya_token, "new_1").create_folder() == "папка создана успешно"
def test2_new_folder_library():
    assert m.NewFolderLibrary(m.ya_token, "new_1").create_folder() == "Ошибка! Такая папка уже существует"
def test3_new_folder_library():
    assert m.NewFolderLibrary(ya_ne_token, "new_3").check_token() == "Ошибка! Токен не подошел"
@pytest.mark.xfail
def test4_new_folder_library():
    assert m.NewFolderLibrary(ya_ne_token, "new_4").check_token() == "успешно"
# @pytest.mark.parametrize(
#     "headers, path",
#     (
#             (m.test_headers, "test1_folder"),
#             (m.test_headers, "test1_folder"),
#             (test_ne_headers, "test3_folder"),
#              (test_headers_no_token, "test4_folder")
#     )
# )
def test_new_folder_request():
    assert m.NewFolderRequest(m.test_headers, "test1_folder").create_folder() == "Папка создана успешно"
def test2_new_folder_request():
    assert m.NewFolderRequest(m.test_headers, "test1_folder").create_folder() == "Ошибка! Такая папка уже существует"
def test3_new_folder_request():
    assert m.NewFolderRequest(test_ne_headers, "test3_folder").create_folder() == "Ошибка! Неверный запрос"
def test4_new_folder_request():
    assert m.NewFolderRequest(test_headers_no_token, "test4_folder").create_folder() == ("Ошибка! Проверьте идентификатор/токен")
@pytest.mark.xfail
def test3_new_folder_request():
    assert m.NewFolderRequest(m.test_headers, "new_4").create_folder() == "Ошибка! Неверный запрос"

