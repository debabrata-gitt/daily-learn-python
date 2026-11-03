try:
    import numpy as np

    np.seterr(over='raise')
    result = np.float64(1e308) * np.float64(1e308)
    print(result)

except FloatingPointError:
    print("Floating point error occurred")