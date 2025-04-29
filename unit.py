

def convert_units(value: float, unit_from: str, unit_to: str):
    print("value>>>", value)
    print("unit_from>>>", unit_from)
    print("unit_to>>>", unit_to)
convert_units(1.9, "kilometer", "meter")    
convert_units(1.9, "kilometer", "mile")
convert_units(1.9, "kilometer", "centimeter")
convert_units(1.9, "kilometer", "millimeter")
convert_units(1.9, "kilometer", "inch")
convert_units(1.9, "kilometer", "foot")
convert_units(1.9, "kilometer", "yard")
convert_units(1.9, "kilometer", "nautical mile")
convert_units(1.9, "kilometer", "light year")

# 1. 9 kilometer = 1900 meter
# 2. 9 kilometer = 1.1808 mile
# 3. 9 kilometer = 190000 centimeter
# 4. 9 kilometer = 1900000 millimeter
# 5. 9 kilometer = 74803.1 inch
# 6. 9 kilometer = 6233.6 foot
# 7. 9 kilometer = 2099.99 yard
# 8. 9 kilometer = 1.024 nautical mile

if __name__ == "__main__":
    # Test the function with some example values
    print(convert_units(1.9, "kilometer", "meter"))  # 1900.0
    print(convert_units(1.9, "kilometer", "mile"))   # 1.1808
    print(convert_units(1.9, "kilometer", "centimeter"))  # 190000.0
    print(convert_units(1.9, "kilometer", "millimeter"))  # 1900000.0
    print(convert_units(1.9, "kilometer", "inch"))   # 74803.1
    print(convert_units(1.9, "kilometer", "foot"))   # 6233.6
    print(convert_units(1.9, "kilometer", "yard"))   # 2099.99
    print(convert_units(1.9, "kilometer", "nautical mile"))  # 1.024
    
    
    
def convert_units(value: float, unit_from: str, unit_to: str):
    
     if(unit_from == "kilometer" and unit_to == "meter"):
          return value * 1000
convert_units(1.9, "kilometer", "meter")  # 1900.0
result = convert_units(1.9, "kilometer", "meter")
print("The value of meter is:", result)  # 1900.0
result = convert_units(1, "kilometer", "mile")
print("The value of mile is:", result)  # 1.0
result = convert_units(7, "kilometer", "centimeter")
print("The value of centimeter is:", result)  # 700000.0
result = convert_units(9, "kilometer", "millimeter")
print("The value of millimeter is:", result)  # 9000000.0
result = convert_units(5, "kilometer", "inch")
print("The value of inch is:", result)  # 196850.4