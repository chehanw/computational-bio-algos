import argparse as ap


def dna_transcriptase(sequence_filename: str):
    """Switches T's for U's in the provided DNA sequence.

    Takes a path to a .txt file containing a single DNA sequence. Reads the sequence and replaces each 'T' (Thymine) with a 'U' (Uracil) in rna_sequence.

    Args:
        sequence_filename: Relative path to .txt file containing DNA sequence.

    Returns:
        DNA sequence string that has undergone transcription (Thymine ('T') switched for Uracil ('U')).
    """
    with open(sequence_filename) as f:
        for line in f:
            print(line)
            rna_sequence = line.replace("T", "U")
        f.close()
    print(rna_sequence)
    return rna_sequence


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    sequence = dna_transcriptase(args.sequence_path)
