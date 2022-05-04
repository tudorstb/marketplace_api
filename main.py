import json

from users.functions import *

from flask import Flask, request, Response


app = Flask("Marketplace API")

@app.route('/list_users', methods=["GET"])
def list_users():
    status_code, users_returned = list_users_flask()
    return Response(status=status_code, response=json.dumps(users_returned))

@app.route('/get_user/<user_id>', methods=["GET"])
def get_user(user_id):
    status_code, users_returned = get_user_flask(user_id)
    return Response(status=status_code, response=json.dumps(users_returned))

@app.route('/add_user',methods=["POST"])
def add_user():
    post_data=json.loads(request.data)
    name = post_data['name']
    email = post_data["email"]
    status_code, user_returned = create_user_flask(name,email)
    return Response(status=status_code, response=json.dumps(user_returned))

@app.route('/delete_user/<user_id>',methods=["DELETE"])
def delete_user(user_id):
    return del_user_flask(user_id)



# TODO: implement the missing APIs for users, products and orders

if __name__ == '__main__':
    app.run()