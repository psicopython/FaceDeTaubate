class User(db.Model):
  
  tablename="user"
  
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(128),nullable=False)
    email = db.Column(db.String(128),unique=True,nullable=False)
    senha  = db.Column(db.String(512),nullable=False)
    data_cr = db.Column(db.DateTime,nullable=False)
    username  = db.Column(db.String, unique=True,nullable=False)
    posts = db.relationship('Post', backref='user',
    	lazy='select', cascade="all, delete-orphan")
  
  def init(self,nome, email,senha,username):
  
    self.nome = nome
    self.email = email
    self.senha  = gph(senha)
    self.data_cr = datetime.now()
    self.username  = username
  
  
  def repr(self):
    return f"<Usuário {self.username}| id:{self.id}>"
  
  
  def ver_pass(self,senha):
    return cph(self.senha,senha)