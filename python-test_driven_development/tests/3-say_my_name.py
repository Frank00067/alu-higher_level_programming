Import `say_my_name`

>>> say_my_name = __import__('3-say_my_name').say_my_name

>>> say_my_name("David", "Emmanuel")
My name is David Emmanuel

>>> say_my_name(2)
Traceback (most recent call last):
TypeError: first_name must be a string

>>> say_my_name("David", 1)
Traceback (most recent call last):
TypeError: last_name must be a string

>>> say_my_name()
Traceback (most recent call last):
TypeError: say_my_name() missing 1 required positional argument: 'first_name'
