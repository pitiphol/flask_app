import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dedupes_order(seq):
    # dedupes array to a dictionary, the key is first index we found for each element
    # and the value is the value of each element
    order_set = set()
    return {element:index for index,element in enumerate(seq) if not (element in order_set or order_set.add(element))}

@app.route('/interview_post', methods=['POST'])
def solution():
    if 'X' in request.form and 'A' in request.form:
        X = int(request.form.get('X'))
        A = eval(request.form.get('A'))
    # the fastest way to find earliest time in the array we need to avoid unnecessary loop
    # so first dedupes the array but keep the first index we found that elements
    # using dedupes_order()
    A = dedupes_order(A)
    # then we check if all leaves is already fall in position and return the maximum time last position leaf fall
    position_set = set(range(1,X+1))
    for key,value in A.items():
        position_set.discard(key)
        if len(position_set) == 0:
            return str(value)
    return '-1'

app.run()