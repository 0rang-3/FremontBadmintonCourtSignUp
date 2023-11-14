from flask import Flask, redirect, url_for, render_template, request
import time, atexit
from datetime import datetime


c1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c3 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c4 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c5 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c6 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

cc = ["", "", "", "", "", ""]

cs = ["", "", "", "", "", ""]

MAX_TIME_ON_COURT = 0.5

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    global MAX_TIME_ON_COURT
    if request.method == "POST":
        courtNum = request.form["courts"]
        nm1 = request.form["nm1"]
        nm2 = request.form["nm2"]
        nm3 = request.form["nm3"]
        nm4 = request.form["nm4"]

        if(nm1 == "admin" and int(courtNum) == 0):
            return redirect(url_for("login"))


        if(int(courtNum) == 1):
            if(c1.index("") == 0):
                cs[0] = time.strftime("%H:%M:%S")
                cc[0] = "10.0"
            c1[c1.index("")] = nm1
            c1[c1.index("")] = nm2
            c1[c1.index("")] = nm3
            c1[c1.index("")] = nm4
        elif(int(courtNum) == 2):
            if(c2.index("") == 0):
                cs[1] = time.strftime("%H:%M:%S")
                cc[1] = "10.0"
            c2[c2.index("")] = nm1
            c2[c2.index("")] = nm2
            c2[c2.index("")] = nm3
            c2[c2.index("")] = nm4
        elif(int(courtNum) == 3):
            if(c3.index("") == 0):
                cs[2] = time.strftime("%H:%M:%S")
                cc[2] = "10.0"
            c3[c3.index("")] = nm1
            c3[c3.index("")] = nm2
            c3[c3.index("")] = nm3
            c3[c3.index("")] = nm4
        elif(int(courtNum) == 4):
            if(c4.index("") == 0):
                cs[3] = time.strftime("%H:%M:%S")
                cc[3] = "10.0"
            c4[c4.index("")] = nm1
            c4[c4.index("")] = nm2
            c4[c4.index("")] = nm3
            c4[c4.index("")] = nm4
        elif(int(courtNum) == 5):
            if(c5.index("") == 0):
                cs[4] = time.strftime("%H:%M:%S")
                cc[4] = "10.0"
            c5[c5.index("")] = nm1
            c5[c5.index("")] = nm2
            c5[c5.index("")] = nm3
            c5[c5.index("")] = nm4
        elif(int(courtNum) == 6):
            if(c6.index("") == 0):
                cs[5] = time.strftime("%H:%M:%S")
                cc[5] = "10.0"
            c6[c6.index("")] = nm1
            c6[c6.index("")] = nm2
            c6[c6.index("")] = nm3
            c6[c6.index("")] = nm4
        

        if(c1.index("") != 0 and cs[0] != ""):
            t1 = datetime.strptime(cs[0], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[5] = str(timeLeftFloat)
        if(c1.index("") != 0 and float(cc[0]) <= 0.0):
            if(c1.index("") > 3):
                c1.remove(c1[3])
                c1.remove(c1[2])
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(4):
                    c1.append("")
            elif(c1.index("") > 2):
                c1.remove(c1[2])
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(3):
                    c1.append("")
            elif(c1.index("") > 1):
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(2):
                    c1.append("")
            elif(c1.index("") > 0):
                c1.remove(c1[0])
                c1.append("")
            cc[0] = MAX_TIME_ON_COURT
            cs[0] = time.strftime("%H:%M:%S")
        if(c2.index("") != 0 and float(cc[1]) <= 0.0):
            if(c2.index("") > 3):
                c2.remove(c2[3])
                c2.remove(c2[2])
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(4):
                    c2.append("")
            elif(c2.index("") > 2):
                c2.remove(c2[2])
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(3):
                    c2.append("")
            elif(c2.index("") > 1):
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(2):
                    c2.append("")
            elif(c2.index("") > 0):
                c2.remove(c2[0])
                c2.append("")
            cc[1] = MAX_TIME_ON_COURT
            cs[1] = time.strftime("%H:%M:%S")
        if(c3.index("") != 0 and float(cc[2]) <= 0.0):
            if(c3.index("") > 3):
                c3.remove(c3[3])
                c3.remove(c3[2])
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(4):
                    c3.append("")
            elif(c3.index("") > 2):
                c3.remove(c3[2])
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(3):
                    c3.append("")
            elif(c3.index("") > 1):
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(2):
                    c3.append("")
            elif(c3.index("") > 0):
                c3.remove(c3[0])
                c3.append("")
            cc[2] = MAX_TIME_ON_COURT
            cs[2] = time.strftime("%H:%M:%S")
        if(c4.index("") != 0 and float(cc[3]) <= 0.0):
            if(c4.index("") > 3):
                c4.remove(c4[3])
                c4.remove(c4[2])
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(4):
                    c4.append("")
            elif(c4.index("") > 2):
                c4.remove(c4[2])
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(3):
                    c4.append("")
            elif(c4.index("") > 1):
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(2):
                    c4.append("")
            elif(c4.index("") > 0):
                c4.remove(c4[0])
                c4.append("")
            cc[3] = MAX_TIME_ON_COURT
            cs[3] = time.strftime("%H:%M:%S")
        if(c5.index("") != 0 and float(cc[4]) <= 0.0):
            if(c5.index("") > 3):
                c5.remove(c5[3])
                c5.remove(c5[2])
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(4):
                    c5.append("")
            elif(c5.index("") > 2):
                c5.remove(c5[2])
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(3):
                    c5.append("")
            elif(c5.index("") > 1):
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(2):
                    c5.append("")
            elif(c5.index("") > 0):
                c5.remove(c5[0])
                c5.append("")
            cc[4] = MAX_TIME_ON_COURT
            cs[4] = time.strftime("%H:%M:%S")
        if(c6.index("") != 0 and float(cc[5]) <= 0.0):
            if(c6.index("") > 3):
                c6.remove(c6[3])
                c6.remove(c6[2])
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(4):
                    c6.append("")
            elif(c6.index("") > 2):
                c6.remove(c6[2])
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(3):
                    c6.append("")
            elif(c6.index("") > 1):
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(2):
                    c6.append("")
            elif(c6.index("") > 0):
                c6.remove(c6[0])
                c6.append("")
            cc[5] = MAX_TIME_ON_COURT
            cs[5] = time.strftime("%H:%M:%S")
        if(c1.index("") == 0):
            cc[0] = ""
        if(c2.index("") == 0):
            cc[1] = ""
        if(c3.index("") == 0):
            cc[2] = ""
        if(c4.index("") == 0):
            cc[3] = ""
        if(c5.index("") == 0):
            cc[4] = ""
        if(c6.index("") == 0):
            cc[5] = ""



        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs)
    else:
        if(c1.index("") != 0 and cs[0] != ""):
            t1 = datetime.strptime(cs[0], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 1)
            cc[5] = str(timeLeftFloat)
        if(c1.index("") != 0 and float(cc[0]) <= 0.0):
            if(c1.index("") > 3):
                c1.remove(c1[3])
                c1.remove(c1[2])
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(4):
                    c1.append("")
            elif(c1.index("") > 2):
                c1.remove(c1[2])
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(3):
                    c1.append("")
            elif(c1.index("") > 1):
                c1.remove(c1[1])
                c1.remove(c1[0])
                for x in range(2):
                    c1.append("")
            elif(c1.index("") > 0):
                c1.remove(c1[0])
                c1.append("")
            cc[0] = MAX_TIME_ON_COURT
            cs[0] = time.strftime("%H:%M:%S")
        if(c2.index("") != 0 and float(cc[1]) <= 0.0):
            if(c2.index("") > 3):
                c2.remove(c2[3])
                c2.remove(c2[2])
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(4):
                    c2.append("")
            elif(c2.index("") > 2):
                c2.remove(c2[2])
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(3):
                    c2.append("")
            elif(c2.index("") > 1):
                c2.remove(c2[1])
                c2.remove(c2[0])
                for x in range(2):
                    c2.append("")
            elif(c2.index("") > 0):
                c2.remove(c2[0])
                c2.append("")
            cc[1] = MAX_TIME_ON_COURT
            cs[1] = time.strftime("%H:%M:%S")
        if(c3.index("") != 0 and float(cc[2]) <= 0.0):
            if(c3.index("") > 3):
                c3.remove(c3[3])
                c3.remove(c3[2])
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(4):
                    c3.append("")
            elif(c3.index("") > 2):
                c3.remove(c3[2])
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(3):
                    c3.append("")
            elif(c3.index("") > 1):
                c3.remove(c3[1])
                c3.remove(c3[0])
                for x in range(2):
                    c3.append("")
            elif(c3.index("") > 0):
                c3.remove(c3[0])
                c3.append("")
            cc[2] = MAX_TIME_ON_COURT
            cs[2] = time.strftime("%H:%M:%S")
        if(c4.index("") != 0 and float(cc[3]) <= 0.0):
            if(c4.index("") > 3):
                c4.remove(c4[3])
                c4.remove(c4[2])
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(4):
                    c4.append("")
            elif(c4.index("") > 2):
                c4.remove(c4[2])
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(3):
                    c4.append("")
            elif(c4.index("") > 1):
                c4.remove(c4[1])
                c4.remove(c4[0])
                for x in range(2):
                    c4.append("")
            elif(c4.index("") > 0):
                c4.remove(c4[0])
                c4.append("")
            cc[3] = MAX_TIME_ON_COURT
            cs[3] = time.strftime("%H:%M:%S")
        if(c5.index("") != 0 and float(cc[4]) <= 0.0):
            if(c5.index("") > 3):
                c5.remove(c5[3])
                c5.remove(c5[2])
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(4):
                    c5.append("")
            elif(c5.index("") > 2):
                c5.remove(c5[2])
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(3):
                    c5.append("")
            elif(c5.index("") > 1):
                c5.remove(c5[1])
                c5.remove(c5[0])
                for x in range(2):
                    c5.append("")
            elif(c5.index("") > 0):
                c5.remove(c5[0])
                c5.append("")
            cc[4] = MAX_TIME_ON_COURT
            cs[4] = time.strftime("%H:%M:%S")
        if(c6.index("") != 0 and float(cc[5]) <= 0.0):
            if(c6.index("") > 3):
                c6.remove(c6[3])
                c6.remove(c6[2])
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(4):
                    c6.append("")
            elif(c6.index("") > 2):
                c6.remove(c6[2])
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(3):
                    c6.append("")
            elif(c6.index("") > 1):
                c6.remove(c6[1])
                c6.remove(c6[0])
                for x in range(2):
                    c6.append("")
            elif(c6.index("") > 0):
                c6.remove(c6[0])
                c6.append("")
            cc[5] = MAX_TIME_ON_COURT
            cs[5] = time.strftime("%H:%M:%S")
        if(c1.index("") == 0):
            cc[0] = ""
        if(c2.index("") == 0):
            cc[1] = ""
        if(c3.index("") == 0):
            cc[2] = ""
        if(c4.index("") == 0):
            cc[3] = ""
        if(c5.index("") == 0):
            cc[4] = ""
        if(c6.index("") == 0):
            cc[5] = ""


        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs)


@app.route("/login/", methods=["POST", "GET"])
def login():
    print("hi2")
    if request.method == "POST":
        print("hi")
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for("admin"))
    else:
        return render_template("login.html")

@app.route("/3517245211658351284258/", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        global MAX_TIME_ON_COURT
        MAX_TIME_ON_COURT = float(request.form['mton'])
        return render_template("admin.html")
    else:
        return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)