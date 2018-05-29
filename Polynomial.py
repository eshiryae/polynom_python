class Polynomial(object):

    def __init__(self, cfs):
        self.coeffs = []
        if isinstance(cfs, list):
            if not cfs:
                self.coeffs = [0]
                #print("List coeffs is empty")
            else:
                for el in cfs:
                    if not isinstance(el, (int, float)):
                        raise TypeError("Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ", el)
                        break
                self.coeffs = cfs
        elif isinstance(cfs, (int, float)):
            self.coeffs = [cfs]
        elif isinstance (cfs, Polynomial):
            self.coeffs = cfs.coeffs
        else:
            raise TypeError("Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ", cfs)

        #delete zeros
        while len(self.coeffs) > 1 and (self.coeffs[0] == 0 or self.coeffs[0] == 0.0):
            self.coeffs.pop(0);

        if self.coeffs:
            self.degree = len(self.coeffs) - 1
        else:
            self.degree = 0

    # Pol+const, Pol+Pol
    def __add__(self, other):
        res = []
        if isinstance(other, (int, float)):
            res = self.coeffs[:]
            res[self.degree] += other
        elif isinstance(other, Polynomial):
            if (self.degree < other.degree):
                tmp = self;
                self = other;
                other = tmp;
            res = self.coeffs[:]
            diff = self.degree - other.degree
            for i, val in enumerate(other.coeffs):
                res[i+diff] += val
        else:
            raise TypeError("Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ", other);
        return Polynomial(res)

    #const+Pol
    def __radd__(self, other):
        return self + other

    # +=
    def __iadd__(self, other):
        return self + other

    def __neg__(self):
        res = self.coeffs[:]
        for i, val in enumerate(res):
            res[i] = -val
        return Polynomial(res)

    # Pol-const, Pol-Pol
    def __sub__(self, other):
        if isinstance(other, (int, float, Polynomial)):
            res = self + (-other)
            return res
        else:
            raise TypeError("Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ", other)

    #const-Pol
    def __rsub__(self, other):
        res = -self + other
        return res

    # -=
    def __isub__(self, other):
        return self.__add__(-other)

    # Pol * Pol, Pol * const
    def __mul__(self, other):
        res = []
        if isinstance(other, (int, float)):
            for el in self.coeffs:
                res.append(other*el)
        elif isinstance(other, Polynomial):
            res = [0] * (self.degree + other.degree + 1)
            for i, firstElem in enumerate(self.coeffs):
                for j, secondElem in enumerate(other.coeffs):
                    res[i+j] += firstElem * secondElem
        else:
            raise TypeError("Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ", other);
        return Polynomial(res)

    def __rmul__(self, other):
        res = self * other
        return res

    def __imul__(self, other):
        return self * other

    def __str__(self):
##        res = ""
##        for pow, coeff in enumerate(self.coeffs):
##            if coeff:
##                if self.degree == 0:
##                    res += str(coeff)
##                else:
##                    if abs(coeff) == 1:
##                        if not (self.degree == pow):
##                            res += ("+x" if coeff > 0 else "-x") + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
##                        else:
##                            res += ("+" if coeff > 0 else "-") + str(abs(coeff))
##                    else:
##                        res += ("+" if coeff > 0 else "-") + str(abs(coeff))
##                        if not (self.degree == pow):
##                            res += "x" + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
##        if res:
##            return res.lstrip("+")
##        else:
##            return "0"
        res = ""
        for i, coef in enumerate(self.coeffs):
            if coef:
                if self.degree == 0:
                    res += str(coef)
                else:
                    pow = self.degree - i
                    if i == 0:
                        if abs(coef) == 1:
                             if coef < 0: res += "-"
                        else:
                             res += str(coef)
                        if pow > 1: res += "x^" + str(pow)
                        elif pow == 1: res += "x"
                        else: res += "1" if abs(coef) == 1 else ""
                    else:
                        if abs(coef) == 1:
                             if coef < 0: res += "-"
                             else: res += "+"
                        else:
                             if coef > 0: res += "+"
                             res += str(coef)
                        if pow > 1: res += "x^" + str(pow)
                        elif pow == 1: res += "x"
                        else: res += "1" if abs(coef) == 1 else ""
        if res:
            return res
        else:
            return "0"

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.coeffs[0] == other
        elif isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif isinstance(other, str):
            return str(self) == other
        return False

    def __ne__(self, other):
        return not self == other

