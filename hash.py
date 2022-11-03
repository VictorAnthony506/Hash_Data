import pandas as pd
import json
from typing import Dict, Any
import hashlib


def dict_hash(dictionary: Dict[str, Any]) -> str:
    """sha256 hash of a dictionary."""
    dhash = hashlib.sha256()
    # We need to sort arguments so {'a': 1, 'b': 2} is
    # the same as {'b': 2, 'a': 1}
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


def output_csv(csv_file_path, output_csv_path, minting_tool=''):
    df = pd.read_csv(csv_file_path)
    dname = 'Current Name' if 'Current Name' in df.columns else 'Filename'
    
    
    hash_list = []
    
    for member in range(len(df)):
        member_details = {
        "format": "CHIP-0007",
        "name": df[dname].iloc[member],
        "description": df['Description'].iloc[member],
        "minting_tool": minting_tool,
        "sensitive_content": True,
        "series_number": member,
        "series_total": len(df),
        "collection": {
            "name": df[dname].iloc[member],
            "id": df['UUID'].iloc[member],
            "gender": df['Gender'].iloc[member] if 'Gender' in df.columns else None,
            "attributes": []
        },
        "other_data": {
            "Descriptor": df['Descriptor'].iloc[member] if 'Descriptor' in df.columns else "",
            "New Name": df["New Name"].iloc[member] if 'New Name' in df.columns else ""
            }
        }
        
        hash_list.append(dict_hash(member_details))
        
    df["Hash"] = hash_list
    df.to_csv(output_csv_path)
    
    
file_path = input('Enter the absolute path of the CSV file: ')
output_path = input('Enter the absolute path of the output file')
output_csv(file_path, output_path)

