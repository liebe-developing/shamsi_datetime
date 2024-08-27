from shamsi_datetime import ShamsiDateTime
import numpy as np

# Create a Shamsi date with specific values
shamsi_date = ShamsiDateTime(1403, 5, 6)
print(f"\nSpecific Shamsi Date: {shamsi_date}")

# Create a Shamsi date with the current date
current_shamsi_date = ShamsiDateTime()
print(f"Current Shamsi Date: {current_shamsi_date}")

# Convert to Gregorian (NumPy datetime64)
gregorian_date = shamsi_date.to_gregorian()
print(f"Gregorian Date: {gregorian_date}")

# Convert back to Shamsi
shamsi_converted_back = ShamsiDateTime.from_gregorian(gregorian_date)
print(f"Converted Back to Shamsi: {shamsi_converted_back}\n")
