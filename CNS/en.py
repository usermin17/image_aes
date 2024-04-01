# Import necessary modules
from flask import Flask, render_template, request
from encrypt import encrypted_image

# Initialize Flask application
app = Flask(__name__)

# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route for image encryption
@app.route('/encrypt', methods=['POST'])
def encrypt():
    # Get image path from form submission
    image_path = request.form['image_path']
    
    try:
        # Encrypt the image using your encryption function
        encrypted_image = encrypted_image(image_path)
        
        # Return a message indicating successful encryption
        return render_template('encryption_success.html')
    except Exception as e:
        # Return an error message if encryption fails
        return render_template('encryption_error.html', error=str(e))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)