import json
def read_json(file_path):
 try:
  with open(file_path, 'r') ad f:
   return json.load(f)
 except json.JSONDecodeError as e:
  print(f"Błąd JSON: {e}")
  raise
