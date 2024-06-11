# Slope Calculator

def calculate_slope(x1, y1, x2, y2):
    """
    Calculates the slope of a line given two points (x1, y1) and (x2, y2).

    Args:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point

    Returns:
        tuple: (slope, y-intercept) of the line in slope-intercept form
    """
    if x1 == x2:
        return "Undefined"  # This means that the equation is a vertical line
    else:
        slope = (y2 - y1) / (x2 - x1)
        y_intercept = y1 - slope * x1
        return slope, y_intercept

def main():
    print("Slope Calculator")
    print("Enter 'new' to create a new equation, or 'quit' to exit the program.")

    while True:
        user_input = input("What would you like to do? ")

        if user_input.lower() == 'new':
            print("Enter the x and y coordinates of two points on the line to create the Slope-Intercept Form")

            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))

            result = calculate_slope(x1, y1, x2, y2)

            if result == "Undefined":
                print("The slope is undefined meaning it is a vertical line.")
            else:
                slope, y_intercept = result
                if slope == 1:
                    slope_str = ""
                elif slope == -1:
                    slope_str = "-"
                else:
                    slope_str = f"{slope:.2f}"
                if y_intercept == 0:
                    y_intercept_str = ""
                elif y_intercept > 0:
                    y_intercept_str = f" + {y_intercept:.2f}"
                else:
                    y_intercept_str = f" - {-y_intercept:.2f}"
                print(f"The equation of the line is: y = {slope_str}x{y_intercept_str}")

        elif user_input.lower() == 'quit':
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()