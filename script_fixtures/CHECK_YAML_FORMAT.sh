# Example usage : "bash CHECK_YAML_FORMAT.sh abilities.yaml" 
# Requires python2 and PyYaml to be installed
python -c "import yaml ; f = open(r'$1', 'rb') ; x = yaml.load(f); print(x)"