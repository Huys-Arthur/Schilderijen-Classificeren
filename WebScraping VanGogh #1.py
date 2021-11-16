from bs4 import BeautifulSoup
import requests
import os

#Site protected against WebScraping

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

urlPictures = []
baseUrl = 'https://www.vangoghgallery.com'
url = '/catalog/Painting/1/Agostina-Segatori-Sitting-in-the-Cafe-du-Tambourin.html'
lastUrl = ''

while url != lastUrl:
    html_doc =requests.get(baseUrl + url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(html_doc)

    src = soup.find('div', {'class': 'artwork-info'}).find('h4').get('href')
    urlPictures.append(baseUrl + src)

    lastUrl = url
    url = soup.find(id = 'nextbtn').find('a').get('href')

path = 'd:\\DATA\\Documenten\\3e Bachelor informatica\\Deep learning\\Project Schilderijen\\schilderijen\\VanGogh'
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)

i = 0
for url in urlPictures:
    if is_url_image(url):
        img_data = requests.get(url).iter_content
        with open(str(i) + '.jpg', 'wb') as handler:
            handler.write(img_data)
        i+=1
    else:
        print("Image doesn't exist at: " + url)