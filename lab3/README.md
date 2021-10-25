## Lab3 - Web scraping - part I (static content).

For more info run:
```
python lab3.py --help
```

```
Required arguments:
  --url URL  Url of website

Optional arguments:
  -h, --help           show this help message and exit
  --div DIV  Div class we want to scrap
  --out OUT  Name of out file
```

```
Default values:

out - 'out'
div - None (print all page content)
```

# Examples:

```python lab3.py --url https://github.com/brokenpumpernickel/PwZN-2021Z-Live/blob/master/projects/project003.md --div 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'```

- Output .json file: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138725458-5f7f94d9-0e4a-4516-a1d9-d119edb8f457.png" alt="Output .json file"/>
</p>

- Output .html file: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/61660055/138725377-544a4adb-c497-4277-9614-a18fc3873ecf.png" alt="Output .html file"/>
</p>
