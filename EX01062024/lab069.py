def is_leap_year(year):
    # Leap year is divisible by 4, but not divisible by 100 unless divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = 2024  # Change this value to test different years
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
