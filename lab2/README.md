## Lab2 - simulation / visualization of the Ising 2D model using the Monte Carlo method.

For more info run:
```
python lab2.py --help
```

```
Required arguments:
  --netsize NETSIZE    Size of net
  --jval JVAL          Value of J
  --bval BVAL          Value of Beta
  --heq HEQ            Equation for H (use TOT, NB, b, j values)
  --steps STEPS        Steps of simulation

Optional arguments:
  -h, --help           show this help message and exit
  --density DENSITY    Initial spin density
  --filename FILENAME  Name of out images
```

```
Default values:

density - 0.5
filename - 'step'
```


# Examples:

```python lab2.py --netsize 60 --jval 2 --bval 100000000 --heq '-j*NB - 0*TOT' --steps 100 --density 0.5 --filename test```
 
- Generated gif: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138491247-781a0a18-6e9e-4185-8658-adad6411ac46.gif" alt="Generated gif"/>
</p>

- Output directory with files: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138491200-6acef225-4d9f-4ef6-b10a-d60689f6762c.png" alt="Output directory with files"/>
</p>


- Console output with progress bar:
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138491290-eec09f12-44ab-4049-92b5-d8aa7381b2b7.png" alt="Console output with progress bar"/>
</p>

- Out .txt file with data for next steps:
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138491361-80ca6733-3db3-4c98-af30-3e5ca24369ce.png" alt="Out .txt file with data for next steps:"/>
</p>

