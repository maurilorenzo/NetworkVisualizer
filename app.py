from flask import Flask, render_template
from utils import  generate_json_for_2d_graph, genereate_json_for_3d_graph

# creat flask app
app = Flask(__name__)


@app.route("/")
def index():
    """Landing page."""
    return render_template("index.html")

# 2d visualization
@app.route('/2d')
def twod():
    json_file = generate_json_for_2d_graph()
    return render_template("2d.html", json_file = json_file)

# 3d visualization
@app.route('/3d')
def threed():
    graphJSON =  genereate_json_for_3d_graph()
    return render_template('3d.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)
