## Lab1 - text file word counter

For more info run:
```
python lab1.py --help
```

```
Optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   Path to file - default text.txt
  --amount AMOUNT       Amount of displayed words - default 10
  --length LENGTH       Minimum length of word - default 0
  --start START         First color of gradient (eng. name or #HEX code) - default red
  --end END             Last color of gradient (eng. name or #HEX code) - default green
  --ignored IGNORED [IGNORED ...] - default []
                        List of ignored words
```

```
Default values:

filename - text.txt
amount - 10
length - 0
start - red
end - green
ignored - []
```

# Examples:

- `python .\lab1.py`
![image](https://user-images.githubusercontent.com/61660055/136831695-1d0c6bcc-1d77-42dd-ac85-e8e0424be24b.png)

- `python .\lab1.py --length 5 --amount 20 --start "#ffffff" --end "#8877CC"` (using color #HEX, **remember to use quotes**)
![image](https://user-images.githubusercontent.com/61660055/136834921-611b0f25-0708-484f-bc41-2d67cb8fa106.png)

- `python .\lab1.py --length 5 --amount 20 --start blue --end red --ignore przez gdzie potem` (using color names)
![image](https://user-images.githubusercontent.com/61660055/136835110-500ac745-1df5-489f-9091-e22a331e1531.png)
<!-- ![image](https://user-images.githubusercontent.com/61660055/136832056-acb38f5a-ebe0-4342-afa2-be6aeb49fc0c.png) -->
