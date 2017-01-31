#!/usr/bin/python

Xa=10000
for i in range(2,Xa):
#    print "start", i
    for r in range(1,i+1):
    #    print i, ":", r
        if r==i:
            print "Prime number: ", r
        elif i%r==0 and r!=1 :
        #    print "break"
            break


else :
    print "Wypisano liczby pierwsze"
