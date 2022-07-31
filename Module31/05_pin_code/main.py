import itertools

from itertools import product

for i_count in product('0123456789'):
    for j_count in product('0123456789'):
        for k_count in product('0123456789'):
            for l_count in product('0123456789'):
                result = ''.join(i_count)+''.join(j_count)+''.join(k_count)+''.join(l_count)
                print(result)