import scipy, numpy, shutil, os, nibabel, imageio, glob
from pathlib import Path
from utils import printProgressBar

def count(input, type):
    count = 0
    for path in Path(input).rglob('*.' + type):
        count += 1

    return count

def extract(input, output, initial_slice=0, final_slice=155):
    patients_HGG = []
    patients_LGG = []

    amount = count(input, 'nii')

    c=0
    for path in Path(input).rglob('*.nii'):
        HGG = False
        data = nibabel.load(path)
        image_array = data.get_fdata()
        nx, ny, nz = image_array.shape

        print('-----')
        print('({}x{}x{}) -> {} dimensions '.format(nx, ny, nz, len(image_array.shape)))
        print('Slices: ', image_array.shape[2])
        print('-----')

        # Handling patient folders
        if path.parts[-3] == 'HGG':
            HGG = True
            if path.parts[-2] not in patients_HGG:
                patients_HGG.append(path.parts[-2])

        else:
            if path.parts[-2] not in patients_LGG:
                patients_LGG.append(path.parts[-2])

        if HGG:
            output_label = output + 'HGG/'
            index = patients_HGG.index(path.parts[-2])
        else:
            output_label = output + 'LGG/'
            index = patients_LGG.index(path.parts[-2])


        patient = 'patient{:03d}'.format(index+1)

        for slice in range(initial_slice, final_slice):
            data = numpy.rot90(numpy.rot90(numpy.rot90(image_array[:, :, slice])))

            if('flair' in path.parts[-1]):
                output_tissue = output_label + 'flair/'

                if not os.path.exists(output_tissue):
                    os.makedirs(output_tissue)
                    print("Created ouput directory: " + output_tissue)

                imageio.imwrite(output_tissue + patient + '_slice{:03d}'.format(slice) + '.png', data)

            if('t1' in path.parts[-1]):
                output_tissue = output_label + 't1/'

                if not os.path.exists(output_tissue):
                    os.makedirs(output_tissue)
                    print("Created ouput directory: " + output_tissue)

                imageio.imwrite(output_tissue + patient + '_slice{:03d}'.format(slice) + '.png', data)

            if('t1ce' in path.parts[-1]):
                output_tissue = output_label + 't1c/'

                if not os.path.exists(output_tissue):
                    os.makedirs(output_tissue)
                    print("Created ouput directory: " + output_tissue)

                imageio.imwrite(output_tissue + patient + '_slice{:03d}'.format(slice) + '.png', data)

            if('t2' in path.parts[-1]):
                output_tissue = output_label + 't2/'

                if not os.path.exists(output_tissue):
                    os.makedirs(output_tissue)
                    print("Created ouput directory: " + output_tissue)

                imageio.imwrite(output_tissue + patient + '_slice{:03d}'.format(slice) + '.png', data)

            if('seg' in path.parts[-1]):
                output_tissue = output_label + 'seg/'

                if not os.path.exists(output_tissue):
                    os.makedirs(output_tissue)
                    print("Created ouput directory: " + output_tissue)

                imageio.imwrite(output_tissue + patient + '_slice{:03d}'.format(slice) + '.png', data)

        printProgressBar(c + 1, amount, prefix='Progress:', suffix='Complete', length=50)
        c+=1

if __name__ == '__main__':
    input = 'D:/BraTS19/Data Training/'
    output = 'D:/BraTS19/Data Training PNG/'
    extract(input, output, 0, 155)