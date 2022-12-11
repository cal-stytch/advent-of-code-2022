from typing import List

class Directory:
    def __init__(self, name, parent) -> None:
        self.contents: List[Directory| File] = []
        self.name: str = name
        self.parent = parent
        self._size = -1
    
    def cd(self, dir_name):
        for c in self.contents:
            if isinstance(c, Directory) and c.name == dir_name:
                return c

        raise Exception(f'Folder {dir_name} not found in {self.name}')
    
    def get_size(self) -> int:
        if self._size != -1: return self._size

        if (len(self.contents) == 0):
            self._size = 0
            return self._size
        val = 0

        for item in self.contents: 
            val += item.get_size()
        
        self._size = val
        return self._size

    

    def __str__(self) -> str:
        return f'DIR: {self.name}'


class File: 
    def __init__(self, name, size) -> None:
        self.name: str = name
        self.size: int = size

    def get_size(self) -> int:
        return self.size

    def __str__(self) -> str:
        return f'FILE: {self.name} : {self.size}'

class Command:
    def __init__(self, i: str, o: List[str]) -> None:
        self.input = i
        self.cmd = i.split(' ')[0]
        self.args = i.split(' ')[1:]
        self.output = o 
    
    def __str__(self) -> str:
        return f'{self.cmd} {self.args} -> {self.output}'


class FileSystem:
    def __init__(self):
        self.root = Directory('/', None)
        self.curr = self.root
    
    def cd(self, dir_name):
        if (dir_name == '/'):
            self.curr = self.root
        elif (dir_name == '..'):
            if self.curr.parent == None:
                raise Exception('Root level directory') 
            self.curr = self.curr.parent
        else:
            self.curr = self.curr.cd(dir_name)
    
    def ls(self):
        print(f'LISTING CONTENTS OF {self.curr.name}')
        for c in self.curr.contents:
            print(str(c))
    
    def touch(self, file_name, size):
        self.curr.contents.append(File(file_name, int(size)))
    
    def mkdir(self, dir_name):
        self.curr.contents.append(Directory(dir_name, self.curr))

        



file_name = 'input.txt'
# file_name = 'test.txt'
f = open(file_name)
contents = f.read()
input_output = contents.split('\n')

# Build command objects from input
commands = []
ib = ''
ob = []
for io in input_output:
    if (io.startswith('$')):
        if (ib != ''):
            commands.append(Command(ib.split(' ', 1)[1], ob))
        ib = io
        ob = []
    else:
        ob.append(io)
commands.append(Command(ib.split(' ', 1)[1], ob))
# for c in commands:
#     print(c) 

# Convert the command objects to the file structure
fs = FileSystem()
for c in commands:
    if (c.cmd == 'cd'):
        fs.cd(c.args[0])
    if (c.cmd == 'ls'):
       
    # Create the files we find in the directory
        for o in c.output:
            meta = o.split()[0]
            name = o.split()[1]

            if meta == 'dir':
                fs.mkdir(name)
            else:
                fs.touch(name, meta)


# CD to root and recursively search through directories
fs.cd('/')
TOTAL_DISK_SPACE = 70000000
UPDATE_SPACE_REQ = 30000000

used_space = fs.curr.get_size()
unused_space = TOTAL_DISK_SPACE - used_space
req_to_delete = UPDATE_SPACE_REQ - unused_space

def get_best_dir(dir:Directory, curr_best_dir):

    

    best_dir = curr_best_dir
    if dir.get_size() >= req_to_delete and dir.get_size() < curr_best_dir.get_size():
        best_dir = dir

    for c in dir.contents:
        if isinstance(c, Directory):
            if get_best_dir(c, best_dir).get_size() < best_dir.get_size():

                best_dir = get_best_dir(c, curr_best_dir)

    
    return best_dir

bd = get_best_dir(fs.root, fs.root)

print(f'NEED TO DETELE AT LEAST: {req_to_delete}')
print(f'DELETING {bd.name} with size {bd.get_size()}')
