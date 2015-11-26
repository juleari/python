# -*- coding: utf8 -*-
import math

def getData():
    xs = []

    while True:
        try:
            s = input()
        except:
            return xs
        else:
            xs.append( float(s) )

def main():

    xs = getData()

    print "       количество введённых чисел: %s\n"\
          "            сумма введённых чисел: %s\n"\
          "среднее арифметическое этих чисел: %s\n"\
          "    наибольшее из введённых чисел: %s\n"\
          "     наименьший квадратный корень: %s\n"\
          "     наибольший квадратный корень: %s\n" % \
            ( len(xs),\
              sum(xs),\
              sum(xs) / len(xs),\
              max(xs),\
              min([math.sqrt(x) for x in xs if x > 0]),\
              max([math.sqrt(x) for x in xs if x > 0]) )

if __name__ == '__main__':
    main()