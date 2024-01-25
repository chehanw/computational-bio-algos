import argparse as ap


def make_codon_dict(codon_filename: str) -> dict:
    """Takes in a file containing codons and their corresponding amino acid pairs and makes a dictionary containing all of the pairs.

    A codon is a 3-nucleotide long sequence of DNA that codes for an amino acid. This function takes in all of those corresponding pairs and returns a dictionary allowing ease of access.

    Args:
        codon_filename: Relative path to .txt file containing codon-amino acid pairings

    Returns:
        A dictionary of codon-amino acid pairs.
    """
    codon_table = {}
    with open(codon_filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            for i, codon in enumerate(line):
                if len(codon) == 3:
                    codon_table[codon] = line[i + 1]
    print(codon_table)
    return codon_table


def translate(sequence_path: str, codon_table: dict) -> str:
    """Given an mRNA sequence, returns the corresponding polypeptide sequence.

    The central dogma of Biology is that DNA becomes RNA and RNA becomes protein. The process by which RNA becomes protein is called translation. This function takes in an mRNA sequence and assigns the corresponding amino acids for each codon (3 nucleotide sequence) in the mRNA sequence to the protein sequence.

    Args:
        sequence_path:  Relative path to .txt file containing DNA sequence.
        codon_table: A dictionary of codon-amino acid pairs.

    Returns:
        Corresponding amino acid sequence for which the mRNA codes.
    """
    protein_sequence = ""
    with open(sequence_path) as f:
        for line in f:
            i = 0
            while i < len(line):
                # UAA, UAG, UGA are stop codons
                if line[i : i + 3] in ["UAA", "UAG", "UGA"]:
                    break
                protein_sequence += codon_table[line[i : i + 3]]
                i += 3
    print(protein_sequence)
    return protein_sequence


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_path",
        help="Path to .txt file containing DNA sequence",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--codon_filename",
        help="Path to .txt file containing codon amino acid pairings",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    codon_table = make_codon_dict(args.codon_filename)
    sequence = translate(args.sequence_path, codon_table)
