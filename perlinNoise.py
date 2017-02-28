from perlin import Perlin
from PIL import Image

image = Image.new ("RGB", (300, 300), "white")
pixels = image.load ()


p = Perlin ()

mn = 10000
mx = -10000

i = 0
j = 0.0
while (i <= 3):
    j = 0;
    while (j <= 3):
        temp = p.getValue (i, j)
        temp *= 255;
        temp = int (temp);
        pixels [100*i, 100*j] = (temp, temp, temp);
        mn = min (mn, temp)
        mx = max (mx, temp)
        j += 0.01;
    i += 0.01;
print (mn, mx)




image.show ()
