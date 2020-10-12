from flask import Flask, render_template, request, jsonify, redirect



######## INITIATE FLASK APP #########################
app= Flask(__name__)

@app.route ("/home")
@app.route("/")
def welcome():
    return render_template('index.html')
# @app.route("/Skin")
# def graph():

#     return  render_template('Skin_index_copy.html')

if __name__ == '__main__':
    app.run(debug=True)