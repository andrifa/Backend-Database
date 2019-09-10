from app import db

class Userteacher(db.Model):
    __tablename__ = 'user_teacher'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, fullname, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password
    
    def serialize(self):
        return {
            'user_id':self.user_id,
            'username':self.username,
            'fullname':self.fullname,
            'email':self.email,
            'password':self.password
            }
#-----------------------------------------------------------------------------#
class Userstudent(db.Model):
    __tablename__ = 'user_student'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, fullname, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password
    
    def serialize(self):
        return {
            'user_id':self.user_id,
            'username':self.username,
            'fullname':self.fullname,
            'email':self.email,
            'password':self.password
            }
#-----------------------------------------------------------------------------#
class Kelas(db.Model):
    __tablename__ = 'kelas'

    kelas_id = db.Column(db.Integer, primary_key=True)
    kelasname = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user_teacher.user_id'), nullable=False)

    def __init__(self, kelasname, user_id):
        self.kelasname = kelasname
        self.user_id = user_id

    
    def serialize(self):
        return {
            'kelas_id':self.kelas_id,
            'kelasname':self.kelasname,
            'user_id':self.user_id
            }
#-----------------------------------------------------------------------------#
class Kelaswork(db.Model):
    __tablename__ = 'kelaswork'

    kelaswork_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.kelas_id'), nullable=False)
    answer = db.Column(db.String())

    def __init__(self, question, kelas_id, answer):
        self.question = question
        self.kelas_id = kelas_id
        self.answer = answer

    
    def serialize(self):
        return {
            'kelaswork_id':self.kelaswork_id,
            'question':self.question,
            'kelas_id':self.kelas_id,
            'answer':self.answer
            }
#-----------------------------------------------------------------------------#
class AnswerKS(db.Model):
    __tablename__ = 'answer_kelaswork_student'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_student.user_id'), nullable=False)
    answer = db.Column(db.String())
    kelaswork_id = db.Column(db.Integer, db.ForeignKey('kelaswork.kelaswork_id'), nullable=False)
    score = db.Column(db.String())

    def __init__(self, user_id, answer, kelaswork_id, score):
        self.user_id = user_id
        self.answer = answer
        self.kelaswork_id = kelaswork_id
        self.score = score

    
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'answer':self.answer,
            'kelaswork_id':self.kelaswork_id,
            'score':self.score
            }
#-----------------------------------------------------------------------------#
class JoinKS(db.Model):
    __tablename__ = 'join_kelas_student'

    id = db.Column(db.Integer, primary_key=True)
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.kelas_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_student.user_id'), nullable=False)

    def __init__(self, kelas_id, user_id):
        self.kelas_id = kelas_id
        self.user_id = user_id

    def serialize(self):
        return {
            'id':self.id,
            'kelas_id':self.kelas_id,
            'user_id':self.user_id
            }
#-----------------------------------------------------------------------------#
class getClassStudent(db.Model):
    __tablename__ = 'getAll_Student_Class'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    kelasname = db.Column(db.String())
    user_id = db.Column(db.Integer)
    kelas_id = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'username':self.username,
            'fullname':self.fullname,
            'email':self.email,
            'password':self.password,
            'kelasname':self.kelasname,
            'kelas_id':self.kelas_id
            }
#-----------------------------------------------------------------------------#
class getClassTeacher(db.Model):
    __tablename__ = 'getAll_Teacher_Class'

    kelas_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    kelasname = db.Column(db.String())
    user_id = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'kelas_id':self.kelas_id,
            'user_id':self.user_id,
            'username':self.username,
            'fullname':self.fullname,
            'email':self.email,
            'password':self.password,
            'kelasname':self.kelasname
            }
#-----------------------------------------------------------------------------#
class getClassbyId(db.Model):
    __tablename__ = 'getClass_byId'

    kelas_id = db.Column(db.Integer)
    kelasname = db.Column(db.String())
    teacherid = db.Column(db.Integer)
    teachername = db.Column(db.String())
    kelaswork_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    teacheranswer = db.Column(db.String())

    def serialize(self):
        return {
            'kelas_id':self.kelas_id,
            'kelasname':self.kelasname,
            'teacherid':self.teacherid,
            'teachername':self.teachername,
            'kelaswork_id':self.kelaswork_id,
            'question':self.question,
            'teacheranswer':self.teacheranswer
        }
#-----------------------------------------------------------------------------#
class getJoinbyId(db.Model):
    __tablename__ = 'getJoin_byId'

    id = db.Column(db.Integer, primary_key=True)
    kelas_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String())

    def serialize(self):
        return {
            'id':self.id,
            'kelas_id':self.kelas_id,
            'user_id':self.user_id,
            'username':self.username
        }
#-----------------------------------------------------------------------------#
class getAnswerStudent(db.Model):
    __tablename__ = 'getAnswer_Student'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    answer = db.Column(db.String())
    kelaswork_id = db.Column(db.Integer)
    score = db.Column(db.String())
    username = db.Column(db.String())

    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'answer':self.answer,
            'kelaswork_id':self.kelaswork_id,
            'score':self.score,
            'username':self.username
        }
#-----------------------------------------------------------------------------#
class getAnswerKelas(db.Model):
    __tablename__ = 'getAnswer_kelas'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    answer = db.Column(db.String())
    kelaswork_id = db.Column(db.Integer)
    kelas_id = db.Column(db.Integer)
    score = db.Column(db.String())
    username = db.Column(db.String())

    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'answer':self.answer,
            'kelaswork_id':self.kelaswork_id,
            'kelas_id':self.kelas_id,
            'score':self.score,
            'username':self.username
        }
#-----------------------------------------------------------------------------#
class SumbyClassId(db.Model):
    __tablename__ = 'sumAll_Score'

    user_id = db.Column(db.Integer, primary_key=True)
    kelas_id = db.Column(db.Integer)
    username = db.Column(db.String())
    sum_ = db.Column(db.Integer)

    def serialize(self):
        return{
            'user_id':self.user_id,
            'kelas_id':self.kelas_id,
            'username':self.username,
            'sum_':self.sum_
        }