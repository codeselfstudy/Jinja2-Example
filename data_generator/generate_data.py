"""You don't need to run this file. It was run once to generate a file of random data that
has no previous copyright."""
from faker import Faker
from random import randint, uniform


# The path should be platform independent, but it's just a quick script.
OUTFILE = './data/table_data.txt'
COLUMN_DELIMITER = '\t'  # TAB-separated
ROW_DELIMITER = '\n'  # Newline
HEADERS = ['Name', 'Species', 'Power', 'Height', 'Weight', 'Age']
SPECIES = ['Kobold', 'Beholder', 'Human', 'Elf', 'Goblin', 'Dragon', 'Giant']
POWERS = ['Fireball', 'None', 'Cure_critical_wounds', 'Lightning_bolt', 'Magic_missile', 'Floating_disk', 'Dimension_door']

fake = Faker()


def pick_a_random(thing):
    """Returns a random something."""
    if thing == 'species':
        choices = SPECIES
    elif thing == 'power':
        choices = POWERS
    else:
        return 'Zork'

    choice = randint(0, len(choices)-1)
    return choices[choice]


def generate_row():
    """Returns a tab-separated, single row of data as a string."""
    name = '_'.join([fake.first_name(), fake.last_name()])
    species = pick_a_random('species')
    power = pick_a_random('power')
    height = str(randint(1, 1000))
    weight = str(randint(1, 1000))
    age = str(round(uniform(1.0, 1000.0), 2))  # A float

    return COLUMN_DELIMITER.join([name, species, power, height, weight, age])


def generate_rows(num_rows):
    """Generates a specified number of rows with a header row on top.

    Returns a string that is ready for saving.
    """
    header = COLUMN_DELIMITER.join(HEADERS)
    content = ''.join([generate_row() + ROW_DELIMITER for _ in range(num_rows)])
    return '{}{}{}'.format(header, ROW_DELIMITER, content)


def main():
    """Runs the program, writing the output to the OUTFILE."""
    with open(OUTFILE, 'w') as f:
        f.write(generate_rows(1000))

if __name__ == '__main__':
    main()
