import logging


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Goood morning ")
#         fx(*args, **kwargs)
#         print("have a nice day")
#     return mfx
#
# #DECORATOR
# @greet
# def hello():
#     print("Hello World")
#
# #ARGUMENT DECORATOR
# @greet
# def sum(a,b):
#     print(a+b)
# #ARGUMENT FUNC NEED ARGUMENT DECORATOR
# #CALLING FUNCTIONS
# sum(1,2)
# hello()

def log_function_call(func):
        def decorated(*args, **kwargs):
            logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned {result}")

            return result
        return decorated

@log_function_call
def add(c,d):
    print(c+d)

add(54,56)