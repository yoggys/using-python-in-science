from collections import Counter
from colour import Color
from ascii_graph import Pyasciigraph
import matplotlib.pyplot as plt
import numpy as np
import argparse
import re
import os


def countWords(word_list, limit, min_length, ignored):
    word_list = [re.sub("[^0-9a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", "", word).lower() for word in word_list]
    count = dict(Counter(word_list))
    for key in list(count.keys()):
        if key == '' or len(key) < min_length or key in ignored:
            del count[key]

    return zip(*sorted(count.items(), key=lambda item: item[1], reverse=True)[0:limit])

def initParser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--filename', help="Path to read file from", type=str, default=f"{os.path.dirname(os.path.abspath(__file__))}"+"\\text.txt")
    parser.add_argument('--amount', help="Amount of displayed words",type=int, default=10)
    parser.add_argument('--length', help="Minimum length of word",type=int, default=0)
    parser.add_argument('--start', help="First color of gradient", type=str, default="red")
    parser.add_argument('--end', help="Last color of gradient", type=str, default="green")
    parser.add_argument('--ignored', help="List of ignored words",nargs='+', type=list, default=[])

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    f = open(args.filename, "r", encoding="utf-8")
    word_list = f.read().strip().split()
    labels, values = countWords(word_list, args.amount, args.length, ["".join(arg) for arg in args.ignored])

    labels = np.array(labels)
    values = np.array(values)
    
    red = Color(args.start)
    colors = list(red.range_to(Color(args.end), args.amount))
    colors = [color.rgb for color in colors]

    graph = Pyasciigraph()
    graph = graph.graph('Words histogram', [(str(labels[i]), values[i]) for i in range(len(values))])

    for index in range(len(graph)):
        if graph[index].startswith('█'):
            print("\033[38;2;{};{};{}m{}".format(int(colors[index-2][0]*255), int(colors[index-2][1]*255), int(colors[index-2][2]*255), graph[index]))
        else:
            print(graph[index])

    #reset to default color
    print('\033[39m')

    index = np.arange(len(labels))
    plt.bar(index, values, color=colors)
    plt.xticks(index + 0.1, labels)
    plt.show()