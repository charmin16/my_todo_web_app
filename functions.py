FILEPATH = 'todo.txt'


def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print('Powerful beyond measures')
# The above print statement will also be executed when another file imports this module and
# runs it. If you don't want it to run elsewhere apart from the script here directly, then, do as shown below

# if __name__ == '__main__':
#   print('Hello Somebody')
#   print('President of the United States')
