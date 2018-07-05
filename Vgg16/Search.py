import requests
from urllib.request import urlretrieve
import os



def Search(name, localpath, page):
    os.makedirs(localpath, exist_ok=True)
    params = {
        'tn': 'resultjsonavatarnew',
        'ie': 'utf-8',
        'cg': '',
        'itg': '',
        'z': '0',
        'fr': '',
        'width': '',
        'height': '',
        'lm': '-1',
        'ic': '0',
        's': '0',
        'word': name,
        'st': '-1',
        'gsm': '',
        'rn': '30'
    };
    params['pn'] = '%d' % page
    Request(params, localpath)
    return;


def Request(param, path):
    searchurl = 'http://image.baidu.com/search/avatarjson'
    response = requests.get(searchurl, params=param)
    json = response.json()['imgs']
    for i in range(0, len(json)):
        filename = os.path.split(json[i]['objURL'])[1]
        Download(json[i]['objURL'], filename, path)


def Download(url, filename, filepath):
    path = os.path.join(filepath, filename)
    try:
        urlretrieve(url, path)
        print('Downloading Images From ', url)
    except:
        print('Downloading None Images!')


if __name__ == '__main__':
    for i in range(0, 25):
        Search('老虎', 'data/tiger', i)
        Search('猫', 'data/cat', i)
