#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Template Notes (remove from your own scripts/modules):
#
# The top line informs UNIX/LINUX that the current file should be executed 
# as a python3 script. Unlike windows, which uses extensions like .doc or
# .pdf, files are determined by their contents in Linux.
#
# In this course, we assume python3, rather than python2.
#
# The second top line informs python3 to use UTF-8 character encoding, which
# enables unicode characters as default.
###

###
# Style Notes (remove from your own scripts/modules):
#
# Lines should never exceed 79 characters so that code is easily readable
# and printable. See the python style guide in the info repository for 
# a complete guide on recommended coding practices.
#
# The comment below is required according to Chapman University CPSC coding
# guidelines, also available in the info repository.
#
###

###
# Name: YOUR_FULL_NAME_HERE
# Student ID: ID_HERE
# Email: CHAPMAN_EMAIL_HERE
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER
###

"""Module Description (Replace with your documentation)
The first docstring at the top of the file appears in the "Description" field 
of the help command. That is, if you load a python interpreter the following 
makes the docstring visible:

  $ python
  >>> import your_module
  >>> help(your_module)

Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually formatted, and what
information is usually included.

This docstring should contain an overview and purpose of the code being
written below, as well as example uses (if appropriate).
"""


# This is the body of the module.  Place all global constants, function 
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.

# Minimize the use of global constants like this one.
CONSTANT1 = 0


def function1(arg1, kwarg1=defaultvalue, *args, **kwargs):
    """Function docstring
    All functions should have their own documentation via docstrings.
    Standard indent size in python is 4 spaces, no tabs. Arguments are
    positional, unless given a default value as a keyword-argument.
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    
    The function doc string should describe the name of the function, 
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.
    
    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    """
    pass


def main(local_argv):
    """Main function
    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
    pass


def test_function1():
    """Test function for nosetests
    Any function name starting with prefix test_ will be automatically run
    by nose. Ideally these should be put in a separate file that also
    begins with the prefix test_.
    
    In a test function, use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    assert True


class class1(object):
    """Class docstring
    """
    def __init__(self, *args, **kwargs):
        """Class constructor
        The self parameter refers to the object instance (similar to
        'this' in C++/Java).
        """
        pass
    
    def method1(self, *args, **kwargs):
        """Method docstring
        """
        pass
    

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)

