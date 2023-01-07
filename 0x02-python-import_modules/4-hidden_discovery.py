#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for variable in dir(hidden_4):
        if variable[0] != '_' and variable[0] != '_':
            print(variable)
