class Atom:
    def __init__(self, Element, AtomicNumber, Symbol, Valency, Group, Period, AtomicMass, AtomicRadius, Density, MeltingPoint, BoilingPoint):
        self.Element = Element
        self.AtomicNumber = AtomicNumber
        self.Symbol = Symbol
        self.Valency = Valency
        self.Group = Group
        self.Period = Period
        self.AtomicMass = AtomicMass
        self.AtomicRadius = AtomicRadius
        self.Density = Density
        self.MeltingPoint = MeltingPoint
        self.BoilingPoint = BoilingPoint



class Temperature:
    
    def __init__(self):
        pass
    
    def KelvinToCelsius(self,Kelvin):
        return Kelvin - 273.15

    def KelvinToFahrenheit(self,Kelvin):
        return (Kelvin - 255.38) * 9 / 5
    
    def CelsiusToFahrenheit(self,Celsius):
        return ((9/5)* Celsius) + 32
    
    def CelsiusToKelvin(self,Celsius):
        return Celsius + 273.15
    
    def FahrenheitToCelsius(self,Fahrenheit):
        return (Fahrenheit - 32) * 5 / 9
    
    def FahrenheitToKelvin(self,Fahrenheit):
        return (5/9) * Fahrenheit + 255.38
    

class UnitConversion:
    def __init__(self):
        pass

    def MetreToYocto(self,Metre):
        return Metre * 10 ** (24)

    def MetreToZepto(self,Metre):
        return Metre * 10 ** (21)

    def MetreToAtto(self,Metre):
        return Metre * 10 ** (18)

    def MetreToFemto(self,Metre):
        return Metre * 10 ** (15)

    def MetreToPico(self,Metre):
        return Metre * 10 ** (12)

    def MetreToNano(self,Metre):
        return Metre * 10 ** (9)

    def MetreToMicro(self,Metre):
        return Metre * 10 ** (6)

    def MetreToMilli(self,Metre):
        return Metre * 10 ** (3)

    def MetreToCenti(self,Metre):
        return Metre * 10 ** (2)

    def MetreToDeci(self,Metre):
        return Metre * 10 ** (1)

    def MetreToDeca(self,Metre):
        return Metre * 10 ** (-1)

    def MetreToHecto(self,Metre):
        return Metre * 10 ** (-2)

    def MetreToKilo(self,Metre):
        return Metre * 10 ** (-3)

    def MetreToMega(self,Metre):
        return Metre * 10 ** (-6)

    def MetreToGiga(self,Metre):
        return Metre * 10 ** (-9)

    def MetreToTera(self,Metre):
        return Metre * 10 ** (-12)

    def MetreToPeta(self,Metre):
        return Metre * 10 ** (-15)

    def MetreToExa(self,Metre):
        return Metre * 10 ** (-18)

    def MetreToZeta(self,Metre):
        return Metre * 10 ** (-21)

    def MetreToYotta(self,Metre):
        return Metre * 10 ** (-24)




def aufbau_series(atomic_number):
    # Initialize variables
    aufbau_config = []
    electron_count = atomic_number
    shell_number = 1

    # Generate Aufbau series dynamically
    while electron_count > 0:
        # Calculate the maximum number of electrons that can fit in the current shell
        max_electrons = 2 * shell_number ** 2

        # Distribute electrons into subshells (s, p, d, f)
        subshell_electrons = min(electron_count, max_electrons)
        aufbau_config.append((f"{shell_number}s", min(subshell_electrons, 2)))
        subshell_electrons -= min(subshell_electrons, 2)

        if subshell_electrons > 0:
            aufbau_config.append((f"{shell_number}p", min(subshell_electrons, 6)))
            subshell_electrons -= min(subshell_electrons, 6)

        if subshell_electrons > 0:
            aufbau_config.append((f"{shell_number}d", min(subshell_electrons, 10)))
            subshell_electrons -= min(subshell_electrons, 10)

        if subshell_electrons > 0:
            aufbau_config.append((f"{shell_number}f", min(subshell_electrons, 14)))

        # Update electron count and move to the next shell
        electron_count -= max_electrons
        shell_number += 1

    return aufbau_config



