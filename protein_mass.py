import argparse as ap 
import pprint

def mass_table(filename: str) -> dict:
    """Builds monoisotopic mass table given unformatted table.

    The given problem provides a monoisotopic mass table in a form that is difficult to parse throuhg. This function simply takes in the given table and puts it into a dictionary format, making the following function more efficient.

    Args:
        filename: Relative path to file containg monoisotopic mass table for amino acids.
    
    Returns:
        Dictionary of amino acids and their corresponding monoisotopic mass.
    """
    table = dict()
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.replace(" ", "")
            if len(line) != 0:
                table[line[0]] = line[1:]
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(table)
    return table

def get_protein_mass(sequence_filename: str, table_filename: str) -> int:
    """Use monoisotopic mass table to find mass of whole protein.

    Each letter in a given string corresponds to an amino acid. The monoisotopic mass table contains the masses of each of those amino acids in a dictionary. This function parses through the string and adds the corresponding mass of each amino acid to the total mass.

    Args:
        sequence_filename: Relative path to file containg amino acid sequence.
        table_filename: Relative path to file containg monoisotopic mass table for amino acids

    Returns:
        Total mass of protein sequence.
    """
    table = mass_table(table_filename)
    mass = 0
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            for amino_acid in line:
                mass += float(table[amino_acid])
    print(mass)
    return mass


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to file containg amino acid sequence",
        type=str,
        required=True
    )
    parser.add_argument(
        "--table_filename",
        help="Relative path to file containg monoisotopic mass table for amino acids",
        type=str,
        required=True
    )
    args = parser.parse_args()
    mass = get_protein_mass(args.sequence_filename, args.table_filename)
