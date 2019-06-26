import sys


def main():
    args = sys.argv[1:]
    for x in args:
        if x == ">":
            outfile = args[x+1]
            _write_data(indata, outfile)
            outfile.close()
            infile.close()
            break
        infile = open(x)
        indata = infile.read()
        print(indata)


def _write_data(indata, outfile ):
    outfile = open(outfile, 'w')
    outfile.write(indata)



if __name__ == "__main__":
    main()