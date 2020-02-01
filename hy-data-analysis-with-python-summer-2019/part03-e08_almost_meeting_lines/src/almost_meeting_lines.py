#!/usr/bin/python3

import numpy as np
from scipy import linalg

def almost_meeting_lines(a1, b1, a2, b2):
    exact = True
    try:
        s = linalg.solve([[a1, -1],[a2, -1]],[-b1,-b2])
    except linalg.LinAlgError:
        A = np.array([[a1, -1],[a2, -1]])
        y = np.array([-b1, -b2])
        x, residuals, rank, sing = linalg.lstsq(A, y)
        s = x
        exact = False
    return s, exact

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
