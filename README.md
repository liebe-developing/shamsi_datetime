# Shamsi DateTime

`ShamsiDateTime` is a Python package developed by Ali Razmjooei that provides a class for working with Shamsi (Jalali) dates. This package integrates seamlessly with NumPy, enabling you to handle Shamsi dates and convert them to and from Gregorian dates.

## Overview

The Shamsi DateTime package allows you to:

- Create and manipulate Shamsi (Jalali) dates.
- Convert Shamsi dates to Gregorian dates and vice versa.
- Easily integrate with NumPy for date manipulations and analysis.

## Installation

To install the package, use `pip`:

```sh
pip install shamsi-datetime
```

## Basic Usage

```python
from shamsi_datetime import ShamsiDateTime
import numpy as np

# Create a Shamsi date
shamsi_date = ShamsiDateTime(1403, 5, 6)
print(f"Shamsi Date: {shamsi_date}")

# Convert to Gregorian (NumPy datetime64)
gregorian_date = shamsi_date.to_gregorian()
print(f"Gregorian Date: {gregorian_date}")

# Convert back to Shamsi
shamsi_converted_back = ShamsiDateTime.from_gregorian(gregorian_date)
print(f"Converted Back to Shamsi: {shamsi_converted_back}")
```

## Features

- **ShamsiDateTime Class**: Represents Shamsi dates with easy conversion to and from Gregorian dates.
- **Conversion Methods**: Convert between Shamsi dates and Gregorian dates using NumPy's `datetime64`.
- **Integration with NumPy**: Leverages NumPy for efficient date operations.

## License 

This project is licensed under the MIT License - see the [LICENSE](https://github.com/liebe-developing/shamsi_datetime/blob/main/LICENSE) file for details.

## Contributing

If you would like to contribute to the development of ShamsiDateTime, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/liebe-developing/shamsi_datetime).

## Contact

For any questions or feedback, you can reach out to the author:

- Ali Razmjooei: [alirazmjooei.webdeveloper@gmail.com](alirazmjooeiwebdeveloper@gmail.com)
- [GitHub](https://github.com/liebe-developing)