import log, logging.config, sys

rez = []

a = [1,1,1]
b = [2,2,2,2]

rez.append(a)
rez.append(b)

a =["to", "t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08", "t09", "t0A","do", "t0B", "d1", "t0C", "t0D", "t0E", "t0F", "zip"]


if __name__ == '__main__':
    for i in a:
        if "t" in i:
            print("t")
        elif "d" in i:
            print("d")
        elif "zip" in i:
            print("zip")
