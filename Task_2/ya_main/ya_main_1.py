import requests

base_url = 'https://cloud-api.yandex.net/v1/disk'
headers = {'Authorization': 'YATOKEN'} #Введите свой токен Яндекса

def create_folder(base_url, headers, folder_name):
    folder_url_pre = f'{base_url}/resources?path=/{folder_name}'
    response = requests.put(folder_url_pre, headers=headers)
    print(response.status_code)
    return response.status_code

def get_folder(base_url, headers, folder_name):
    folder_url_pre = f'{base_url}/resources?path=/{folder_name}'
    response = requests.get(folder_url_pre, headers=headers)
    print(response.status_code)
    return response.status_code

def delete_folder(base_url, headers, folder_name):
    folder_url_pre = f'{base_url}/resources?path=/{folder_name}'
    response = requests.delete(folder_url_pre, headers=headers)
    print(response.status_code)
    return response.status_code

def main():
    create_folder(base_url, headers, 'TESTFOLDER1')
    get_folder(base_url, headers, 'TESTFOLDER1')
    delete_folder(base_url, headers, 'TESTFOLDER1')

if __name__ == '__main__':
    main()


