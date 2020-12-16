# a)
gs = {}
with open('data_different_g.dat','r') as infile:
    line = infile.readline().split()

    while(line[0] == 'City:'):

        # Test if the name contains a space
        if (len(line) > 3):
            city = line[1] + " "+ line[2]
        else:
            city = line[1]

        g = line[-1][2:]
        gs[city] = float(g)
        line = infile.readline().split()

# b)
with open('on_Earth.dat','r') as infile:
    line = infile.readline().split()

    while(line[0] != 'On'):

        start = 2
        city1 = line[0]
        if(line[1] != 'to'):
            city1 += " "+line[1]
            start += 1

        city2 = ' '.join(line[start:])

        print str(gs[city1]) + " to " + str(gs[city2])
        line = infile.readline().split()
