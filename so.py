from flask import Flask, redirect

app = Flask(name)

@app.route('/')
def home():
    # Redirects to an external URL, http://localhost/flag
    return redirect('http://localhost/flag', code=302)

@app.route('/flag')
def flag():
    return 'This is now an unused route in the context of redirection.'

if name == 'main':
    app.run(debug=True, host='0.0.0.0')
