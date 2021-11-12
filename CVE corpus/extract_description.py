# Goal of this function is to 
# 1 - read the CVE xm file
# 2 - extract information from 'desc' tag
# 3 - write to a text file
import xml.etree.ElementTree as ET
data_file = 'allitems.xml'
tree = ET.parse(data_file)
root = tree.getroot()

data = []

for desc in root.iter('{http://cve.mitre.org/cve/downloads/1.0}desc'):
    #print("="*5,desc.tag,"="*5)
    data.append(desc.text)
# data_lower_case = [i.lower() for i in data]

with open('cve_desc.txt', 'w') as f:
    f.write("\n".join(data))
print(f"Total {len(data)} lines found and stored in cve_desc.txt.")

## 195591 lines collected from allitems.xml