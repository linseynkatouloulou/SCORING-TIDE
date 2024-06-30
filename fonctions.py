import os
import zipfile
from sas7bdat import SAS7BDAT
import pandas as pd
from sklearn.model_selection import train_test_split
import zipfile

def chargement_data(zip_file_path, file_name, extraction_dir):
    os.makedirs(extraction_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_dir)

    extracted_files = os.listdir(extraction_dir)
    print(f"Extracted files: {extracted_files}")

    file_path = os.path.join(extraction_dir, file_name)

    with SAS7BDAT(file_path) as file:
        data = file.to_data_frame()

    return data



def split_data(data, test_size=0.2, random_state=None, zip_path='.../data/train_test_split.zip'):
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    
    train_file = 'train_data'
    test_file = 'test_data'
    train_data.to_csv(train_file, index=False)
    test_data.to_csv(test_file, index=False)
    
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(train_file)
        zipf.write(test_file)
    
    os.remove(train_file)
    os.remove(test_file)
    
    return train_data, test_data
