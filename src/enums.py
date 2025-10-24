from enum import Enum

class UserType(int, Enum):
    SuperUser = 1
    User = 2
    Watcher = 3
