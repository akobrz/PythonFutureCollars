from os.path import abspath, splitext, dirname, exists
from os import listdir
import sys
import csv
import json
import pickle

class Base:
    def __init__(self, args):
        self.path_in, self.path_out = abspath(args[0]), abspath(args[1])
        self.root_in, self.ext_in = splitext(self.path_in)
        self.root_out, self.ext_out = splitext(self.path_out)
        self.data = []
        self.args = args

    def __str__(self):
        return str(self.data)


class ReaderCsv(Base):
    def loader(self):
        with open(self.path_in, "r") as f:
            if self.ext_in == ".csv":
                self.data = [row for row in csv.reader(f)]

    def saver(self):
        if self.ext_out == ".csv":
            with open(self.path_out, 'w', newline='') as f:
                csv.writer(f).writerows(self.data)

class ReaderJson(Base):
    def loader(self):
        with open(self.path_in, "r") as f:
            if self.ext_in == ".private":
                self.data = json.load(f)

    def saver(self):
        if self.ext_out == ".private":
            with open(self.path_out, 'w', newline='') as f:
                json.dump(self.data, f)

class ReaderPickle(Base):
    def loader(self):
        with open(self.path_in, "rb") as f:
            if self.ext_in == ".pickle":
                self.data = pickle.load(f)

    def saver(self):
        if self.ext_out == ".pickle":
            with open(self.path_out, "wb") as f:
                pickle.dump(self.data, f)


class Reader(ReaderCsv, ReaderJson, ReaderPickle):

    def loader(self):
        ReaderCsv.loader(self)
        ReaderJson.loader(self)
        ReaderPickle.loader(self)

    def saver(self):
        ReaderCsv.saver(self)
        ReaderJson.saver(self)
        ReaderPickle.saver(self)

    def changer(self):
        for arg in self.args[2:]:
            y, x, w = arg.split(",")
            self.data[int(y)][int(x)] = w

    def print_dir_in(self):
        print(dirname(self.path_in))


if __name__ == "__main__":
    r = Reader(sys.argv[1:])
    if not exists(dirname(r.path_in)):
        print(f"Input directory does not exist")
    elif not exists(r.path_in):
        print(f"Input file does not exist, but in input directory may be some other files:")
        print(listdir(dirname(r.path_in)))
    elif not exists(dirname(r.path_out)):
        print(f"Output directory does not exist")
    else:
        r.loader()
        r.changer()
        print(r)
        r.saver()