Hydrogen = Atom("Hydrogen", 1, "H", [1], 1, 1, 1.008, 53, 0.08988, 13.99, 20.28)
Helium = Atom("Helium", 2, "He", [0], 18, 1, 4.0026, 31, 0.1786, 0.95, 4.22)
Lithium = Atom("Lithium", 3, "Li", [1], 1, 2, 6.94, 167, 0.534, 453.69, 1615)
Beryllium = Atom("Beryllium", 4, "Be", [2], 2, 2, 9.0122, 112, 1.85, 1560, 2743)
Boron = Atom("Boron", 5, "B", [3], 13, 2, 10.81, 87, 2.34, 2348, 4200)
Carbon = Atom("Carbon", 6, "C", [4], 14, 2, 12.011, 67, {"Graphite" : 2.267, "Diamond" : 3.51}, {"Graphite" : 3800, "Diamond" : 4300}, {"Graphite" : 4200, "Diamond" : "Sublimes"})
Nitrogen = Atom("Nitrogen", 7, "N", [3, 5], 15, 2, 14.007, 56, 0.0012506, 63.15, 77.36)
Oxygen = Atom("Oxygen", 8, "O", [2], 16, 2, 15.999, 48, 0.001429, 54.36, 90.20)
Fluorine = Atom("Fluorine", 9, "F", [1], 17, 2, 18.998, 42, 0.001696, 53.53, 85.03)
Neon = Atom("Neon", 10, "Ne", [0], 18, 2, 20.180, 38, 0.0008999, 24.56, 27.07)
Sodium = Atom("Sodium", 11, "Na", [1], 1, 3, 22.99, 190, 0.97, 370.87, 1156)
Magnesium = Atom("Magnesium", 12, "Mg", [2], 2, 3, 24.305, 145, 1.738, 923, 1380)
Aluminum = Atom("Aluminum", 13, "Al", [3], 13, 3, 26.982, 118, 2.7, 933.47, 2792)
Silicon = Atom("Silicon", 14, "Si", [4], 14, 3, 28.085, 111, 2.33, 1687, 3538)
Phosphorus = Atom("Phosphorus", 15, "P", [3, 5], 15, 3, 30.974, 98, 1.82, 317.30, 550)
Sulfur = Atom("Sulfur", 16, "S", [2, 4, 6], 16, 3, 32.06, 88, 2.07, 388.36, 717.87)
Chlorine = Atom("Chlorine", 17, "Cl", [1, 3, 5, 7], 17, 3, 35.45, 79, 0.003214, 171.6, 239.11)
Argon = Atom("Argon", 18, "Ar", [0], 18, 3, 39.948, 71, 0.0017837, 83.8, 87.3)
Potassium = Atom("Potassium", 19, "K", [1], 1, 4, 39.098, 243, 0.89, 336.7, 1032)
Calcium = Atom("Calcium", 20, "Ca", [2], 2, 4, 40.078, 194, 1.54, 1115, 1757)
Scandium = Atom("Scandium", 21, "Sc", [3], 3, 4, 44.956, 184, 2.989, 1814, 3109)
Titanium = Atom("Titanium", 22, "Ti", [3, 4], 4, 4, 47.867, 176, 4.506, 1941, 3560)
Vanadium = Atom("Vanadium", 23, "V", [2, 3, 4, 5], 5, 4, 50.942, 171, 6.11, 2183, 3680)
Chromium = Atom("Chromium", 24, "Cr", [2, 3, 6], 6, 4, 51.996, 166, 7.15, 2180, 2944)
Manganese = Atom("Manganese", 25, "Mn", [2, 3, 4, 6, 7], 7, 4, 54.938, 161, 7.44, 1519, 2334)
Iron = Atom("Iron", 26, "Fe", [2, 3], 8, 4, 55.845, 156, 7.874, 1811, 3134)
Cobalt = Atom("Cobalt", 27, "Co", [2, 3], 9, 4, 58.933, 152, 8.86, 1768, 3200)
Nickel = Atom("Nickel", 28, "Ni", [2, 3], 10, 4, 58.693, 149, 8.912, 1728, 3186)
Copper = Atom("Copper", 29, "Cu", [1, 2], 11, 4, 63.546, 145, 8.96, 1357.77, 2835)
Zinc = Atom("Zinc", 30, "Zn", [2], 12, 4, 65.38, 142, 7.14, 692.88, 1180)
Gallium = Atom("Gallium", 31, "Ga", [3], 13, 4, 69.723, 136, 5.907, 302.9146, 2477)
Germanium = Atom("Germanium", 32, "Ge", [2, 4], 14, 4, 72.630, 125, 5.323, 1211.4, 3106)
Arsenic = Atom("Arsenic", 33, "As", [3, 5], 15, 4, 74.922, 114, 5.776, 1090, 887)
Selenium = Atom("Selenium", 34, "Se", [2, 4, 6], 16, 4, 78.971, 103, 4.809, 494, 958)
Bromine = Atom("Bromine", 35, "Br", [1, 3, 5, 7], 17, 4, 79.904, 94, 3.1028, 265.8, 332)
Krypton = Atom("Krypton", 36, "Kr", [0], 18, 4, 83.798, 88, 0.003733, 115.79, 119.93)
Rubidium = Atom("Rubidium", 37, "Rb", [1], 1, 5, 85.468, 265, 1.532, 312.46, 961)
Strontium = Atom("Strontium", 38, "Sr", [2], 2, 5, 87.62, 219, 2.63, 1042, 1655)
Yttrium = Atom("Yttrium", 39, "Y", [3], 3, 5, 88.906, 212, 4.469, 1799, 3609)
Zirconium = Atom("Zirconium", 40, "Zr", [4], 4, 5, 91.224, 186, 6.52, 2128, 4682)
Niobium = Atom("Niobium", 41, "Nb", [3, 5], 5, 5, 92.906, 171, 8.57, 2750, 5017)
Molybdenum = Atom("Molybdenum", 42, "Mo", [2, 3, 4, 5, 6], 6, 5, 95.95, 156, 10.22, 2896, 4912)
Technetium = Atom("Technetium", 43, "Tc", [4, 5, 6, 7], 7, 5, 98, 145, 11.5, 2430, 4538)
Ruthenium = Atom("Ruthenium", 44, "Ru", [2, 3, 4, 5, 6, 8], 8, 5, 101.07, 134, 12.37, 2607, 4423)
Rhodium = Atom("Rhodium", 45, "Rh", [2, 3, 4], 9, 5, 102.91, 134, 12.41, 2237, 3968)
Palladium = Atom("Palladium", 46, "Pd", [2, 4], 10, 5, 106.42, 137, 12.02, 1828.05, 3236)
Silver = Atom("Silver", 47, "Ag", [1, 2, 3], 11, 5, 107.87, 144, 10.49, 1234.93, 2435)
Cadmium = Atom("Cadmium", 48, "Cd", [2], 12, 5, 112.41, 151, 8.65, 594.22, 1040)
Indium = Atom("Indium", 49, "In", [1, 3], 13, 5, 114.82, 156, 7.31, 429.75, 2345)
Tin = Atom("Tin", 50, "Sn", [2, 4], 14, 5, 118.71, 145, 7.31, 505.08, 2875)
Antimony = Atom("Antimony", 51, "Sb", [3, 5], 15, 5, 121.76, 133, 6.68, 903.78, 1860)
Tellurium = Atom("Tellurium", 52, "Te", [2, 4, 6], 16, 5, 127.60, 123, 6.24, 722.66, 1261)
Iodine = Atom("Iodine", 53, "I", [1, 3, 5, 7], 17, 5, 126.90, 115, 4.93, 386.85, 457.4)
Xenon = Atom("Xenon", 54, "Xe", [0], 18, 5, 131.29, 108, 0.005887, 161.4, 165.03)
Cesium = Atom("Cesium", 55, "Cs", [1], 1, 6, 132.91, 298, 1.873, 301.59, 944)
Barium = Atom("Barium", 56, "Ba", [2], 2, 6, 137.33, 253, 3.62, 1000, 2170)
Lanthanum = Atom("Lanthanum", 57, "La", [3], 3, 6, 138.91, 247, 6.145, 1193, 3737)
Cerium = Atom("Cerium", 58, "Ce", [3, 4], 3, 6, 140.12, 240, 6.77, 1071, 3697)
Praseodymium = Atom("Praseodymium", 59, "Pr", [3], 3, 6, 140.91, 239, 6.773, 1204, 3793)
Neodymium = Atom("Neodymium", 60, "Nd", [3], 3, 6, 144.24, 228, 7.01, 1289, 3347)
Promethium = Atom("Promethium", 61, "Pm", [3], 3, 6, 145, 247, 7.22, 1315, 3273)
Samarium = Atom("Samarium", 62, "Sm", [2, 3], 3, 6, 150.36, 238, 7.52, 1345, 2067)
Europium = Atom("Europium", 63, "Eu", [2, 3], 3, 6, 151.96, 231, 5.24, 1099, 1802)
Gadolinium = Atom("Gadolinium", 64, "Gd", [3], 3, 6, 157.25, 233, 7.90, 1311, 3233)
Terbium = Atom("Terbium", 65, "Tb", [3, 4], 3, 6, 158.93, 225, 8.23, 1356, 3123)
Dysprosium = Atom("Dysprosium", 66, "Dy", [3], 3, 6, 162.50, 228, 8.55, 1412, 2567)
Holmium = Atom("Holmium", 67, "Ho", [3], 3, 6, 164.93, 226, 8.79, 1470, 2720)
Erbium = Atom("Erbium", 68, "Er", [3], 3, 6, 167.26, 226, 9.07, 1522, 2510)
Thulium = Atom("Thulium", 69, "Tm", [3], 3, 6, 168.93, 222, 9.32, 1545, 1727)
Ytterbium = Atom("Ytterbium", 70, "Yb", [2, 3], 3, 6, 173.05, 222, 6.90, 824, 1196)
Lutetium = Atom("Lutetium", 71, "Lu", [3], 3, 6, 174.97, 217, 9.84, 1652, 3315)
Hafnium = Atom("Hafnium", 72, "Hf", [4], 4, 6, 178.49, 208, 13.31, 2506, 4876)
Tantalum = Atom("Tantalum", 73, "Ta", [5], 5, 6, 180.95, 200, 16.65, 3290, 5731)
Tungsten = Atom("Tungsten", 74, "W", [2, 3, 4, 5, 6], 6, 6, 183.84, 193, 19.25, 3695, 5828)
Rhenium = Atom("Rhenium", 75, "Re", [3, 4, 5, 6, 7], 7, 6, 186.21, 188, 21.02, 3459, 5869)
Osmium = Atom("Osmium", 76, "Os", [2, 3, 4, 6, 8], 8, 6, 190.23, 185, 22.59, 3306, 5285)
Iridium = Atom("Iridium", 77, "Ir", [2, 3, 4, 6], 9, 6, 192.22, 180, 22.56, 2719, 4701)
Platinum = Atom("Platinum", 78, "Pt", [2, 4], 10, 6, 195.08, 177, 21.45, 2041.4, 4098)
Gold = Atom("Gold", 79, "Au", [1, 3], 11, 6, 196.97, 174, 19.32, 1337.33, 3129)
Mercury = Atom("Mercury", 80, "Hg", [1, 2], 12, 6, 200.59, 171, 13.53, 234.32, 629.88)
Thallium = Atom("Thallium", 81, "Tl", [1, 3], 13, 6, 204.38, 156, 11.85, 577, 1746)
Lead = Atom("Lead", 82, "Pb", [2, 4], 14, 6, 207.2, 154, 11.34, 600.61, 2022)
Bismuth = Atom("Bismuth", 83, "Bi", [3, 5], 15, 6, 208.98, 143, 9.78, 544.7, 1837)
Polonium = Atom("Polonium", 84, "Po", [2, 4, 6], 16, 6, 209, 135, 9.32, 527, 1235)
Astatine = Atom("Astatine", 85, "At", [1, 3, 5, 7], 17, 6, 210, 127, 7, 575, 610)
Radon = Atom("Radon", 86, "Rn", [0], 18, 6, 222, 120, 0.00973, 202, 211.3)
Francium = Atom("Francium", 87, "Fr", [1], 1, 7, 223, 348, 1.87, 300, 950)
Radium = Atom("Radium", 88, "Ra", [2], 2, 7, 226, 283, 5.5, 973, 2010)
Actinium = Atom("Actinium", 89, "Ac", [3], 3, 7, 227, 260, 10.07, 1323, 3573)
Thorium = Atom("Thorium", 90, "Th", [4], 3, 7, 232.04, 237, 11.72, 2115, 5061)
Protactinium = Atom("Protactinium", 91, "Pa", [5], 3, 7, 231.04, 243, 15.37, 1841, 4300)
Uranium = Atom("Uranium", 92, "U", [4, 5, 6], 3, 7, 238.03, 233, 19.16, 1405.3, 4404)
Neptunium = Atom("Neptunium", 93, "Np", [3, 4, 5, 6, 7], 3, 7, 237, 225, 20.45, 912, 4273)
Plutonium = Atom("Plutonium", 94, "Pu", [3, 4, 5, 6], 3, 7, 244, 244, 19.86, 912.5, 3501)
Americium = Atom("Americium", 95, "Am", [2, 3, 4, 5, 6], 3, 7, 243, 244, 13.69, 1449, 2284)
Curium = Atom("Curium", 96, "Cm", [3, 4], 3, 7, 247, 244, 13.51, 1613, 3383)
Berkelium = Atom("Berkelium", 97, "Bk", [3, 4], 3, 7, 247, 244, 14.79, 1259, 2900)
Californium = Atom("Californium", 98, "Cf", [2, 3, 4], 3, 7, 251, 244, 15.1, 1173, 1743)
Einsteinium = Atom("Einsteinium", 99, "Es", [3], 3, 7, 252, 244, 13.5, 1133, 1269)
Fermium = Atom("Fermium", 100, "Fm", [3], 3, 7, 257, 244, 9.7, 1800, None)
Mendelevium = Atom("Mendelevium", 101, "Md", [3], 3, 7, 258, 244, None, 1100, None)
Nobelium = Atom("Nobelium", 102, "No", [2, 3], 3, 7, 259, 244, None, 1100, None)
Lawrencium = Atom("Lawrencium", 103, "Lr", [3], 3, 7, 266, 244, None, 1900, None)
Rutherfordium = Atom("Rutherfordium", 104, "Rf", [4], 4, 7, 267, 244, None, None, None)
Dubnium = Atom("Dubnium", 105, "Db", [5], 5, 7, 268, 244, None, None, None)
Seaborgium = Atom("Seaborgium", 106, "Sg", [6], 6, 7, 269, 244, None, None, None)
Bohrium = Atom("Bohrium", 107, "Bh", [7], 7, 7, 270, 244, None, None, None)
Hassium = Atom("Hassium", 108, "Hs", [8], 8, 7, 269, 244, None, None, None)
Meitnerium = Atom("Meitnerium", 109, "Mt", [9], 9, 7, 278, 244, None, None, None)
Darmstadtium = Atom("Darmstadtium", 110, "Ds", [10], 10, 7, 281, 244, None, None, None)
Roentgenium = Atom("Roentgenium", 111, "Rg", [11], 11, 7, 282, 244, None, None, None)
Copernicium = Atom("Copernicium", 112, "Cn", [2, 4], 12, 7, 285, 244, None, None, None)
Nihonium = Atom("Nihonium", 113, "Nh", [1], 13, 7, 286, 244, None, None, None)
Flerovium = Atom("Flerovium", 114, "Fl", [2], 14, 7, 289, 244, None, None, None)
Moscovium = Atom("Moscovium", 115, "Mc", [3], 15, 7, 290, 244, None, None, None)
Livermorium = Atom("Livermorium", 116, "Lv", [2, 4], 16, 7, 293, 244, None, None, None)
Tennessine = Atom("Tennessine", 117, "Ts", [1, 3, 5], 17, 7, 294, 244, None, None, None)
Oganesson = Atom("Oganesson", 118, "Og", [0], 18, 7, 294, 244, None, None, None)



# Create the all_atoms list dynamically
all_atoms = [obj for name, obj in globals().items() if isinstance(obj, Atom) and name != "Atom"]

number = {e.AtomicNumber:e for e in all_atoms}
symbol = {e.Symbol:e for e in all_atoms}
mass = {e.AtomicMass:e for e in all_atoms}

class MolecularMass:
    def __init__(self, formula):
        self.formula = formula

    def calculate_molecular_mass(self):
        molecular_mass = 0
        parsed_formula = self.parse_formula()
        for symbol, count in parsed_formula.items():
            for atom in all_atoms:
                if atom.Symbol == symbol:
                    molecular_mass += atom.AtomicMass * count
                    break
        return molecular_mass
    def parse_formula(self):
        parsed_formula = {}
        i = 0
        while i < len(self.formula):
            atom = self.formula[i]
            count = 1
            i += 1
            if i < len(self.formula) and self.formula[i].isdigit():
                count = int(self.formula[i])
                i += 1
            if atom in parsed_formula:
                parsed_formula[atom] += count
            else:
                parsed_formula[atom] = count
        return parsed_formula

