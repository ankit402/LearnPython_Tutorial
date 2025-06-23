try:
    name = 'readmsde.txt'

    content = open(name, 'r')
    print(content.read())
except FileNotFoundError as ex:
    print(ex)
finally:
    if 'file' in locals() and not content.closed:
        content.close()
        print('file is closed')