# -*- coding:utf8 -*-
import json
import time

from flask import request, Response, Blueprint

from app.API.decorators import ResponseFormat, auth

api_module = Blueprint('api_module', __name__)

from models import *


@api_module.route('/')
def hello_world():
    return 'Hello World!'


@api_module.route('/api/reg', methods=['post'])
def regist():
    from app.API.models import User, md5, db_add
    jsonobj = request.json
    user = User()
    user.email = jsonobj['email']
    user.username = jsonobj['username']
    user.psw = md5(jsonobj['psw'])
    if not user.IsExist():
        db_add(user)
        return ResponseFormat().get_json()
    else:
        return ResponseFormat(1, 'user already exist').get_json()


@api_module.route('/api/authkey', methods=['post'])
def getAuthKey():
    jsonobj = request.json
    user = User()
    user.email = jsonobj['email']
    user.psw = md5(jsonobj['psw'])
    authnum = user.IsAuth()
    if authnum >= 0:
        auth_t = Auth()
        auth_t.authnum = authnum
        auth_t.genNewKey(user)
        date_list = []
        if auth_t.IsUserExist():
            Auth.query.filter(Auth.userid == auth_t.userid) \
                .update({Auth.authkey: auth_t.authkey, Auth.expires: auth_t.expires})
            db.session.commit()
        else:
            db_merge(auth_t)
        date_list.append({'key': auth_t.authkey})
        return ResponseFormat(data_list=date_list).get_json()
    return ResponseFormat(1, 'error').get_json()


@api_module.route('/api/post', methods=['post'])
@auth(0)
def post():
    jsonobj = request.json
    time1 = time.strptime(jsonobj['date'], '%Y%m%d %H:%M:%S')
    date = datetime(time1.tm_year, time1.tm_mon, time1.tm_mday, time1.tm_hour, time1.tm_min, time1.tm_sec)

    data = Data(jsonobj['unique_id'],
                jsonobj['lat'],
                jsonobj['lon'],
                jsonobj['error_msg'],
                date)
    res = ResponseFormat()
    if not data.IsExist():
        db_add(data)
        res.code = 1
        res.msg = '已经提交过了'

    return res.get_json()


@api_module.route('/api/get/<int:num>', methods=['get'])
def get(num):
    data = Data.getRandomN(num)
    data_list = []
    for item in data:
        data_list.append(item.getDict())

    res_dict = ResponseFormat(data_list=data_list)

    return json.dumps(res_dict.get_dict())


@api_module.route('/api/position', methods=['post'])
@auth(0)
def lineerror():
    jsonobj = request.json
    pos = Position()
    pos.identification = jsonobj['identification']
    pos.line = jsonobj['line']
    pos.lat = jsonobj['lat']
    pos.lon = jsonobj['lon']
    pos.positiondata = jsonobj['positiondata']
    pos.positiontype = jsonobj['positiontype']
    db_add(pos)
    return ResponseFormat(1, 'user already exist').get_json()


@api_module.route('/api/position', methods=['post'])
@auth(0)
def position():
    jsonobj = request.json
    pos = Position()
    pos.identification = jsonobj['identification']
    pos.line = jsonobj['line']
    pos.lat = jsonobj['lat']
    pos.lon = jsonobj['lon']
    pos.positiondata = jsonobj['positiondata']
    pos.positiontype = jsonobj['positiontype']
    db_add(pos)
    return ResponseFormat(1, 'user already exist').get_json()


@api_module.route('/api/mainline', methods=['post'])
@auth(0)
def mainline():
    jsonobj = request.json
    ml = Mainline()
    ml.identification = jsonobj['identification']
    ml.line = jsonobj['line']
    ml.lat = jsonobj['lat']
    ml.lon = jsonobj['lon']
    ml.positiondata = jsonobj['positiondata']
    ml.positiontype = jsonobj['positiontype']
    ml.handred = jsonobj['handred']
    ml.thousand = jsonobj['thousand']
    db_add(ml)
    return ResponseFormat(0, 'success').get_json()


@api_module.route('/api/lineerror', methods=['get'])
def checkErrorGet():
    res = LineError.getAll()
    return ResponseFormat(0, 'success', res).get_json()


@api_module.route('/api/upload', methods=['post'])
def checkErrorPost():
    resjson = request.json
    le = LineError()
    # le.Name = resjson['Name']
    # le.time = resjson['time']
    # le.identification = resjson['identification']
    # le.thousand = resjson['thousand']
    # le.hundred = resjson['hundred']
    # le.Latitude = resjson['Latitude']
    # le.Longitude = resjson['Longitude']
    # le.special = resjson['special']
    # le.kjqs = resjson['kjqs']
    # le.kjqs_mark = resjson['kjqs_mark']
    # le.kjsd = resjson['kjsd']
    # le.kjsd_mark = resjson['kjsd_mark']
    # le.kjxs = resjson['kjxs']
    # le.kjxs_mark = resjson['kjxs_mark']
    # le.cddjd = resjson['cddjd']
    # le.cddjd_mark = resjson['cddjd_mark']
    # le.ckdjd = resjson['ckdjd']
    # le.ckdjd_mark = resjson['ckdjd_mark']
    # le.lgzd = resjson['lgzd']
    # le.lgzd_mark = resjson['lgzd_mark']
    # le.gmcs = resjson['gmcs']
    # le.gmcs_mark = resjson['gmcs_mark']
    # le.hfyzm = resjson['hfyzm']
    # le.hfyzm_mark = resjson['hfyzm_mark']
    # le.jtlssd = resjson['jtlssd']
    # le.jtlssd_mark = resjson['jtlssd_mark']
    # le.jtlsqs = resjson['jtlsqs']
    # le.jtlsqs_mark = resjson['jtlsqs_mark']
    # le.dcfj = resjson['dcfj']
    # le.dcfj_mark = resjson['dcfj_mark']
    # le.zmsx = resjson['zmsx']
    # le.zmsx_mark = resjson['zmsx_mark']
    # le.jybh = resjson['jybh']
    # le.jybh_mark = resjson['jybh_mark']
    # le.dcqz = resjson['dcqz']
    # le.dcqz_mark = resjson['dcqz_mark']
    # le.ljzc = resjson['ljzc']
    # le.ljzc_mark = resjson['ljzc_mark']
    # le.sgds = resjson['sgds']
    # le.sgds_mark = resjson['sgds_mark']
    # le.dxqz = resjson['dxqz']
    # le.dxqz_mark = resjson['dxqz_mark']
    # le.xldp = resjson['xldp']
    # le.xldp_mark = resjson['xldp_mark']
    # le.xldx = resjson['xldx']
    # le.xldx_mark = resjson['xldx_mark']
    # le.fbwps = resjson['fbwps']
    # le.fbwps_mark = resjson['fbwps_mark']
    # le.ggcm = resjson['ggcm']
    # le.ggcm_mark = resjson['ggcm_mark']
    # le.ggchm = resjson['ggchm']
    # le.ggchm_mark = resjson['ggchm_mark']
    # le.sgps = resjson['sgps']
    # le.sgps_mark = resjson['sgps_mark']
    # le.xlbz = resjson['xlbz']
    # le.xlbz_mark = resjson['xlbz_mark']
    # le.other = resjson['other']
    # le.other_mark = resjson['other_mark']
    if le.isValid():
        return ResponseFormat(1, 'Post parameters invalid').get_json()
    if le.IsExist():
        db_merge(le)
    else:
        db_add(le)
    return ResponseFormat(0, 'success').get_json()
