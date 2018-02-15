import re

param_re = re.compile('\s*([^ :]+) ?.*: .*')

def AutoInit(cls):
    doc = cls.__doc__
    in_args = False
    param_names = []

    if doc:
        for line in doc.split('\n'):
            if in_args:
                m = param_re.match(line)

                if m:
                    param_names.append(m.group(1))
                else:
                    break
            else:
                if line.strip() == 'Args:':
                    in_args = True

    def new_init(self, *args, **kwargs):
        for name, arg in zip(param_names, args):
            setattr(self, name, arg)

        for name, value in kwargs.items():
            if not name in param_names:
                raise TypeError(
                    '{}() got an unexpected keyword argument \'{}\''.format(
                        cls.__name__, name))
            setattr(self, name, value)

    cls.__init__ = new_init
    return cls

if __name__ == '__main__':

    @AutoInit
    class Foo(object):
        '''Example class

        Args:
            param1 (str): This is a string
            param2: This is something else
        '''
        def run(self):
            assert(self.param1 == 'test')
            assert(self.param2 == 42)

    f = Foo('test', 42)
    f.run()

    f = Foo(param2 = 42, param1 = 'test')
    f.run()

    print('All tests passed')
