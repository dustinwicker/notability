import os
import pandas as pd
from pdfminer.high_level import extract_text

# Increase maximum width in characters of columns - will put all columns in same line in console readout
pd.set_option("expand_frame_repr", False)
# Increase number of rows printed out in console
pd.set_option('display.max_rows', 600)
# Able to read entire value in each column (no longer truncating values)
pd.set_option('display.max_colwidth', None)

# Change directory
notability_directory = 'C:\\Users\\dustin.wicker\\PycharmProjects\\Notability'
os.chdir(notability_directory)

notability = []
for i in os.listdir():
    if os.path.isfile(i):
        try:
            notability.append([i, notability_directory.split('\\')[-1], extract_text(i)])
        except:
            print(f'{i} is not a PDF.')
    elif os.path.isdir(i):
        os.chdir(i)
        for j in os.listdir():
            try:
                notability.append([j, i, extract_text(j)])
            except:
                print(f'{j} is not a dir.')
        os.chdir(notability_directory)
notability = pd.DataFrame(notability, columns=['file', 'folder', 'text'])
notability.text = notability.text.str.lower()
notability.to_pickle('notability_info.pkl')

# start here
notability = pd.read_pickle('notability_info.pkl')
# Search notability
notability.loc[notability.text.str.lower().str.contains('ridge regression'), ['file', 'folder']]