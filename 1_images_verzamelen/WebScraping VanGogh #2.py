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

html_doc =requests.get('https://www.vincentvangogh.org/van-gogh-paintings.jsp').text
soup = BeautifulSoup(html_doc, 'html.parser')

urlPictures = []

images = soup.find('table').find_all('img')
for img in images:
    urlPictures.append('https://www.vincentvangogh.org' + img.get('src'))

path = 'd:\\DATA\\Documenten\\3e Bachelor informatica\\Deep learning\\Project Schilderijen\\schilderijen\\VanGogh'
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)

i = 0
for url in urlPictures:
    print(url)
    if is_url_image(url):
        img_data = requests.get(url).iter_content
        with open(str(i) + '.jpg', 'wb') as handler:
            print(img_data.json())
            handler.write(img_data)
        i+=1
    else:
        print("Image doesn't exist at: " + url)