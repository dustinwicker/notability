import os
import pandas as pd

# will now pull from google drive location to pull down data and upload the notability_info.pkl
# Change directory
notability_directory = 'C:\\Users\\dustin.wicker\\PycharmProjects\\Notability'
os.chdir(notability_directory)

# Open pickled file
notability = pd.read_pickle('notability_info.pkl')

# Search notability
search_term = 'ridge regression'
search_results = notability.loc[notability.text.str.lower().str.contains(search_term), ['file', 'folder']]
print(f"Search Results for '{search_term}':\n{search_results}")
