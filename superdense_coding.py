####################################

#Created by: Simsarul Haq Vengasseri
#Date: 30/10/2017

# This program demonstrations superdense coding.
# Please modify the path to the referenceqvm directory to import the api library.



import sys
sys.path.insert(0, '/home/infinitylabs/Documents/QSimulations/QSims/reference-qvm/referenceqvm')
import api
import pyquil.quil as pq
from pyquil.gates import *

qvm = api.SyncConnection()

def superdense_coding(cbit):
    ins = pq.Program()

    if(cbit==0):
        ins.inst(I(0), I(1), H(0), CNOT(0,1)) #Creating B00
        ins.inst(CNOT(0,1),H(0)).measure(0,0).measure(0,0).measure(1,1)
        qbits, addr = qvm.wavefunction(ins, [0,1])
    elif(cbit==1):
        ins.inst(I(0), X(1), H(0), CNOT(0,1)) #Creating B01
        ins.inst(CNOT(0,1),H(0)).measure(0,0).measure(0,0).measure(1,1)
        qbits, addr = qvm.wavefunction(ins, [0,1])
    elif(cbit==2):
        ins.inst(X(0), I(1), H(0), CNOT(0,1)) #Creating B10
        ins.inst(CNOT(0,1),H(0)).measure(0,0).measure(0,0).measure(1,1)
        qbits, addr = qvm.wavefunction(ins, [0,1])
    elif(cbit==3):
        ins.inst(X(0), X(1),H(0), CNOT(0,1)) #Creating B11
        ins.inst(CNOT(0,1),H(0)).measure(0,0).measure(0,0).measure(1,1)
        qbits, addr = qvm.wavefunction(ins, [0,1])
    return addr


if __name__ == '__main__':
    if (len(sys.argv)>1):
        try:
            cbit = int(sys.argv[1])
            result = superdense_coding(cbit)
            print result
        except ValueError:
            print ("Enter a number from range 0-3 as argument.")
            sys.exit(1)
    else:
        print "Please specify a number from range 0-3 as argument."
