def register_class(course_number, course_prefix='Comp'):
    print(f"Let's register for {course_prefix}{course_number}")

def main():
    register_class(152)
    register_class(161, "Math")


main()
