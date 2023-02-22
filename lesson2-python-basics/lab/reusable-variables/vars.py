import sys


def hello(name):
    print('Hello ' + name)


name = sys.argv[1]
hello(name)


# # local variable
# def hello():
#     name = "Pius"
#     print("Hello " + name)

#     hello()


# # global variable
# name = "Pius"

# def goodbye():
#     print('Goodbye ' + name)

#     goodbye()
