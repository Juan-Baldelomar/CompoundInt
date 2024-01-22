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
    return log((m + (b/r)*(r+1))/(c + b/r * (r+1)), r+1)

def get_b_from_compound(m, c, r, n):
    """
    m : target value
    c : initial money value
    r : interest rate
    n : number of periods
    """
    n = n + 1
    return (m - c*(r+1)**(n-1))/((r+1)**n - (r+1))*r

def get_r_from_compound(m, c, b, n):
    n = n + 1
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
    n = n + 1
    return c*(r+1)**(n-1) + b/r * ((r+1)**n - (r+1))

def compound_recursive(a, r, b, n):
    if n == 0:
        return a

    prev = compound_recursive(a, r, b, n-1)
    newinv = prev + b
    return newinv*(r+1)

def compound_iterative(a, r, b, n, inflation=0.):
    final = a
    adjusted_b = b 
    for _ in range(n):
        adjusted_b = adjusted_b * (1 + inflation) if inflation > 0. else adjusted_b
        final = (final + adjusted_b) * (r+1)
    return final

    prev = compound_recursive(a, r, b, n-1)
    newinv = prev + b
    return newinv*(r+1)

def simple(c, r, b, n):
    """
    c : initial money value
    r : interest rate
    b : quantity to add every period
    n : number of periods
    """
    return (c+b)*r*(n-1) + c + (n-1)*b

def living_cost(c, inflation_rate, n):
    return compound(c, inflation_rate, 0, n)

def adquisition_power(c, r, n):
    return c/((1+r)**n)

def show_results(c, b, n, r):
    total = compound(c, r, b, n)
    inversion = c + b * n
    win = total - inversion
    print("Total1: {:.2f}\nGanancias: {:.2f}\n% Ganancias/Total {:.2f}".format(total, win, win/total))
    return total, inversion, win

def show_month_expenditures(retirement, period, offset, inflation):
    current_adquisition_power = adquisition_power(retirement, inflation, offset)
    print('Total: {:.2f}, monthly: {:.2f}'.format(retirement, retirement/(12*period)))
    print('Adquisition Power Total: {:.2f}, Adquisition Power monthly: {:.2f}'.format(current_adquisition_power, current_adquisition_power/(12*period)))




total, inversion, win  = show_results(300_000, 10_000, 36*12, 0.10/12)

show_month_expenditures(total, 20, 36, 0.05)





