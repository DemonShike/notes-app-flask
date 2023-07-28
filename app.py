from flask import render_template,request,flash,redirect,url_for,session
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from models import Nota, User, app, db  
from forms import MyForm, RegistrationForm, LoginForm


ckeditor = CKEditor(app) #asignamos ckeditor a la app 

#herramienta apra hacer migraciones
migrate = Migrate(app, db)

# Endpoints

@app.route('/')
def index():
    if session.get('user_id'): #Comprobamos si el usuario esta logeado tomando su id
        user_id = session['user_id']#forma alternativa de obtener el id u otros datos de la sesion actual,puede ser funcional en algunos casos

        notas = Nota.query.order_by(Nota.id.desc()).filter_by(user_id = user_id).all() #recibimos los datos de la nota en base al user

        user = User.query.get(user_id) # sacamos la id del usuario del modelo 
        """
        columnas = [[], [], [], []]

        for i, nota in enumerate(notas):
            columna = i % 4
            columnas[columna].append(nota)  ##Este codigo es "complejo" en resumen enumerate hace que la lista ademas de su contenido tenga en forma de dupla un item numerico y el contenido, luego se lo recorre con el for
                                        #y columna divide el item en 4 y el resto que es el resultado que usa ,lo utiliza para poner en la columna correcta el contenido y con append(nota) agrega el contenido ya ordenado por el numero
         """   
        return render_template('index.html', columnas=notas, user=user)
    else:

        return render_template('index.html')



@app.route('/crear-nota', methods=['POST', 'GET'])
def crear_nota():
    form = MyForm()
    if not session.get('user_id'):
           
        return 'DEBES INICIAR SESION'

    if form.validate_on_submit():#valida que el metodo sea post y se cumplan los requisitos necesarios del formulario(longitud,tipos permitido, etc..)


            titulo = request.form['titulo']#obtenemos los datos por metodo request
            contenido = request.form['contenido']
            
            nueva_nota = Nota(titulo=titulo, contenido=contenido, user_id=session['user_id'])
            db.session.add(nueva_nota)
            db.session.commit() #toda la manipulacion para la db 

            flash(f'Has creado la nota {titulo}')
            return redirect(url_for('index'))

    return render_template('crear_nota.html', form=form, user=session.get('user_id'))



@app.route('/editar-nota/<int:notaid>', methods=['POST','GET'])
def editar_nota(notaid):
    
        user_id = session['user_id']
        if not user_id:
            return redirect(url_for('acceder'))
        
        notas = Nota.query.filter_by(id=notaid, user_id = user_id).first() # "primer" y unica nota que se filtra
        
        if notas is None:
            flash('La nota no existe o no tienes permisos para editarla.', 'error')
            return redirect(url_for('index'))
        form = MyForm()

        if form.validate_on_submit(): 
            notas.titulo = request.form['titulo'] #asignamos el nuevo contenido 
            notas.contenido = request.form['contenido']
            db.session.commit()
            flash(f'La nota {notas.titulo} ha sido actualizada.', 'success')
            return redirect(url_for('index'))

        
        form.contenido.data =  notas.contenido #igualamos los datos del contenido en la db para que se carguen en el campo contenido del ckeditor

        return render_template('crear_nota.html', form=form, notas=notas,user=session.get('user_id'))#aqui pasamos los datos actuales de la nota para que se carguen en el input

#registro

@app.route('/registrarse', methods=['POST','GET'])
def registrarse():
    user_id = session.get('user_id')
    if user_id:
            return redirect(url_for('index'))
    else:
        registro = RegistrationForm()
        
        if registro.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']



            nuevo_user = User(username=username, email=email)
            nuevo_user.set_password(password) #esta funcion codifica la contraseña y la agrega a nuevo_user al atributo password_hash la contraseña,se puede ver en models

            db.session.add(nuevo_user)
            db.session.commit()

            flash(f'Has creado correctamente el usuario {username}')
            return redirect(url_for('index'))

        return render_template('registro.html',registro=registro)


@app.route('/acceder',methods=['GET','POST'])
def acceder():
    user_id = session.get('user_id')
    if user_id:
            return redirect(url_for('index'))
    else:
        login = LoginForm()

        if login.validate_on_submit():
            email = login.email.data #aqui obtenemos los datos desde el formulario lo que es mas eficiente que desde la request dado que los datos ya estan procesados
            password = login.password.data

            user = User.query.filter_by(email=email).first() #buscamos el usuario
            if user and user.check_password(password): #si eso y ademas comprobamos que la contraseña coincidacon la de la db entonces iniciamos sesion
                session['user_id'] = user.id #esto se hace para guardar la id de la sesion del usuario,asignamos user.id a la variables de session  'user_id'
                return redirect(url_for('index'))
            else:
                flash('La contraseña o el correo no coinciden')

        return render_template('acceder.html', login=login)


@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión correctamente.')
    return redirect(url_for('index'))


@app.route('/delete-note/<int:notaid>', methods=['POST','GET'])
def delete(notaid):


    nota = Nota.query.filter_by(id=notaid, user_id=session['user_id']).first()

    db.session.delete(nota)
    db.session.commit()

    flash('La nota se borro correctamente')
    return redirect(url_for('index'))

@app.route('/search', methods=['POST', 'GET'])
def search():
    user = session['user_id']

    if not user:
        return 'DEBES INICIAR SESION'

    search_query = request.args.get('q','')

    nota = Nota.query.filter(Nota.titulo.ilike(f'%{search_query}%')).all() # barra de search que toma el dato directamente desde la url
                                        # contains(serch_query) otro metodo de busqueda si ilike no funcionase..
    return render_template('otra.html', columnas=nota, user=user)

if __name__ == '__main__':
    app.run(debug=True)

