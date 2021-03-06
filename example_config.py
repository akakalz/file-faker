from abstracts.file_faker import FileFakerConfig
from abstracts.field import DelimitedField


config = FileFakerConfig(
    file_name="example_file.txt",
    fields=[
        DelimitedField(name="full name", type="name"),
        DelimitedField(name="address", type="address_line_1"),
        DelimitedField(name="city", type="address_city"),
        DelimitedField(name="state", type="address_state"),
        DelimitedField(name="zip code", type="address_zip"),
        DelimitedField(name="customer key", type="uuid"),
        DelimitedField(name="date of birth", type="dob"),
        DelimitedField(name="description", type="string"),
        DelimitedField(name="balance", type="currency"),
    ],
    has_header=True,
    row_count=100000,
    delimiter="|",
)
