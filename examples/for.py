from htmotor import HTML

motor = HTML(prevent_xss=True)

print(motor.render_file(
    "for.htmo", 
    message="For Loop Test!"
))