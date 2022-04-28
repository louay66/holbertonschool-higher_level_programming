#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mod = dir(hidden_4)
    for elm in mod:
        if elm[0] != '_':
            print(elm)
