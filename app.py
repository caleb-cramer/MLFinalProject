# we are going to use Flask, a micro web framework
import os
import pickle

from flask import Flask
from flask import render_template
from flask import request, jsonify, redirect

# make a Flask app
app = Flask(__name__)

# we need to add two routes (functions that handle requests)
# one for the homepage
@app.route("/", methods=["GET"])
def index():
    # return content and a status code
    return "<h1>Welcome to my App</h1>", 200

@app.route("/predict", methods=["GET"])
def predict():
    # DATE,TMAX,TMIN,RAIN for seattle
    date = request.args.get("att0", "")
    t_Max = request.args.get("att1", type=float)
    t_Min = request.args.get("att2", type=float)
    # rain = request.args.get("att3", "")

    prediction = predict_rain_well([date, t_Max, t_Min])

    if prediction is not None:
        result = {"prediction": prediction}
        return jsonify(result), 200
    else:
        return jsonify([date, t_Max, t_Min]), 400

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Attribute":
        attribute_index = header.index(tree[1])
        instance_value = instance[attribute_index]
        # now I need to find which "edge" to follow recursively
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == instance_value:
                # we have a match!! recurse!!
                return tdidt_predict(header, value_list[2], instance)
    else: # "Leaf"
        return tree[1] # leaf class label

def predict_rain_well(instance):
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()

    try: 
        return tdidt_predict(header, tree, instance) # recursive function
    except:
        return None




if __name__ == "__main__":

    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port) # TODO: set debug to False for production
    # by default, Flask runs on port 5000