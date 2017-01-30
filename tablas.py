#!/usr/bin/env python
rango = range(1,11)
for numero in rango:
    print "\nTabla del " + str(numero) + '\n' + '-------------'
    for numero2 in rango:
        print str(numero) + ' por ' + str(numero2) + ' es ' + str(numero * numero2)
