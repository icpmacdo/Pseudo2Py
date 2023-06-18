def pseudo_to_python(pseudo_code):
    python_code = ""
    lines = pseudo_code.split("\n")
    for line in lines:
        if line.startswith("Create a function"):
            function_name = line.split(" ")[3]
            python_code += "def " + function_name + "():\n"
        elif line.startswith("Print"):
            to_print = line[6:]
            python_code += "\tprint('" + to_print + "')\n"
        elif line.startswith("Set"):
            parts = line.split(" ")
            python_code += "\t" + parts[1] + " = " + parts[3] + "\n"
        elif line.startswith("Add"):
            parts = line.split(" ")
            python_code += "\t" + parts[1] + " = " + parts[1] + " + " + parts[3] + "\n"
    return python_code

pseudo_code = """Create a function add_numbers
Set x to 5
Set y to 10
Add x and y
Print x"""

print(pseudo_to_python(pseudo_code))

