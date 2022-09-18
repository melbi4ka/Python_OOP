def even_numbers(function):

    def wrapper(numbers):

        result = [num for num in numbers if num%2 == 0]
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))


# функцията гет нъмбърс ни връща числа, подаваме и като параметър лист от числа
# за да ги върне с избраната от нас логика - декорираме функцията
# на ивън намбърс подаваме - функцията
# на рапъра - подаваме листа от числа на гет намбърс
# пишем си логиката и връщаме резултата
# функцията ивън намбърс извиква референцията към рапъра - т.е резултата от рапъра
# и те го връщат на принта 

