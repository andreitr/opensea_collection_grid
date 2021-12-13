from PIL import Image, ImageDraw
import urllib.request, json
import random

# OpenSea collection slug
os_slug = "vortex-by-jen-stark"

# Number of pages to sampe. Default is 2 which is about 100 images
os_sample = 3

collage = Image.new("RGBA", (1500, 500), color=(255,255,255,255))
images = []

img_idx = 0
for i in range(os_sample):
  offset = i*50
  with urllib.request.urlopen("https://api.opensea.io/api/v1/assets?order_direction=desc&offset=%s&limit=50&collection=%s" % (offset,os_slug)) as url:

    data = json.loads(url.read().decode())
  
    for item in data['assets']:
      img_name =  "images/%s.png" % (img_idx) 
      urllib.request.urlretrieve(item['image_url'], img_name)
      images.append(img_name)
      img_idx += 1


random.shuffle(images)
img_idx = 0

for i in range(15):
  for j in range(5):
    
    file = images[img_idx]
    img = Image.open(file).convert("RGBA")
    img = img.resize((100, 100))
    img_idx += 1
    collage.paste(img, (i * 100, j * 100))
  
collage.show()
