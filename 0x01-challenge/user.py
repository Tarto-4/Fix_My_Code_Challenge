#!/usr/bin/env python3
"""User class module."""


class User:
    """A class representing a user with an email address."""

    def __init__(self):
        """Initialize a new User instance with an empty email."""
        self.__email = None

    @property
    def email(self):
        """Retrieve the user's email address."""
        return self.__email

    @email.setter
    def email(self, value):
        """Set the user's email address, ensuring it's a string."""
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
