from flask import Flask, request    #导入Flask类
app = Flask(__name__)  # 实例化flask

class Student():

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    # toString
    # def __repr__(self):
    #         return f"Student[id={self.id},name={self.name},age={self.age}]"

@app.route("/api/post/json",methods=["POST"])
def testPostJson():
    id = request.json.get("id")
    name = request.json.get("name")
    age = request.json.get("age")
    stu = Student(id,name,age)
    # print(stu)
    return "测试OK了！"


if __name__ == '__main__':
    app.run(debug=True)

