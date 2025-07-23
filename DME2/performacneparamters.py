import math as m
import numpy as np
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)


def Somerfeld(ldr, S):
    df = pd.read_excel('Book1.xlsx')
    df = df.set_index(['l/d', 'S'])
    print(df)
    print(df.loc[ldr, S])


def minimumfilmthickness(ldr, mftv):
    df = pd.read_excel('Book1.xlsx')
    df = df.set_index(['ldr', 'h0/c'])
    print(df.loc[ldr, mftv])


if __name__ == '__main__':

    print('Enter the following information(enter 0 if the value is unknown):')
    dia = float(input("1. Shaft diameter(mm): "))
    length = float(input("2. Bearing length(mm): "))
    ldr = length / dia
    print('Length to diameter ratio: {}'.format(ldr))
    cl = float(input("3. Radial clearance(micron): "))*0.001
    n = float(input("4. Rotational speed(rpm): "))
    h0 = float(input("5. Minimum film thickness: "))
    v = float(input("6. Viscosity(cP): "))*0.000000001
    den = float(input("7. Density(kg/m^3): "))
    cp = float(input("8. Specific heat capacity(kJ/kg{}C): ".format(chr(176))))
    W = float(input("9. Enter radial load(N): "))
    if W is not None:
        p = W / (dia * length)
        print('Pressure:', p)
    else:
        p = 0

    if cl or n or v or p is not None:
        S = ((((dia/2) / cl)**2) * v * (n / 60)) / p
        S = round(S, 3)
        print('Sommerfeld:', S)
        Somerfeld(ldr, S)
    else:
        S = 0

    if h0 and cl is not None:
        mftv = float(h0) / (float(cl) * 10e-3)
        print(mftv)
        minimumfilmthickness(ldr, mftv)



