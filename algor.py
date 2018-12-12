
rowmax = 5
colmax = 21




P = []
Points = []
file = open('cisla.txt','r')

cisla = []

cisla = file.readlines()


for line in cisla:
    
    # print(line.split()[0],line.split()[1])
    P = [float(line.split()[0]),float(line.split()[1])]
    Points.append(P)

Points.pop(0)
xy = Points[0]
Points.pop(0)
print('Pocet radku: '+str(xy[1])+' a sloupcu: '+str(xy[0]))
for i in Points:
    print(i)


file.close()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Create a dataset:
# Create a dataset:
df=pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101) })

# plot
plt.plot( 'x', 'y', data=df, linestyle='none', marker='o')
plt.show()
