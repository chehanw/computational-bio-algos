import argparse as ap


def transcription(sequence_filename: str):
    """Finds the complementary strand of a given template strand.

    Reverses the given template strand (5' to 3') then matches each nucleotide to their complementary base pair (DNA polymerase). Uses base pair dictionary to match each nucleotide.

    Args:
        sequence_filename: Relative path to .txt file containing DNA sequence.

    Returns:
        The complementary sequence of given template sequence.
    """
    base_pairs = {"A": "T", "C": "G", "G": "C", "T": "A"}
    with open(sequence_filename) as f:
        for template_strand in f:
            template_strand = template_strand.strip()
            reversed_sequence = template_strand[::-1]
            complementary_strand = ""
            for nuc in reversed_sequence:
                complementary_strand += base_pairs[nuc]
        f.close()
    print(complementary_strand)
    return complementary_strand


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    sequence = transcription(args.sequence_path)
