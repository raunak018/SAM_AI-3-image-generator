from PIL import Image, ImageDraw
import random

prompt = input("Prompt Likho: ")

img = Image.new('RGB', (500, 500), (20, 20, 20))
draw = ImageDraw.Draw(img)

for i in range(40):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    r = random.randint(20, 80)
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    draw.ellipse([x, y, x+r, y+r], fill=(c1, c2, c3))

draw.text((20, 450), prompt, fill=(255, 255, 255))
img.save("output.png")
img.show()