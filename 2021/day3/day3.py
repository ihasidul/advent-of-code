with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
def split(b_nums):
    return [char for char in b_nums]

def most_common(lst):
        return max(set(lst), key=lst.count)

def get_gamma_epsilon(lst):
    l = []
    idx = 0
    gamma = []
    epsilon = []
    while(idx < 12):
        for num in lst:
            n = split(num)
            print('nnnn',n)
            l.append(n[idx])
#        print('idx', idx)
#        print('l',l)
        # find which one is more and less 
#        print( 'most common',most_common(l))
        m_c_b = most_common(l)
        gamma.append(m_c_b)
        epsilon.append('1') if m_c_b == '0' else epsilon.append('0')

        l = []
        idx = idx + 1
#        print('gamma',gamma)
#        print('epsilon',epsilon)
    g = int(bin(int(''.join(gamma),2)),2)
    e = int(bin(int(''.join(epsilon),2)),2)
#    print(int(bin(int(''.join(gamma),2)),2))
    return g * e

print(get_gamma_epsilon(lines))
