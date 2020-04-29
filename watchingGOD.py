from watchgod import watch

def main():
    for changes in watch('.'):
        for item in changes:
            if (item[0] == 2):
                path_to_py = item[1]
                exec(open(path_to_py).read())

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
