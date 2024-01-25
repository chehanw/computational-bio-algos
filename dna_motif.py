import argparse as ap


def motif(sequence: str, motif: str) -> list:
    """Gives indices of given substring within a DNA sequence.

    A motif is a recurring sequence of nucleotides that can be found within a DNA sequence. In the human genome, motifs of up to 1 million base pairs can be found, however the motif must always be shorter than the given sequence. This function tracks all the indices for which the given substring (motif) occurs in the given DNA sequence.

    Args:
        sequence: Sequence of DNA nucleotides
        motif: Substring being searched for in sequence

    Returns:
        List of all indices where the substring is found within the sequence.
    """
    indices = []
    i = 0
    while i < len(sequence):
        if motif not in sequence[i:]:
            break
        substring_idx = sequence.find(motif, i) + 1
        indices.append(substring_idx)
        i = substring_idx

    print(indices)
    return indices


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence",
        help="Sequence of DNA nucleotides",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--motif",
        help="Substring being searched for in sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    sequence = motif(args.sequence, args.motif)
