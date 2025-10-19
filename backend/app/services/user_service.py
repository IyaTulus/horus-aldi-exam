from ..extensions import db
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError

def create_user(nama, username, email, password):
    user = User(
        nama=nama,
        username=username,
        email=email
    )
    user.set_password(password)
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except SQLAlchemyError as e:
        db.session.rollback()
        return None
    
def get_user_by_id(id):
    return User.query.get(id)

def get_all_users(page=1, per_page=10):
    return User.query.paginate(page=page, per_page=per_page, error_out=False)

def update_user(user_id, **kwargs):
    user = get_user_by_id(user_id)
    if not user:
        return None
    if 'nama' in kwargs:
        user.nama = kwargs['nama']
    if 'email' in kwargs:
        user.email = kwargs['email']
    if 'password' in kwargs:
        user.set_password(kwargs['password'])
    db.session.commit()
    return user

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def authenticate_user(username, password):
    user = User.query.filter(
        (User.username == username)
    ).first()
    
    if user and user.check_password(password):
        return user
    return None