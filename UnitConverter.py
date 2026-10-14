# 22th gothub project --> Unit converter
print('----------Unit Converter----------')
def show_menu():
    print_separator()
    print("UNIT CONVERTER".center(40))
    print_separator()
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Speed")
    print("5. Area")
    print("6. Volume")
    print("7. Quit")
    print_separator()


def print_separator():
    print("=" * 40)


def print_title(title):
    print_separator()
    print(title.center(40))
    print_separator()


def get_choice(prompt, valid_options):
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        options_text = ", ".join(valid_options)
        print(f"Invalid choice. Please enter one of: {options_text}")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def build_unit(name, factor):
    return {"name": name, "factor": factor}


LENGTH_UNITS = {
    "1": build_unit("Meters", 1.0),
    "2": build_unit("Kilometers", 1000.0),
    "3": build_unit("Centimeters", 0.01),
    "4": build_unit("Millimeters", 0.001),
    "5": build_unit("Miles", 1609.344),
    "6": build_unit("Yards", 0.9144),
    "7": build_unit("Feet", 0.3048),
    "8": build_unit("Inches", 0.0254),
}

WEIGHT_UNITS = {
    "1": build_unit("Kilograms", 1.0),
    "2": build_unit("Grams", 0.001),
    "3": build_unit("Milligrams", 0.000001),
    "4": build_unit("Pounds", 0.453592),
    "5": build_unit("Ounces", 0.0283495),
    "6": build_unit("Metric Tons", 1000.0),
}

SPEED_UNITS = {
    "1": build_unit("Meters per second", 1.0),
    "2": build_unit("Kilometers per hour", 0.277778),
    "3": build_unit("Miles per hour", 0.44704),
    "4": build_unit("Knots", 0.514444),
    "5": build_unit("Feet per second", 0.3048),
}

AREA_UNITS = {
    "1": build_unit("Square meters", 1.0),
    "2": build_unit("Square kilometers", 1000000.0),
    "3": build_unit("Square feet", 0.092903),
    "4": build_unit("Square yards", 0.836127),
    "5": build_unit("Acres", 4046.86),
    "6": build_unit("Hectares", 10000.0),
}

VOLUME_UNITS = {
    "1": build_unit("Liters", 1.0),
    "2": build_unit("Milliliters", 0.001),
    "3": build_unit("Cubic meters", 1000.0),
    "4": build_unit("Gallons (US)", 3.78541),
    "5": build_unit("Quarts (US)", 0.946353),
    "6": build_unit("Cups (US)", 0.236588),
    "7": build_unit("Fluid ounces (US)", 0.0295735),
}

TEMPERATURE_UNITS = {
    "1": {"name": "Celsius", "symbol": "C"},
    "2": {"name": "Fahrenheit", "symbol": "F"},
    "3": {"name": "Kelvin", "symbol": "K"},
}

CATEGORIES = {
    "1": {"name": "Length", "units": LENGTH_UNITS},
    "2": {"name": "Weight", "units": WEIGHT_UNITS},
    "3": {"name": "Temperature", "units": TEMPERATURE_UNITS},
    "4": {"name": "Speed", "units": SPEED_UNITS},
    "5": {"name": "Area", "units": AREA_UNITS},
    "6": {"name": "Volume", "units": VOLUME_UNITS},
}


def convert_linear(value, from_factor, to_factor):
    value_in_base = value * from_factor
    return value_in_base / to_factor


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def to_celsius(value, symbol):
    if symbol == "C":
        return value
    if symbol == "F":
        return fahrenheit_to_celsius(value)
    return kelvin_to_celsius(value)


def from_celsius(celsius, symbol):
    if symbol == "C":
        return celsius
    if symbol == "F":
        return celsius_to_fahrenheit(celsius)
    return celsius_to_kelvin(celsius)


def convert_temperature(value, from_symbol, to_symbol):
    if from_symbol == to_symbol:
        return value

    celsius = to_celsius(value, from_symbol)
    return from_celsius(celsius, to_symbol)


def show_units(units):
    print()
    for key, unit in units.items():
        print(f"{key}. {unit['name']}")


def pick_unit(units, prompt):
    show_units(units)
    valid_keys = list(units.keys())
    return get_choice(prompt, valid_keys)


def show_result(value, from_name, result, to_name):
    print(f"\n{value} {from_name} = {result:.4f} {to_name}")


def run_linear_conversion(category_name, units):
    print_title(f"{category_name} Conversion")

    from_key = pick_unit(units, "Convert from: ")
    to_key = pick_unit(units, "Convert to: ")

    value = get_number("Enter value: ")

    from_unit = units[from_key]
    to_unit = units[to_key]

    result = convert_linear(value, from_unit["factor"], to_unit["factor"])
    show_result(value, from_unit["name"], result, to_unit["name"])


def run_temperature_conversion():
    print_title("Temperature Conversion")

    from_key = pick_unit(TEMPERATURE_UNITS, "Convert from: ")
    to_key = pick_unit(TEMPERATURE_UNITS, "Convert to: ")

    value = get_number("Enter value: ")

    from_unit = TEMPERATURE_UNITS[from_key]
    to_unit = TEMPERATURE_UNITS[to_key]

    result = convert_temperature(value, from_unit["symbol"], to_unit["symbol"])
    show_result(value, from_unit["name"], result, to_unit["name"])


def run_category(choice):
    if choice == "3":
        run_temperature_conversion()
        return

    category = CATEGORIES[choice]
    run_linear_conversion(category["name"], category["units"])


def ask_to_convert_again():
    answer = input("\nConvert again? (yes/no): ").strip().lower()
    return answer in ("yes", "y")


def main():
    while True:
        show_menu()

        valid_choices = list(CATEGORIES.keys()) + ["7"]
        choice = get_choice("Choose a category: ", valid_choices)

        if choice == "7":
            print("\nGoodbye!")
            return

        run_category(choice)

        if not ask_to_convert_again():
            print("Goodbye!")
            return

        print()



main()