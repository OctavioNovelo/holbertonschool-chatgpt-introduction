#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
