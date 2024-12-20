import lib
from flask import Flask, render_template,request,abort

app  = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',name='423')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'admin' and password == '1234':
            return render_template('user.html',user_name='admin')
        else:
            abort(401)
if __name__ == '__main__':
    app.run(host=lib.get_ipv6_address(),port=81)