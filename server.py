import string
from flask import Flask,  render_template, request, redirect
app = Flask(__name__)
print (__name__)
@app.route('/')
def my_home():
    return render_template('index.html')



@app.route('/<string:page_name>')
def route_to_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    content = data['content']
    with open('database.txt','a')  as db:
        db.write('\n')
        db.write(f'{email},{subject},{content}')
@app.route('/submit_form', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('./thankyou.html')
    else:
        return ("Something Went Wrong ! Please try again") 

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

  

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory('static/fav1.ico')    

# @app.route('/<username>')
# def send_name(username=None):
#     return render_template('sample.html', name = username)