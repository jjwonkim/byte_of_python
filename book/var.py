'''
Created on 2016. 7. 10.

@author: jkim
'''
import sys
from math import sqrt


def main(argv):


    print 'Square root of 16 is', sqrt(16)
    i = 5;
    print i;
    i = i + 1;
    print i;

    s = '''
This is a multi-line string.
This is the second line.''';
    print s;


    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
