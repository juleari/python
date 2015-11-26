from random import randint

def random_safe( xs, n ):
    a = []

    for i in range(n):
        x = xs[ randint( 0, len(xs) - 1 ) ]
        xs.remove(x)
        a.append(x)

    return a

def random_sample( xs, n ):
    xs = list( set(xs) )
    return [] if len(xs) < n else random_safe( xs, n )

def main():
    xs = [2, 4, 0, 7, 9, 5]

    print random_sample( xs, 3 )
    print random_sample( xs, 3 )
    print random_sample( xs, 3 )
    print random_sample( xs, 8 )

if __name__ == '__main__':
    main()