def show_func(func):
    def inner():
        print('Start decorator')
        func()
        print('Stop decorator')

    return inner


@show_func  # say = show_func(say)
def say():
    print('Hello World')


say()


def show_func2(func):
    def inner(*args):
        print('Start decorator')
        func(*args)
        print('Stop decorator')

    return inner


@show_func2  # say = show_func2(say)
def say(first_name, last_name):
    print(f'Hello {first_name} {last_name}')


print()
name = input('Enter name: ')
last = input('Last name: ')
say(name, last)

# Start decorator
# Hello World
# Stop decorator
#
# Enter name: Mikhail
# Last name: Derkunov
# Start decorator
# Hello Mikhail Derkunov
# Stop decorator
