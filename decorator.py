
def log(func):
    def wrapper():
        print("before calling",func.__name__)
        func()
        print("ending calling",func.__name__)
    return wrapper()
@log
def hello():
    print("hello")

if __name__=="__main__":
    hello()