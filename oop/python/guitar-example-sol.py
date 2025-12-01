# 1. Instrument Class: Encapsulates the physical item's properties.
# This ensures instrument data is protected and managed internally (Encapsulation).
class Instrument:
    def __init__(self, serialNumber, price, properties):
        self.serialNumber = serialNumber
        self.price = price
        self.properties = properties
        
    def get_property(self, key):
        return self.properties.get(key)
    
    def get_properties(self):
        return self.properties

# 2. InstrumentSpec Class (Search Specification): Encapsulates the varying search criteria.
# The core responsibility of comparison is delegated to this object.
class InstrumentSpec:
    def __init__(self, properties):
        self.properties = properties

    def matches(self, instrument):
        """Checks if the instrument matches all properties in this specification."""
        
        # We only compare properties defined in the search spec
        for key, expected_value in self.properties.items():
            actual_value = instrument.get_property(key)
            
            # Simple check: if a required property is missing or mismatched, it fails.
            if actual_value is None or actual_value != expected_value:
                return False
        
        # If we checked all criteria in the spec and none failed, it's a match.
        return True

# 3. Inventory Class: Manages the collection and delegates search responsibility.
class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, serialNumber, price, properties):
        instrument = Instrument(serialNumber, price, properties)
        self.instruments.append(instrument)

    # The search logic is now flexible (Decoupled/Delegation): 
    # The search method does not know *what* it is searching for, only *how* to ask.
    def search(self, spec):
        matching_instruments = []
        for instrument in self.instruments:
            # Delegation: The Inventory asks the Spec object to perform the comparison.
            if spec.matches(instrument):
                matching_instruments.append(instrument)
        return matching_instruments

# --- Setup and Test Drive ---

# Create Inventory and populate it (similar to Rick's original inventory)
inventory = Inventory()
inventory.add_instrument(
    'V95693', 1499.99, {'type': 'electric', 'model': 'Stratocastor', 'numStrings': 6}
)
inventory.add_instrument(
    '11277', 1200.00, {'type': 'electric', 'model': 'SG', 'numStrings': 6}
)
inventory.add_instrument(
    'A86420', 1800.00, {'type': 'mandolin', 'model': 'F-style', 'numStrings': 8}
)

# Test 1: Search for a specific electric guitar
search_properties_1 = {'type': 'electric', 'numStrings': 6, 'model': 'SG'}
spec1 = InstrumentSpec(search_properties_1)
results1 = inventory.search(spec1)

print("--- Test 1: Search for SG Electric (Matches) ---")
if results1:
    for instr in results1:
        print(f"Found: SN {instr.serialNumber}, Model {instr.get_property('model')}, Props: {instr.get_properties()}")
else:
    print("No matches found.")

# Test 2: Search by type only (Requires flexibility)
search_properties_2 = {'type': 'mandolin'}
spec2 = InstrumentSpec(search_properties_2)
results2 = inventory.search(spec2)

print("\n--- Test 2: Search for Type 'mandolin' only ---")
if results2:
    for instr in results2:
        print(f"Found: SN {instr.serialNumber}, Model {instr.get_property('model')}, Props: {instr.get_properties()}")
else:
    print("No matches found.")
