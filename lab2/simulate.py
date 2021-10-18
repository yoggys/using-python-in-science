import numpy as np
import os
import imageio
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from PIL import Image, ImageDraw
from pathlib import Path
import random
import math

class Simulation:
    def __init__(self, size, j, b, h, steps, density, filename):
        self.path = os.getcwd()+"/out"
        self.size = size
        self.amount = size**2
        self.net = [1 for _ in range(int(self.amount*(density)))]+[-1 for _ in range(int(self.amount*(1-density)))]
        while True:
            if len(self.net) == self.amount:
                break
            self.net.append(random.choice([-1,1]))

        self.net = random.sample(self.net, self.amount)
        self.net = [self.net[iterator*size:size+iterator*size] for iterator in range(size)]

        self.steps = steps
        self.j = j
        self.b = b
        self.h = h
        self.m = 0
        self.density = density
        self.filename = filename
        print("Simulation initialized...")

    def __del__(self):
        print("Simulation ended...")

    def start(self):
        print("Starting simulation...\n")
        
        with Progress(
            "{task.completed} of {task.total}\n",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            '| Elapsed:',
            TimeElapsedColumn(),
            '| Remaining:',
            TimeRemainingColumn()
        ) as progress:
            task = progress.add_task(None, total=self.steps)
            while not progress.finished:
                iterator = progress.tasks[0].completed
                self.calculateMagnetization(iterator)
                self.iterate()
                
                self.generate_image(iterator)
                progress.update(task, advance=1)

        self.finish()

    def iterate(self):
        for _ in range(self.amount):
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)

            before = self.calculateEnergy()
            self.net[x][y] *= -1
            after = self.calculateEnergy()
            delta = after-before
            if not (delta < 0):
                if not (random.random() < math.e**(-self.b*delta)):
                    self.net[x][y] *= -1

    def calculateEnergy(self):
        return 0

    def calculateMagnetization(self, step):
        pass

    def generate_image(self, iterator):
        Path(self.path).mkdir(parents=True, exist_ok=True)    
 
        size = 1+self.size*4
        img = Image.new('RGB', (size, size), color = 'black')
        draw = ImageDraw.Draw(img)
        for i in range(self.size):
            for j in range(self.size):
                x = 1 if j == 0 else 1+j*3+(j)
                y = 1 if i == 0 else 1+i*3+(i)

                if self.net[i][j] == 1:
                    draw.rectangle((x, y,x+2, y+2), fill=(0, 0, 255))
                else:
                    draw.rectangle((x, y,x+2, y+2), fill=(255, 255, 255))

        img.save(self.path+f'/{self.filename}{iterator}.png')

    def finish(self):
        print("Simulation finished!")

        images = []
        for iterator in range(self.steps):
            images.append(imageio.imread(self.path+f'/{self.filename}{iterator}.png'))
        imageio.mimsave(self.path+f'/{self.filename}.gif', images)