# LAMMPS AND RDF

In order to analyse the distribution of atoms, we can use radial distribution function to get.

LAMMPS is a good tool to calculate.

There, we can use these command to get the RDF

''''
**
compute myRDF ETTR_without_H rdf 500 1 2 2 1 cutoff 10.0

fix rdf1 all ave/time 10 100 1000 c_myRDF[*] file rdf_AB.txt mode vector
**
''''

However, the curve is not smooth due to the one timestep data.

Then I write this python to average the g(r) based on your all timestep.

If you have any questions, please feel free to ask me.
