# -*- coding:utf8 -*-
from datetime import datetime, timedelta
import json
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

    id = Column(Integer, autoincrement=1)
    Name = Column(String)
    Time = Column(String)
    Identification = Column(String)
    Thousand = Column(String)
    Hundred = Column(String)
    Special = Column(String)
    Serial = Column(String)
    Longitude = Column(String)
    Latitude = Column(String)
    KJQS = Column(String)
    KJQS_mark = Column(String)
    KJSD = Column(String)
    KJSD_mark = Column(String)
    KJXS = Column(String)
    KJXS_mark = Column(String)
    CDDJD = Column(String)
    CDDJD_mark = Column(String)
    CKDJD = Column(String)
    CKDJD_mark = Column(String)
    LGZD = Column(String)
    LGZD_mark = Column(String)
    GMCS = Column(String)
    GMCS_mark = Column(String)
    HFYZM = Column(String)
    HFYZM_mark = Column(String)
    JTLSSD = Column(String)
    JTLSSD_mark = Column(String)
    JTLSQS = Column(String)
    JTLSQS_mark = Column(String)
    DCFJ = Column(String)
    DCFJ_mark = Column(String)
    ZMSX = Column(String)
    ZMSX_mark = Column(String)
    JYBH = Column(String)
    JYBH_mark = Column(String)
    DCQZ = Column(String)
    DCQZ_mark = Column(String)
    LJZC = Column(String)
    LJZC_mark = Column(String)
    SGDS = Column(String)
    SGDS_mark = Column(String)
    DXQZ = Column(String)
    DXQZ_mark = Column(String)
    XLDP = Column(String)
    XLDP_mark = Column(String)
    XLDX = Column(String)
    XLDX_mark = Column(String)
    FBWPS = Column(String)
    FBWPS_mark = Column(String)
    GGCM = Column(String)
    GGCM_mark = Column(String)
    GGCHM = Column(String)
    GGCHM_mark = Column(String)
    SGPS = Column(String)
    SGPS_mark = Column(String)
    XLBZ = Column(String)
    XLBZ_mark = Column(String)
    other = Column(String)
    other_mark = Column(String)
    UUID = Column(String,primary_key=True)


    @staticmethod
    def getRandomN(n):
        res = LineError.query.order_by(LineError.id.desc()).limit(n).all()
        return res

    @staticmethod
    def getAll():
        res = LineError.query.order_by(LineError.id.desc()).all()
        return res

    @staticmethod
    def delAll():
        db.session.query(LineError).delete()
        db.session.commit()



    def IsExist(self):
        # to-do
        res = LineError.query.filter(LineError.UUID == self.UUID).order_by(LineError.id.desc()).first()
        if res:
            return True
        else:
            return False

    def isValid(self):
        if self.Time and self.Name and self.Longitude and self.Latitude:
            return False
        else:
            return True



    def get_dict(self):
        res = {
            'Special': self.Special,
            'JYBH_mark': self.JYBH_mark,
            'JTLSQS_mark': self.JTLSQS_mark,
            'DCFJ_mark': self.DCFJ_mark,
            'XLDX': self.XLDX,
            'CDDJD_mark': self.CDDJD_mark,
            'DCQZ_mark': self.DCQZ_mark,
            'XLDX_mark': self.XLDX_mark,
            'XLDP': self.XLDP,
            'LGZD_mark': self.LGZD_mark,
            'GGCHM': self.GGCHM,
            'DXQZ_mark': self.DXQZ_mark,
            'KJXS_mark': self.KJXS_mark,
            'Hundred': self.Hundred,
            'LGZD': self.LGZD,
            'CKDJD_mark': self.CKDJD_mark,
            'ZMSX': self.ZMSX,
            'LJZC': self.LJZC,
            'JYBH': self.JYBH,
            'Serial': self.Serial,
            'DXQZ': self.DXQZ,
            'DCQZ': self.DCQZ,
            'Longitude': self.Longitude,
            'JTLSQS': self.JTLSQS,
            'XLDP_mark': self.XLDP_mark,
            'SGDS_mark': self.SGDS_mark,
            'other': self.other,
            'KJQS': self.KJQS,
            'SGPS_mark': self.SGPS_mark,
            'GMCS': self.GMCS,
            'XLBZ_mark': self.XLBZ_mark,
            'GGCM_mark': self.GGCM_mark,
            'HFYZM_mark': self.HFYZM_mark,
            'CKDJD': self.CKDJD,
            'GMCS_mark': self.GMCS_mark,
            'Time': self.Time,
            'HFYZM': self.HFYZM,
            'ZMSX_mark': self.ZMSX_mark,
            'XLBZ': self.XLBZ,
            'Latitude': self.Latitude,
            'LJZC_mark': self.LJZC_mark,
            'KJSD_mark': self.KJSD_mark,
            'GGCM': self.GGCM,
            'other_mark': self.other_mark,
            'CDDJD': self.CDDJD,
            'JTLSSD_mark': self.JTLSSD_mark,
            'DCFJ': self.DCFJ,
            'FBWPS': self.FBWPS,
            'SGDS': self.SGDS,
            'JTLSSD': self.JTLSSD,
            'GGCHM_mark': self.GGCHM_mark,
            'Identification': self.Identification,
            'SGPS': self.SGPS,
            'Name': self.Name,
            'Thousand': self.Thousand,
            'KJQS_mark': self.KJQS_mark,
            'KJXS': self.KJXS,
            'KJSD': self.KJSD,
            'FBWPS_mark': self.FBWPS_mark,
            'UUID':self.UUID
        }
        return res


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
