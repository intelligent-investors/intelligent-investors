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
- \Phi(Z) is the probability that the standard normal variable Z is less than or equal to z.
- Z  is a random variable with a normal distribution (mean of 0 and standard deviation of 1).
- z is the value of interest (in ter
"""

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

if __name__ == '__main__':
    probability_levels = [0.5, 0.90, 0.95, 0.99, 0.995]
    for level in probability_levels:
        z = norm.ppf(level)
        print(f"z_score for probability level {level:.3f}: {z:.6f}")