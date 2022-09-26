from flask import Flask,render_template,request
import json
def WirteIn():
    Country = request.form.get('Country')
    Province = request.form.get('Province')
    City = request.form.get('City')
    County = request.form.get('County')
    street_number = request.form.get('street_number')
    CurrentPosition = request.form.get('CurrentPosition')
    FirstStitchDate = request.form.get('FirstStitchDate')
    TwoStitchDate = request.form.get('TwoStitchDate')
    ThreeStitchDate = request.form.get('ThreeStitchDate')
    Vaccination = request.form.get('Vaccination')
    BRHGTJZRSFYXLQKOne = request.form.get('BRHGTJZRSFYXLQKOne')
    BRHGTJZRSFYXLQKTwo = request.form.get('BRHGTJZRSFYXLQKTwo')
    SZSQTNSFFSYQ = request.form.get('SZSQTNSFFSYQ')
    LJSHJCS = request.form.get('LJSHJCS')
    BRHGTJZRSFYYXZZWQY = request.form.get('BRHGTJZRSFYYXZZWQY')
    JRSFCSWFL = request.form.get('JRSFCSWFL')
    JRSFCSNQTDJSFQ = request.form.get('JRSFCSNQTDJSFQ')
    TodaySchedule = request.form.get('TodaySchedule')
    DayTemperature = request.form.get('DayTemperature')
    Remark = request.form.get('Remark')
    TodayScheduleOther = request.form.get('TodayScheduleOther')
    IsInSchoolOfDay = request.form.get('IsInSchoolOfDay')
    ISNATDay = request.form.get('ISNATDay')
    PushPlus = request.form.get('PushPlus')
    username = request.form.get('username')
    userpassword = request.form.get('userpassword')
    PushPlustoken = request.form.get('PushPlustoken')
    ConfigData = {
        "cookies":{"insert_cookie":"29594869"},
        "NowDate":"",
        "Country":Country,
        "Province":Province,
        "City":City,
        "County":County,
        "street_number":street_number,
        "CurrentPosition":CurrentPosition,
        "title":"地点",
        "desc":"详细地点",
        "FirstStitchDate":FirstStitchDate,
        "TwoStitchDate":TwoStitchDate,
        "ThreeStitchDate":ThreeStitchDate,
        "Vaccination":Vaccination,
        "BRHGTJZRSFYXLQKOne":BRHGTJZRSFYXLQKOne,
        "BRHGTJZRSFYXLQKTwo":BRHGTJZRSFYXLQKTwo,
        "SZSQTNSFFSYQ":SZSQTNSFFSYQ,
        "LJSHJCS":LJSHJCS,
        "BRHGTJZRSFYYXZZWQY":BRHGTJZRSFYYXZZWQY,
        "JRSFCSWFL":JRSFCSWFL,
        "JRSFCSNQTDJSFQ":JRSFCSNQTDJSFQ,
        "TodaySchedule":TodaySchedule,
        "DayTemperature":DayTemperature,
        "Remark":Remark,
        "TodayScheduleOther":TodayScheduleOther,
        "IsInSchool":"",
        "IsInSchoolOfDay": IsInSchoolOfDay,
        "ISNATDay": ISNATDay
    }
    UserData = {
        "PushPlus":PushPlus,
        "Log":"1",
        "username":username,
        "userpassword":userpassword,
        "PushPlustoken":PushPlustoken
    }
    config = "config.json"
    user = "user.json"
    with open(config,'w',encoding='utf-8') as f1:
        json.dump(ConfigData,f1,ensure_ascii=False,indent=4)
    with open(user,'w',encoding='utf-8') as f2:
        json.dump(UserData,f2,ensure_ascii=False,indent=4)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET','POST'])
def main():  
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        WirteIn()
    with open('config.json','r',encoding='utf-8') as f3:
        line1 = f3.read()
    with open('user.json','r',encoding='utf-8') as f4:
        line2 = f4.read()
    return '请将如下信息复制到config.json:<br><br><br>'+line1+'<br><br><br><br>'+'请将如下信息复制到user.json:<br><br><br>'+line2
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)