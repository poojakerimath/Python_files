class Library:
    def __init__(self, title,author,availability_status):
        self.title = title
        self.author = author
        self.availability_status = availability_status

    def display_details(self):
        print(f"title: {self.title},author: {self.author},availability_status: {self.availability_status}")  
     
    def update_availability(self,availability_status):
        self.update_availability = availability_status
        print(f"availability_status:{self.availability_status}")

lib1 = Library("romeo and juliet","george","avail")
lib2 = Library("Ramayan","valmiki","avail")

lib1.display_details()
lib2.display_details()

lib1.update_availability("not avail")
lib2.update_availability("avail")

print(isinstance(lib1,Library))
print(isinstance(lib2,Library))