import os
import pickle as pkl


class FileWriter:

    def __init__(self, path):
        if self._check_path(path):
            print("Path  valid")
            self._path = path
            self.file = None
            self.file_exists = os.path.exists(self._path)
        else:
            print("Path not valid")
            raise Exception("Path not valid")

    def _check_path(self, path):
        if os.path.isfile(path):
            return True
        if os.path.isdir(path[:path.rfind('/')]):
            return True
        return False

    @property
    def path(self):
        return self._path

    @path.deleter
    def path_deleter(self):
        del self._path

    @path.setter
    def path(self, new_path):
        if self._check_path(new_path):
            self._path = new_path
            self.file_exists = os.path.exists(self._path)
        else:
            raise Exception('The specified directory does not exist')


    def __enter__(self):
        if self.file_exists:
            self.file = open(self.path, 'a')
        else:
            self.file_exists = True
            self.file = open(self.path, 'w')
        return self.file


    def __exit__(self, *args):
        self.file.close()


    def print_file(self):
        if self.file_exists:
            with open(self.path) as file:
                print(file.read())


    def write(self, some_string):
        with open(self._path, 'a' if self.file_exists else 'w') as file:
            file.write(some_string + '\n')
            self.file_exists = True


    def save_yourself(self, file_name):
        with open(file_name,'wb') as file:
            pkl.dump(FileWriter(self._path), file)


    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as file:
            return (pkl.load(file))
        return FileWriter(data['path'])

