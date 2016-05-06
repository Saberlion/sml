# -*- coding:utf8 -*-
from datetime import datetime, timedelta

import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from app.app import db


def md5(rawstr):
    import hashlib
    m = hashlib.md5()
    m.update(rawstr)
    return m.hexdigest()


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=1)
    email = Column(String(20), unique=True)
    username = Column(String(20))
    psw = Column(String(30))
    auth = Column(Integer, default=0)

    def IsAuth(self):
        res = User.query.filter(sqlalchemy.and_(User.email == self.email, User.psw == self.psw)).first()
        if res:
            self.id = res.id
            return res.auth
        else:
            return -1

    def IsExist(self):
        res = User.query.filter(User.email == self.email).first()
        if res:
            return True
        else:
            return False


class Data(db.Model):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, autoincrement=1)
    lat = Column(String(20))
    lon = Column(String(20))
    error_msg = Column(String(100))
    date = Column(DateTime)
    unique_id = Column(String(30), unique=True)

    def __init__(self, unique_id, lat=None, lon=None, error_msg=None, date=None):
        self.lat = lat
        self.lon = lon
        self.error_msg = error_msg
        self.date = date
        self.unique_id = unique_id

    def __repr__(self):
        return 'Date %r,%r,%r,%r' % (self.id, self.lat, self.lon, self.error_msg)

    @staticmethod
    def getRandomN(n):
        res = Data.query.order_by(Data.id.desc()).limit(n).all()
        return res

    def getDict(self):
        res = {'id': self.id, 'lat': self.lat,
               'lon': self.lon,
               'error_msg': self.error_msg,
               'unique_id': self.unique_id,
               'date': self.date.strftime('%Y%m%d %H:%M:%S')}

        return res

    def IsExist(self):
        res = Data.query.filter(Data.unique_id == self.unique_id).order_by(Data.id.desc()).first()
        if res:
            return True
        else:
            return False


class Position(db.Model):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, autoincrement=1)
    line = Column(String(20))
    identification = Column(String(20))
    lat = Column(String(20))
    lon = Column(String(20))
    positiontype = Column(Integer)
    positiondata = Column(String(20))
    remark = Column(String(20))


class Mainline(db.Model):
    __tablename__ = "mainline"

    id = Column(Integer, primary_key=True, autoincrement=1)
    line = Column(String(20))
    identification = Column(String(20))
    time = Column(DateTime)
    lat = Column(String(20))
    lon = Column(String(20))
    thousand = Column(Integer)
    handred = Column(Integer)
    remark = Column(String(30))


class LineError(db.Model):
    __tablename__ = "LineError"

    id = Column(Integer, primary_key=True, autoincrement=1)
    Name = Column(String(10))
    time = Column(DateTime)
    identification = Column(String)
    thousand = Column(String)
    hundred = Column(String)
    Latitude = Column(String)
    Longitude = Column(String)
    special = Column(String)
    kjqs  = Column(String)
    kjqs_mark = Column(String)
    kjsd  = Column(String)
    kjsd_mark = Column(String)
    kjxs = Column(String)
    kjxs_mark = Column(String)
    cddjd = Column(String)
    cddjd_mark = Column(String)
    ckdjd = Column(String)
    ckdjd_mark = Column(String)
    lgzd = Column(String)
    lgzd_mark = Column(String)
    gmcs = Column(String)
    gmcs_mark= Column(String)
    hfyzm= Column(String)
    hfyzm_mark= Column(String)
    jtlssd= Column(String)
    jtlssd_mark= Column(String)
    jtlsqs= Column(String)
    jtlsqs_mark= Column(String)
    dcfj= Column(String)
    dcfj_mark= Column(String)
    zmsx= Column(String)
    zmsx_mark= Column(String)
    jybh= Column(String)
    jybh_mark= Column(String)
    dcqz= Column(String)
    dcqz_mark= Column(String)
    ljzc= Column(String)
    ljzc_mark= Column(String)
    sgds= Column(String)
    sgds_mark= Column(String)
    dxqz= Column(String)
    dxqz_mark= Column(String)
    xldp= Column(String)
    xldp_mark= Column(String)
    xldx= Column(String)
    xldx_mark= Column(String)
    fbwps= Column(String)
    fbwps_mark= Column(String)
    ggcm= Column(String)
    ggcm_mark= Column(String)
    ggchm= Column(String)
    ggchm_mark= Column(String)
    sgps= Column(String)
    sgps_mark= Column(String)
    xlbz= Column(String)
    xlbz_mark= Column(String)
    other= Column(String)
    other_mark= Column(String)

    @staticmethod
    def getRandomN(n):
        res = LineError.query.order_by(LineError.id.desc()).limit(n).all()
        return res

    @staticmethod
    def getAll():
        res = LineError.query.order_by(LineError.id.desc()).all()
        return res

    def IsExist(self):
        #to-do
        res = Data.query.filter(sqlalchemy.and_(LineError.Name == self.Name,
                                                LineError.Latitude == self.Latitude,
                                                LineError.Longitude == self.Longitude)).order_by(Data.id.desc()).first()
        if res:
            return True
        else:
            return False


    def isValid(self):
        if self.time and self.name and self.Longitude and self.Latitude:
            return False
        else:
            return True


    def __repr__(self):
        return 'LineError %r,%r,%r,%r' % (self.id, self.Latitude, self.Longitude, self.time)



class Auth(db.Model):
    __tablename__ = 'auth'

    id = Column(Integer, primary_key=True, autoincrement=1)
    userid = Column(Integer, unique=True)
    authkey = Column(String(30))
    authnum = Column(Integer)
    expires = Column(DateTime)

    def genNewKey(self, user, expires=7200):
        time_now = datetime.now()
        time_str = time_now.strftime("%Y%m%d %H:%M:%S")
        time_expires = time_now + timedelta(seconds=expires)
        self.expires = time_expires
        self.authkey = md5(user.email + user.psw + time_str)
        self.userid = user.id

    def IsExist(self):
        res = Auth.query.filter(Auth.authkey == self.authkey).order_by(Auth.id.desc()).first()
        if res:
            return True
        else:
            return False

    def IsUserExist(self):
        res = Auth.query.filter(Auth.userid == self.userid).order_by(Auth.id.desc()).first()
        if res:
            return True
        else:
            return False

    def IsTimeOut(self):
        res = Auth.query.filter(Auth.authkey == self.authkey).first()
        timenow = datetime.datetime.now()
        timediff = res.expires - timenow
        if timediff.days >= 0:
            return False
        else:
            return True


def db_add(item):
    try:
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        print e
        db.session.rollback()


def db_merge(item):
    try:
        db.session.merge(item)
        db.session.commit()
    except Exception as e:
        print e
        db.session.rollback()

