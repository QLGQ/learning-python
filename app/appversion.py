import json
import logging
from datetime import datetime

from flask import current_app
from flask_login import current_user, login_required
from ripozo import fields
from ripozo.resources import ResourceBase
from ripozo.decorators import apimethod 

from cabbage_backend.db.db import Session
from cabbage_backend.db.appversion import Appversion
from utils import body_check
from exceptions import (HTTPBaseException, BadRequestException)

_logger = logging.getLogger(__name__)

class Appversion(ResourceBase):
    resource_name = 'appversion'

    @classmethod
    @login_required
    @apimethod(methods=['POST'])
    def create(cls, request, *args, **kwargs):
	body_fields = tuple(['message'])
        try:
	    db_session = Session()
	    body_args = request.body_args
	    body_check(body_fields, body_args)

	    message = body_args['message'].strip()
	    at = datetime.now()
	    user_id = current_user.user_id

	    new_appversion = Appversion(message=message,
				    at=at,
		 		    user_id=user_id)
	    new_opratingsystem = Operatingsystem(message=message,
				    at=at,
				    user_id=user_id)
	    db_session.add(new_appversion)
	    db_session.commit()

	    properties = {'content':"add the appversion successfully"}
	    meta = {'id':new_appversion.id}

	    return cls(properties=properties, meta=meta)
	except Exception as exc:
	    if not isinstance(exc, HTTPBaseException):
		_logger.exception(exc)
		raise BadRequestException(message='Bad request')
	    else:
		raise exc
	finally:
	    db_session.close()


class Operatingsystem(ResoureBase):
    def __init__(self, data)
if __name__=='__main__':
    print app.version
    print app.operatingsystem
#define interface address constant
#replace server domain name
def domain(string):
    address = "http://www.ngbit.com/"
    return address
#check for updating API
def check_update(string):
    check_update = address
    return check_update

#define request method
def create(request, *args):
    body_fields = tuple(['message'])
    body_args = request.body_args
    body_checkupdate(body_fileds,body_args)
    return request

#define callback method
class Appversion(ResourceBase):
    resource_name1 = 'appversion'
    resource_name2 = 'appoperatingsystem'

    @classmethod
    @login_required
    @apimethod(methods=['POST'])
    def create(cls, request, *args, **kwargs):
	body_fields = tuple(['message'])
	try:
	    JSONObject firstObject = (JSONObject)response.get("app_ireader")
            frequency = firstOject.opt("frequency")
 	    sendLogStatus = firstObject.opt("send_log")     #get log update configuration
            versionName = firstObject.opt("app_version")    #latest version
	    versionCode = firstObject.opt("version_code")   #version number
            features = firstObject.get("features")          #update content
            sdkversion = firstObject.opt("sdk_version")     #sdk version
            osversion = firstObject.opt("os_version")       #operatingsystem version
            currentversioncode = Utils.getAppversionCode(mContext) #get current version number
            url = firstObject.opt("update_url")             #apk download address
	    last_force_update_version = firstObject.opt("last_force_update_version")    #get last force update version
            iscanupdate = none
	    if(currentversioncode < last_force_update_version):
		return iscanupdate = true
    	    else:
		return iscanupdate = false
   
#save updated information     
    GlobalSetting.saveNewVersionInfo(mContext, versionName, url, features, iscanupdate)
    UpdateInfo updateInfo = new UpdateInfo()
    updateInfo.setVersionName(versionName)
    updateInfo.setVersionCode(versionCode)
    updateInfo.setFeatures(features)
    updateInfo.setSdkVersion(sdkVersion)
    updateInfo.setOsVersion(osversion)
    updateInfo.setUpdateUrl(url)
    updateInfo.setLastForceUpdate(last_force_update_version)

    def onFinish():
	super.onFinish()
        progressDialog.dismiss()

    def onCancel():
 	super.onCancel()
    	progressDialog.cancel()

#invoke checkupdate method
if __name__=='__main__'
    super.onCreate(saveInstanceState)
    CheckUpdate = findView()
    AppUpdateManager.getInstance(MainActivity.this).checkUpdate()
    print appversion
    print apposversion
