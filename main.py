

def main():
    print("this is the main function")
    result = helper()
    print(result)

def new_func():
    print('This is a new func')
    print("changed this print")
    another_func()

def another_func():
    print("YAY")

def helper():
    new_func()
    return 1 + 10


if __name__ == "__main__":
    main()