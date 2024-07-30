# python-projrcts




## Random Password Generator

This Python script generates a secure, random password of a specified length, incorporating a mix of digits, symbols, uppercase letters, and lowercase letters. The generated password aims to provide robust security by ensuring a diverse character set and shuffling the characters to avoid predictable patterns.

### Features

- **Random Password Generation:** Creates a password with a specified length, ensuring the inclusion of at least one digit, one symbol, one uppercase letter, and one lowercase letter.
- **Customizable Length:** Easily adjustable to generate passwords of different lengths.
- **Character Variety:** Utilizes a wide range of characters, including digits, symbols, and both uppercase and lowercase letters, to maximize security.
- **Shuffling:** Shuffles the password characters to eliminate any predictable sequences.

### How It Works

1. **Character Sets:** The script defines separate lists for digits, symbols, uppercase letters, and lowercase letters.
2. **Random Selection:** It selects one random character from each set to ensure that the password contains at least one character from each category.
3. **Password Construction:** Additional random characters are appended to reach the desired length.
4. **Shuffling:** The characters are shuffled to ensure randomness in the final password.
5. **Output:** The script prints the generated password.

### Usage

To use the script, simply run it in a Python environment. The password length is set to 12 by default, but you can modify the `LENGTH` variable in the script to change the password length.

```python
# Example usage:
python generate_password.py
```

### Dependencies

- Python 3.x
- `random` module (standard in Python's library)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
