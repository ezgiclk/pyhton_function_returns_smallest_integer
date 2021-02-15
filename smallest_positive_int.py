#finding the smallest positive integer that does not occur in a serie.

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

A=pd.Series([1, 3, 6, 4, 1, 2])
B=pd.Series([-1,-2])
C=pd.Series([-1,-2,1,3,4])
D=pd.Series([0])

def find_min_int(my_serie):
    my_serie= my_serie.sort_values(ascending=True)
    my_serie= my_serie.unique()
    my_serie=my_serie[my_serie>0]
    j=1
    result =1
    for i in my_serie:
        if my_serie[0]!=1:
            result=1
        elif j == i:
             j+=1
        else:
            result=j
    return result

print(find_min_int(A))
print(find_min_int(B))
print(find_min_int(C))
print(find_min_int(D))