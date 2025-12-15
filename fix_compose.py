import yaml

with open('docker-compose.yml', 'r') as f:
    # Use safe_load to avoid arbitary code execution, though minimal risk here
    # Standard yaml loader might read duplicated keys? PyYAML usually overwrites or errors on duplicate keys during load.
    # If it errors, we can't load it.
    try:
        data = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        print(f"Error loading YAML: {e}")
        # If we can't load, we must fallback to string manipulation or manual fix
        exit(1)

services = data.get('services', {})
for svc_name in ['tb-core1', 'tb-core2']:
    if svc_name in services:
        svc = services[svc_name]
        # Remove duplicate tmpfs if present (PyYAML normalizes to one key, so just setting it ensures it's clean)
        # Ensure tmpfs is a list
        svc['tmpfs'] = ['/var/log/thingsboard']
        # Ensure container_name is correct
        svc['container_name'] = f"{svc_name}-fix"

with open('docker-compose.yml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False)
print("YAML Fixed")
