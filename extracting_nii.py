import scipy, numpy, shutil, os, nibabel, imageio, glob
from pathlib import Path

'''input_file = 'D:/Datasets/BRATS15/train/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_Flair.54512.nii'
output_file = 'D:/Datasets/BRATS15_preprocessed/tumor/'

image_array = nibabel.load(input_file).get_data()
nx, ny, nz = image_array.shape
print('-----')
print('({}x{}x{}) -> {} dimensions '.format(nx, ny, nz, len(image_array.shape)))

total_slices = image_array.shape[2]
print('Slices: ', total_slices)
print('-----')

#Convert and save

#data = image_array[:, :, 77]
data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, 77])))
imageio.imwrite(output_file + 'teste2.png', data)
'''




output = 'D:/Datasets/BRATS15_preprocessed/tumor/'

for path in Path('D:/Datasets/BRATS15/train/HGG/').rglob('*.nii'):
    input_file = path
    data = nibabel.load(input_file)
    image_array = data.get_fdata()
    nx, ny, nz = image_array.shape
    #print('-----')
    #print('({}x{}x{}) -> {} dimensions '.format(nx, ny, nz, len(image_array.shape)))
    #print('Slices: ', image_array.shape[2])
    #print('-----')

    # Convert and save
    # data = image_array[:, :, 77]
    #print(path.name[18:21])

    data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, 91])))
    #print(type(data))

    if(path.name[18:21] == 'Fla'):
        output_path = output + 'Flair/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print("Created ouput directory: " + output_path)

        imageio.imwrite(output_path + path.name[:-4] + '.png', data)

    if (path.name[18:21] == 'T1.'):
        output_path = output + 'T1/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print("Created ouput directory: " + output_path)

        imageio.imwrite(output_path + path.name[:-4] + '.png', data)

    if (path.name[18:21] == 'T1c'):
        output_path = output + 'T1c/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print("Created ouput directory: " + output_path)

        imageio.imwrite(output_path + path.name[:-4] + '.png', data)

    if (path.name[18:21] == 'T2.'):
        output_path = output + 'T2/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print("Created ouput directory: " + output_path)

        imageio.imwrite(output_path + path.name[:-4] + '.png', data)

    if (path.name[18:21] == '.XX' or path.name[18:21] == '.O.'):
        output_path = output + 'Tumor/'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print("Created ouput directory: " + output_path)

        imageio.imwrite(output_path + path.name[:-4] + '.png', data)
