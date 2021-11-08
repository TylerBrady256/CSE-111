#Tyler Brady 
 
  # #calls function to get the periodic_table_dict and then cycles through the postions in the dictionary 0: [0,1]1 key is 0 list is 1
    # for position in make_periodic_table().items():
    #     #gets Elements Key 
    #     symbol_key = position[0]
    #     #gets dictionary list ["Name",weight]
    #     element_attributes = position[1]
    #     name = element_attributes[NAME_INDEX]
    #     weight= element_attributes[ATOMIC_MASS_INDEX]
    #     # print(f",'{symbol}': ['{name}', {weight}]")
    #     print(f"{symbol_key} , {name} , {weight}")

#these are Super nice USE THEM PLEASE
# These are the indexes of the
# elements in the periodic table
NAME_INDEX = 0 
ATOMIC_MASS_INDEX =1

def main():

    # Get a chemical formula for a molecule from the user.
    molecule = input("What molecule do you have today? Type as H2O ")
     # Chemical coumpound name formulator 
    the_name_people_know_it_by = get_formula_name(molecule,make_known_molecules())
    print(the_name_people_know_it_by)
    # Get a mass in grams from the user.
    user_mass = float(input("how many grams do you have? "))

   

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    divided_molecule = parse_formula(molecule,periodic_table_dict)
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass= compute_molar_mass(divided_molecule,periodic_table_dict)
    # Compute the number of moles of the sample.
    number_of_moles=user_mass/molar_mass
    # Print the molar mass.
    print(f"Molar Mass: {molar_mass}")
    # Print the number of moles.
    print(f"{number_of_moles:.5f} Moles")

    protons = sum_protons(divided_molecule,periodic_table_dict)
    print(f"the number of protons: {protons}")
    

def make_known_molecules():
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }
    return known_molecules_dict
    
