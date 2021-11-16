import requests

headers = {
  'Authorization': 'yMHw4UidZM1Hha82AZtMjI50bYCfC3sdX7vvB',
}

# change to a full file path of the image you want to transform
body = {
  'image': open('./Random pictures/WGYJhgkdvBk.jpg', 'rb'),
}

response = requests.post('https://api-bin.hotpot.ai/remove-background', headers=headers, files=body)

# change to a full file path where you want to save the resulting image
with open('./Random pictures/test.jpg', 'wb') as file:
  file.write(response.content)

