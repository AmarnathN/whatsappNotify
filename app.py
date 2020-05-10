  
from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SANDBOX_ID'] = os.environ.get('SANDBOX_ID')
app.config['WHATSAPP_NUMBER'] = os.environ.get('WHATSAPP_NUMBER')
@app.route("/")
def hello():
    print(app.config['SANDBOX_ID'])
    return "WhatsApp notify service is up !!!!"

@app.route("/notify", methods=['POST'])
def send_notify():
    account_sid = app.config['SANDBOX_ID']
    auth_token = app.config['SECRET_KEY']
    data = request.form.to_dict()
    mail_subject=((data['subject']))
    if ("is now on Netflix".lower() in mail_subject.lower()):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                media_url=['https://www.gannett-cdn.com/presto/2019/07/24/USAT/4cb62745-ee53-4eca-8905-c34f0da4faf7-VPC_COMING_TO_NETFLIX_AUG_DESK_THUMB.00_00_23_11.Still002.jpg?width=1320&height=744&fit=crop&format=pjpg&auto=webp'],
                from_='whatsapp:+14155238886',
                body=(mail_subject),
                to='whatsapp:{}'.format(app.config['WHATSAPP_NUMBER'])
            )
        print("notify mail from netflix has been whatsapped !!!")
    else:
        print("not valid notify mail from netflix")

    return str("success")

if __name__ == "__main__":
    app.run(debug=True)
