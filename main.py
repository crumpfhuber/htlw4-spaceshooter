from database import conn
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

# connect to database server
# for more information, see database.py
cur = conn.cursor()

# create flask and api
app = Flask(__name__)
api = Api(app)

# get user by id
@app.route('/user/<int:user_id>', methods=['GET'])
def route_user_get(user_id):
    cur.execute("SELECT * FROM `user` WHERE `id` = ?", (int(user_id),))
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv: json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

# get statistics by id
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