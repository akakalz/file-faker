from faker import Faker
from example_config import config
from src.file_faker import FileFaker


ff = FileFaker(config)

ff.fake()
print("done")
