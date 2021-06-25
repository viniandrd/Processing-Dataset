import os
from glob import glob
from PIL import Image
from utils import printProgressBar

path = 'D:/Datasets/BRATS15_77/notumor/T1c/'
output_path = 'C:/Users/vinic/Desktop/Filtered Brats_77_224/notumor/T1c/'

if not os.path.exists(output_path):
    os.makedirs(output_path)

imgs = glob(path + '*.png')
print('Total images: {}'.format(len(imgs)))
c=0
for img in imgs:
    img_open = Image.open(img)
    img_open = img_open.resize((224, 224), Image.ANTIALIAS)
    if 'T1c' in path:
        filename = output_path + img[-19:]
    else:
        filename = output_path + img[-21:]
        
    img_open.save(filename)
    print('Saving: {}'.format(filename))
    printProgressBar(c + 1, len(imgs), prefix='Progress:', suffix='Complete', length=50)
    c+=1