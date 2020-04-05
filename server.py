from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)
@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:file>')
def index(file):
	print("hello")
	return render_template(file)


def write_to_file(data):
	with open('database.txt', mode='a') as file:
		f = file.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')


def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as file2:
		csv_writer = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([data["email"],data["subject"],data["message"]])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			print(data)
			write_to_csv(data)
		except:
			return 'did not save'
		return render_template('thankyou.html')
	else:
		return 'form not submitted'