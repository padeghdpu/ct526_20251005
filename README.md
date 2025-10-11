# ct526_20251005
assignment CT526  , assigned date 20251005




### คำอธิบายของ Assignment 20251005

การพัฒนา web ด้วยการใช้ framework flask 

ก่อนเริ่มการพัฒนาโปรแกรม ด้วย Flask Framework เราจะต้องทำการติดตั้ง Flask Framework เสียก่อน แต่อย่างไรก็ตาม เพื่อให้ระบบทำงานได้อย่างมีประสิทธิภาพ  เราควรที่จะพัฒนาโปรแกรมภาบใต้ VIrtual Environment สาเหตุเนื่องจาก การที่เราทำการติดตั้ง python ในรูปแบบ GLobal จะมีปัญหาเมื่อเรามีความต้องการ พัฒนาหลายโปรแกรม และแต่ละโปรแรกม อาจจะมีความจำเป็นที่จะต้องติดตั้ง Python ที่ต่าง versionกัน  ด้วยเหตุผลดังกล่าว จึงก่อให้เกิดปัญหาเรื่อง การ conflict version ของ python  ดังนั้นเพื่อให้สามารถ รองรับเงื่อนไขดังกล่าวได้ และไม่ให้มีการ conflict ระหว่างกัน จึงเลือกใช้งาน แบบ Virtual Environment




### 1. การสร้าง Virtual Environment

##### 1.1 Create Virtual Environment

สามารถสร้างได้โดยเริ่มต้นจากการสร้าง folder ขึ้นมา เพื่อให้เป็น ชื่อ Project ของโปรแกรมที่เราต้องการ โดยจะใช้คำสั่ง ดังนี้ 

```
$yourprompt> python -m venv [ ชื่อของ Virtual Environment หรือ ก็คือชื่อ folder ]

ซึ่งในกรณีนี้ จะใช้ชื่อ folder คือ ct526

$yourprompt> python -m venv ct526
```


:::warning

ข้อสังเกตุ เมื่อระบบทำการสร้าง Virtual Environment ขึ้นมาสำเร็จแล้ว จะพบว่ามี file และ folder จำนวหนึ่งขึ้นมาภายใน folder ดังกล่าว 

:::

##### 1.2 Activate Virtual Environemt

- หลังจากที่ได้สร้างพื้นที่ของ Virtual Environment แล้ว ในขั้นตอน ต่อไป จะต้องทำการ activate ให้เริ่มทำงาน โดยใช้คำสั่ง


```
$yourprompt> env\Scripts\activate

โดยที่ env คือ ชื่อของ Virtual Environment หรือ ก็คือชื่อ folder

ซึ่งในที่นี้ จะใช้ชื่อ folder คือ ct526 

$yourprompt> ct526\Scripts\activate
```

- เมื่อขั้นตอนนี้สำเร็จ ระบบจะมีการเปลี่ยน prompt ไปเป็นอีกแบบตามด้านล่างนี้

```
(ct526) $yourprompt> 
```

### 2. ติดตั้ง Framework Flask

- ทำการติดตั้ง Framework Flask  โดยก่อนการติดตั้ง ควรทำการตรวจสอบว่าขณะนี้กำลังอยู่ใน path ของ project หรือไม่ โดยสังเกตว่า จะต้องอยู่ที่ path ระดับเดียวกันกับ file ชื่อ  pyvenv.cfg  โดยใช้คำสั่งในการติดตั้ง คือ 

```
pip install flask

```

- เมื่อขั้นตอนนี้สำเร็จ สามารถตรวจสอบได้โดย เข้าไปใน folder ชื่อ Lib\site-packages จะพบ folder ที่มีชื่อ flask ปรากฏขึ้นมา ก็ถือได้ว่าพร้อมใช้งาน

```
(ct526) $yourprompt>
```


### 3. เริ่มพัฒนาโปรแกรม
- ในการพัฒนาโปรแกรม หากต้องการใช้งาน Flask Framework จะต้องทำการ Import flask class เข้ามา ด้วยคำสั่ง
- ทำการ สร้าง instance ของ class ของ Flask  
- ใช้ route decorator เพื่อจะบอกให้ flask รู้ว่า ที่ URL ที่กำหนดอยู๋ใน วงเล็บ นั้น จะต้องให้ทำการไป trig function ชื่ออะไร 
- หลังจากนั้นโปรแกรมก็จะ run ตามกระบวนการตามที่จ้องการ 
- และเมื่อประมวลผลสำเร็จ จะทำการ return ค่า ออกไปแสดงที่ html file , พร้อมกับ สามารถมีค่า parameter ต่างได้ โดยค่า parameter นี้ จะสามารถ เป็น data type ที่เป็น String , NUmber และ เป็นแบบ array ได้ 
- if __name__ == '__main__'  เป็นการบอกให้ python ให้แน่ใจว่า โค้ดที่อยู่ภายใน file ที่กำลัง run อยู่นี้ เป็น file ที่ต้องการให้ run เป็นโปรแกรมหลัก 
- สามารถกำหนด port ที่ต้องการได้ โดยการ กำหนด ที่ parameter ชื่อว่า port อย่างไรก็ตาม จะต้องเป็น port ที่ไม่ได้ถูกใช้งาน จาก Applicationอื่นๆ เช่น Mysql ใช้ port number = 3306  หากตั้ง Port Number ตรงกัน จะทำให้ MySql ทำงานไม่ได้ 


