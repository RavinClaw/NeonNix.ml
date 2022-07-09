# The Code That Runs The Website
# Website URL: NeonNix.ml

from flask import Flask, render_template, url_for, redirect, request
from random import randint as rd

app = Flask(__name__)
account_count_used = []

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/menu")
def menu():
  return render_template("menu.html")

@app.route("/account/new", methods=["GET", "POST"])
def account_new():
  global account_count
  if request.method == "POST":
    account_count = rd(1, 10000)
    account_count_used.append(account_count)
    print(f"Account Number: #{account_count}")
    print(request.form["surname"])
    print(request.form["lastname"])
    print(request.form["username"])
    print(request.form["email"])
    print(request.form["password"])
    return
  return render_template("new_account.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=7482)
