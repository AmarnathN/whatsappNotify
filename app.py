  
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

@app.route("/")
def hello():
    return "WhatsApp notify service is up !!!!"

@app.route("/notify", methods=['POST'])
def send_notify():
    account_sid = 'AC26655be2355e4c0ee534631e5376092a'
    auth_token = '9d5a7cb0c8503f303f4e9bd7c8a0cd95'
    data = request.form.to_dict()
    mail_subject=((data['subject']))
    if ("is now on Netflix".lower() in mail_subject.lower()):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                media_url=['https://www.gannett-cdn.com/presto/2019/07/24/USAT/4cb62745-ee53-4eca-8905-c34f0da4faf7-VPC_COMING_TO_NETFLIX_AUG_DESK_THUMB.00_00_23_11.Still002.jpg?width=1320&height=744&fit=crop&format=pjpg&auto=webp'],
                from_='whatsapp:+14155238886',
                body=(mail_subject),
                to='whatsapp:+918099357257'
            )
        print("notify mail from netflix has been whatsapped !!!")
    else:
        print("not valid notify mail from netflix")

    return str("success")

if __name__ == "__main__":
    app.run(debug=True)
