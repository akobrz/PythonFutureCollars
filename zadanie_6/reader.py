import os.path
import sys
import csv
import json
import pickle

class Reader():
    def __init__(self, args):
        self.path_in, self.path_out = args[0], args[1]
        _, self.file_in = os.path.splitext(args[0])
        _, self.file_out = os.path.splitext(args[1])
        self.data = []
        self.args = args

    def loader(self):
        with open(self.path_in, "r") as f:
            if self.file_in == ".csv":
                self.data = [row for row in csv.reader(f)]
            if self.file_in == ".json":
                self.data = json.load(f)
        with open(self.path_in, "rb") as f:
            if self.file_in == ".pickle":
                self.data = pickle.load(f)

    def saver(self):
        if self.file_out == ".csv":
            with open(self.path_out, 'w', newline='') as f:
                csv.writer(f).writerows(self.data)
        if self.file_out == ".json":
            with open(self.path_out, 'w', newline='') as f:
                json.dump(self.data, f)
        if self.file_out == ".pickle":
            with open(self.path_out, "wb") as f:
                pickle.dump(self.data, f)

    def changer(self):
        for arg in self.args[2:]:
            y, x, w = arg.split(",")
            self.data[int(y)][int(x)] = w

if __name__ == "__main__":
    try:
        r = Reader(sys.argv[1:])
        r.loader()
        r.changer()
        r.saver()
    except FileNotFoundError:
        print(f"Input file not exists")
