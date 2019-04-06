import Polynomial
import sys
def main():
    polynom_str = sys.argv[1]
    if type(polynom_str) != str:
        raise TypeError

    var = input("differentiate with respect to: ")
    polin = Polynomial.Polynomial(var, [])
    polin.parse_from_string(polynom_str)

    print(polin.derive())

if __name__=='__main__':
    main()