def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    student = (input("Name: "), input("House: "))
    return student

if __name__ == "__main__":
    main()
