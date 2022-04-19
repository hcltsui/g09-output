# g09-output

This repository is used to extract data from gaussian09 output file. 
There are two modules: g09_opt and g09_polar.

## g09_opt
This module is used to extract coordinates from gaussian09 optimization output file.
The code extracts the final section of standard orientation in the optimization. 
  
It can be used in command line:
```g09-opt filename``` or ```python -m g09_opt filename```
or in python:
```
from g09_opt import Opt

f = Opt(filename)
f.get_xyz()
```

## g09_polar
This module is used to extract data from gaussian09 polar output file.
The code extracts the polarization components and store in a directory under the same name as the output file. 
  
It can be used in command line:
```g09-polar filename``` or ```python -m g09_polar filename```
or in python:
```
from g09_polar import Polar

f = Polar(filename)
f.get_data()
```

## build and install
Download the repository and in the location where ```setup.cfg``` is run
```python -m build```
To install the module
```python -m pip install dist\g09_output-0.2.0-py3-none-any.whl```