from json import load, dump

# fn - file name
def read_json(fn):
    jsondata = []
    try:
        with open(fn, "r") as f:
            jsondata = load(f)
        f.close()
    except FileNotFoundError:
        with open(fn, "w") as f:
            dump(jsondata, f)
        f.close()
    return jsondata


# fn - file name
def write_json(fn, jsondata):
    try:
        with open(fn, "w") as f:
            dump(jsondata, f)
        f.close()
    except FileNotFoundError:
        pass
    return jsondata


# fn - file name
# a - agent file to append in json file
def add2json(fn, a):
    jsondata = read_json(fn)
    if len(jsondata) > 0:
        if a not in jsondata:
            jsondata.append(a)
            with open(fn, "w") as f:
                dump(jsondata, f)
            f.close()
    else:
        jsondata.append(a)
        with open(fn, "w") as f:
            dump(jsondata, f)
        f.close()
    return