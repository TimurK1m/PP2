import json

# Load data from the JSON file
with open('lab4\\sample-data.json', 'r') as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<45} {:<17} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface details
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<20} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
