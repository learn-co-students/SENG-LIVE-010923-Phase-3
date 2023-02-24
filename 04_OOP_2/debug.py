#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
from lib.pet import *
from lib.cat import *

# Instance of the Pet class
cookie = Pet('cookie', 1, 'Dachshund', 'hyper')

# Instance of the Cat class
grace = Cat('grace', 7, 'domestic longhair', 'affectionate', True)

import ipdb; ipdb.set_trace()