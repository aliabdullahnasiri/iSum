#!/usr/bin/env python
"""
iSum Module

This module defines a class, iSum, that performs the sum operation on a variable number of numeric inputs.

Classes:
    iSum: A class for performing the sum operation on numeric inputs.

Example:
    To create a iSum object and print its representation:
    ```
    if __name__ == "__main__":
        print(f"{iSum(12, 12)!r}")
    ```

Attributes:
    - __name__: The name of the module (automatically set by Python).
    - __class__: The class of the module (automatically set by Python).

Author:
    [Ali Abdullah Nasiri]

Date:
    [1/1/2024]
"""

from typing import List, Union


class iSum:
    """
    iSum Class

    This class represents a simple numeric sum operation. It takes a variable number of numeric inputs
    during initialization and provides methods to calculate and represent the sum result.

    Attributes:
        nums (List[Union[int, str]]): A list of numeric inputs provided during object initialization.

    Methods:
        __init__(self, *nums: Union[int, str]) -> None:
            Initializes a iSum object with a variable number of numeric inputs.

        sum(self) -> str:
            Performs the sum operation on the provided numeric inputs and returns the result as a string.

        __repr__(self) -> str:
            Returns a string representation of the iSum object.

        __str__(self) -> str:
            Returns a string representation of the sum result.

        nums (property) -> List[Union[int, str]]:
            Getter for the numeric inputs.

        nums (setter) -> None:
            Setter for the numeric inputs. Validates that inputs are digits.

        nums (deleter) -> None:
            Deleter for the numeric inputs attribute.

    Example:
        To create a iSum object and print its representation:
        ```
        my_sum = iSum(12, 12)
        print(repr(my_sum))
        ```

    Author:
        [Ali Abdullah Nasiri]

    Date:
        [1/1/2024]
    """

    def __init__(self, *nums: Union[int, str]) -> None:
        """
        Initialize the iSum object with a variable number of numeric inputs.

        Args:
            *nums (Union[int, str]): Variable number of numeric inputs.
        """
        self.nums = list(nums)

    def sum(self) -> str:
        """
        Perform the sum operation on the provided numeric inputs.

        Returns:
            str: The sum of the numeric inputs as a string.
        Raises:
            ValueError: If any input is not a digit.
        """
        for num in self.nums:
            if not str(num).isdigit():
                raise ValueError("Input must be a digit.")

        largest: int = max(len(str(num)) for num in self.nums)

        nums: List[str] = list(map(str, self.nums))

        for index, num in enumerate(nums):
            nums[index] = "0" * (largest - len(str(num))) + str(num)

        answer = [0] * largest
        carry = 0

        for i in range(largest - 1, -1, -1):
            total = sum(int(num[i]) for num in nums) + carry
            answer[i] = total % 10
            carry = total // 10

        if carry:
            answer = [carry] + answer

        return "".join(map(str, answer))

    def __repr__(self) -> str:
        """
        Return a string representation of the iSum object.

        Returns:
            str: String representation.
        """
        return f"<{__name__}.{self.__class__.__name__}{self.nums} object at 0x{id(self):x}>"

    def __str__(self) -> str:
        """
        Return a string representation of the sum result.

        Returns:
            str: String representation of the sum result.
        """
        return self.sum()

    @property
    def nums(self) -> List[Union[int, str]]:
        """
        Get the numeric inputs.

        Returns:
            List[Union[int, str]]: List of numeric inputs.
        """
        return self._nums

    @nums.setter
    def nums(self, value: List[Union[int, str]]) -> None:
        """
        Set the numeric inputs.

        Args:
            value (List[Union[int, str]]): List of numeric inputs.
        Raises:
            ValueError: If any input is not a digit.
        """
        for num in value:
            if not str(num).isdigit():
                raise ValueError("Input must be a digit.")
        self._nums = value

    @nums.deleter
    def nums(self) -> None:
        """
        Delete the numeric inputs attribute if it exists.
        """
        if hasattr(self, "_nums"):
            del self._nums
