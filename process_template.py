"""Reads in the data file and template and produces the rendered template."""
from jinja2 import Template


# TODO: check the correct way on how to make this cross-platform for Windows
TEMPLATE_FILE = './templates/page.html'
DATA_FILE = './data/table_data.txt'
OUT_FILE = './output/output.html'


def row_to_columns(row):
    """Takes a row as a string and returns it as a list of columns."""
    return [column for column in row.split() if column.strip() != '']


def data_to_dict(txt):
    """Takes a string of text from a file and returns it as a dict."""

    # Create a list made up of lines in the file.
    lines = txt.split('\n')

    # Remove the zeroth line and save it as 'header'
    header = lines.pop(0)

    # Create the dictionary and give it two key-value pairs:
    # the header_row for the top of the table, and a list of the rows, split into columns.
    d = {
        'header_row': header.split(),
        'rows': [row_to_columns(line) for line in lines if line.strip() != '']
    }
    return d


def main():
    with open(DATA_FILE, 'r') as data_file:
        raw_data = data_file.read()

    # Create the dictionary of data
    data = data_to_dict(raw_data)

    # Open the template
    with open(TEMPLATE_FILE, 'r') as template_file:
        template = Template(template_file.read())

    # Assign the finished string to 'output'
    output = template.render(data=data)

    with open(OUT_FILE, 'w') as outfile:
        outfile.write(output)

if __name__ == '__main__':
    main()
