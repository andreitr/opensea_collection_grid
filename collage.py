from PIL import Image, ImageDraw
import urllib.request, json
import random
import sys
import requests


# OpenSea collection slug
os_slug = sys.argv[1]

# OpenSea api key
headers = {
 "Accept": "application/json",
 "X-API-KEY": sys.argv[2]
}


# Number of pages to sample. Default is 2 which is about 100 images.
# You can increase this number for more variability
os_sample = 3

images = []
img_idx = 0

for i in range(os_sample):
  # Pagination offset
  offset = (i*50)

  # Load collection data
  url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=%s&limit=50&collection=%s" % (offset,os_slug)

  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)

  # Loop through collection's assets and save images in the images folder
  for item in data['assets']:
    img_name =  "images/%s.png" % (img_idx)
    print(img_name)
 
    if item['image_url']:
      urllib.request.urlretrieve(item['image_url'], img_name)
      images.append(img_name)
      img_idx += 1

# Randomize saved images
random.shuffle(images)
img_idx = 0

# Create 1500x500 collage and open the resulting image
collage_xs = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
for i in range(15):
  for j in range(5):
    
    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((100, 100))
    collage_xs.paste(img, (i * 100, j * 100))
    img_idx +=1 

# Create 1500x500 collage and open the resulting image
img_idx = 0
random.shuffle(images)
collage_sm = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
for i in range(12):
  for j in range(4):

    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((125, 125))
    collage_sm.paste(img, (i * 125, j * 125))
    img_idx +=1


# Create 1500x500 collage and open the resulting image
img_idx = 0
random.shuffle(images)
collage_sm = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
for i in range(12):
  for j in range(4):

    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((125, 125))
    collage_sm.paste(img, (i * 125, j * 125))
    img_idx +=1

img_idx = 0
random.shuffle(images)
collage_md = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
for i in range(6):
  for j in range(2):

    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((250, 250))
    collage_md.paste(img, (i * 250, j * 250))
    img_idx +=1

img_idx = 0
random.shuffle(images)
collage_lg = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
for i in range(3):
  for j in range(1):

    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((500, 500))
    collage_lg.paste(img, (i * 500, j * 500))
    img_idx +=1

collage_lg.show()
collage_md.show()
collage_sm.show()
collage_xs.show()
