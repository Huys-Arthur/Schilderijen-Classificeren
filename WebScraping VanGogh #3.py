from bs4 import BeautifulSoup, element
import requests
import os
import urllib.request

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False

urlPictures = []
baseUrl = 'http://www.vggallery.com/painting/'
url = 'p_0370.htm'
elementFound = True

urls = []
while elementFound :
    html_doc =requests.get(baseUrl + url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    src = soup.find_all('img')[2].get('src')
    urlPictures.append(baseUrl + src)

    # Oplossen loops in website
    if url == 'p_0169a.htm':
        url = 'p_0086.htm'
    elif url == 'p_0142.htm':
        url = 'p_0098.htm'

    else:
        elementFound = False
        elements = soup.find_all('a')
        for a in elements:
            font = a.find('font')
            if font and a.find('font').text == 'Next painting':
                url = a.get('href')
                elementFound = True

    '''# Check for loops
    if url in urls:
        print('Loop!!!!!')
    else:
        urls.append(url)
        print(url, elementFound)'''

path = 'd:\\DATA\\Documenten\\3e Bachelor informatica\\Deep learning\\Project Schilderijen\\schilderijen\\VanGogh'
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
