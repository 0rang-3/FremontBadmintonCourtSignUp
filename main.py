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

minCol = ["white", "white", "white", "white", "white", "white"]
reserved = ["white", "white", "white", "white", "white", "white"]
reserve_length = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]

MAX_TIME_ON_COURT = 10.0

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    global MAX_TIME_ON_COURT
    if request.method == "POST":

        try:
            adminLogin = request.form['adminButton']
            if(adminLogin == "ADMIN LOGIN"):
                return redirect(url_for("login"))
        except:
            print()


        courtNum = request.form["courts"]
        nm1 = request.form["nm1"]
        nm2 = request.form["nm2"]
        nm3 = request.form["nm3"]
        nm4 = request.form["nm4"]


        if(int(courtNum) == 1):
            if(c1.index("") == 0):
                cs[0] = time.strftime("%H:%M:%S")
                cc[0] = "10.0"
            try:
                c1[c1.index("")] = nm1
            except:
                print()
            try:
                c1[c1.index("")] = nm2
            except:
                print()
            try:
                c1[c1.index("")] = nm3
            except:
                print()
            try:
                c1[c1.index("")] = nm4
            except:
                print()
        elif(int(courtNum) == 2):
            if(c2.index("") == 0):
                cs[1] = time.strftime("%H:%M:%S")
                cc[1] = "10.0"
            try:
                c2[c2.index("")] = nm1
            except:
                print()
            try:
                c2[c2.index("")] = nm2
            except:
                print()
            try:
                c2[c2.index("")] = nm3
            except:
                print()
            try:
                c2[c2.index("")] = nm4
            except:
                print()
        elif(int(courtNum) == 3):
            if(c3.index("") == 0):
                cs[2] = time.strftime("%H:%M:%S")
                cc[2] = "10.0"
            try:
                c3[c3.index("")] = nm1
            except:
                print()
            try:
                c3[c3.index("")] = nm2
            except:
                print()
            try:
                c3[c3.index("")] = nm3
            except:
                print()
            try:
                c3[c3.index("")] = nm4
            except:
                print()
        elif(int(courtNum) == 4):
            if(c4.index("") == 0):
                cs[3] = time.strftime("%H:%M:%S")
                cc[3] = "10.0"
            try:
                c4[c4.index("")] = nm1
            except:
                print()
            try:
                c4[c4.index("")] = nm2
            except:
                print()
            try:
                c4[c4.index("")] = nm3
            except:
                print()
            try:
                c4[c4.index("")] = nm4
            except:
                print()
        elif(int(courtNum) == 5):
            if(c5.index("") == 0):
                cs[4] = time.strftime("%H:%M:%S")
                cc[4] = "10.0"
            try:
                c5[c5.index("")] = nm1
            except:
                print()
            try:
                c5[c5.index("")] = nm2
            except:
                print()
            try:
                c5[c5.index("")] = nm3
            except:
                print()
            try:
                c5[c5.index("")] = nm4
            except:
                print()
        elif(int(courtNum) == 6):
            if(c6.index("") == 0):
                cs[5] = time.strftime("%H:%M:%S")
                cc[5] = "10.0"
            try:
                c6[c6.index("")] = nm1
            except:
                print()
            try:
                c6[c6.index("")] = nm2
            except:
                print()
            try:
                c6[c6.index("")] = nm3
            except:
                print()
            try:
                c6[c6.index("")] = nm4
            except:
                print()
        
        try:
            tryEx = c1.index("")
        except:
            c1.pop()
            c1.append("")
        try:
            tryEx = c2.index("")
        except:
            c2.pop()
            c2.append("")
        try:
            tryEx = c3.index("")
        except:
            c3.pop()
            c3.append("")
        try:
            tryEx = c4.index("")
        except:
            c4.pop()
            c4.append("")
        try:
            tryEx = c5.index("")
        except:
            c5.pop()
            c5.append("")
        try:
            tryEx = c6.index("")
            c6.append("")
        except:
            c6.pop()

        if(c1.index("") != 0 and cs[0] != ""):
            t1 = datetime.strptime(cs[0], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[0] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[0]-round(timeOnCourt, 2)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[1] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[1]-round(timeOnCourt, 2)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[2] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[2]-round(timeOnCourt, 2)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[3] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[3]-round(timeOnCourt, 2)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[4] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[4]-round(timeOnCourt, 2)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[5] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[5]-round(timeOnCourt, 2)
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
            if(c1.index("") != 0):
                minCol[0] = "lightgreen"
            else:
                minCol[0] = "white"
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
            if(c2.index("") != 0):
                minCol[1] = "lightgreen"
            else:
                minCol[1] = "white"
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
            if(c3.index("") != 0):
                minCol[2] = "lightgreen"
            else:
                minCol[2] = "white"
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
            if(c4.index("") != 0):
                minCol[3] = "lightgreen"
            else:
                minCol[3] = "white"
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
            if(c5.index("") != 0):
                minCol[4] = "lightgreen"
            else:
                minCol[4] = "white"
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
            if(c6.index("") != 0):
                minCol[5] = "lightgreen"
            else:
                minCol[5] = "white"
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
        if(cc[0] != "" and float(cc[0]) > 0.0 and float(cc[0]) <= 2.0):
            minCol[0] = "lightcoral"
        if(cc[0] != "" and float(cc[0]) > 2.0 and float(cc[0]) <= 5.0):
            minCol[0] = "yellow"
        if(cc[0] != "" and float(cc[0]) > 5.0):
            minCol[0] = "lightgreen"
        if(cc[1] != "" and float(cc[1]) > 0.0 and float(cc[1]) <= 2.0):
            minCol[1] = "lightcoral"
        if(cc[1] != "" and float(cc[1]) > 2.0 and float(cc[1]) <= 5.0):
            minCol[1] = "yellow"
        if(cc[1] != "" and float(cc[1]) > 5.0):
            minCol[1] = "lightgreen"
        if(cc[2] != "" and float(cc[2]) > 0.0 and float(cc[2]) <= 2.0):
            minCol[2] = "lightcoral"
        if(cc[2] != "" and float(cc[2]) > 2.0 and float(cc[2]) <= 5.0):
            minCol[2] = "yellow"
        if(cc[2] != "" and float(cc[2]) > 5.0):
            minCol[2] = "lightgreen"
        if(cc[3] != "" and float(cc[3]) > 0.0 and float(cc[3]) <= 2.0):
            minCol[3] = "lightcoral"
        if(cc[3] != "" and float(cc[3]) > 2.0 and float(cc[3]) <= 5.0):
            minCol[3] = "yellow"
        if(cc[3] != "" and float(cc[3]) > 5.0):
            minCol[3] = "lightgreen"
        if(cc[4] != "" and float(cc[4]) > 0.0 and float(cc[4]) <= 2.0):
            minCol[4] = "lightcoral"
        if(cc[4] != "" and float(cc[4]) > 2.0 and float(cc[4]) <= 5.0):
            minCol[4] = "yellow"
        if(cc[4] != "" and float(cc[4]) > 5.0):
            minCol[4] = "lightgreen"
        if(cc[5] != "" and float(cc[5]) > 0.0 and float(cc[5]) <= 2.0):
            minCol[5] = "lightcoral"
        if(cc[5] != "" and float(cc[5]) > 2.0 and float(cc[5]) <= 5.0):
            minCol[5] = "yellow"
        if(cc[5] != "" and float(cc[5]) > 5.0):
            minCol[5] = "lightgreen"



        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs, minCol=minCol, reserved=reserved)
    else:
        if(c1.index("") != 0 and cs[0] != ""):
            t1 = datetime.strptime(cs[0], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[0] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[0]-round(timeOnCourt, 2)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[1] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[1]-round(timeOnCourt, 2)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[2] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[2]-round(timeOnCourt, 2)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[3] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[3]-round(timeOnCourt, 2)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[4] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[4]-round(timeOnCourt, 2)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            if(reserved[5] == "white"):
                timeLeftFloat = MAX_TIME_ON_COURT-round(timeOnCourt, 2)
            else:
                timeLeftFloat = reserve_length[5]-round(timeOnCourt, 2)
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
            if(c1.index("") != 0):
                minCol[0] = "lightgreen"
            else:
                minCol[0] = "white"
            if(reserved[0] == "red"):
                reserved[0] = "white"
                reserve_length[0] = "0.0"
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
            if(c2.index("") != 0):
                minCol[1] = "lightgreen"
            else:
                minCol[1] = "white"
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
            if(c3.index("") != 0):
                minCol[2] = "lightgreen"
            else:
                minCol[2] = "white"
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
            if(c4.index("") != 0):
                minCol[3] = "lightgreen"
            else:
                minCol[3] = "white"
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
            if(c5.index("") != 0):
                minCol[4] = "lightgreen"
            else:
                minCol[4] = "white"
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
            if(c6.index("") != 0):
                minCol[5] = "lightgreen"
            else:
                minCol[5] = "white"
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
        if(cc[0] != "" and float(cc[0]) > 0.0 and float(cc[0]) <= 2.0):
            minCol[0] = "lightcoral"
        if(cc[0] != "" and float(cc[0]) > 2.0 and float(cc[0]) <= 5.0):
            minCol[0] = "yellow"
        if(cc[0] != "" and float(cc[0]) > 5.0):
            minCol[0] = "lightgreen"
        if(cc[1] != "" and float(cc[1]) > 0.0 and float(cc[1]) <= 2.0):
            minCol[1] = "lightcoral"
        if(cc[1] != "" and float(cc[1]) > 2.0 and float(cc[1]) <= 5.0):
            minCol[1] = "yellow"
        if(cc[1] != "" and float(cc[1]) > 5.0):
            minCol[1] = "lightgreen"
        if(cc[2] != "" and float(cc[2]) > 0.0 and float(cc[2]) <= 2.0):
            minCol[2] = "lightcoral"
        if(cc[2] != "" and float(cc[2]) > 2.0 and float(cc[2]) <= 5.0):
            minCol[2] = "yellow"
        if(cc[2] != "" and float(cc[2]) > 5.0):
            minCol[2] = "lightgreen"
        if(cc[3] != "" and float(cc[3]) > 0.0 and float(cc[3]) <= 2.0):
            minCol[3] = "lightcoral"
        if(cc[3] != "" and float(cc[3]) > 2.0 and float(cc[3]) <= 5.0):
            minCol[3] = "yellow"
        if(cc[3] != "" and float(cc[3]) > 5.0):
            minCol[3] = "lightgreen"
        if(cc[4] != "" and float(cc[4]) > 0.0 and float(cc[4]) <= 2.0):
            minCol[4] = "lightcoral"
        if(cc[4] != "" and float(cc[4]) > 2.0 and float(cc[4]) <= 5.0):
            minCol[4] = "yellow"
        if(cc[4] != "" and float(cc[4]) > 5.0):
            minCol[4] = "lightgreen"
        if(cc[5] != "" and float(cc[5]) > 0.0 and float(cc[5]) <= 2.0):
            minCol[5] = "lightcoral"
        if(cc[5] != "" and float(cc[5]) > 2.0 and float(cc[5]) <= 5.0):
            minCol[5] = "yellow"
        if(cc[5] != "" and float(cc[5]) > 5.0):
            minCol[5] = "lightgreen"
        


        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs, minCol=minCol, reserved=reserved)


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        correctUsername = "admin"
        correctPassword = "!firebirdsbadminton8"

        if(username == correctUsername and password == correctPassword):
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/3517245211658351284258/", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        global MAX_TIME_ON_COURT, c1, c2, c3, c4, c5, c6
        MAX_TIME_ON_COURT_STR = request.form['mton']
        if(MAX_TIME_ON_COURT_STR != ""):
            MAX_TIME_ON_COURT=float(MAX_TIME_ON_COURT_STR)
        reserve_court_str = request.form['courts']
        reserve_length_str = request.form['reserve_length']
        if(reserve_court_str != "" and reserve_length_str != ""):
            reserve_court = int(reserve_court_str)
            reserved[reserve_court-1] = "red"
            cs[reserve_court-1] = time.strftime("%H:%M:%S")
            if(reserve_court == 1):
                c1.clear()
                c1 = [""]*21
                c1[0] = "Reserved by Admin"
                c1[1] = " "
                c1[2] = " "
                c1[3] = " "
                reserve_length[0] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[0]
            if(reserve_court == 2):
                c2.clear()
                c2 = [""]*21
                c2[c2.index("")] = "Reserved by Admin"
                c2[1] = " "
                c2[2] = " "
                c2[3] = " "
                reserve_length[1] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[1]
            if(reserve_court == 3):
                c3.clear()
                c3 = [""]*21
                c3[c3.index("")] = "Reserved by Admin"
                c3[1] = " "
                c3[2] = " "
                c3[3] = " "
                reserve_length[2] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[2]
            if(reserve_court == 4):
                c4.clear()
                c4 = [""]*21
                c4[c4.index("")] = "Reserved by Admin"
                c4[1] = " "
                c4[2] = " "
                c4[3] = " "
                reserve_length[3] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[3]
            if(reserve_court == 5):
                c5.clear()
                c5 = [""]*21
                c5[c5.index("")] = "Reserved by Admin"
                c5[1] = " "
                c5[2] = " "
                c5[3] = " "
                reserve_length[4] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[4]
            if(reserve_court == 6):
                c6.clear()
                c6 = [""]*21
                c6[c6.index("")] = "Reserved by Admin"
                c6[1] = " "
                c6[2] = " "
                c6[3] = " "
                reserve_length[5] = float(reserve_length_str)
                cc[reserve_court-1] = reserve_length[5]

        

        return render_template("admin.html")
    else:
        return render_template("admin.html")


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)