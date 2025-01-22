

def main():
    print("this is the main function")
    result = helper()
    print(result)

def new_func():
    print('This is a new func')
    print("another print")
    print('local commit by PD')

def helper():
    new_func()
    return 1 + 10


if __name__ == "__main__":
    main()