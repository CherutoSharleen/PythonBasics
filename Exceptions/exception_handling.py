def main():
    # open('test.txt', 'w').write('Hello, world!')
    file_name = 'jumanji.txt'
    try:
        open(file_name)
    except FileNotFoundError as err:
        print(f"The file:{file_name} could not be found \n", err)
    except IsADirectoryError :
        print(f"The file:{file_name} is not a file but a folder")
    #group exceptions
    except(BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")



if __name__ == '__main__':
    main()


