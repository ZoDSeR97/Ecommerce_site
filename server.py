from app import app
from app.controllers import users, items

if __name__ == "__main__":
    app.run(debug=True)