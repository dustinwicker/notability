import os
import pandas as pd

# will now pull from google drive location to pull down data and upload the notability_info.pkl

def search(term):
    """Search notability using keyword."""
    term = term.lower()
    results = df.loc[df.text.str.contains(term), ['folder', 'file']]
    print(f"Search results for '{term}':\n{results}")

# search
search(term='histogram')

# see duplicate files (can delete duplicates)
df[df.text.isin(set(df.text.value_counts()[df.text.value_counts()>1].index))][['file', 'folder']]