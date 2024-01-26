import argparse as ap


def get_expected_offspring(sequence_filename: str) -> int:
    """Calculates expected value of offspring carrying dominant allele.

    Given populations of every possible combination of mates for a two allele trait, this function calculates the expected value that the two offspring of those mates carry the dominant allele.

    All possible mating pairs for two allele trait:
        1. A-AA
        2. AA-Aa
        3. AA-aa
        4. Aa-Aa
        5. Aa-aa
        6. aa-aa

    Args:
        sequence_filename: Relative path to sequence containing population numbers.

    Returns:
        Expected value of random offspring among any two mates of any two genotypes in the population.
    """

    # Contains population indices and the corresponding probabilites.
    probabilities = {0: 1.00, 1: 1.00, 2: 1.00, 3: 0.75, 4: 0.5, 5: 0.0}
    expected_value = 0
    with open(sequence_filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            for i, population in enumerate(line):
                expected_value += int(population) * probabilities[i]
    # 2 offspring per mating pair.
    expected_value *= 2
    print(expected_value)
    return expected_value


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--sequence_filename",
        help="Relative path to sequence containing population numbers",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    expected_offspring = get_expected_offspring(args.sequence_filename)
