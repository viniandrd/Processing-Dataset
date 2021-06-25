from glob import glob
import os

path_to_tumors = ''  # ../notumor/Tumor
path_to_t1c = ''  # ../notumor/T1c

tumors = glob(path_to_tumors + '/*.png')
t1cs = glob(path_to_t1c + '/*.png')

tumors_filter = []
t1cs_filters = []

print('Tumors: {}'.format(len(tumors)))
print('T1cs: {}'.format(len(t1cs)))

################################ Renaming to a pattern in list

idx = 0
for tumor in tumors:
    tumors_filter.append(tumor[-16:])
    idx += 1

idx = 0
for t1c in t1cs:
    t1cs_filters.append(t1c[-16:])
    idx += 1

print()
print('------------')
print()

################################## Printing first ten
idx = 0
for tumor in tumors_filter:
    if (idx < 10):
        print(tumor)
    idx += 1
print()
print('------------')
print()

idx = 0
for t1c in t1cs_filters:
    if (idx < 10):
        print(t1c)
    idx += 1

################################## Comparing

count = 0
idx = 0
for t1c in t1cs_filters:
    if not t1c in tumors_filter:
        os.remove(t1cs[idx])
        count += 1
    idx += 1

print()
print('------------')
print('Before deleting: ', count)

count2 = 0
for t1c in t1cs_filters:
    if not t1c in tumors_filter:
        count2 += 1

print('After deleting: ', count2)
