command = "new_command"
flag = "-f"
argument = "hello"

match command, flag:
    case "print" | "write" | "say", "console":
        print(argument)
    case "decorate", _ as f:
        print(f, argument)
    case _:
        print("error")