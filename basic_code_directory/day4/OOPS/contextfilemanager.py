# "Create a class named `FileManager` that implements the context manager protocol
# to open and close a file. Use this class to read the contents of a file.\n",


class FileManager:
    #To initialize attributes (variables) of a class.
    #The __init__ method in Python is a constructor
    def __init__(self, filename):
        try:
            self._filename = filename
            self._file = None
            print(f'FileManager Started {self._filename}')
        except FileNotFoundError:
            print(f'File {self._filename} not found')

    def open(self):
        try:
            with open(self._filename, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError as ex:
            print(f'File {self._filename} {ex}')

    def close(self):
       try:
           if self._file and not self._file.closed:
               self._file.close()
               print(f'File has been closed: {self._filename}')
           else:
               print("File is not open or already closed.")
       except FileNotFoundError:
           print("File not found.")

f1=FileManager('text.txt')
f1.open()
f1.close()
