import xml.etree.ElementTree as ET

# 讀取XML檔案
tree = ET.parse(r'C:\Users\User\Desktop\專題程式\CWD\response_1683105379753.xml')

# 取得根節點
root = tree.getroot()

# 取得每個fields元素的id和type
fields = root.findall('.//fields')
for field in fields:
    field_id = field.find('id').text
    field_type = field.find('type').text
    print(field_id, field_type)