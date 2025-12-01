# Represents Rick's initial, inflexible search application.
# Data Structure: We use a list of dictionaries to simulate the inventory.

inventory = [
    {'model': 'Stratocastor', 'type': 'electric', 'numStrings': 6, 'price': 1499.99},
    {'model': 'SG', 'type': 'electric', 'numStrings': 6, 'price': 1200.00},
    {'model': 'A-style', 'type': 'mandolin', 'numStrings': 8, 'price': 800.00},
    {'model': 'F-style', 'type': 'mandolin', 'numStrings': 8, 'price': 1800.00},
]

def find_instrument(search_spec):
    """
    Finds instruments matching a hardcoded set of criteria.
    This simulates Rick's original search() method which iterates over all choices.
    """
    matching_instruments = []
    
    # 1. Hardcoded, inflexible comparison logic:
    for instrument in inventory:
        if instrument['type'] == search_spec['type'] and \
           instrument['numStrings'] == search_spec['numStrings'] and \
           instrument['model'] == search_spec['model']:
            matching_instruments.append(instrument)
            
    return matching_instruments

# Test Drive the initial, simple application
search_criteria = {'type': 'electric', 'numStrings': 6, 'model': 'SG'}
results = find_instrument(search_criteria)

print(f"Searching for: {search_criteria}")
if results:
    for instrument in results:
        print(f"Match found: Model={instrument['model']}, Type={instrument['type']}")
else:
    print("No matching instruments found.")

