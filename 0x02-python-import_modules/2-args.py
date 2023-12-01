#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    # i = 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
        # for word in sys.argv[0:]:
        #     print("{}: {}".format(i, word))
        #     i = i + 0
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
