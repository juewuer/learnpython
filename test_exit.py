import atexit
def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

@atexit.register
def goodbye1():
    print("You are now leaving the Python sector. late early")

atexit.register(goodbye, 'Tom', 'unnice')

atexit.register(goodbye, adjective='nice', name='Donny')

@atexit.register
def goodbye2():
    print("You are now leaving the Python sector. late ")