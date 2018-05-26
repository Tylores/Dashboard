import random
from der.models import Resource

# initialize the Resource model 100 "bess" resources with random energy
for x in range(10):
    rand = random.randint(10000, 30000)
    bess = Resource(type='bess', energy=rand)
    bess.save()
	
# initialize the Resource model 100 "ewh" resources with random energy
for x in range(10):
    rand = random.randint(100, 1500)
    ewh = Resource(type='ewh', energy=rand)
    ewh.save()