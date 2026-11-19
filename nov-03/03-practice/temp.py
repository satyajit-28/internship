class ValidationError(Exception):
    pass

class InvalidAge(ValidationError):
    pass

class InvalidEmail(ValidationError):
    pass

class OutOfRange(ValidationError):
    pass


def validate_age(age):
    if type(age) is not int:
        raise InvalidAge("Age must be an integer")
    if not 0 <= age <= 120:
        raise InvalidAge("Age must be between 0 and 120")
    return age


def validate_email(email):
    if type(email) is not str or "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmail("Invalid email")
    return email


def validate_range(value, low, high):
    if not low <= value <= high:
        raise OutOfRange(f"{value} not in range {low}-{high}")
    return value


for func, args in [(validate_age, (25,)), (validate_age, ("25",)),
                   (validate_email, ("a@b.com",)), (validate_email, ("abc",)),
                   (validate_range, (50, 1, 100)), (validate_range, (150, 1, 100))]:
    try:
        print("OK:", func(*args))
    except ValidationError as e:
        print("Error:", e)