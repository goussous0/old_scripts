def lst_comp(x,y,z,n):

    cuboid_dims = ([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) <= n)])
    return cuboid_dims

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = lst_comp(x,y,z,n)
    print (res)