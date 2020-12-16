from math import cos,pi

#a)
with open('slide_books.dat','r') as infile:
    infile.readline()
    masses = [float(value) for value in infile.readline().split()]

    infile.readline()
    degrees = [float(value) for value in infile.readline().split()]

    infile.readline()
    friction_coeff = [float(value) for value in infile.readline().split()]

#b)
g = 9.81
with open('slide_books_result.dat','w') as infile:

    for m in masses:
        infile.write("--- Book with mass %.2f kg ---\n"%m)
        for th in degrees:
            th_rad = (th*pi)/180.
            infile.write("theta = %.2f rad\n"%th_rad)
            for f in friction_coeff:
                infile.write("coefficient of friction = %g\n"%f)
                infile.write("needed friction force is %.2f N\n\n"%(f*m*g*cos(th_rad)))
    infile.write("\n")
