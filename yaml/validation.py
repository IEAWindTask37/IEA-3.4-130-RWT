from jsonschema import validate
import yaml
import os

clear = lambda: os.system('cls')
clear()

with open('IEAonshoreWT.yaml', 'r') as myfile:
  inputs = myfile.read()

with open('IEAontology_schema.yaml', 'r') as myfile:
  schema = myfile.read()

validate(yaml.load(inputs), yaml.load(schema))


wt_data= yaml.load(inputs)

print(wt_data['components']['blade']['outer_shape_bem']['reference_axis'])