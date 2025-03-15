import argparse

cli = argparse.ArgumentParser(description="Simple CLI math")

cli.add_argument("command", choices=["add", "sub", "mul", "div"], help = "Operation to perform")
cli.add_argument("num", type = float, nargs = "?", default = 0, help="Num 1 for operations")
cli.add_argument("tnum", type = float, nargs = "?", default = 1, help="Num 2 for operations")

arg = cli.parse_args()

if arg.command == "add":
    print(f"Sum is {arg.num + arg.tnum}")
if arg.command == "sub":
    print(f"Sum is {arg.num - arg.tnum}")
if arg.command == "mul":
    print(f"Sum is {arg.num * arg.tnum}")
if arg.command == "div":
    print(f"Sum is {arg.num / arg.tnum}")