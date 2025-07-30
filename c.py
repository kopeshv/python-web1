from flask import Flask,request,render_template,redirect
import json,os

web=Flask(__name__) #crating object
@web.route("/",methods=["POST","GET"]) # creating a route with the methods of get and post
def home():
    rf=os.path.dirname(os.path.abspath(__file__)) # to find the current full path where we run this
                                                    # diname = cut the file name from the path
    df=os.path.join(rf,"data.json")                # join the a data file into currect folder path
    k=[] 
    ms=""
    with open(df,"r") as r:
        try:
            k = json.load(r)
        except json.JSONDecodeError: #if any line is not a proggrame line then it would run
            k = []
        
    if request.method=="POST":  #cheking that is there post method..?
        action=request.form.get("action")   # if we have many post method in a file then we can give a action name to call that particularly
        if action == "add": # it would run if the submit button passed the "add" on the action parameter.
            
            name=request.form["name"].capitalize() #these are the variable that inputed from html
            age=request.form["age"]
            dip=request.form["dip"].upper()
            num=request.form["num"]
            if num:
                num=request.form["num"]  
            else:
                 num="they didn't interest to give"  
            if age:
                age=request.form["age"]  
            else:
                age="they didn't interest to give"    
            if name and dip :
                k.append({"name":name,"age":age,"dipartment":dip,"number":num})
                ms="Student Data Has Added"
            else:
                ms="You Should Give Name And Age"
        elif action=="delete":
            dname=request.form["dname"].capitalize()
            ol=len(k)
            k=[i for i in k if i["name"] != dname]    # see this quary properly 
            if ol>len(k):
                ms="DELETED"
            else:
                ms="STUDENT NOT FUNDED"
        elif action=="show":
            ms="Student Datas"
            return render_template("index.html",msg=ms,li=k)
    with open(df,"w") as w:
        json.dump(k,w)    # we are writing the datas from k to json file
    return render_template("index.html",msg=ms)
        
               
                
                
web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
