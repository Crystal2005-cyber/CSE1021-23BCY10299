def get_non_empty(prompt):
    """Get a non-empty string from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer(prompt, minimum=None, maximum=None):
    """Get a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt, minimum=None):
    """Get a valid floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid amount.")


def get_choice(prompt, choices):
    """Get a choice from a list of valid choices."""
    while True:
        value = input(prompt).strip().lower()

        if value in choices:
            return value

        print("Invalid choice. Please try again.")