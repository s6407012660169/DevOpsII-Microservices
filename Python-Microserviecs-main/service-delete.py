from flask import Flask, request, jsonify
import data_user as us
import datetime

app = Flask(__name__)
username = us.user_name()

# @app.route('/username/<user>', methods = ['DELETE'])
# def user(user):
#     _user = us.find_username(user)
#     if _user is None:
#         return jsonify({'error': 'Username does not exist.'}), 404
#     else:
#         user.remove(_user[0]) 
#         return jsonify({"username deleted succuessfully"}) ,200
    
    # data = [x for x in username if x['user'] != user]
    # return jsonify(data),200

@app.route('/username/<user>', methods = ['DELETE'])
def delete_user(user):
    _user = us.find_username(user)
    if not _user:
        return jsonify({'error': 'Username does not exist.'}), 404
    else:
        try:
            # username.remove(user) 
            us.delete_user(user)
            return jsonify({"message": "Username deleted successfully"}) ,200
        except Exception as e:
            return jsonify({"error":str(e)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug = True)
