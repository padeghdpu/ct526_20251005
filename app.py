from flask import Flask , render_template 
import re


app = Flask(__name__)


@app.route("/")
def indexpage():
   return render_template("index.html")


@app.route("/tech")
def technology():
   topic = "เทคโนโลยีที่สนใจ"
   techinterest = [ 
      "Secured Software Development" , 
      "Machine Learning" ,
      "Block Chain Technology" ,
      "Internet of thing" , 
      "Embedded Systems"  , 
      "Real-time operating system"    
   ]

   return render_template("technology.html" , title=topic, techinterest=techinterest)

 
@app.route("/myid")
def myid():
   myid = 68130039
   return render_template("myid.html" , id=myid )
 

displaymsg="Please enter integer value and more than 0"


@app.route("/draw/")
def drawnull():
   disp_err = displaymsg  
   return render_template("draw.html" , defmsg=disp_err)    


@app.route("/draw/<inputnumber>")
def draw( inputnumber):   
   res = [] 
   disp_err = ""

   x = re.findall("[1-9]", inputnumber )

   if x:
      inputval =  int(inputnumber)       
      inputval  = inputval + 1
      if inputval > 0:
         for round in range ( 0 , inputval  ) :   
            symbol =  "" 
            output =  ""
            for addsym in range ( 1 , round + 1):
               symbol  = symbol + "x"
               output = "แสดงแถวที่ "  + str(addsym ) + " : " + symbol
            res.append (output)
   else:
      res = []
      disp_err = displaymsg  
 
   return render_template("draw.html" , result=res , defmsg=disp_err )    

 
 
if __name__ == "__main__":
   app.run( host='0.0.0.0' , debug=True, port=80 )
 
