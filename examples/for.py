from htmotor import HTML

motor = HTML(prevent_xss=True)

print(motor.render_file(
    "test.html", 
    message="For Loop Test!"
    )
)