from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [

     {
        'Don': 'Abhinay',
        'title': 'Blog post 1',
        'Content': 'First post',
        'Date': 'Nov 17, 2020'
     },
     {
        'Don': 'One and only Abhinay',
        'title': 'Blog post 2',
        'Content': 'Second post',
        'Date': 'Nov 17, 2020'
     }

]

@app.route("/")
@app.route("/home")
def home():
	return render_template('homepage.html', posts = posts)


@app.route("/about")
def about():
	return render_template('about.html', title= 'About') 





if __name__ == '__main__':
	app.run(debug = True)
    