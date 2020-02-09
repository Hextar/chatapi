from main import login_manager
from app.session.user import User

@login_manager.user_loader
def load_user(user_id):
    return User(
        'usronecampus@avansys.edu.pe',
        'usronecampus@avansys.edu.pe'
    )