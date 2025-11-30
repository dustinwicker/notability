# Notability

Python tools for extracting text from Notability PDF exports and creating a searchable database of your notes.

## Features

- **PDF Text Extraction** - Extract text content from Notability PDF exports
- **Searchable Database** - Create a pickled DataFrame for fast keyword searches
- **Folder Organization** - Maintains folder structure from Notability
- **Duplicate Detection** - Find duplicate notes across folders

## Setup

### Prerequisites

- Python 3.x
- Notability notes exported as PDFs

### Installation

```bash
pip install pandas pdfminer.six
```

## Usage

### 1. Extract Text from PDFs

First, export your Notability notes as PDFs and run the reader:

```python
from pdfminer.high_level import extract_text
import pandas as pd
import os

notability_directory = '/path/to/your/notability/pdfs'
os.chdir(notability_directory)

notability = []
for file in os.listdir():
    if file.endswith('.pdf'):
        text = extract_text(file)
        notability.append([file, 'folder_name', text])

df = pd.DataFrame(notability, columns=['file', 'folder', 'text'])
df.to_pickle('notability_info.pkl')
```

### 2. Search Your Notes

```python
import pandas as pd

df = pd.read_pickle('notability_info.pkl')

def search(term):
    """Search notability notes using keyword."""
    term = term.lower()
    results = df.loc[df.text.str.contains(term), ['folder', 'file']]
    print(f"Search results for '{term}':\n{results}")

# Example searches
search('machine learning')
search('ridge regression')
search('histogram')
```

### 3. Find Duplicates

```python
# Find duplicate notes
duplicates = df[df.text.isin(
    set(df.text.value_counts()[df.text.value_counts() > 1].index)
)][['file', 'folder']]
```

## Files

| File | Description |
|------|-------------|
| `notability_pdf_reader.py` | Extracts text from PDFs and creates searchable database |
| `notability_pdf_search.py` | Search functionality for the extracted notes |
| `main.py` | Main search interface |

## Output

The script creates `notability_info.pkl` containing:

| Column | Description |
|--------|-------------|
| `file` | PDF filename |
| `folder` | Parent folder name |
| `text` | Extracted text content (lowercase) |

## License

MIT
