# Other necessary calls
labels = []
for w in [-10,-5,0,5,10]:
    # Here we will solve for x and y using ODESolver
    labels.append("w = %g"%w)
    plt.plot(x,y)

plt.legend(labels)
plt.show()
