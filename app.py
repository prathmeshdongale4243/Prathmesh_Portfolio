from flask import Flask, render_template, request,send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']
        with open('contacts.txt', 'a', encoding='utf-8') as f:
            f.write(f'Name: {name}\nEmail: {email}\nMessage: {msg}\n---\n')
        message = 'Your message has been sent!'
        return render_template('PrathmeshPortfolo.html', message=message)  # <-- changed here
    return render_template('PrathmeshPortfolo.html', message=message)      # <-- and here
# ...existing code...

@app.route('/resume/view')
def view_resume():
    return send_from_directory('static/images', 'Prathmesh Dongale Resume.pdf')

@app.route('/resume/download')
def download_resume_file():  # <-- changed name so it's unique
    return send_from_directory('static/images', 'Prathmesh Dongale Resume.pdf', as_attachment=True)

# -------------------
if __name__ == '__main__':
    app.run(debug=True)