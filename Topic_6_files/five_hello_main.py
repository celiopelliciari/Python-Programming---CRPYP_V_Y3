#! /usr/bin/env python3

import sys


def hello():
    return "Hello, World!"


def main():
    print("This is the main function")
    print(hello())


if __name__ == "__main__":
    main()
else:
    print(f"'__name__' is not '__main__',", 
          f"called from '{__name__}'")
    sys.exit(1)

# End
