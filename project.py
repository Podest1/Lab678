def dict_to_xml(data, root_tag):
 root = ET.Element(root_tag)
 for key, val in data.items():
  element = ET.Sub.Element(root, key)
  element.text = str(val)
 return ET.ElementTree(root)
def write_xml(data, file_path, root_tag='root'):
 tree = dict_to_xml(data, root_tag)
 tree.write(file_path, encoding='utf-8', xml_declaration=True)
