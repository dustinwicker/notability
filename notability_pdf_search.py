import os
import pandas as pd

# Increase maximum width in characters of columns - will put all columns in same line in console readout
pd.set_option("expand_frame_repr", False)
# Increase number of rows printed out in console
pd.set_option('display.max_rows', 600)
# Able to read entire value in each column (no longer truncating values)
pd.set_option('display.max_colwidth', None)

# Change directory
notability_directory = 'C:\\Users\\dustin.wicker\\PycharmProjects\\Notability'
os.chdir(notability_directory)

# Open pickled file
notability = pd.read_pickle('notability_info.pkl')

# Search notability
search_term = 'ridge regression'
search_results = notability.loc[notability.text.str.lower().str.contains(search_term), ['file', 'folder']]
print(f"Search Results for '{search_term}':\n{search_results}")
