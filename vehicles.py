# vehicles.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

def main():
    # Create a dictionary that contains data about six vehicles.
    # The key for each vehicle in the dictionary is the vehicle's
    # identification number (VIN). The value for each vehicle is
    # a list that contains the year, manufacturer, model, color,
    # engine design, and engine displacement.
    vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    YEAR_INDEX = 0
    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3
    ENG_DESIGN_INDEX = 4
    ENG_DISPLACE_INDEX = 5

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    # Check if the vin is a key that is in the vehicles dictionary.
    if vin in vehicles:
        car_qualities = vehicles[vin]


        # Find the data for the vehicle that the user wants.
        year = car_qualities[YEAR_INDEX]
        manufactorer = car_qualities[MANUFACTURER_INDEX]
        model = car_qualities[MODEL_INDEX]
        color = car_qualities[COLOR_INDEX]
        eng_design = car_qualities[ENG_DESIGN_INDEX]
        eng_displace = car_qualities[ENG_DISPLACE_INDEX]
        

        # Print the manufacturer, model, and color of the vehicle.
        # Don't print the year, engine design, or displacement.
        print (f"Manufacturer: {manufactorer}\nModel: {model}\nColor: {color}")

    else:
        # Print a message stating that the VIN entered
        # by the user is not in the dictionary.
        print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
