from bs4 import BeautifulSoup
import requests
import os
import urllib.request

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

html_doc =requests.get('http://www.rembrandtpainting.net/complete_catalogue/complete_catalogue.htm').text
soup = BeautifulSoup(html_doc, 'html.parser')

urlCatalogues = []

for link in soup.find('table', {'class': 'tablelinks'}).find_all('a'):
    urlCatalogues.append('http://www.rembrandtpainting.net/complete_catalogue/' + link.get('href'))

urlPicturePages = []

for url in urlCatalogues:
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    for td in soup.find_all('td', {'class': None}):
        urlPicturePages.append('http://www.rembrandtpainting.net/complete_catalogue/' + td.find('a').get('href'))

urlPictures = []
for url in urlPicturePages:
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    div = soup.find('div', {'id': 'workimage'})
    if div:
        urlParent = url[:str(url).rindex('/')+1]
        src = div.find('img').get('src')
        src = src.replace(' ', '%20')

        filePath = 'file:///C|/SITES/REMBRANDTold'
        if src.startswith(filePath):
            urlPictures.append('http://www.rembrandtpainting.net' + src[len(filePath):])
        else:
            urlPictures.append(urlParent + src)


path = 'd:\\DATA\\Documenten\\3e Bachelor informatica\\Deep learning\\Project Schilderijen\\schilderijen\\Rembrandt'
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)

i = 0
for url in urlPictures:
    if is_url_image(url):
        urllib.request.urlretrieve(url, str(i) + '.jpg')
        i+=1
    else:
        print("Image doesn't exist at: " + url)