class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

# validate('jabeqwqw')

class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass

try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)
