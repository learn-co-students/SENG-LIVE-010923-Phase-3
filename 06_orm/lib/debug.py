#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.create_table()

Pet.create("spot", "dog", "chihuahua", "feisty")
Pet.create("rex", "dog", "boxer", "chill")
Pet.create("grace", "cat", "siamese", "mysterious")

import ipdb; ipdb.set_trace()
