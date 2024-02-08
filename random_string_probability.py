import argparse as ap
import math

def get_probability(sequence_filename: str) -> None:
    """Finds probability of given sequence occuring for each provided gc score.

    The given file contains a sequence of length at most 100 base pairs and a matrix of at most 20 gc scores. This function returns a matrix where each index k contains the probability that a random string with the GC content provided in the corresponding k index of the GC score matrix is the same as the provided sequence. 

    Args:
        sequence_filename: Relative path to file containing DNA sequence and GC score array.
    
    Returns: 
        String containing probability of provided string being randomly produced for each given GC score.
    """
    line_num = 0
    all_probabilities = list()
    seq_probability = 1
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            if line_num == 0:
                sequence = line
                line_num += 1
                continue
            if line_num == 1:
                gc_scores = line.split(" ")
    for gc_score in gc_scores:
        score = float(gc_score)
        for nuc in sequence:
            if nuc == "A" or nuc == "T":
                seq_probability *= (1 - score) / 2
            if nuc == "C" or nuc == "G":
                seq_probability *= score / 2
        log_seq_probability = math.log(seq_probability, 10)
        log_seq_probability = round(log_seq_probability, 3)
        all_probabilities.append(str(log_seq_probability))
        seq_probability = 1
    all_probabilities = " ".join(all_probabilities)
    print(sequence)
    print(gc_scores)
    print(all_probabilities)
                
if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to file containing DNA sequence and GC score array.",
        type=str,
        required=True
    )
    args = parser.parse_args()
    probabilities = get_probability(args.sequence_filename)