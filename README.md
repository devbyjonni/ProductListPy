# ProductListPy

## Overview
ProductListPy is a **Python console application** that validates and stores product entries in the format `NAME-XXX`.

## Features
- Accepts input in the format `NAME-XXX`, where:
  - `NAME` contains **only letters** (A-Z, a-z) and is **exactly 4 characters long**.
  - `XXX` is a **3-digit number** between **200-500**.
- **Strict validation** ensures correct input format.
- **Sorted output** for better readability.

## How to Use
1. Run the application with `python3 main.py`.
2. Enter product names in the correct format (e.g., `ABCD-400`).
3. Type `exit` to display the sorted list.

## Future Improvements
- Implement unit tests for validation.

## Author
Developed by **Jonni Akesson**.