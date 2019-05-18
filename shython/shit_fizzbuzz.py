from random import randint
def fizz_buzz():
    def _fizz_buzz_checker(n):
        def is_divisible_by_three_and_five(number): return"FizzBuzz" if number % 3 == 0 and number % 5 == 0 else None
        def is_divisible_by_three(number):return "fizz" if number % 3 == 0 else None
        def is_divisible_by_five(number):return "buzz" if number % 5 == 0 else None
        first_check = is_divisible_by_three_and_five(number=n)
        if first_check is not None:return first_check
        second_check = is_divisible_by_three(number=n)
        if second_check is not None:return second_check
        third_check = is_divisible_by_five(number=n)
        if third_check is not None:return third_check
        else:return str(n)
    def generate_random_int():
        return randint(1,100)
    completed_vals = []
    output = []
    counter = 1
    while True:
        counter += 1
        a = generate_random_int()
        if len(completed_vals) == 100:
            break
        if a not in completed_vals:
            completed_vals.append(a)
            output.append(_fizz_buzz_checker(a))
    [print(i) for i in output]


if __name__ == "__main__":
    fizz_buzz()
