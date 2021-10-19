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

```python lab2.py --netsize 100 --jval 2 --bval 3 --heq '-j*NB - b*TOT' --steps 10 --density 0.57 --filename test```
 
- Generated gif: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/137857795-8ac9b333-2e67-45d4-a2b5-17ff5939b456.gif" alt="Generated gif"/>
</p>

- Output directory with files: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/137857372-fa1f5f8d-8d15-42e6-ab8a-0d4d2c6c2cb9.png" alt="Output directory with files"/>
</p>

- Console output with progress bar:
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/137857193-6d527b95-a7f2-4974-871f-f4f941933df5.png" alt="Console output with progress bar"/>
</p>

- Out .txt file with data for next steps:
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/137857966-9d3c2277-06f1-4ca7-a7c5-4558e6da6ce7.png" alt="Out .txt file with data for next steps:"/>
</p>

