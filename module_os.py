import os
from datetime import datetime

print(os.getcwd())

os.chdir('/Users/kristynalangova/PycharmProjects/PYTHON')

# os.mkdir('OS-Demo-2/Sub-Dir-1')

# os.makedirs('OS-Demo-2/Sub-Dir-1')



# os.rmdir('OS-Demo-2/Sub-Dir-1')   # removedirs je nebezpecny

# os.rename('sample.log','renamed_sample.log')

# print(os.listdir())


print(os.stat('renamed_sample.log'))
print(os.stat('renamed_sample.log').st_mtime)
mod_time = os.stat('renamed_sample.log').st_mtime   # prevod na normalni cisla

print(datetime.fromtimestamp(mod_time))


# for dirpath, dirnames, filenames in os.walk('/Users/kristynalangova/PycharmProjects/'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()

print(os.environ.get('HOME'))
# print(os.environ)

print('\n'*2)
file_path = os.path.join(os.environ.get('HOME'), 'PycharmProjects/PYTHON/renamed_sample.log')

print(file_path)

with open(file_path, 'r') as f:
    f.read()

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

# print(dir(os.path))