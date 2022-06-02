#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{}: {}".format(i, sys.argv[i]))
