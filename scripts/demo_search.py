""" Test search and parse a single query from command line
"""

import os
import argparse
import pandas as pd
import WebSearcher as ws

pd.set_option('display.width', 120, 
              'display.max_rows', None, 
              'display.max_columns', None)

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="A search query", required=True)
args = parser.parse_args()

# Settings
query = args.query
data_dir = os.path.join("data", f"demo-ws-v{ws.__version__}")
print(f'WebSearcher v{ws.__version__} | Search Query: {args.query} | Output: {data_dir}')

# Filepaths
fp_serps = os.path.join(data_dir, 'serps.json')
fp_results = os.path.join(data_dir, 'results.json')
dir_html = os.path.join(data_dir, 'html')
os.makedirs(dir_html, exist_ok=True)

# Search, parse, and save
se = ws.SearchEngine()                  # Initialize searcher
se.search(query)                        # Conduct Search
se.parse_results()                      # Parse Results
se.save_serp(append_to=fp_serps)        # Save SERP to json (html + metadata)
se.save_results(append_to=fp_results)   # Save results to json
se.save_serp(save_dir=dir_html)         # Save SERP html to dir (no metadata)

# Convert results to dataframe and print select columns
results = pd.DataFrame(se.results)
print(results[['type', 'title', 'url']])