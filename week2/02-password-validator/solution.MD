Here is the complete Python solution to the Password Validator problem, including all five helper functions, the main validator, and the bonus implementation.

---

### Complete Python Solution

```python
def has_min_length(password: str) -> bool:
    """Check if password has at least 8 characters."""
    return len(password) >= 8


def has_uppercase(password: str) -> bool:
    """Check if password contains at least one uppercase letter."""
    return any(c.isupper() for c in password)


def has_lowercase(password: str) -> bool:
    """Check if password contains at least one lowercase letter."""
    return any(c.islower() for c in password)


def has_digit(password: str) -> bool:
    """Check if password contains at least one digit."""
    return any(c.isdigit() for c in password)


def has_special(password: str) -> bool:
    """Check if password contains at least one special character (non-alphanumeric, non-whitespace)."""
    return any(not c.isalnum() and not c.isspace() for c in password)


def is_valid_password(password: str) -> bool:
    """Check if password meets all five security rules."""
    return all([
        has_min_length(password),
        has_uppercase(password),
        has_lowercase(password),
        has_digit(password),
        has_special(password)
    ])


def get_failed_requirements(password: str) -> list[str]:
    """Return a list of rule names that failed in the correct order."""
    checks = [
        ("min_length", has_min_length(password)),
        ("uppercase", has_uppercase(password)),
        ("lowercase", has_lowercase(password)),
        ("digit", has_digit(password)),
        ("special", has_special(password))
    ]
    return [name for name, passed in checks if not passed]

```

---

### Line-by-Line Explanation

#### 1. `has_min_length(password)`

* **`len(password) >= 8`**: Calculates the total number of characters in the `password` string and checks if it is greater than or equal to $8$. Returns `True` if it meets the length requirement, otherwise `False`.

#### 2. `has_uppercase(password)`

* **`any(c.isupper() for c in password)`**: Loops through every character `c` in the password string using a generator expression. The `.isupper()` method checks if a character is an uppercase letter. The built-in `any()` function returns `True` as soon as it finds at least one uppercase letter (short-circuit evaluation).

#### 3. `has_lowercase(password)`

* **`any(c.islower() for c in password)`**: Similar to the uppercase check, this iterates through each character `c` and uses the `.islower()` method to verify if at least one lowercase letter exists.

#### 4. `has_digit(password)`

* **`any(c.isdigit() for c in password)`**: Checks each character `c` using the `.isdigit()` method to determine if at least one numeric digit (0–9) is present in the password.

#### 5. `has_special(password)`

* **`any(not c.isalnum() and not c.isspace() for c in password)`**:
* `c.isalnum()` checks if a character is alphanumeric (either a letter or a digit).
* `not c.isalnum()` ensures it is **not** a letter or digit.
* `not c.isspace()` ensures it is **not** whitespace (so spaces like `" "` are correctly excluded, as requested).
* Combining them checks for valid special characters (like `@`, `#`, `!`, etc.).



#### 6. `is_valid_password(password)`

* **`all([...])`**: Takes an iterable of boolean values and returns `True` **only if all** elements inside the list are `True`. By calling our five helper functions here, we avoid duplicating validation logic.

#### 7. `get_failed_requirements(password)` (Bonus)

* **`checks = [...]`**: Defines a list of tuples pairing each rule's descriptive name string with the boolean result of its respective helper function.
* **`[name for name, passed in checks if not passed]`**: Uses a list comprehension to iterate through our `checks` list. If `passed` is `False` (`not passed`), it collects the rule's `name` into the resulting list in the precise order specified.