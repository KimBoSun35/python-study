from flask import Flask, render_template, request

#Flask 사용 app이라는 변수로 선언
app=Flask(__name__)

#최상위 경로 "/"어떤거로 return할거냐
@app.route('/')
def index():
   return render_template("index.html")

@app.route('/data',methods=['POST'])
def data():
   input_data=request.form.get("input_data")
   return f"<h3>입력된 데이터:{input_data}</h3>"

if __name__=="__main__":

   app.run(host='0.0.0.0', port=8888)