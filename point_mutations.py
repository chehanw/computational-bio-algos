import argparse as ap


def hamming_distance(sequence_filename: str):
    """Calculates Hamming distance between two sequences.

    The Hamming distance is the number of point mutations between two sequences.

    Args:
        sequence_filename: Relative path to .txt file containing DNA sequence.

    Returns:
        Total number of point mutations between the two given sequences, also known as the Hamming distance.
    """

    sequence_1 = ""
    sequence_2 = ""
    num_mutations = 0
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            if len(sequence_1) == 0:
                sequence_1 += line
            else:
                sequence_2 += line
        for nuc1, nuc2 in zip(sequence_1, sequence_2):
            if nuc1 != nuc2:
                num_mutations += 1
    print(num_mutations)
    return num_mutations


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    sequence = hamming_distance(args.sequence_path)
