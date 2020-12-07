#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth("Token")

valid_token = os.environ["TOKEN_PASS"]

@auth.verify_token
def verify_token(token):
    return token == valid_token

@app.route("/")
@auth.login_required
def main_route():
   return "devops test server flying!!"

if __name__ == '__main__':
    app.run("0.0.0.0", port=8081)