def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    """
    if formula in known_molecules_dict:
        name = known_molecules_dict[formula]
    else:
        name = "unknown compound"

    return name
    

def make_periodic_table():
    periodic_table_dict=  {#Symbol = 0, Name =1, Atomic mass = 2
    'Ac': ['Actinium', 227,89]
    ,'Ag': ['Silver', 107.8682,47]
    ,'Al': ['Aluminum', 26.9815386,13]
    ,'Am': ['Americium', 243,95]
    ,'Ar': ['Argon', 39.948,18]
    ,'As': ['Arsenic', 74.9216,33]
    ,'At': ['Astatine', 210,85]
    ,'Au': ['Gold', 196.966569,79]
    ,'B': ['Boron', 10.811,5]
    ,'Ba': ['Barium', 137.327,56]
    ,'Be': ['Beryllium', 9.012182,4]
    ,'Bh': ['Bohrium', 272,107]
    ,'Bi': ['Bismuth', 208.9804,83]
    ,'Bk': ['Berkelium', 247,97]
    ,'Br': ['Bromine', 79.904,35]
    ,'C': ['Carbon', 12.0107,6]
    ,'Ca': ['Calcium', 40.078,20]
    ,'Cd': ['Cadmium', 112.411,48]
    ,'Ce': ['Cerium', 140.116,58]
    ,'Cf': ['Californium', 251,98]
    ,'Cl': ['Chlorine', 35.453,17]
    ,'Cm': ['Curium', 247,96]
    ,'Cn': ['Copernicium', 285,112]
    ,'Co': ['Cobalt', 58.933195,27]
    ,'Cr': ['Chromium', 51.9961,24]
    ,'Cs': ['Cesium', 132.9054519,55]
    ,'Cu': ['Copper', 63.546,29]
    ,'Db': ['Dubnium', 268,105]
    ,'Ds': ['Darmstadtium', 281,110]
    ,'Dy': ['Dysprosium', 162.5,66]
    ,'Er': ['Erbium', 167.259,63]
    ,'Es': ['Einsteinium', 252,99]
    ,'Eu': ['Europium', 151.964,63]
    ,'F': ['Fluorine', 18.9984032,9]
    ,'Fe': ['Iron', 55.845,26]
    ,'Fl': ['Flerovium', 289,114]
    ,'Fm': ['Fermium', 257,100]
    ,'Fr': ['Francium', 223,87]
    ,'Ga': ['Gallium', 69.723,31]
    ,'Gd': ['Gadolinium', 157.25,64]
    ,'Ge': ['Germanium', 72.64,32]
    ,'H': ['Hydrogen', 1.00794,1]
    ,'He': ['Helium', 4.002602,2]
    ,'Hf': ['Hafnium', 178.49,72]
    ,'Hg': ['Mercury', 200.59,80]
    ,'Ho': ['Holmium', 164.93032,67]
    ,'Hs': ['Hassium', 277,108]
    ,'I': ['Iodine', 126.90447,53]
    ,'In': ['Indium', 114.818,49]
    ,'Ir': ['Iridium', 192.217,77]
    ,'K': ['Potassium', 39.0983,19]
    ,'Kr': ['Krypton', 83.798,36]
    ,'La': ['Lanthanum', 138.90547,57]
    ,'Li': ['Lithium', 6.941,3]
    ,'Lr': ['Lawrencium', 262,103]
    ,'Lu': ['Lutetium', 174.9668,71]
    ,'Lv': ['Livermorium', 293,116]
    ,'Mc': ['Moscovium', 288,115]
    ,'Md': ['Mendelevium', 258,101]
    ,'Mg': ['Magnesium', 24.305,12]
    ,'Mn': ['Manganese', 54.938045,25]
    ,'Mo': ['Molybdenum', 95.96,42]
    ,'Mt': ['Meitnerium', 276,109]
    ,'N': ['Nitrogen', 14.0067,7]
    ,'Na': ['Sodium', 22.98976928,11]
    ,'Nb': ['Niobium', 92.90638,41]
    ,'Nd': ['Neodymium', 144.242,60]
    ,'Ne': ['Neon', 20.1797,10]
    ,'Nh': ['Nihonium', 284,113]
    ,'Ni': ['Nickel', 58.6934,28]
    ,'No': ['Nobelium', 259,102]
    ,'Np': ['Neptunium', 237,93]
    ,'O': ['Oxygen', 15.9994,8]
    ,'Og': ['Oganesson', 294,118]
    ,'Os': ['Osmium', 190.23,76]
    ,'P': ['Phosphorus', 30.973762,15]
    ,'Pa': ['Protactinium', 231.03588,91]
    ,'Pb': ['Lead', 207.2,82]
    ,'Pd': ['Palladium', 106.42,46]
    ,'Pm': ['Promethium', 145,61]
    ,'Po': ['Polonium', 209,84]
    ,'Pr': ['Praseodymium', 140.90765,59]
    ,'Pt': ['Platinum', 195.084,78]
    ,'Pu': ['Plutonium', 244,94]
    ,'Ra': ['Radium', 226,88]
    ,'Rb': ['Rubidium', 85.4678,37]
    ,'Re': ['Rhenium', 186.207,75]
    ,'Rf': ['Rutherfordium', 267,104]
    ,'Rg': ['Roentgenium', 280,111]
    ,'Rh': ['Rhodium', 102.9055,45]
    ,'Rn': ['Radon', 222,86]
    ,'Ru': ['Ruthenium', 101.07,44]
    ,'S': ['Sulfur', 32.065,16]
    ,'Sb': ['Antimony', 121.76,51]
    ,'Sc': ['Scandium', 44.955912,21]
    ,'Se': ['Selenium', 78.96,34]
    ,'Sg': ['Seaborgium', 271,106]
    ,'Si': ['Silicon', 28.0855,14]
    ,'Sm': ['Samarium', 150.36,62]
    ,'Sn': ['Tin', 118.71,50]
    ,'Sr': ['Strontium', 87.62,38]
    ,'Ta': ['Tantalum', 180.94788,73]
    ,'Tb': ['Terbium', 158.92535,65]
    ,'Tc': ['Technetium', 98, 43]
    ,'Te': ['Tellurium', 127.6,52]
    ,'Th': ['Thorium', 232.03806,90]
    ,'Ti': ['Titanium', 47.867,22]
    ,'Tl': ['Thallium', 204.3833,81]
    ,'Tm': ['Thulium', 168.93421,69]
    ,'Ts': ['Tennessine', 294,117]
    ,'U': ['Uranium', 238.02891,92]
    ,'V': ['Vanadium', 50.9415,23]
    ,'W': ['Tungsten', 183.84,74]
    ,'Xe': ['Xenon', 131.293,54]
    ,'Y': ['Yttrium', 88.90585,39]
    ,'Yb': ['Ytterbium', 173.054,70]
    ,'Zn': ['Zinc', 65.38,30]
    ,'Zr': ['Zirconium', 91.224,40]
    }
    
    return periodic_table_dict

class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """
    pass


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]
    """
    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    elem_dict[symbol] = prev + group_dict[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError(
                            "invalid formula, unknown element symbol:",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError(
                        "invalid formula, unmatched close parenthesis:",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula:"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character:"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError(
                "invalid formula, unmatched open parenthesis:",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list. Each element in
    symbol_quantity_list is a list in the form: ["symbol", quantity].

    As an example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_mass=0
    for i in symbol_quantity_list:

        molecular_name = i[NAME_INDEX]
        quantity = i[1]
       
            #using the key it sets the element_attributes to be the the list inside the dictionary
        element_attributes = periodic_table_dict[molecular_name]
        atomic_weight = element_attributes[ATOMIC_MASS_INDEX]

        #adds all the masses of each element
        total_mass += atomic_weight*quantity
    return total_mass

    # For each element in the symbol_quantity_list:
    #   Split the element into symbol and quantity.
    #   Get the atomic mass for the symbol.
    #   Multiply the atomic mass by the quantity.
    #   Add the product into the total mass.
    
def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.
    """
    total_protons = 0
    for i in symbol_quantity_list:

        molecular_name = i[NAME_INDEX]
        quantity = i[1]
       
            #using the key it sets the element_attributes to be the the list inside the dictionary
        element_attributes = periodic_table_dict[molecular_name]
        electrons = element_attributes[2]

        total_protons += electrons * quantity

    return total_protons

        
       

if __name__ == "__main__":
    main()
