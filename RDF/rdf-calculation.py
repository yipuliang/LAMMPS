import numpy as np
import matplotlib.pyplot as plt

rdf_file = 'rdf_AB.txt'

r_values = []
g_values = []

current_g = []  # storge current g(r)

with open(rdf_file, 'r') as file:
    for line in file:
        if line.startswith("#"):  # skip # line
            continue
        columns = line.split()
        
        if len(columns) == 2 and columns[0].isdigit():
            if current_g:  # if there are old data, then append
                g_values.append(current_g)
                current_g = []  # clear
            continue
        
        r = float(columns[1])    #read r and g(r)   columns[0] is bin number, please skip
        g = float(columns[2])
        
        if r not in r_values:
        #if not r_values:
            r_values.append(r)
        #print(r_values)
        current_g.append(g)
    
    # storage the last timestep data
    if current_g:
        g_values.append(current_g)

# convert to NumPy
r_values = np.array(r_values)
g_values = np.array(g_values)

# calculate the g(r)
g_average = np.mean(g_values, axis=0)

print(len(r_values),len(g_average))

plt.plot(r_values, g_average, label='Average RDF')
plt.xlabel('Distance (r)')
plt.ylabel('g(r)')
plt.title('Average Radial Distribution Function')
plt.grid(True)
plt.legend()
plt.show()


with open('average_rdf.dat', 'w') as output:
    output.write("# r g(r)\n")
    for r, g in zip(r_values, g_average):
        output.write(f"{r:.6f} {g:.6f}\n")

print("Average RDF saved to 'average_rdf.dat'")
