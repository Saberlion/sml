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

    data_list = []
    for item in res:
        data_list.append(item.get_dict())

    res_dict = ResponseFormat(data_list=data_list)

    return json.dumps(res_dict.get_dict())
    return ResponseFormat(0, 'success', res).get_json()


@api_module.route('/api/del', methods=['get'])
def delPost():
    LineError.delAll()
    return ResponseFormat(0).get_json()

@api_module.route('/api/upload', methods=['post'])
def checkErrorPost():
    resjson = request.json
    le = LineError()
    le.Name = resjson['Name']
    le.Time = resjson['Time']
    le.Identification = resjson['Identification']
    le.Thousand = resjson['Thousand']
    le.Hundred = resjson['Hundred']
    le.Special = resjson['Special']
    le.Serial = resjson['Serial']
    le.Longitude = resjson['Longitude']
    le.Latitude = resjson['Latitude']
    le.KJQS = resjson['KJQS']
    le.KJQS_mark = resjson['KJQS_mark']
    le.KJSD = resjson['KJSD']
    le.KJSD_mark = resjson['KJSD_mark']
    le.KJXS = resjson['KJXS']
    le.KJXS_mark = resjson['KJXS_mark']
    le.CDDJD = resjson['CDDJD']
    le.CDDJD_mark = resjson['CDDJD_mark']
    le.CKDJD = resjson['CKDJD']
    le.CKDJD_mark = resjson['CKDJD_mark']
    le.LGZD = resjson['LGZD']
    le.LGZD_mark = resjson['LGZD_mark']
    le.GMCS = resjson['GMCS']
    le.GMCS_mark = resjson['GMCS_mark']
    le.HFYZM = resjson['HFYZM']
    le.HFYZM_mark = resjson['HFYZM_mark']
    le.JTLSSD = resjson['JTLSSD']
    le.JTLSSD_mark = resjson['JTLSSD_mark']
    le.JTLSQS = resjson['JTLSQS']
    le.JTLSQS_mark = resjson['JTLSQS_mark']
    le.DCFJ = resjson['DCFJ']
    le.DCFJ_mark = resjson['DCFJ_mark']
    le.ZMSX = resjson['ZMSX']
    le.ZMSX_mark = resjson['ZMSX_mark']
    le.JYBH = resjson['JYBH']
    le.JYBH_mark = resjson['JYBH_mark']
    le.DCQZ = resjson['DCQZ']
    le.DCQZ_mark = resjson['DCQZ_mark']
    le.LJZC = resjson['LJZC']
    le.LJZC_mark = resjson['LJZC_mark']
    le.SGDS = resjson['SGDS']
    le.SGDS_mark = resjson['SGDS_mark']
    le.DXQZ = resjson['DXQZ']
    le.DXQZ_mark = resjson['DXQZ_mark']
    le.XLDP = resjson['XLDP']
    le.XLDP_mark = resjson['XLDP_mark']
    le.XLDX = resjson['XLDX']
    le.XLDX_mark = resjson['XLDX_mark']
    le.FBWPS = resjson['FBWPS']
    le.FBWPS_mark = resjson['FBWPS_mark']
    le.GGCM = resjson['GGCM']
    le.GGCM_mark = resjson['GGCM_mark']
    le.GGCHM = resjson['GGCHM']
    le.GGCHM_mark = resjson['GGCHM_mark']
    le.SGPS = resjson['SGPS']
    le.SGPS_mark = resjson['SGPS_mark']
    le.XLBZ = resjson['XLBZ']
    le.XLBZ_mark = resjson['XLBZ_mark']
    le.other = resjson['other']
    le.other_mark = resjson['other_mark']
    le.UUID = resjson['UUID']
    # if le.isValid():
    #     return ResponseFormat(1, 'Post parameters invalid').get_json()
    if le.IsExist():
        db_merge(le)
        return ResponseFormat(0, 'update').get_json()
    else:
        db_add(le)
        return ResponseFormat(0, 'success').get_json()
