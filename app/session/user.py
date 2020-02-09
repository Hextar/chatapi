class User(object):

    __is_active = True
    __is_authenticated = True

    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email
    
    def set_active(self, is_active):
        self.__is_active = is_active
    
    def is_active(self):
        return self.__is_active
    
    def set_authenticated(self, is_authenticated):
        self.__is_authenticated = is_authenticated
    
    def is_authenticated(self):
        return self.__is_authenticated
    
    def get(self, user_id):
        return self
    
    def get_id(self):
        return str(self.user_id)
    
    def username(self):
        return self.email