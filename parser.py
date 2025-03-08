import re

# ========================Your school adn raw data====================================
SCHOOL_NAME = "your school"
raw_data = """
Your raw input
"""
# ========================Your school adn raw data====================================

lines = raw_data.split("\n")

# Define a set to store unique names
unique_names = set()

name_pattern = re.compile(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$")

# Process each line
for line in lines:
    line = line.strip()
    if name_pattern.match(line):  
        unique_names.add(line)

people = [{"name": name, "school": SCHOOL_NAME} for name in sorted(unique_names)]


