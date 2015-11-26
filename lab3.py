import string

def main():

    s = "    skfhlaskd\n\r SLSkcbC1213 324908jlfgdsHJGShfg BLsd adagc \n sdi    y   "
    s = s.lower()

    t = [   chr(o) + '-' + str( s.count( chr(o) ) ) \
            for o in range( ord('a'), ord('z') + 1 ) \
            if s.count( chr(o) ) ]

    print string.join( t, '\n' )

if __name__ == '__main__':
    main()