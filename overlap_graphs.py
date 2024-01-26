import argparse as ap


def get_overlap_graph(sequence_filename: str, substring_length: int):
    """Takes sequences in FASTA file and produces adjacency list from their overlap.

    An overlap graph is a directed graph where the end of the tail node and the start of the head node share a substring of minimum length k. This function treats each sequence as a node, comparing its tail to the head of ever other node in the group. If they share a substring of length k, an edge is created and the pairing is added to the adjacency list.

    Args:
        sequence_filename: Relative path to file containing FASTA file.
        substring_length: minimum length of substring that two nodes share.

    Returns:
        Adjacency list containing all edges (pairings of nodes that share substrings).
    """

    sequences = {}
    curr_ID = ""
    adjacency_list = []
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            # Add FASTA IDs to dictionary.
            if line.startswith(">"):
                curr_ID = line[1:]
                sequences[curr_ID] = ""
                continue
            # Update value of curr_ID to match sequence in FASTA file.
            sequences[curr_ID] += line
    print(sequences)
    for id1 in sequences:
        for id2 in sequences:
            if id1 == id2:
                continue
            if sequences[id1][-substring_length:] == sequences[id2][:substring_length]:
                edge = [id1, id2]
                adjacency_list.append(edge)
    for i, edge in enumerate(adjacency_list):
        print(" ".join(edge))
    print(adjacency_list)
    return adjacency_list


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to file containing FASTA format sequences",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--substring_length",
        help="Minimum length of substring overlap",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    overlap_graph = get_overlap_graph(args.sequence_filename, args.substring_length)
