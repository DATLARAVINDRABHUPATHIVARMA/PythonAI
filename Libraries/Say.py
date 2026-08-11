# import cowsay
# import sys

# if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
#     cowsay.trex("Hello, " + sys.argv[1])

import sys
from Sayings import hello, goodbye

if len(sys.argv) == 3:
    hello(sys.argv[1])
    goodbye(sys.argv[2])