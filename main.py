from app import create_app

# Create the Flask app instance
app = create_app()

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
