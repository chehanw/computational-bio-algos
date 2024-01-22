import argparse as ap


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
