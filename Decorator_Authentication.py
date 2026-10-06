def login_required(func):

    def wrapper(username):

        if username == "admin":
            return func(username)

        print("Access Denied")

    return wrapper


@login_required
def dashboard(username):
    print("Welcome to Dashboard")


dashboard("admin")
dashboard("user")