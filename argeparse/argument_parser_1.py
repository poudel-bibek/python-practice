"""
Argument parser helps process command line arguments in Python
"""

import argparse

"""
### First
parser = argparse.ArgumentParser(
    description= "A simple parser",
    epilog= "Example Usage"
    )

# By default print the argument parsing instructions (arguments, examples)
parser.print_help()
"""

### Second
def get_args():
    parser = argparse.ArgumentParser(
        description= " A simple parser",
        epilog= "Example Usage"
    )

    return parser.parse_args()

if __name__ == '__main__':
    get_args()


