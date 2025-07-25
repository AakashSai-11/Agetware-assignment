# 💰 Problem: Convert Number to Indian Currency Format

## 📄 Description

In the Indian numbering system, commas are placed differently than in the Western system. For example:

- Western format: `123,456,789.00`
- Indian format: `12,34,56,789.00`

This code takes a floating-point number as input and returns a string formatted in the **Indian currency style**.

For example:

```
Input: 123456.7891
Output: 1,23,456.7891
```

---

## ✅ Features

- Handles both **positive** and **negative** numbers.
- Supports numbers with or without decimal points.
- Commas are added as per **Indian numbering system**: first 3 digits, then every 2 digits.
- Maintains precision of the decimal part as-is.

---

## 🧪 Example

```python
print(convert_number_to_Indian_currency(1234567.89))
# Output: 12,34,567.89

print(convert_number_to_Indian_currency(-123456789.1234))
# Output: -12,34,56,789.1234
```

---

### Function Parameters:

- `num`: A floating-point number (can be negative)

### Function Returns:

- A string with the number formatted in Indian style

---

## 🧠 Notes

- Focus was given to logic clarity, clean formatting, and edge case handling.
- The code manually parses the number and applies comma formatting logic.

---
