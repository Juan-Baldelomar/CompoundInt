from math import log
from sympy import Eq, nsolve, symbols
import numpy as np

def get_n_from_compound(m, c, r, b):
    """
    m : target value
    c : initial money value
    r : interest rate
    b : quantity to add every period
    """
    return log((m + (b/r)*(r+1))/(c + b/r * (r+1)), r+1)+1

def get_b_from_compound(m, c, r, n):
    """
    m : target value
    c : initial money value
    r : interest rate
    n : number of periods
    """
    return (m - c*(r+1)**(n-1))/((r+1)**n - (r+1))*r

def get_r_from_compound(m, c, b, n):
    y = symbols('x')
    eq1 = Eq(c*(x+1)**(n-1) + b/x*((x+1)**n-(x+1))-m, 0)
    sol = nsolve(eq1, 0.1)
    return sol

def get_r(start, end, period=1):
    """
    start : initial money value
    end : money after interest was applied
    period : period is assumed to be a year. If you want it in months then period=1/12, days=1/365
    """
    return ((end-start)/start)/period

def compound(c, r, b, n):
    """
    c : initial money value
    r : interest rate
    b : quantity to add every period
    n : number of periods
    """
    return c*(r+1)**(n-1) + b/r * ((r+1)**n - (r+1))

def compound_recursive(a, r, b, n):
    if n == 1:
        return a*r + a

    prev = compound_recursive(a, n-1, r, b)
    newinv = prev + b
    return r*(newinv) + newinv

def simple(c, r, b, n):
    """
    c : initial money value
    r : interest rate
    b : quantity to add every period
    n : number of periods
    """
    return (c+b)*r*(n-1) + c + (n-1)*b
