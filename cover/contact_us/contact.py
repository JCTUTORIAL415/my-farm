from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gaiyas.iot.agriculture.tw@gmail.com'  
app.config['MAIL_PASSWORD'] = 'pedsAp-zicxej-4redwix'  

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject="New Message from Contact Us Page",
                      sender=email,
                      recipients=["gaiyas.iot.agriculture.tw@gmail.com"])  
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        try:
            mail.send(msg)
            return jsonify({"status": "success", "message": "Message sent successfully!"})
        except Exception as e:
            return jsonify({"status": "error", "message": f"Failed to send message: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
