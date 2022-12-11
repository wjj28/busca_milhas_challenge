import json
from getting_all_files import all_laptops


# For optimization purposes, the collected data is exported to JSON
data = all_laptops

with open('lenovo_laptops.json', 'w') as fp:
    json.dump(data, fp)