class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number: float, message):
        if number <= 0:
            raise ValueError(message)