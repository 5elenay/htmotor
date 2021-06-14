from htmotor import HTML

motor = HTML(prevent_xss=True)

print(motor.render_file(
    "variable.htmo", 
    test="Hello!", # Normal Variable
    test2=("<h1>test 123</h1>", False) # Disable XSS Preventation.
))