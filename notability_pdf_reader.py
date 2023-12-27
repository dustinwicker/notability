import os
import pandas as pd
from pdfminer.high_level import extract_text

# Change directory
notability_directory = 'C:\\Users\\dustin.wicker\\PycharmProjects\\Notability'
os.chdir(notability_directory)

# Empty list to append results of extracted text to
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
