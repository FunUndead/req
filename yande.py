import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        TOKEN = ""
        headers = {'Content-Type': 'application/json', 'Authorization': TOKEN}


        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers_2 = headers
        params = {"path": self.file_path, "overwrite": "true"}
        response_2 = requests.get(upload_url, headers=headers_2, params=params)
        x = response_2.json()
        #print(response_2.json())
        href = x.get("href")
        #print(href)

        response_3 = requests.put(href, data=open(self.file_path, 'rb'))
        response_3.raise_for_status()
        #print(response_3.raise_for_status())

        return print('OK!')


if __name__ == '__main__':
    uploader = YaUploader('1.txt')
    result = uploader.upload()