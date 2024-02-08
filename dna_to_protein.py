import argparse as ap 

def get_protein_sequence(sequence_filename:str, dna_codon_table: dict, rna_codon_table: dict) -> list:
    """Takes in given DNA sequence and finds all possible protein sequences that the sequence codes for.

    The given strand of DNA can either be the template strand or coding strand for transcription. This means that the sequence's reverse complement(transcribed DNA) must also be translated into a protein sequences. The translation from DNA to protein or RNA to protein starts at their respective start codons and ends at their respective stop codons. The protein sequence is every amino acid in between the two. 

    Args:
        sequence_filename: Relative path to file containing FASTA formatted sequence.
        dna_codon_table: Dictionary containg DNA codon-amino acid pairings.
        rna_codon_table: Dictionary containg RNA codon-amino acid pairings.
    Returns:
        List of all protein sequences for which the given sequence can encode.
    """
    base_pairs = {"A": "U", "C": "G", "G": "C", "T": "A"}
    sequence = ""
    all_protein_seqs = list()
    protein_sequence = ""
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                continue
            sequence += line
    reversed_sequence = sequence[::-1]
    reverse_complement = ""
    for nuc in reversed_sequence:
        reverse_complement += base_pairs[nuc]
    print(reverse_complement)
    rna_seqs = get_sequence(reverse_complement, rna_codon_table, "AUG", ["UAG", "UGA", "UAA"])
    for seq in rna_seqs:
        all_protein_seqs.append(seq)
    dna_seqs = get_sequence(sequence, dna_codon_table, "ATG", ["TAG","TGA","TAA"])
    for seq in dna_seqs:
        if seq not in all_protein_seqs:
            all_protein_seqs.append(seq)
    all_protein_seqs = "\n".join(all_protein_seqs)
    print(all_protein_seqs)
    return all_protein_seqs

def get_sequence(sequence: str, codon_table:dict, start_codon: str, stop_codon: list) -> set:
    """Helper function that translates the given sequence into the protein sequence it encodes for.

    The function of creating a list of all possible protein sequences for which the given DNA or RNA sequence encodes. It returns a set to avoid any repeat sequences.

    Args:
        sequence: DNA or RNA sequence to translate to protein.
        codon_table: Dictionary containg DNA or RNA amino acid pairings.
        start_codon: "AUG" if RNA and "ATG" if DNA.
        stop_codon: ["TAG","TGA","TAA"] if DNA and ["UAG", "UGA", "UAA"] if RNA

    Returns:
        Set of all possible protein sequences for which the provided sequence encodes.
    """
    seqs = set()
    protein_sequence = ""
    for i in range(len(sequence) - 3):
        if sequence[i: i + 3] == start_codon:
            protein_sequence += codon_table[sequence[i: i + 3]]
            j = i + 3
            while (sequence[j: j + 3] not in stop_codon) and j + 3 <= len(sequence):
                protein_sequence += codon_table[sequence[j: j + 3]]
                j += 3
            if j >= len(sequence):
                protein_sequence = ""
                continue
            seqs.add(protein_sequence)
            protein_sequence = ""
    print(seqs)
    return seqs

def get_codon_table(codon_filename:str) -> dict:
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

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to file containing FASTA formatted sequence.",
        type=str,
        required=False
    )
    parser.add_argument(
        "--rna_codon_filename",
        help="Path to .txt file containing codon amino acid pairings for RNA",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--dna_codon_filename",
        help="Path to .txt file containing codon amino acid pairings for DNA",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    rna_codon_table = get_codon_table(args.rna_codon_filename)
    dna_codon_table = get_codon_table(args.dna_codon_filename)
    protein_sequence = get_protein_sequence(args.sequence_filename, dna_codon_table, rna_codon_table)
