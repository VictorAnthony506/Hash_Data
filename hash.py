import pandas as pd
import json
from typing import Dict, Any
import hashlib


def dict_hash(dictionary: Dict[str, Any]) -> str:
    """sha256 hash of a dictionary."""
    dhash = hashlib.sha256()
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


"""Line 17, Attribute Colomn: data was not well separated with semi colon"""
# defining a constant for that field LINE17ATTRIBUTE.
LINE17ATTRIBUTE = [
    {
        "trait_type": "hair", "value": "bald",
        "trait_type": "eyes", "value": "black",
        "trait_type": "teeth", "value": "none",
        "trait_type": "clothing", "value":"yellow and purple agbada",
        "trait_type": "accessories", "value": "mask",
        "trait_type": "expression", "value": "none",
        "trait_type": "strength", "value": "none",
        "trait_type": "weakness", "value": "none"
    }
]


def output_csv(csv_file_path, show_json="n"):
    df = pd.read_csv(csv_file_path)
    hash_list = []
    semi_colon, team_names = pd.DataFrame(), pd.DataFrame()
    semi_colon = df["Attributes"].str.split(";")
    team_names = df["TEAM NAMES"]
    team_names.ffill(inplace=True)

    for member in range(len(df)):
        minting_tool = team_names.iloc[member]   
        member_details = {           
            "format": "CHIP-0007",
            "name": df["Filename"].iloc[member],
            "description": df['Description'].iloc[member],
            "minting_tool": minting_tool,
            "sensitive_content": False,
            "series_number": member,
            "series_total": len(df),
            "attributes": [{"trait_type": o.split(":")[0], "value": o.split(":")[1]} for o in semi_colon.iloc[member]] if member!=17 else LINE17ATTRIBUTE,
            "collection": {
                "name": "Zuri NFT Tickets for Free Lunch",
                "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9."
                    }
                    ]
                }
                }
        
        if show_json=="y":
            print(member_details)
            
                
        hash_list.append(dict_hash(member_details))
        
    df["Hash"] = hash_list
    df.to_csv("filename.output.csv", index=False)
    
    
file_path = input('Enter the absolute path of the CSV file: ')
show = input("Do you want to see json output: [y/n]:")

output_csv(file_path, show)

