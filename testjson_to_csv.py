import pandas as pd
import json

df = pd.read_json(r'C:\Users\mpxb8400\Desktop\val\reports\sfjson.json')
df.to_csv(r'C:\Users\mpxb8400\Desktop\val\reports\sfjsontest.json')
