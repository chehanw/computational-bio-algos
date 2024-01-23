import argparse as ap


def inheritance(num_dominant: int, num_heterozygous: int, num_recessive: int):
    """Models Mendelian inheritance for given population numbers.

    In Mendelian inheritance, homozygous dominant organisms have a 100% chance of producing dominant carrying offspirng. Heterozygous have a 75% chance when mating with other heterozygous and 50% chance when mating with recessive organisms. Recessive organisms cannot produce dominant carrying offspring. This function uses those probabilities to calculate the probability that a random offspring among any two organisms in the population carries a dominant allele.

    Args:
        num_dominant: Number of organisms with two dominant alleles in the population.
        num_heterozygous: Number of organisms with one dominant and one recessive allele in the population.
        num_recessive: Number of organisms with two recessive alleles in the population.

    Returns:
        The probability that the offspirng of two organisms in the population possesses a dominant allele and thus displays the dominant phenotype.
    """

    expected_value = 0
    num_outcomes = (
        mate_within_type(num_dominant)
        + mate_within_type(num_heterozygous)
        + mate_within_type(num_recessive)
        + (num_dominant * num_heterozygous)
        + (num_dominant * num_recessive)
        + (num_heterozygous * num_recessive)
    )
    expected_value += 1.00 * (
        (num_dominant * num_heterozygous)
        + (num_dominant * num_recessive)
        + mate_within_type(num_dominant)
    )
    expected_value += 0.75 * (mate_within_type(num_heterozygous))
    expected_value += 0.5 * (num_heterozygous * num_recessive)
    print(expected_value / num_outcomes)
    return expected_value / num_outcomes


def mate_within_type(num_organisms):
    """Calculates number of possible mating pairs within organism type.

    The total number of mating pairs among each type can be calculated by adding (n-1) + (n-2) + (n-3) ... (n-n) where n is the population of the organism. This represents each unique pairing for which the organism type can mate within itself.

    Args:
        num_organisms: The number of dominant, heterozygous, or recessive organisms in the population.

    Returns:
        Total number of unique combinations of mates within a single organism type.
    """
    i = num_organisms
    total_combinations = 0
    while i > 0:
        i -= 1
        total_combinations += i
    return total_combinations


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--num_dominant",
        help="Number of organisms with two dominant alleles in the population.",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--num_heterozygous",
        help="Number of organisms with one dominant and one recessive allele in the population.",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--num_recessive",
        help="Number of organisms with two recessive alleles in the population.",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    total_pairs = inheritance(
        args.num_dominant, args.num_heterozygous, args.num_recessive
    )
