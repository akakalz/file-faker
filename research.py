# from faker import Faker
from example_config import config
from delimited_faker.file_faker import DelimitedFaker
from datetime import datetime


# f = Faker()
# f.seed_instance("this_seed")
# print(f.profile())
# print(f.profile())

ff = DelimitedFaker(config)

then = datetime.utcnow()
ff.fake()
now = datetime.utcnow()
print("done", str(now - then))  # done 0:00:01.790577 worst case so far
