from flask import Flask, redirect, url_for, render_template, request
import time, atexit
from datetime import datetime


c1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c3 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c4 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c5 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
c6 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

cc = ["", "", "", "", "", ""]

cs = ["", "", "", "", "", ""]

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        courtNum = request.form["courts"]
        nm1 = request.form["nm1"]
        nm2 = request.form["nm2"]
        nm3 = request.form["nm3"]
        nm4 = request.form["nm4"]
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
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[5] = str(timeLeftFloat)



        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs)
    else:
        if(c1.index("") != 0 and cs[0] != ""):
            t1 = datetime.strptime(cs[0], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[0] = str(timeLeftFloat)
        if(c2.index("") != 0 and cs[1] != ""):
            t1 = datetime.strptime(cs[1], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[1] = str(timeLeftFloat)
        if(c3.index("") != 0 and cs[2] != ""):
            t1 = datetime.strptime(cs[2], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[2] = str(timeLeftFloat)
        if(c4.index("") != 0 and cs[3] != ""):
            t1 = datetime.strptime(cs[3], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[3] = str(timeLeftFloat)
        if(c5.index("") != 0 and cs[4] != ""):
            t1 = datetime.strptime(cs[4], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[4] = str(timeLeftFloat)
        if(c6.index("") != 0 and cs[5] != ""):
            t1 = datetime.strptime(cs[5], "%H:%M:%S")
            t2 = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
            delta = t2-t1
            timeOnCourt = delta.total_seconds()/60
            timeLeftFloat = 10.0-round(timeOnCourt, 1)
            cc[5] = str(timeLeftFloat)



        return render_template("index.html", c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, cc=cc, cs=cs)


if __name__ == "__main__":
    app.run(debug=True)