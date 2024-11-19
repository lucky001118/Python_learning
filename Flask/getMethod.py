# Dictionary of courses with dummy data
courses = {
    1: {
        "course_name": "Introduction to Python",
        "fee": 150.00,
        "description": "Learn the basics of Python programming, including syntax, variables, and basic operations."
    },
    2: {
        "course_name": "Data Science with Python",
        "fee": 300.00,
        "description": "Explore data science concepts using Python, including data manipulation, visualization, and machine learning."
    },
    3: {
        "course_name": "Web Development with JavaScript",
        "fee": 250.00,
        "description": "A comprehensive course on front-end and back-end web development using JavaScript, HTML, and CSS."
    },
    4: {
        "course_name": "Machine Learning Basics",
        "fee": 400.00,
        "description": "An introductory course to machine learning concepts, covering supervised and unsupervised learning algorithms."
    },
    5: {
        "course_name": "Database Management",
        "fee": 200.00,
        "description": "Learn the fundamentals of relational databases, SQL, and database management techniques."
    },
    6: {
        "course_name": "Cloud Computing Essentials",
        "fee": 350.00,
        "description": "An overview of cloud computing principles, cloud services, and deployment models with hands-on examples."
    },
    7: {
        "course_name": "Introduction to Cybersecurity",
        "fee": 280.00,
        "description": "Understand the basics of cybersecurity, including common threats, security practices, and defense mechanisms."
    },
    8: {
        "course_name": "Mobile App Development",
        "fee": 500.00,
        "description": "Learn to build mobile applications for Android and iOS using popular frameworks and tools."
    }
}

# Accessing course data by ID
course_id = 1  # Replace with any course ID you want to look up
course = courses.get(course_id)

if course:
    print(f"Course ID: {course_id}")
    print(f"Name: {course['course_name']}")
    print(f"Fee: ${course['fee']}")
    print(f"Description: {course['description']}")
else:
    print(f"Course with ID {course_id} not found.")
print(courses[1])