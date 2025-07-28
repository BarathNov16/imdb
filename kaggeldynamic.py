import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import sys 

if len(sys.argv) < 4:
    print(f"Usage: python {sys.argv[0]} <file_paths> <link> <file_name>")
    print(" - file_paths: path(s) to your input file(s)")
    print(" - link: URL you want to process or reference")
    print(" - file_name: name you want to save the output as")
    sys.exit(1)

sys.argv
file_paths = sys.argv[1]
link = sys.argv[2]   
file_name = sys.argv[3]


df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    link,
     file_paths,
    )

    
print("First 20 records:", df.head())

 # Save the received DataFrame to a local CSV file
df.to_csv( file_name, index=False)
print("File saved successfully as my_local_copy.csv")
