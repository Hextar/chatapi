from main import login_manager
from app.models.user import User as UserModel
from app.session.user import User

@login_manager.user_loader
def load_user(user_id):
    obj_user = UserModel.query.filter_by(email=user_id).first()
    if obj_user is None:
        return None
    
    return User(obj_user.email, obj_user.email) 
