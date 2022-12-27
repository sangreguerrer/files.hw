import requests
from tocsi import TOKEN


base_url='https://akabab.github.io/superhero-api/api/all.json'

superhero_list=['Hulk','Captain America', 'Thanos']

supher={}
response=requests.get(base_url)
response=response.json()
for s in response:
    for hero in superhero_list:
        if hero in s["name"]:
            supher[hero]=s["powerstats"]["intelligence"]

max_iq=max(supher.values())
for name,iq in supher.items():
    if max_iq == iq:
        print(name)






class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type':'application/json',
            'Authorization':f'OAuth {self.token}'
        }
    def upload(self, path: str):
        self.base_host='https://cloud-api.yandex.net/'
        uri = 'v1/disk/resources/upload/'
        request_url=self.base_host+uri
        params={'path':'GOTY.py','overwrite':True}
        resp = requests.get(request_url, headers=self.get_headers(), params=params).json()
        print(resp)
        response=requests.put(url=resp['href'],data=open(path,'rb'),headers=self.get_headers())
        if response.status_code==201:
            print("загрузка прошла успешно")


if __name__ == '__main__':
    full_path=r'B:\Netology\GIt PYHW\GOTY.py'
    token=TOKEN
    uploader=YaUploader(token)
    uploader.upload(full_path)

