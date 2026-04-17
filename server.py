from flask import Flask, request, abort

app = Flask(__name__)   # setting up flask

@app.route('/webhook', methods=['POST'])   # the uri that is being listened on 
def webhook():                     #  calll the function webhook  methof
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
