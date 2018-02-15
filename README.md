Do you hate writing __init__ methods, but love documentation doubling as code
generation? Then I have the module for you! AutoInit will parse your class
documentation and create an __init__ method custom-built, just for you!

Example:

```python
from auto_init import AutoInit

@AutoInit
class Greeter(object):
    '''Stupid example, prints a custom greeting
    
    Args:
        greeting (str): The message to greet with
    '''
    def greet(self, name):
        print('{}, {}'.format(self.greeting, name))

greeter = Greeter('Hello')
greeter.greet('Mike') # Hello, Mike
greeter.greet('Susan') # Hello, Susan
```

In this example, the AutoInit decorator finds the docstring for our class,
parses out the "greeing" argument, and sets up an __init__ for Greeter that
sets self.greeting=args[0]. Genius!

