import importlib
import sys
from unittest.mock import MagicMock

def load(pkg, method, err=None):

    if not err:
        err = '{0}.{1} does not exist!'.format(pkg, method)

    def fail(*args, **kwargs):
        raise AssertionError(err)

    try:
        return getattr(importlib.import_module(pkg), method)
    except Exception:
        return fail

def get_out():
    return sys.stdout.getvalue().strip()

def get_err():
    return sys.stderr.getvalue().strip()

def any_contains(needle, haystack):
    any(map(lambda x: needle in x, haystack))


# This solution to wrap a patched method comes originally from
# https://stackoverflow.com/questions/25608107/python-mock-patching-a-method-without-obstructing-implementation
def spy_decorator(method_to_decorate, name):
    mock = MagicMock(name="%s method" % name)
    def wrapper(self, *args, **kwargs):
        mock(*args, **kwargs)
        return method_to_decorate(self, *args, **kwargs)
    wrapper.mock = mock
    return wrapper

class patch_helper(object):
    
    def __init__(self, module_name):
        import importlib
        self.m = module_name
        
    def __call__(self, d):
        #import importlib
        parts=d.split(".")
        # If e.g. d == package.subpackage.subpackage2.attribute,
        # and our module is called mystery_data.
        try:
            getattr(importlib.import_module(self.m), parts[-1])   # attribute
            p=".".join([self.m, parts[-1]])
            # p='src.mystery_data.attribute'
        except ModuleNotFoundError:
            raise
        except AttributeError:
            if len(parts) == 1:
                raise
            try:
                getattr(importlib.import_module(self.m), parts[-2]) # subpackage2.attribute
                p=".".join([self.m] + parts[-2:])
                # p='src.mystery_data.subpackage2.attribute'
            except AttributeError:
                if len(parts) == 2:
                    raise
                try:
                    getattr(importlib.import_module(self.m), parts[-3]) # subpackage.subpackage2.attribute
                    p=".".join([self.m] + parts[-3:])
                    # p='src.mystery_date.subpackage.subpackage2.attribute'
                except AttributeError:
                    if len(parts) == 3:
                        raise
                    # package.subpackage.subpackage2.attribute
                    getattr(importlib.import_module(self.m), parts[-4])
                    p=".".join([self.m] + parts[-4:])
                    # p='src.mystery_date.package.subpackage.subpackage2.attribute'
        return p
