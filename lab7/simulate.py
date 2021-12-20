import numpy as np
import os
import imageio
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from scipy.signal import convolve2d
from PIL import Image, ImageDraw
from pathlib import Path
import random
import math
from numba import jit
from math import *

class Simulation:
    def __init__(self, size, j, b, h, steps, density, filename):
        self.path = os.getcwd()+"\\out"
        self.filename = filename
        self.file = None
    
        self.steps = steps
        self.j = j
        self.b = b
        self.h = h
        self.m = 0
        self.density = density
        self.size = size
        self.amount = size**2
        self.net = [1 for _ in range(int(self.amount*(density)))]+[-1 for _ in range(int(self.amount*(1-density)))]
        while True:
            if len(self.net) == self.amount:
                break
            self.net.append(random.choice([-1,1]))

        self.net = random.sample(self.net, self.amount)
        self.net = np.matrix([self.net[iterator*size:size+iterator*size] for iterator in range(size)])
        
        if "b" in self.h:
            self.h = self.h.replace("b", str(self.b))
        if "j" in self.h:
            self.h = self.h.replace("j", str(self.j))

        self.energy = self.calculateEnergy()

        if self.energy is None:
            print("Simulation initialization failed...")
            print("[ERROR] - Energy calculation failed, wrong H format.")
            del self
            return

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
                if self.net.sum() == self.amount:
                    progress.remove_task(task)
                    self.steps = iterator
                    break
                
                self.calculateMagnetization()
                self.generate_image(iterator)
                self.writeFile(iterator)
                self.iterate()
                progress.update(task, advance=1)

        self.finish()

    def iterate(self):
        for _ in range(self.amount):
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)

            self.net[x,y] *= -1
            after = self.calculateEnergy()
            delta = after-self.energy
            if delta > 0:
                if not (random.random() < math.e**(-self.b*delta)):
                    self.net[x,y] *= -1
                else:
                    self.energy = after
            else:
                self.energy = after

    def calculateEnergy(self):
        tmp = str(self.h)

        if "TOT" in tmp:
            tmp = tmp.replace('TOT', str(self.net.sum()))

        if "NB" in tmp:
            kernel = np.array([
                [0,1,0],
                [1,0,1],
                [0,1,0]
            ])
            out = convolve2d(self.net, kernel, 'same', 'wrap')
            out *= self.net
    
            tmp = tmp.replace('NB', f"({str(out.sum())})")

        try:
            return eval(tmp)/2
        except:
            return None

    def calculateMagnetization(self):
        self.magnetization = self.net.sum()/self.amount

    def writeFile(self, step):
        if self.file == None:
            Path(self.path).mkdir(parents=True, exist_ok=True)
            self.file = open(self.path+f"\\{self.filename}.txt", "w")
            self.file.write(f"Step  Magnetization   Energy\n")

        self.file.write(f"{step}    {self.magnetization}    {self.energy}\n")

    def generate_image(self, iterator):
        Path(self.path).mkdir(parents=True, exist_ok=True)    
 
        size = 1+self.size*4
        img = Image.new('RGB', (size, size), color = 'black')
        draw = ImageDraw.Draw(img)
        for i in range(self.size):
            for j in range(self.size):
                x = 1 if j == 0 else 1+j*3+(j)
                y = 1 if i == 0 else 1+i*3+(i)

                if self.net[i,j] == 1:
                    draw.rectangle((x, y,x+2, y+2), fill=(0, 0, 255))
                else:
                    draw.rectangle((x, y,x+2, y+2), fill=(255, 255, 255))

        img.save(self.path+f'\\{self.filename}{iterator}.png')

    def finish(self):
        print("Simulation finished!")
        print("Starting generating gif...")
        try:
            self.file.close()
        except:
            print("[WARNING] No images found to create gif...")
            return

        images = []
        for iterator in range(self.steps):
            images.append(imageio.imread(self.path+f'\\{self.filename}{iterator}.png'))
        imageio.mimsave(self.path+f'\\{self.filename}.gif', images, fps=20)
        print("Generating finished!")
        