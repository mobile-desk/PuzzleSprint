def generate_leap_years(start_year, count):
    leap_years = []
    current_year = start_year

    while len(leap_years) < count:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            leap_years.append(current_year)
        current_year += 1

    return leap_years

# Example
next_20_leap_years = generate_leap_years(2023, 20)
print(next_20_leap_years)