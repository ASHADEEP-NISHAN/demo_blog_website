from flask import Flask,render_template,request
import requests
API_NPOINT_URL="https://api.npoint.io/3786272a7e373af25bdc"
response=requests.get(url=API_NPOINT_URL)
json_data=response.json()


app=Flask(__name__)

@app.route("/")
def get_blog():
    return render_template("index.html",all_posts=json_data)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])
        return render_template("contact.html",msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)

@app.route("/post/<num>")
def get_post(num):
    requested_post = None
    for post in json_data:
        if post["id"] == int(num):
            requested_post = post
    return render_template("post.html",post=requested_post)

if __name__=="__main__":
    app.run(debug=True)

