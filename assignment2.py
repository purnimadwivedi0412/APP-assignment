# Decorator to format the report
def report_formatter(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("        DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        result = func(*args, **kwargs)
        print("=" * 50)
        return result
    return wrapper


class Report:
    # Class variable
    default_template = "General Report"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class Method
    @classmethod
    def set_template(cls, template):
        cls.default_template = template

    # Magic Method
    def __str__(self):
        return f"Template : {Report.default_template}\nTitle    : {self.title}\nContent  : {self.content}"

    # Magic Method
    def __len__(self):
        return len(self.content)

    # Decorated Method
    @report_formatter
    def generate_report(self):
        print(self)

    # Formatting Method
    def format_report(self, style):
        if style.lower() == "uppercase":
            self.title = self.title.upper()
            self.content = self.content.upper()

        elif style.lower() == "lowercase":
            self.title = self.title.lower()
            self.content = self.content.lower()

        elif style.lower() == "title":
            self.title = self.title.title()
            self.content = self.content.title()

        else:
            print("Invalid formatting option!")


# ---------------- MAIN PROGRAM ----------------

# Set report template using class method
Report.set_template("College Project Report")

# User Input
title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

report = Report(title, content)

print("\nChoose Formatting Option")
print("1. Uppercase")
print("2. Lowercase")
print("3. Title Case")

choice = input("Enter choice: ")

if choice == "1":
    report.format_report("uppercase")
elif choice == "2":
    report.format_report("lowercase")
elif choice == "3":
    report.format_report("title")
else:
    print("No Formatting Applied")

# Generate Report
report.generate_report()

# Using Magic Method __len__
print("\nContent Length:", len(report))


#output
#Enter Report Title: college student report
#Enter Report Content: python concept
#Choose Formatting Option
#1. Uppercase
#2. Lowercase
#3. Title Case
#Enter choice: 1
#==================================================
#        DYNAMIC REPORT GENERATOR
#==================================================
#Template : College Project Report
#Title    : COLLEGE STUDENT REPORT
#Content  : PYTHON CONCEPT
#==================================================
#content Length: 14