import os
from flask import Flask,render_template,send_from_directory
import pyjade

app = Flask(__name__)
# use the jade template engine
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/history_sniffing.html')
def history_sniffing():
	return render_template('history_sniffing.html')

@app.route('/cache_timing.html')
def cache_timing():
	return render_template('cache_timing.html')

	
if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 3000))
	
	app.run(host='0.0.0.0', port=port, debug=True)


