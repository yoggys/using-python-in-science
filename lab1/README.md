## Lab1 - text file word counter

For more info run:
```
python lab1.py --help
```

```
optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   Path to read file from
  --amount AMOUNT       Amount of displayed words
  --length LENGTH       Minimum length of word
  --start START         First color of gradient
  --end END             Last color of gradient
  --ignored IGNORED [IGNORED ...]
                        List of ignored words
```

Examples:

- `python .\lab1.py`
![image](https://user-images.githubusercontent.com/61660055/136831695-1d0c6bcc-1d77-42dd-ac85-e8e0424be24b.png)

- `python .\lab1.py --length 5 --amount 20 --start blue --end green`
![image](https://user-images.githubusercontent.com/61660055/136831877-03b5ee94-b7ab-499b-ab98-887ac55cd74b.png)

- `python .\lab1.py --length 5 --amount 20 --start blue --end red`
![image](https://user-images.githubusercontent.com/61660055/136832056-acb38f5a-ebe0-4342-afa2-be6aeb49fc0c.png)