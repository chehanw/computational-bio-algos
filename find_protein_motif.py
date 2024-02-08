import argparse as ap
import urllib.request

def read_url(url: str):
    """Takes in url leading to FASTA formatted protein sequence and returns the protein sequence.

    The url provided as an argument to this function leads to a FASTA formatted protein sequence. The first line of this sequence is the protein sequences ID, and the following lines contain the amino acids of the protein sequence. This function returns a string containing the protein sequence without the ID.

    Args:
        url: URL leading to FASTA formatted protein sequence.

    Returns:
        String containing the desired protein sequence.
    """
    sequence = urllib.request.urlopen(url)
    new_sequence = ""
    for line in sequence:
        line = line.strip()
        line = line.decode('utf-8')
        if line.startswith(">"):
            continue
        new_sequence += line
    print(url)
    return new_sequence

def get_protein_motif(sequence_filename):
    """Finds all protein sequences with "N{P}[ST]{P}" motif and each occurence of that motif.

    The way to read "N{P}[ST]{P}" is N, any amino acid but P, S or T, and any amino acid but P. The motif is satisfied for these conditions. This function takes in a file containing protein IDs for the UNIPROT database. It uses the read_url function to search the UNIPROT database for the corresponding protein sequence. It then parses through each sequence and checks for all occurences of the "N{P}[ST]{P}" motif. 

    Args:
        sequence_filename: Relative path to file containing UniProt Protein Database access IDs.

    Returns:
        Dictionary of each ID containing the "N{P}[ST]{P}" motif with its value being a list of the indices within each sequence where it occurs.
    """
    motif_occurences = dict()
    with open(sequence_filename) as f: 
        for line in f:
            line = line.strip()
            new_line = line
            if "_" in line:
                idx = line.find("_")
                new_line = line[: idx]

            url = f"http://www.uniprot.org/uniprot/{new_line}.fasta"
            sequence = read_url(url)
            for i in range(len(sequence) - 3):
                if sequence[i] == "N":
                    if sequence[i + 1] != "P":
                        if sequence[i + 2] == "S" or sequence[i + 2] == "T":
                            if sequence[i + 3] != "P":
                                if line not in motif_occurences:
                                    motif_occurences[line] = list()
                                motif_occurences[line].append(i + 1)
    print(motif_occurences)
    return motif_occurences

def format_motif(motif_occurences: dict) -> None:
    """Formats dictionary to fit Rosalind problem's desired formatting.

    Args:
        motif_occurences: Dictionary of each ID containing the "N{P}[ST]{P}" motif with its value being a list of the indices within each sequence where it occurs.     
    """
    for id in motif_occurences:
        print(id)
        indexes = [str(idx) for idx in motif_occurences[id]]
        print(" ".join(indexes))
        
    


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to file containing UniProt Protein Database access IDs",
        type=str,
        required=True,
    )
    
    args = parser.parse_args()
    motif_occurences = get_protein_motif(args.sequence_filename)
    format_motif(motif_occurences)

