from flask import Flask, render_template
from routes import LoadImages, UploadImage

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("entrypage.html")
	
app.register_blueprint(LoadImages.LoadImages_bp)
app.register_blueprint(UploadImage.UploadImage_bp)

if __name__ == '__main__':
	app.run(debug=True)
