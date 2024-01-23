import argparse as ap


def compute_gc(sequence_filename: str):
    """Calculates percentage of guanine and cytosine in a given DNA sequence and returns the max GC score along with the ID of the sequence.


    The GC score of a nucleotide sequence represents the percentage of guanine and cytosine in that sequence. It is used to differentiate between genetically different species. Two humans should have very similar GC scores whereas a human and a banana should differ in their GC scores. This function finds the GC score and corresponding ID for each sequence. It keeps track of the max GC score and once it parses the entire file, returns the max score along with its corresponding ID.

    Args:
        sequence_filename: Relative path to .txt file containing DNA sequence.

    Returns:
        max_id: The ID of the sequence with the max gc score of thhe form Rosalind_XXXX)
        max_gc: The highest gc score among the given sequences.
    """

    sequence = ""
    max_id = ""
    current_id = ""
    max_gc = 0
    current_gc = 0
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            if line[0] == ">":
                if len(sequence) != 0:
                    current_gc = (
                        (sequence.count("C") + sequence.count("G"))
                        / len(sequence)
                        * 100
                    )
                    sequence = ""
                if current_gc > max_gc:
                    max_gc = current_gc
                    max_id = current_id
                current_id = line[1:]
                continue
            sequence += line
        current_gc = (sequence.count("C") + sequence.count("G")) / len(sequence) * 100
        if current_gc > max_gc:
            max_gc = current_gc
            max_id = current_id

    print(max_id, max_gc)
    return max_id, max_gc


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    sequence = compute_gc(args.sequence_path)
