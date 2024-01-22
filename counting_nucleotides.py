import argparse as ap


"""
1. type hints
2. One line describing the function
3. (Optional) Longer description of the function
4. Args: list arguments, their types, and what they are kind of
5. Returns: tell the user what is returned by the function
"""


def function_name(args: str):
    """This is a test function for python formatting rules.

    This is a longer description of what the function does. It will take in the arguments I received from the argument parser and do blah blah blah with them.

    Args:
        args: blah blah blah.

    Returns:
        Blah blah blah returns blah blah blah.
    """

    # Declaring this variable for later use.
    x = 1
    return x


def count_nucleotides(sequence_filename: str):
    """Counts the number of each nucleotide in a given DNA sequence.

    Takes a path to a .txt file containing a single DNA sequence. Reads the sequence and individually stores, prints, and returns the number of each nucleotide in their respective variable (ex. # of 'A' to adenine).

     Args:
         sequence_filename: Relative path to .txt file containing DNA sequence.

     Returns:
         A tuple containing the number of each nucleotide in the form (# of Adenine, # of Cytosine, # of Guanine, # of Thymine).
    """
    with open(sequence_filename) as f:
        for line in f:
            adenine = line.count("A")
            cytosine = line.count("C")
            guanine = line.count("G")
            thymine = line.count("T")
        f.close()
    print(adenine, cytosine, guanine, thymine)
    return adenine, cytosine, guanine, thymine


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    adenine, cytosine, guanine, thymine = count_nucleotides(args.sequence_path)
