import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    
@app.route("/submitJSON", methods=["POST"])
def processJSON():
    jsonStr = request.get_json()
    #print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    l=jsonObj['l'].split(',')
    k=int(jsonObj['k'])
    max=0
    max_ele=""
    maxlist=[]
    freq=[]
    for i in range(k):
        max=0
        for j in range(len(l)):
            c=l.count(l[j])
            if (c>=max) and (l[j] not in maxlist) :
                max=c
                max_ele=l[j]
        if max_ele not in maxlist:
            maxlist.append(max_ele)
            freq.append(max)
    for g in range(len(maxlist)):
        response+="Item {} with frequency {} <br>".format(maxlist[g],freq[g])
    return response
  
if __name__ == "__main__":
   app.run(debug=True)
    
    
