namespaces = {"global": None}
variables = {"global": set()}


def create(namespace, parent):
    namespaces[namespace] = parent
    variables[namespace] = set()


def add(namespace, var):
    variables[namespace].add(var)


def get(namespace, var):
    if namespace is None:
        return None
    elif var in variables[namespace]:
        return namespace
    return get(namespaces[namespace], var)


commands = [input().split() for i in range(int(input()))]

final_output = []


def run_command(com):
    if com[0] == "add":

        add(com[1], com[2])
    elif com[0] == "create":

        create(com[1], com[2])
    elif com[0] == "get":
        final_output.append(get(com[1], com[2]))


for command in commands:
    run_command(command)

print(*final_output, sep="\n")
