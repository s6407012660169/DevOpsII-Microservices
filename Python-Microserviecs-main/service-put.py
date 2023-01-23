from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
#import jwt
import data_user as us

app = Flask(__name__)


@app.route('/username', methods=['PUT'])
def update_user():
    user = request.form.get('user')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]

    if data:
        us.update_user(user,passwd,name)
        return jsonify({'message': 'Update successfully'}), 200
    else:
        return jsonify({'message': 'Fail to update'}), 401
    # for i in range(len(_user)):
    #     if _user[i]['user'] == user:
    #         _user[i]['user'] = new_name
    #         return jsonify(_user)
    # return jsonify({"message": "User not found."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug = True)

