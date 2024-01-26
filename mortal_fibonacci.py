import argparse as ap


def mortal_fibonacci(
    num_months: int, offspring_per_generation: int, lifespan: int
) -> int:
    """Models rabbit reproduction and death using Fibonacci sequence.

    Given a specific number of offspring per generation and a lifespan of a rabbit in months, this function calculates the population of the rabbits in pairs after a given number of months. It is assumed that the reproductive age of the rabbits is 1 month old.

    Args:
        num_months: Number of months after first rabbit pair is born.
        offspring_per_generation: Number of pairs of offspring per rabbit pair.
        lifespan: Lifespan of each rabbit in months.

    Returns:
        Population of rabbits in pairs after given number of months.
    """

    a = 1
    b = 1
    # num_births[i] rabbits die at i + lifespan months
    num_births = [1, 0]
    for i in range(2, num_months):
        if i >= lifespan:
            a, b = (
                b - num_births[i - lifespan],
                offspring_per_generation * a + b - num_births[i - lifespan],
            )
            num_births.append(b - a)
        else:
            a, b = b, offspring_per_generation * a + b
            num_births.append(b - a)
        print(num_births)
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
    parser.add_argument(
        "--lifespan",
        help="Lifespan of the rabbits in months",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    total_pairs = mortal_fibonacci(
        args.num_months, args.offspring_per_generation, args.lifespan
    )
