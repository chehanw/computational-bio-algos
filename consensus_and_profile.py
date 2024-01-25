import argparse as ap
import numpy as np


def get_profile_matrix(sequence_filename: str) -> np.ndarray:
    """Takes in FASTA format file and returns the profile matrix of the sequences.

    A profile matrix is a 4 x N matrix containing the count of each nucleotide at each index. The 4 rows represent the 4 DNA nucleotides in the following order: ["A", "C", "G", "T"]. N represents the length of each sequence. For example, the 4th row at the jth index of the profile matrix will contain the number of times T appears in the jth index of each sequence. This function finds the profile matrix for any number of sequences provided in FASTA format.

    Args:
        sequence_filename: Relative path to file containing FASTA formatted file.

    Returns:
        4 x N matrix containing the count of each nucleotide at each index.
    """

    nucleotide_counts = []
    sequence = ""
    nucleotide_indices = {"A": 0, "C": 1, "G": 2, "T": 3}
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if len(sequence) > 0:
                    if len(nucleotide_counts) == 0:
                        for i in range(4):
                            nucleotide_counts.append([0] * len(sequence))
                    for i, ch in enumerate(sequence):
                        nucleotide_counts[nucleotide_indices[ch]][i] += 1
                sequence = ""
                continue
            sequence += line
    for i, ch in enumerate(sequence):
        nucleotide_counts[nucleotide_indices[ch]][i] += 1

    profile_matrix = np.array(nucleotide_counts)
    print(profile_matrix)
    return profile_matrix


def get_consensus_string(profile_matrix: np.ndarray) -> str:
    """Takes in profile matrix and returns a consensus string of the given matrix.

    The consensus string contains the most common nucleotide at each index for all sequences. Its function is to "average" many different sequences to find the likely ancestral DNA sequence from which the provided sequences are derived. Using the profile matrix, this function finds the nucleotide with the highest frequency at each index and adds it to the consensus string.

    Args:
        profile_matrix: The profile matrix created from the given sequences.

    Returns:
        Consensus string containing most common nucleotide at each index.
    """

    nucleotide_indices = {0: "A", 1: "C", 2: "G", 3: "T"}
    consensus_string = ""
    max_indices = profile_matrix.argmax(axis=0)
    for idx in max_indices:
        consensus_string += nucleotide_indices[idx]

    print(consensus_string)
    return consensus_string


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        type=str,
        help="Relative path to file containing FASTA organized sequences",
        required=True,
    )
    args = parser.parse_args()
    profile_matrix = get_profile_matrix(args.sequence_filename)
    consensus_string = get_consensus_string(profile_matrix)
