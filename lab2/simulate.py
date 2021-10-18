class Simulation:
    def __init__(self, size, j, b, h, steps, density, filename):
        self.steps = steps
        self.size = size
        self.j = j
        self.b = b
        self.h = h
        self.density = density
        self.filename = filename
        print("Simulation initialized...")

    def __del__(self):
        print("Simulation ended...")

    def start(self):
        print("Starting simulation...\n")
        from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn
        
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
                self.generate_image(progress.tasks[0].completed)
                progress.update(task, advance=1)

        print("Simulation finished!")

    def generate_image(self, iterator):
        from PIL import Image
        from pathlib import Path
        import os

        cwd = os.getcwd()
        Path(cwd+"/out").mkdir(parents=True, exist_ok=True)    
 
        img = Image.new('RGB', (60, 30), color = 'red')
        img.save(cwd+f'/out/{self.filename}{iterator}.png')
