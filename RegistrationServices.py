import re

class InvalidEmailError(ValueError):
    """Raised when the email is missing or fails format validation."""
    def __init__(self, email: str, reason: str = "does not match the required email format"):
        self.email = email
        super().__init__(f"Invalid email '{email}': {reason}.")


class UnderageError(Exception):
    """Raised when the applicant is below the minimum age of 18."""
    MINIMUM_AGE = 18
    def __init__(self, age: int):
        self.age = age
        self.minimum_age = self.MINIMUM_AGE
        super().__init__(
            f"Age {age} does not meet the minimum age requirement of {self.MINIMUM_AGE}."
        )

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")


class RegistrationService:
    def __init__(self, service_enabled: bool = True):
        self.service_enabled = service_enabled

    def register_user(self, email: str, age: int) -> bool:
        # Internal invariant: service must be active before processing
        assert self.service_enabled, "RegistrationService must be enabled before use."

        # Email presence check
        if not email or not email.strip():
            raise InvalidEmailError(repr(email), reason="email must not be null or empty")

        # Email format check
        if not EMAIL_REGEX.match(email):
            raise InvalidEmailError(email)

        # Age restriction check
        if age < UnderageError.MINIMUM_AGE:
            raise UnderageError(age)

        return True