from flask import Flask,render_template,request
import requests
API_NPOINT_URL="https://api.npoint.io/3786272a7e373af25bdc"
my_email=""
password=""
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
        send_mail(name=request.form['name'],email=request.form['email'],phone=request.form['phone'],message=request.form['message'])
        # print(request.form['name'], request.form['email'], request.form['phone'], request.form['message'])
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

def send_mail(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=email_message)

if __name__=="__main__":
    app.run(debug=True)

