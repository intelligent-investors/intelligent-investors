"""
This module provides functions to calculate the t-score for a given probability
level and degrees of freedom, as well as the probability level for a given t-score.

The t-score is a value derived from Student's t-distribution, which is used 
in statistical analyses to estimate population parameters when the sample size 
is small and the population standard deviation is unknown. The t-distribution 
is similar to the standard normal distribution but has heavier tails, meaning 
it is more prone to producing values that fall far from its mean.

The t-score for a probability level \( p \) and degrees of freedom \( df \) is 
calculated using the inverse cumulative distribution function (CDF) of the 
t-distribution:

t = T^{-1}(p, df)

where:
- T^{-1} is the inverse CDF (also known as the quantile function) of the 
  t-distribution.
- p is the probability level (a value between 0 and 1).
- df is the degrees of freedom.

The cumulative distribution function (CDF) for the t-distribution is defined as follows:

T(t, df) = P(T \leq t)

where:
- T(t, df) is the probability that the t-distributed random variable T with df 
  degrees of freedom is less than or equal to t.
- T is a random variable with a t-distribution.
- t is the value of interest.

In other words, the CDF indicates the probability that a t-distributed random 
variable is less than or equal to a given value t. The inverse CDF, also known 
as the quantile function, provides the value t for a given probability level p 
and degrees of freedom df.
"""
import argparse
from scipy.stats import t

def t_score(probability_level: float, degrees_of_freedom: int) -> float:
    """Calculates the t-score for a given probability level and degrees of freedom.

    Args:
        probability_level (float): The probability level (a value between 0 and 1).
        degrees_of_freedom (int): The degrees of freedom.
    
    Returns:
        float: The t-score corresponding to that probability level and degrees of freedom.

    Examples:
        >>> t_score(0.975, 10)
        2.2281388519649385
        
        >>> t_score(0.5, 20)
        0.0

        >>> t_score(0.025, 15)
        -2.131449545559323
    """
    return t.ppf(probability_level, degrees_of_freedom)


def probability_level_t(t_value: float, degrees_of_freedom: int) -> float:
    """Calculates the probability level for a given t-score and degrees of freedom.

    Args:
        t_value (float): The t-score.
        degrees_of_freedom (int): The degrees of freedom.
    
    Returns:
        float: The probability level corresponding to that t-score and degrees of freedom.

    Examples:
        >>> probability_level_t(2.2281388519649385, 10)
        0.975
        
        >>> probability_level_t(0.0, 20)
        0.5

        >>> probability_level_t(-2.131449545559323, 15)
        0.025
    """
    return t.cdf(t_value, degrees_of_freedom)

def main():
    parser = argparse.ArgumentParser(description="Calculate t-score or probability level for a given degrees of freedom.")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-p', '--probability', type=float, help="Calculate t-score for a given probability level.")
    group.add_argument('-t', '--tscore', type=float, help="Calculate probability level for a given t-score.")
    parser.add_argument('-d', '--degrees', type=int, help="Degrees of freedom.")
    args = parser.parse_args()

    if args.probability is not None and args.degrees is not None:
        if 0 < args.probability < 1:
            t_val = t_score(args.probability, args.degrees)
            print(f"t-score for probability level {args.probability:.3f} with {args.degrees} degrees of freedom: {t_val:.6f}")
        else:
            print("Error: Probability level must be between 0 and 1.")
    elif args.tscore is not None and args.degrees is not None:
        p = probability_level_t(args.tscore, args.degrees)
        print(f"Probability level for t-score {args.tscore:.6f} with {args.degrees} degrees of freedom: {p:.6f}")
    else:
        # Default examples if no arguments are provided
        default_degrees = 10  # Example degrees of freedom
        probability_levels = [0.5, 0.90, 0.95, 0.975, 0.99, 0.995]
        print(f"Default examples with {default_degrees} degrees of freedom:")
        for level in probability_levels:
            t_val = t.ppf(level, default_degrees)
            print(f"t-score for probability level {level:.3f}: {t_val:.6f}")

        t_scores = [0.0, 1.2815515655446004, 1.6448536269514722, 1.959963984540054, 2.3263478740408408, 2.5758293035489004]
        for t_val in t_scores:
            p = t.cdf(t_val, default_degrees)
            print(f"Probability level for t-score {t_val:.6f}: {p:.6f}")

if __name__ == '__main__':
    main()