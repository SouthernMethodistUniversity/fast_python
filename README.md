# Tools for Developing Fast Python Code

## Center for Scientific Computation (CSC)

* Maintains our primary shared resource for research computing, ManeFrame II (M2),
  in collaboration with OIT
* Provides research computing tools, support, and training to all faculty, staff,
  and students using research computing resources
  [www.smu.edu/csc](https://www.smu.edu/csc) has documentation and news
* [help@smu.edu](mailto:help@smu.edu) or
  [rkalescky@smu.edu](mailto:rkalescky@smu.edu) for help
  
## CSC Workshop Series

Date          Workshop
------------- -------------------------------------------------------------
January 21    M2 Introduction
January 28    Introduction to LAPACK and BLAS
February 4    Text Mining with Python on M2 (Lead by Dr. Eric Godat)]
February 11   Using the New HPC Portal
February 18   Using GitHub
February 25   Writing Portable Accelerator Code with KOKKOS, RAJA, and OCCA
March 3       M2 Introduction
March 10      Introduction to Parallelization Using MPI
March 17      No Workshop Spring Break
March 24      Writing High Performance Python Code
March 31      Creating Portable Environments with Docker and Singularity
April 7       M2 Introduction
April 14      Introduction to Parallelization Using OpenMP and OpenACC
April 21      Profiling Applications on M2
April 28      Improving Code Vectorization
                                                                                              
## Using This Notebook on ManeFrame II (M2)

1.  Go to [hpc.smu.edu](https://hpc.smu.edu/).
2.  Sign in using your SMU ID and SMU password.
3.  Select "JupyterLab from the "Interactive Apps" drop-down menu.
4.  Select options required for your JupyterLab instance. These options are the
    same as those requested via a standard Slurm script on M2. For this tutorial:
    beginning with the "Partition" field the values should be: "htc", 4, 1, 2, 0,
    6.
5.  Select "Launch" Wait for the job to start on M2. When the job starts
    a new button "Connect to JupyterLab" button will appear.
6.  Select "Connect to JupyterLab" The JupyterLab graphical interface will be
    presented and running on the M2 resource requested.
7.  From "Launcher" tab select "Terminal".
8.  Type ``git clone
    https://github.com/SouthernMethodistUniversity/Text_Mining_Python.git`` and
    press "Enter"
9.  In the file browser on the left double-click "Text_Mining_Python" and then
    double click "text_mining_python.ipynb"

