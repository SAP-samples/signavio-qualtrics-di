# For more information about the Python3Operator, drag it to the graph canvas, right click on it, and
# click on "Open Documentation".

# To uncomment the snippets below you can highlight the relevant lines and press Ctrl+/
# on Windows and Linux or Cmd+/ on Mac.

# # Basic Example 1: Count inputs so far and send on output port (port type string)
# # When using the snippet below make sure you create an output port of type string
# counter = 0
#
# def on_input(data):
#     global counter
#     counter += 1
#     api.send("output", str(counter))
#
# api.set_port_callback("input", on_input)


# # Basic Example 2: Count inputs so far and send on output port (port type int64)
# # When using the snippet below make sure you create an output port of type int64
# counter = 0
#
# def on_input(data):
#     global counter
#     counter += 1
#     api.send("output", counter)
#
# api.set_port_callback("input", on_input)


# # Basic Example 3: Identity operator.
# # When using the snippet below make sure you create input and output ports of the same type.
# def on_input(data):
#     api.send("output", data)
#
# api.set_port_callback("input", on_input)


# # Basic Example 4: Sum both inputs and output result.
# # When using the snippet below make sure you create input and output ports of the same type and
# # that the corresponding python types can be added with the `+` operator. Example of valid
# # port types for this snippet are: string, int64, and float64.
# def on_input(data1, data2):
#     api.send("output", data1 + data2)
#
# api.set_port_callback(["input1", "input2"], on_input)


# # Generators
# # When using the snippet below make sure you create an output port of type int64
# counter = 0
#
# def gen():
#     global counter
#     for i in range(0, 3):
#         api.send("output", counter)
#         counter += 1
#
# api.add_generator(gen)
# api.add_generator(gen)  # Adding the generator twice will make the function be executed twice.


# # Timer
# # When using the snippet below make sure you create an output port of type int64
# counter = 0
#
# def t1():
#     global counter
#     api.send("output", counter)
#     counter += 1
#
# api.add_timer("1s", t1)

# # Timer
# # When using the snippet below make sure you create an output port of type string
# counter = 0
#
# def t2():
#     global counter
#     api.send("output", str(counter))
#     counter += 1
#
# api.add_timer("1s", t2)


# # Shutdown
# counter = 0
#
# def on_input(data):
#     global counter
#     counter += 1
#
# api.set_port_callback("input", on_input)
#
# def shutdown1():
#     print("shutdown1: %d" % counter)
#
# def shutdown2():
#     print("shutdown2: %d" % counter)
#
# api.add_shutdown_handler(shutdown1)
# api.add_shutdown_handler(shutdown2)
