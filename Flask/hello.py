from flask import Flask, request, jsonify
app = Flask(__name__)

courses= {
    "courses":[
    {
        "id": 1,
        "course_name": "Introduction to Python",
        "fee": 150.00,
        "description": "Learn the basics of Python programming, including syntax, variables, and basic operations."
    },
    {
        "id": 2,
        "course_name": "Data Science with Python",
        "fee": 300.00,
        "description": "Explore data science concepts using Python, including data manipulation, visualization, and machine learning."
    },
    {
        "id": 3,
        "course_name": "Web Development with JavaScript",
        "fee": 250.00,
        "description": "A comprehensive course on front-end and back-end web development using JavaScript, HTML, and CSS."
    },
    {
        "id": 4,
        "course_name": "Machine Learning Basics",
        "fee": 400.00,
        "description": "An introductory course to machine learning concepts, covering supervised and unsupervised learning algorithms."
    },
    {
        "id": 5,
        "course_name": "Database Management",
        "fee": 200.00,
        "description": "Learn the fundamentals of relational databases, SQL, and database management techniques."
    },
    {
        "id": 6,
        "course_name": "Cloud Computing Essentials",
        "fee": 350.00,
        "description": "An overview of cloud computing principles, cloud services, and deployment models with hands-on examples."
    },
    {
        "id": 7,
        "course_name": "Introduction to Cybersecurity",
        "fee": 280.00,
        "description": "Understand the basics of cybersecurity, including common threats, security practices, and defense mechanisms."
    },
    {
        "id": 8,
        "course_name": "Mobile App Development",
        "fee": 500.00,
        "description": "Learn to build mobile applications for Android and iOS using popular frameworks and tools."
    }
    ]
}

#default call
@app.route('/')
def index():
    return "Hellow world!"

#Get call in flask
@app.route('/courses',methods=['GET'])
def geting():
    return jsonify({'courses':courses})

#getting the data with id or maching parameters
@app.route('/couses/<int:id>',methods=['GET'])
def get_course(id):
    return jsonify({'courses':courses["courses"][id-1]})

#POST call
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    return data

if __name__== "__main__":
    app.run(debug=True)

