from datetime import datetime

def get_days_from_date(date_string):
    try:
        now = datetime.now().date()
        given_date = datetime.strptime(date_string,"%Y-%m-%d").date()
        difference = now - given_date
        return difference.days
    except ValueError:
        print("Nice try, please enter date in YYYY-MM-DD: ")

def main():
    date_string = input("Enter your date in YYYY-MM-DD format: ")
    result = get_days_from_date(date_string)
    print(result)

if __name__ == "__main__":
    main()

