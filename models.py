from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash,Bcrypt,bcrypt,generate_password_hash
from flask_login import current_user,login_required,LoginManager,UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/appnotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "soy_una_secret"



db = SQLAlchemy(app)
class Nota(db.Model):#creamos el modelo de la trabla 
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    contenido = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Nota {self.id}>"
    
class User(db.Model):

    # __tablename__ = 'usuarios' #con esto podemos cambiar el nombre de la tabla despues de migrar si quisieramos, se importa de sqlAlchemy
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128),  nullable=False)
    notas = db.relationship('Nota', backref='usuario')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)