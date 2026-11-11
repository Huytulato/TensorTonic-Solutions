import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    alpha = 1.6732632423543772
    scale = 1.0507009873554805
    return [
        round(
         scale* (v if v>0 else alpha*(math.exp(v)-1)), 4
        ) 
        for v in x
    ]