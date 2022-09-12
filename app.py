from flask import Flask,render_template,request
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET','POST'])
def hello_world():  # put application's code here
    # return 'Hello World!'
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
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
        Server = request.form.get('Server')
        UserName = request.form.get('UserName')
        UserPassword = request.form.get('UserPassword')
        ServerKey = request.form.get('ServerKey')
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
        "Server":Server,
        "Log":"1",
        "UserName":UserName,
        "UserPassword":UserPassword,
        "ServerKey":ServerKey
    }
    config = "config.json"
    user = "user.json"
    with open(config,'w',encoding='utf-8') as f1:
        json.dump(ConfigData,f1,ensure_ascii=False)
    with open(user,'w',encoding='utf-8') as f:
        json.dump(UserData,f,ensure_ascii=False)
    return "信息填写完毕！"
if __name__ == '__main__':
    app.run()
