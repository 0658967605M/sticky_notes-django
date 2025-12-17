class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

#''' Add another method in the Course class that prints 
# the head office location: Cape Town'''

    def head_office_location(self):
        print("Head Office Location: Cape Town")

 # Create a subclass of the Course class   
class OOPCourse(Course):
    # Override the course name for this specific course
    name = "Object-Oriented Programming"

# '''Make a constructor that initialises two instance
# attributes with default values ''' 
    
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # Method to display course details
    
    def course_details(self):
        print("Course Name:", self.name)
        self.contact_details()
        self.head_office_location()
    
# Method to display trainer details
   
    def trainer_details(self):
        print("Course Description:", self.description)
        print("Trainer Name:", self.trainer)
        print("Course Name:", self.name)

# '''Make a method in the OOPCourse subclass named show_course_id 
# that prints the ID number of the course'''
    
    def show_course_id(self):
        print("Course ID Number: #12345")

# '''Create an object of the OOPCourse subclass called course_1 
# and call the methods'''

course_1 = OOPCourse()
course_1.course_details()
course_1.trainer_details()
course_1.show_course_id()