**file program  ชื่อ app.py**


```
from flask import Flask , render_template 

app = Flask(__name__)


@app.route("/")
def indexpage():
   message = "Hello World"

   somedataset = [ 
      "dataone" , 
      "datatwo" , 
      "datathree" , 
      "datafour" , 
   ]

   return render_template("index.html"  , message , somedataset )



if __name__ == "__main__":
   app.run(port=80 ,debug=True)


```

### 4. Run โปรแกรม

- หลังจากที่ทำการ Coding เป็นที่เรียบร้อย แล้ว ต้องการที่จะ run โปรแกรม ให้ใช้คำสั่ง ต่อไปนี้ 

```
python <file ที่ต้องการให้เป็น โปรแกรมหลัก>

ในตัวอย่างนี้ คือ file ชื่อ  app.py


(ct526) $yourprompt> python app.py

และ ระบบจะมีข้อความดังต่อไปนี้ ออกมา โดยฝนภาพจะเป็น ตัวอย่าง เท่านั้น ในของจริง อาจจะมี ข้อความ ออกมามากกว่านี้

* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:80
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!



```



### 5. เปิด Browser 

ใส่ URL  http://localhost:80  หรือ  http://127.0.0.1:80


**ในขณะที่ web server กำลังทำงาน**

- เมื่อ ผู้ใช้งาน เรียก ใช้งาน browser จาก URL ที่มีอนู๋ในโปรแกรม เข่นในกรณีตัวอย่างนี้ เมื่อ ผู้ใช้งาน เรียก path ที่มีการกำหนดไว้  Flask จะรับรู้ และ ไป trig function ที่อยู๋บรรทัดติดกัน ให้ทำงาน และทำการ return ค่าต่างๆ เข้าไปยัง index.html (หรือ ชื่อ file อื่นๆก็ได้)
- สามารถส่งข้อความ "Hello World" เข้าไปยัง index.html ผ่านไปทาง ตัวแปรที่ชื่อ message
- สามารถส่งข้อมูลตัวแปร List " เข้าไปยัง index.html ผ่านไปทาง ตัวแปรที่ชื่อ somedataset

 
```
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Simple Web using Python Flask</title>

</head>
<body>

<p>{{ message }}</p>

<img src="/static/<imgfile>"



</body>
</html>


```



 


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


### ขั้นตอนการ Clone Project เพื่อไปทำการ run โปรแกรม

#### 1. สร้าง Web Server

##### 1. ทำการ Clone code มาจาก repository บน Github

```
$yourprompt>git clone [ ชื่อ folder ของ repo]

ซึ่งในassignment นี้ ชื่อ fodler คือ ct526_20251005

$yourprompt>git clone ct526_20251005


```





##### 2. Installation Virtual Environment

- **1. สร้าง virtual Environment**  

สามารถสร้างได้โดยเริ่มต้นจากการสร้าง folder ที่ขื่อเดียวกันกับ path ของ repo ที่จะถูกสร้างขึ้นมา ขั้นตอนนี้ทำครั้งเดียว ในการใช้งานครั้ง ต่อไป ไม่ต้องติดตั้งซ้ำ โดยจะใช้คำสั่ง ดังนี้ 

```
$yourprompt>python -m venv [ ชื่อของ Virtual Environment หรือ ก็คือชื่อ folder ]

ซึ่งในassignment นี้จะใช้ชื่อ folder คือ ct526_20251005

$yourprompt>python -m venv ct526_20251005

```
ระบบจะทำการสร้าง Virtual Envorpnment ขึ้นมาโดยจะมี file และ folder ขึ้นมาภายใน ทั้งนี้ จะยังคงต้องมี file ในส่วนที่เรา clone มาจาก repo บน github ซึ่งจะต้องไม่ถูกทับ หรือ ลบ หายไป 


- **2. Activate Virtual Environemt**

- หลังจากที่ได้สร้างพื้นที่ของ Virtual Environment แล้ว ในขั้นตอน ต่อไป ก็คือ การ activate ให้เริ่มทำงาน โดยใช้คำสั่ง


```
$yourprompt>[ ชื่อของ Virtual Environment หรือ ก็คือชื่อ folder ]\Scripts\activate

ซึ่งในassignment นี้จะใช้ชื่อ folder คือ ct526_20251005

$yourprompt>ct526_20251005\Scripts\activate

```

- เมื่อขั้นตอนสำเร็จ ระบบจะมีการเปลี่ยน prompt ไปเป็นอีกแบบ ด้านล่างนี้ 

```
(ct526_20251005) $yourprompt> 

```

- **3. ทำการทดสอบ Run โปรแกรม**

เมื่อต้องการ run โปรแกรม  ให้ใช้คำสั่ง python app.py


```
(ct526_20251005) $yourprompt>python app.py

```

เปิด Browser บนเครื่องของท่าน โดยให้เรียกใช้งาน ด้วย URL คือ  http://localhost:5000 หรือ อาจจะมีการเปลี่ยนไปที่ port80 ก็ให้เรียกไปที่ http://localhost:80



