def write_yaml(data, file_path):
 with open(file_path, 'w') as f:
  yaml.dump(data, f, default_flow_style=False)
