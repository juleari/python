import math

def recgcd( a, b ):
    if a < b:
        return recgcd( b, a )

    r = a % b
    return b if r == 0 else recgcd( b, r )

def loopgcd( a, b ):

    if a < b: a, b = b, a
    
    while a % b != 0:
        a, b = b, a % b

    return b

def reclcm( a, b ):
    return a * b / recgcd( a, b )

def looplcm( a, b ):
    return a * b / loopgcd( a, b )

def intsqrt( x ):
    return int( math.ceil( math.sqrt(x) ))

def prime( n ):
    s = intsqrt( n )
    e = range(2, s)

    for i in range(2, intsqrt(s)):
        if i in e:
            e = filter( lambda x: x == i or x % i, e )

    return not( len(e) ) or not( len( filter( lambda x: not(n % x), e ) ) )

if __name__ == '__main__':
    print recgcd( 3542, 2462 )
    print reclcm( 3, 4 )
    print loopgcd( 3542, 2462 )
    print looplcm( 3, 4 )
    print prime( 11 )
    print prime( 12 )
    print prime( 3571 )