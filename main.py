from database import conn
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

# connect to database server
# for more information, see database.py
conn.autocommit = True
cur = conn.cursor()

# create flask and api
app = Flask(__name__)
api = Api(app)

# get user information by email and username
@app.route('/user/<username>', methods=['GET'])
def route_user_get(username):
    cur.execute("SELECT * FROM `user` WHERE `username` = ?", (username, ))
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv: json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

# register user
# success: return user id
# error: return -1
@app.route('/user', methods=['PUT'])
def route_user_put():
    email = request.args.get('email', '')
    username = request.args.get('username', '')
    cur.execute("INSERT INTO `user`(`username`, `email`) VALUES (?, ?)", (username, email))
    return cur.warnings == 0 and route_user_get(email, username) or 'false'

# get statistics by id
# success: array with statistics
# error: empty array
@app.route('/statistics/<int:user_id>', methods=['GET'])
def route_statistics_get(user_id):
    cur.execute("SELECT * FROM `statistic` WHERE `user_id` = ?", (int(user_id),))
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv: json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


# run main
if __name__ == '__main__':
    # print(db.table_names())
    # print(app.url_map)
    app.run(port='5001', debug=True)