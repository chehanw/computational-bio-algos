import argparse as ap


def fibonacci(num_months: int, offspring_per_generation: int) -> int:
    """Models rabbit reproduction after num_months for # of offspring_per_generation.

    Takes in two arguments, num_months and offspring_per_generation and returns the total number of pairs of offspring. Is modeled such that pairs can only reproduce after reaching maturity (one month).

    Args:
        num_months: Number of months for which the rabbits will be reproducing.
        offspring_per_generation: Number of offspring per pair of rabbits that mate.

    Returns:
        Total number of pairs of rabbits after num_months months.
    """

    a = 1
    b = 1
    for i in range(2, num_months):
        a, b = b, offspring_per_generation * a + b
    print(b)
    return b


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument(
        "--num_months",
        help="Number of months for which the rabbits will be reproducing",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--offspring_per_generation",
        help="Number of offspring per pair of rabbits that mate",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    total_pairs = fibonacci(args.num_months, args.offspring_per_generation)
