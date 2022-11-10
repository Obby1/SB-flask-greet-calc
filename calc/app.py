# Put your app in here.
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/add')
# def do_add(a, b):
def do_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)


@app.route('/mult')
def do_mult():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def do_div():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer = div(a,b)
    return str(answer)

"""Basic math operations."""

def add(a, b):
    """Add a and b."""
    
    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b

def mult(a, b):
    """Multiply a and b."""

    return a * b

def div(a, b):
    """Divide a by b."""

    return a / b


# python3 -m unittest test.py

### PART TWO
# Further Study
# You probably have a lot of code duplication in your calc routes, given that you’re doing such similar things in each.

# Make a single route/view function that can deal with 4 different kinds of URLs:

# /math/add
# /math/sub
# /math/mult
# /math/div
# You can write this in one function with one route by using a route parameter for the actual operation (“add”, “sub”, etc).

# As an extra-bonus, see if you can find a way to do this in the route without a whole series of if/elif statements. One good way is to use a dictionary to map operation names to the functions that do the underlying math.

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)