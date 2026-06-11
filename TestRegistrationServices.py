import pytest

from RegistrationServices import (
    RegistrationService, InvalidEmailError, UnderageError
)

@pytest.fixture
def service():
    """Provide a fresh, enabled RegistrationService for every test."""
    return RegistrationService(service_enabled=True)

@pytest.fixture
def disabled_service():
    """Provide a disabled RegistrationService to test the assert invariant."""
    return RegistrationService(service_enabled=False)

class TestSuccessfulRegistration:
    def test_valid_email_and_adult_age(self, service):
        assert service.register_user("alice@example.com", 25) is True

    def test_exactly_minimum_age(self, service):
        """Boundary: age == 18 must succeed."""
        assert service.register_user("bob@domain.org", 18) is True

    def test_email_with_plus_tag_and_subdomain(self, service):
        assert service.register_user("user+tag@mail.company.co", 30) is True

class TestInvalidEmail:
    def test_raises_for_none_email(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user(None, 25)

    def test_raises_for_empty_string(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("", 25)

    def test_raises_for_missing_at_symbol(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("invalidemail.com", 25)

    def test_raises_for_missing_tld(self, service):
        with pytest.raises(InvalidEmailError):
            service.register_user("user@domain", 25)

    def test_is_subclass_of_value_error(self, service):
        """InvalidEmailError must be catchable as a ValueError."""
        with pytest.raises(ValueError):
            service.register_user("bad-email", 25)

    def test_message_contains_offending_email(self, service):
        with pytest.raises(InvalidEmailError) as exc_info:
            service.register_user("bademail", 25)
        assert "bademail" in str(exc_info.value)

class TestUnderage:
    def test_raises_for_age_below_minimum(self, service):
        with pytest.raises(UnderageError):
            service.register_user("young@example.com", 17)

    def test_raises_for_age_zero(self, service):
        with pytest.raises(UnderageError):
            service.register_user("young@example.com", 0)

    def test_is_not_a_value_error(self, service):
        """UnderageError must NOT inherit from ValueError."""
        with pytest.raises(UnderageError) as exc_info:
            service.register_user("young@example.com", 16)
        assert not isinstance(exc_info.value, ValueError)

    def test_message_contains_age_and_minimum(self, service):
        with pytest.raises(UnderageError) as exc_info:
            service.register_user("young@example.com", 15)
        assert "15" in str(exc_info.value)
        assert "18" in str(exc_info.value)

class TestServiceInvariant:
    def test_assert_fires_when_service_disabled(self, disabled_service):
        with pytest.raises(AssertionError):
            disabled_service.register_user("user@example.com", 25)

    def test_email_validated_before_age(self, service):
        """When both inputs are invalid, email check must fire first."""
        with pytest.raises(InvalidEmailError):
            service.register_user("not-valid", 10)