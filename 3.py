print ("3.1")
def right_justify(s):
    return (70-len(s))*" "+s
print(right_justify("monty"))

print("3.2")
def do_twice(f):
    return f()+" "+f()
def print_spam():
    return "spam"
print(do_twice(print_spam))
exit(0)

