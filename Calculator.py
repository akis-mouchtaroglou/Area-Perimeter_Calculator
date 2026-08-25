shape_choice = input("Choose one of the following shapes and input its corresponding number: \n  1. Rectangle(or Square) \n  2. Triangle \n  3. Circle \n  4. Trapezoid \nInput number here:")
while shape_choice not in ("1", "2", "3", "4"):
    shape_choice = input("\nYou can only input the corresponding number of a shape listed above \nInput number here:")

print("Shape selected: " , end="")
match shape_choice:
    case "1":
        print("Rectangle (or Square)")
        side1 = input("\nInsert the length of its first side \nInput number here:")
        while True:
            try:
                side1 = float(side1)
                break
            except ValueError:
                side1 = input("\nSides can only be numbers. \nInput number here:")
        
        side2 = input("\nInsert the length of its second side \nInput number here:")
        while True:
            try:
                side2 = float(side2)
                break
            except ValueError:
                side2 = input("\nSides can only be numbers. \nInput number here:")
        
        perim = (side1 + side2) * 2   
        area = side1 * side2
        if side1 == side2:
            end = "Square"
        else:
            end = "Rectangle"

    case "2":
        print("Triangle")
        base = input("\nInsert the length of its base \nInput number here:")
        while True:
            try:
                base = float(base)
                break
            except ValueError:
                base = input("\nThe base can only be a number. \nInput number here:")
        
        side2 = input("\nInsert the length of its first side \nInput number here:")
        while True:
            try:
                side2 = float(side2)
                break
            except ValueError:
                side2 = input("\nSides can only be numbers. \nInput number here:")
        
        side3 = input("\nInsert the length of its second side \nInput number here:")
        while True:
            try:
                side3 = float(side3)
                break
            except ValueError:
                side3 = input("\nSides can only be numbers. \nInput number here:")
        
        height = input("\nInsert its height \nInput number here:")
        while True:
            try:
                height = float(height)
                break
            except ValueError:
                height = input("\nthe height can only be a number. \nInput number here:")
        
        perim = base + side2 + side3 
        area = (base * height) / 2
        end = "Triangle"

    case "3":
        print("Circle")
        radius = input("\nInsert the length of its radius \nInput number here:")
        while True:
            try:
                radius = float(radius)
                break
            except ValueError:
                radius = input("\nThe radius can only be a number. \nInput number here:")
        
        perim = radius * 2 * 3.14
        area = radius**2 * 3.14
        end = "Circle"

    case "4":
        print("Trapezoid")
        small_base = input("\nInsert the length of its small base \nInput number here:")
        while True:
            try:
                small_base = float(small_base)
                break
            except ValueError:
                small_base = input("\nThe base can only be a number. \nInput number here:")
        
        big_base = input("\nInsert the length of its big base \nInput number here:")
        while True:
            try:
                big_base = float(big_base)
                break
            except ValueError:
                big_base = input("\nThe base can only be a number. \nInput number here:")
        
        leg1 = input("\nInsert the length of its first leg \nInput number here:")
        while True:
            try:
                leg1 = float(leg1)
                break
            except ValueError:
                leg1 = input("\nThe base can only be a number. \nInput number here:")
        
        leg2 = input("\nInsert the length of its second leg \nInput number here:")
        while True:
            try:
                leg2 = float(leg2)
                break
            except ValueError:
                leg2 = input("\nThe base can only be a number. \nInput number here:")
        
        height = input("\nInsert its height \nInput number here:")
        while True:
            try:
                height = float(height)
                break
            except ValueError:
                height = input("\nthe height can only be a number. \nInput number here:")
        
        perim = small_base + big_base + leg1 + leg2 
        area = ((small_base + big_base) * height) / 2
        end = "Trapezoid"

print(f"The perimeter of the {end} is {perim}")
print(f"The area of the {end} is {area}")