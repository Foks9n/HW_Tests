from Task_2.ya_main.ya_main_1 import get_folder, create_folder, base_url, headers
import pytest

bad_token = 'fsdffegrqrq'
bad_headers = {'Authorization': bad_token}

params_1 = [
    ('Test_Folder_1', headers, 201), #папка создана
    ('Test_Folder_1', headers, 409), #папка уже существует
    ('Test_Folder_bad', bad_headers, 401), #неавторизованный пользователь
    ('Test_Folder_2', headers, 201), #папка создана
    ('Test_Folder_3', headers, 201) #папка создана
]

params_2 = [
    ('Test_Folder_1', headers), #папка существует на диске
    ('Test_Folder_2', headers), #папка существует на диске
    ('Test_Folder_3', headers) #папка существует на диске
]

@pytest.mark.parametrize('foldername, headers, result', params_1)
def test_create_folder(foldername, headers, result):
    assert create_folder(base_url, headers, foldername) == result

@pytest.mark.parametrize('foldername, headers', params_2)
def test_get_folder(foldername, headers):
    assert get_folder(base_url, headers, foldername) == 200