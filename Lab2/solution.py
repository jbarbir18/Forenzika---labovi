import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = '.'

# create an empty list to store the file names
file_names = []

# create an empty list to store the extensions
extensions = []

md5s = []
sha1s = []
sha256s = []

magic_numbers = []
mag_obj = magic.Magic(mime=True)

extension_matches = []

# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        (file_name, extension) = os.path.splitext(file)
        file_names.append(file_name)
        extensions.append(extension)

        with open(file, 'rb') as f:
            data = f.read()
            magic_number = mag_obj.from_file(os.path.join(dir_path, file))
            magic_numbers.append(magic_number)

            md5hash = hashlib.md5(data).hexdigest()
            md5s.append(md5hash)

            sha1hash = hashlib.sha1(data).hexdigest()
            sha1s.append(sha1hash)

            sha256hash = hashlib.sha256(data).hexdigest()
            sha256s.append(sha256hash)

            # check if the magic number contains the file extension
            if extension.lower() == '':
                extension_matches.append(False)
            elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
                extension_matches.append(True)
            else:
                extension_matches.append(False)


# create a Pandas dataframe with the file names
df = pd.DataFrame({'file_name': file_names, 'extension': extensions,
                  'md5': md5s, 'sha1': sha1s, 'sha256': sha256s, 'magic_numbers': magic_numbers, 'extension_matches': extension_matches})
# print the dataframe
print(df)
print(df['sha1'])
