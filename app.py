from flask import Flask, jsonify, request, json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user':'postgres',
    'pw':'postgres',
    'db':'classroom',
    'host':'localhost',
    'port':'5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#----------------------------------------------------------------------------------------------------------#
db.init_app(app)
from model.dbkelasroom import Userteacher
from model.dbkelasroom import Userstudent
from model.dbkelasroom import Kelas
from model.dbkelasroom import Kelaswork
from model.dbkelasroom import AnswerKS
from model.dbkelasroom import JoinKS
from model.dbkelasroom import getClassStudent
from model.dbkelasroom import getClassTeacher
from model.dbkelasroom import getClassbyId
from model.dbkelasroom import getJoinbyId
from model.dbkelasroom import getAnswerStudent
from model.dbkelasroom import getAnswerKelas
from model.dbkelasroom import SumbyClassId

#----------------------------------------------------------------------------------------------------------#
@app.route('/regTeacher', methods=['POST'])
def regTeacher():
    body = request.json
    try:
        teacherx = Userteacher.query.all()
        for tch in teacherx:
            if body['username'] == tch.username:
                return jsonify({
                    'message':'username already exist'
                }), 400
            elif body['email'] == tch.email:
                return jsonify({
                    'message':'email already exist'
                }), 400

        teacher = Userteacher(body['username'],body['fullname'],body['email'],body['password'])
        db.session.add(teacher)
        db.session.commit()
        return jsonify({
            'user_id':teacher.user_id,
            'message':'register teacher success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/regStudent', methods=['POST'])
def regStudent():
    body = request.json
    try:
        studentx = Userstudent.query.all()
        for std in studentx:
            if body['username'] == std.username:
                return jsonify({
                    'message':'username already exist'
                }), 400
            elif body['email'] == std.email:
                return jsonify({
                    'message':'email already exist'
                }), 400

        student = Userstudent(body['username'],body['fullname'],body['email'],body['password'])
        db.session.add(student)
        db.session.commit()
        return jsonify({
            'user_id':student.user_id,
            'message':'register student success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/createClass', methods=['POST'])
def createClass():
    body = request.json
    try:
        kelas = Kelas(body['kelasname'],body['user_id'])
        db.session.add(kelas)
        db.session.commit()
        return jsonify({
            'kelas_id':kelas.kelas_id,
            'message':'create class success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/createKelaswork', methods=['POST'])
def createKelaswork():
    body = request.json
    try:
        kelaswork = Kelaswork(body['question'],body['kelas_id'],body['answer'])
        db.session.add(kelaswork)
        db.session.commit()
        return jsonify({
            'kelaswork_id':kelaswork.kelaswork_id,
            'message':'create classwork success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/answerKS', methods=['POST'])
def answer_KS():
    body = request.json
    try:
        answer1 = AnswerKS.query.all()
        for ans in answer1:
            if ans.user_id==body['user_id'] and ans.kelaswork_id==body['kelaswork_id']:
                return jsonify({'message':'user id already submit classwork'})

        answer = AnswerKS(body['user_id'],body['answer'],body['kelaswork_id'],body['score'])
        db.session.add(answer)
        db.session.commit()
        return jsonify({
            'message':'success',
            'id':answer.id
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/joinKS', methods=['POST'])
def join_KS():
    body = request.json
    try:
        join1 = JoinKS.query.all()
        for j in join1:
            if body['kelas_id']==j.kelas_id and body['user_id']==j.user_id:
                return jsonify({'message':'user already in this class'}) 

        join = JoinKS(body['kelas_id'],body['user_id'])
        db.session.add(join)
        db.session.commit()
        return jsonify({
            'id':join.id,
            'message':'join success'
        })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/student', methods=['GET'])
def getClass_Student():
    try:
        student = getClassStudent.query.all()
        return jsonify({'student':[std.serialize() for std in student]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/student/<id_>', methods=['GET'])
def getClass_Student_byId(id_):
    try:
        student = getClassStudent.query.filter_by(kelas_id=id_).all()
        return jsonify({'student':[std.serialize() for std in student]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/teacher', methods=['GET'])
def getClass_Teacher():
    try:
        teacher = getClassTeacher.query.all()
        return jsonify({'teacher':[tch.serialize() for tch in teacher]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/teacher/<id_>', methods=['GET'])
def getClass_Teacher_byId(id_):
    try:
        teacher = getClassTeacher.query.filter_by(user_id=id_).all()
        return jsonify({'teacher':[tch.serialize() for tch in teacher]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/loginTeacher', methods=['POST'])
def loginTeacher():
    body = request.json
    try:
        teacher = Userteacher.query.all()
        for tch in teacher:
            if body['username'] == tch.username and body['password'] == tch.password:
                return jsonify({
                    'data' : tch.serialize(),
                    'message':'login berhasil'
                    })
        
        return jsonify({'message':'login gagal'}), 400

    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/loginStudent', methods=['POST'])
def loginStudent():
    body = request.json
    try:
        student = Userstudent.query.all()
        for std in student:
            if body['username'] == std.username and body['password'] == std.password:
                return jsonify({
                    'data' : std.serialize(),
                    'message':'login berhasil'
                    })
        
        return jsonify({'message':'login gagal'}), 400

    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/getAllClass', methods=['GET'])
def getAllClass():
    try:
        kelas = Kelas.query.all()
        return jsonify({'data':[k.serialize() for k in kelas]})
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/kelas/<id_>', methods=['GET'])
def getClass_byId(id_):
    try:
        kelas = getClassbyId.query.filter_by(kelas_id=id_).all()
        if kelas == [None]:
            kelas = getClassTeacher.query.filter_by(kelas_id=id_).all()
            return jsonify({
            'kelas_id':kelas[0].kelas_id,
            'kelasname':kelas[0].kelasname,
            'teachername':kelas[0].username,
            'data':[]
            })
        return jsonify({
            'kelas_id':kelas[0].kelas_id,
            'kelasname':kelas[0].kelasname,
            'teachername':kelas[0].teachername,
            'data':[kls.serialize() for kls in kelas]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/joinKelas/<id_>', methods=['GET'])
def getJoin_byId(id_):
    try:
        joinKelas = getJoinbyId.query.filter_by(kelas_id=id_).all()
        return jsonify({
            'data':[jkls.serialize() for jkls in joinKelas]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/answerStudent/<id_>', methods=['GET'])
def getAnswer_Student(id_):
    try:
        answerStd = getAnswerStudent.query.filter_by(kelaswork_id=id_).all()
        return jsonify({
            'data':[astd.serialize() for astd in answerStd]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/answer/<id_>', methods=['GET'])
def getAnswer(id_):
    try:
        answerStd = getAnswerKelas.query.filter_by(user_id=id_).all()
        return jsonify({
            'data':[astd.serialize() for astd in answerStd]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/answerbyClass/<id_>', methods=['GET'])
def getAnswerbyClassId(id_):
    try:
        answerStd = getAnswerKelas.query.filter_by(kelas_id=id_).all()
        return jsonify({
            'data':[astd.serialize() for astd in answerStd]
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()
#----------------------------------------------------------------------------------------------------------#
@app.route('/sumByClass/<id_>', methods=['GET'])
def sumByClass(id_):
    try:
        sum_byClass = SumbyClassId.query.filter_by(kelas_id=id_).all()
        return jsonify({
            'data':[sbc.serialize() for sbc in sum_byClass],
            'message':'Get Sum Success'
            })
    except Exception as e:
        return jsonify(str(e)), 500
    
    finally:
        db.session.close()