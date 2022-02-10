
# Imports
from flask import Flask  # Import Flask to allow us to create our app


# Instatiating from Flask
app = Flask(__name__) # Create a new instance of the Flask class called "app"









# Routing Methods
@app.route('/')             # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/wow')
def wow():
    return 'Wooooowwwww!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name





if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.


