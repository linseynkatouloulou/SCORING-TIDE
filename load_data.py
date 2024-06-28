import os
import zipfile
from sas7bdat import SAS7BDAT

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

if __name__ == "__main__":
    zip_file_path = 'data/autorisations.zip'
    file_name = 'autorisations.sas7bdat'
    extraction_dir = 'data'
    
    data_frame = chargement_data(zip_file_path, file_name, extraction_dir)
    print(data_frame.head(10))
