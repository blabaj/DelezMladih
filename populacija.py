# -*- coding: utf-8 -*-

def mladi (vsi, mladi):
    procent_mladih = (float(mladi) / float(vsi)) * 100
    return float(procent_mladih)

def main():
    vsi = float(raw_input("Vnesi populacijo:"))
    stMladih = float(raw_input("Vnesi število mladih:"))
    delez = mladi(vsi,stMladih)
    print "Procent mladih: ", delez, "%"

if __name__ == '__main__':
    main()