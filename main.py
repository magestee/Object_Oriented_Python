class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindore", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Missing House")
        
        self.name = name
        self.house = house
    
    def get_patronous(self):
        if self.name == "Harry":
            print("🦌")
        elif self.name == "Ron":
            print("🐕")
        else:
            print("🪄")

def main():
    student = get_student()
    print(f"{ student.name } from {student.house}")
    student.get_patronous()

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()