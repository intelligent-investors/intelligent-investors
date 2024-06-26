"""
This module provides a function to calculate the z-score for a given probability
level.

The z-score is the number of standard deviations a data point is from the mean 
of a normalized distribution (a normal distribution with a mean of 0 and a 
standard deviation of 1). It indicates the extent and direction of a value's 
deviation from the mean.

The z-score for a probability level \( p \) is calculated using the inverse 
cumulative distribution function (CDF) of the normal distribution:

z = \Phi^{-1}(p)

where:
- \Phi^{-1} is the inverse CDF (also known as the quantile function).
- p is the probability level (a value between 0 and 1).

The cumulative distribution function (CDF) for a normal distribution is defined as follows:

\Phi(Z) = P(Z \leq z)

where:
- \Phi(Z) is the probability that the standard normal random variable Z is less than or equal to z.
- Z is a random variable with a normal distribution (mean of 0 and standard deviation of 1).
- z is the value of interest (in terms of the number of standard deviations from the mean).

In other words, the CDF indicates the probability that a normally distributed random variable is less than or equal to a given value z.
The inverse CDF, also known as the quantile function, provides the value z for a given probability level p.
"""
import argparse
from scipy.stats import norm

def z_score(probability_level: float) -> float:
    """Calculates the z-score for a given probability level.

    Args:
        probability_level (float): The probability level (a value between 0 and 1).
    
    Returns:
        float: The z-score corresponding to that probability level.

    Examples:
        >>> z_score(0.995)
        2.5758293035489004
        
        >>> z_score(0.5)
        0.0

        >>> z_score(0.025)
        -1.959963984540054
    """
    return norm.ppf(probability_level)


def probability_level(z: float) -> float:
    """Calculates the probability level for a given z-score.

    Args:
        z (float): The z-score.
    
    Returns:
        float: The probability level corresponding to that z-score.

    Examples:
        >>> probability_level(2.5758293035489004)
        0.995
        
        >>> probability_level(0.0)
        0.5

        >>> probability_level(-1.959963984540054)
        0.025
    """
    return norm.cdf(z)

def main():
    parser = argparse.ArgumentParser(description="Calculate z-score or probability level.")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-p', '--probability', type=float, help="Calculate z-score for a given probability level.")
    group.add_argument('-z', '--zscore', type=float, help="Calculate probability level for a given z-score.")
    args = parser.parse_args()

    if args.probability is not None:
        if 0 < args.probability < 1:
            z = z_score(args.probability)
            print(f"z-score for probability level {args.probability:.3f}: {z:.6f}")
        else:
            print("Error: Probability level must be between 0 and 1.")
    elif args.zscore is not None:
        p = probability_level(args.zscore)
        print(f"Probability level for z-score {args.zscore:.6f}: {p:.6f}")
    else:
        probability_levels = [0.5, 0.90, 0.95, 0.975, 0.99, 0.995]
        for level in probability_levels:
            z = norm.ppf(level)
            print(f"z_score for probability level {level:.3f}: {z:.6f}")

        z_scores = [0.0, 1.2815515655446004, 1.6448536269514722, 1.959963984540054, 2.3263478740408408, 2.5758293035489004]
        for z in z_scores:
            p = probability_level(z)
            print(f"Probability level for z_score {z:.6f}: {p:.6f}")

if __name__ == '__main__':
    main()