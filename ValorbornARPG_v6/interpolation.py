# Linear interpolation function
# Takes a start value, an end value, and an alpha value to interpolate between them.
def lerp(start, end, alpha):
    return start + alpha * (end - start)

