from flask import Flask, render_template, request, make_response, jsonify
#import flask class

app = Flask(__name__)

# #create a route for index/ homepage
# # q= - setting query paramater 
# @app.route("/")
# def index():
#     query_param = request.args.get("q")
#     return render_template("index.html", query=query_param)


# #example of a post method
# @app.route("/login", methods=["POST"])
# def login():
#     names = ["frae", "fi", "miguel", "sheryl", "kim"]
#     name = request.json["name"]
    
#     if name in names:
#         return make_response(f"{name} is logged in", 200)

#     return make_response(f"Unsuccessful", 404)

# #create another route for /about
# @app.route("/about")
# def about():
#     return f"This is the about page"

# #example of a dynamic route - could be /frae, /fi but not /about since already defined
# #use jsonify (see imports) to 
# @app.route("/<name>")
# def show(name):
#     user = {
#         "name": name
#     }

#     return make_response(jsonify(user), 200)

#     #return make_response(render_template("show.html", name=name))

# students = [
#     "john", "mary", "clare", "leon"
# ]

# @app.route("/students")
# def show_students():
#     return render_template("show_students.html", students=students)

# # #specifying data type
# # @app.route("/students/<int:id>")
# # def student(id):
# #     return f"The student ID is {id}"

# # #specifying another data type
# # @app.route("/students/<string:name>")
# # def student_name(name):
# #     return f"The student name is {name}"   

if __name__ == "__main__":
    #debug here will auto refresh/ hot reload
    app.run(port=4000, debug=True)


