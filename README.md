# Hash_Data

This script uses the **CSV** absolute file path provided by HNG[9] teams, and generates a CHIP-0007 compatible JSON to calculate the sha256, this is then added to to original CSV in column **Hash**.

Make sure your csv have columns "UUID" and "Description". The scripts goes through all the columns and rows of your csv file to generate an appropriate Hash.

You'll be prompted to provide your csv file path and an empty csv file path. The output will be stored in the empty csv absolute file path provided. 
