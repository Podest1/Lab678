import xml.etree.ElementTree as ET
def read_xml(file_path):
 try:
  tree = ET.parse(file_path)
  return tree.getroot()
 except ET.ParseError as e:
  print(f"Błąd XML: {e}")
  raise
