"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_info(data)


def get_data():
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        print(f"{parts}")
        data.append(parts)
    input_file.close()
    return data


def print_subject_info(data):
    for entry in range(len(data)):
        print(f"{data[entry][0]} is taught by {data[entry][1]} and has {data[entry][2]} students")


main()
