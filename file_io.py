def read_input_file():
    """
    Reads game input data from input.txt
    Line 1: (ignored name placeholder)
    Line 2: Player starting health
    """

    with open("input.txt", "r") as file:
        file.readline()              # ignore name line
        health = int(file.readline())

    return health


def write_output_file(text):
    """
    Writes game result to output.txt
    """

    file = open("output.txt", "w")
    file.write(text)
    file.close()
