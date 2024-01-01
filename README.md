# iSum Module

This module defines a Python class, `iSum`, that facilitates the summation of a variable number of numeric inputs.

## Classes

### iSum

A class for performing the sum operation on numeric inputs.

#### Attributes

- `nums` (List[Union[int, str]]): A list of numeric inputs provided during object initialization.

#### Methods

- `__init__(self, *nums: Union[int, str]) -> None`:

  - Initializes a iSum object with a variable number of numeric inputs.

- `sum(self) -> str`:

  - Performs the sum operation on the provided numeric inputs and returns the result as a string.
  - Raises `ValueError` if any input is not a digit.

- `__repr__(self) -> str`:

  - Returns a string representation of the iSum object.

- `__str__(self) -> str`:

  - Returns a string representation of the sum result.

- `nums` (property) -> List[Union[int, str]]:

  - Getter for the numeric inputs.

- `nums` (setter) -> None:

  - Setter for the numeric inputs. Validates that inputs are digits.

- `nums` (deleter) -> None:
  - Deleter for the numeric inputs attribute.

#### Example

```python
if __name__ == "__main__":
    example = iSum(12, 12)
    print(example)

```
