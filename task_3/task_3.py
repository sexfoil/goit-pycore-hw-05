import re

name = ["asd", "some"]
phone_number_pattern = re.compile(r"\(\d{3}\) \d{3}-\d{2}-\d{2}")
print(phone_number_pattern.match("(123) 456-78-90"))