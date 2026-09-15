# Local and global scope

message = "Global variable"


def show_scope():
    local_message = "Local variable"
    print(message)
    print(local_message)


show_scope()
print(message)
