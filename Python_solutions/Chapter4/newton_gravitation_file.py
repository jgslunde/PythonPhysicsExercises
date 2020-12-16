import sys

try:
    filename = sys.argv[1]
    M = float(sys.argv[2])

    G = 6.674*1e-11
    F = 0
    with open(filename,'r') as infile:
        for line in infile:
            values = line.split()
            m = float(values[0])
            r = float(values[1])
            F += G*m*M/(r**2)

    print "Total force on object with mass %g kg is %g N"%(M,F)

except IndexError:
    print "Error: Not enough arguments. Expected arguments: M filename"
except IOError:
    print "Error: File %s not found"%filename
except ValueError:
    print "Error: Value of M is not valid."
