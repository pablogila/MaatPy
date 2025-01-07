'''
# Description
This module contains common dictionaries to normalize and correct user inputs.

# Index
- `unit`
- `parameters`
- `experiment`
- `file`
- `boolean`

---
'''


unit: dict = {
    'mol'  : ['mol', 'mols', 'mole', 'moles', 'Mol', 'Mols', 'Mole', 'Moles', 'MOL', 'MOLS', 'MOLE', 'MOLES'],
    'g'    : ['g', 'gram', 'grams', 'G', 'Gram', 'Grams', 'GRAM', 'GRAMS'],
    'kg'   : ['kg', 'Kg', 'KG', 'kilogram', 'kilograms', 'Kilogram', 'Kilograms', 'KILOGRAM', 'KILOGRAMS'],
    'amu'  : ['amu', 'AMU', 'Amu', 'atomicmassunit', 'atomicmassunits', 'Atomicmassunit', 'Atomicmassunits', 'ATOMICMASSUNIT', 'ATOMICMASSUNITS'],
    'eV'   : ['eV', 'ev', 'EV', 'electronvolt', 'electronvolts', 'Electronvolt', 'Electronvolts', 'ELECTRONVOLT', 'ELECTRONVOLTS'],
    'meV'  : ['meV', 'mev', 'MEV', 'millielectronvolt', 'millielectronvolts', 'Millielectronvolt', 'Millielectronvolts', 'MILLIELECTRONVOLT', 'MILLIELECTRONVOLTS'],
    'J'    : ['J', 'j', 'JOULE', 'JOULES', 'joule', 'joules', 'Joule', 'Joules'],
    'cal'  : ['cal', 'Cal', 'CAL', 'calorie', 'calories', 'Calorie', 'Calories', 'CALORIE', 'CALORIES'],
    'kcal' : ['kcal', 'Kcal', 'KCAL', 'kilocalorie', 'kilocalories', 'Kilocalorie', 'Kilocalories', 'KILOCALORIE', 'KILOCALORIES'],
    'Ry'   : ['Ry', 'ry', 'RY', 'rydberg', 'rydbergs', 'Rydberg', 'Rydbergs', 'RYDBERG', 'RYDBERGS'],
    'cm-1' : ['cm^{-1}', 'cm1', 'cm-1', 'cm^-1', 'Cm1', 'Cm-1', 'Cm^-1', 'Cm^{-1}', 'CM1', 'CM-1', 'CM^-1', 'CM^{-1}'],
    'cm'   : ['cm', 'CM', 'Cm', 'centimeter', 'centimeters', 'Centimeter', 'Centimeters', 'CENTIMETER', 'CENTIMETERS'],
    'A'    : ['A', 'a', 'AA', 'aa', 'angstrom', 'angstroms', 'Angstrom', 'Angstroms', 'ANGSTROM', 'ANGSTROMS', 'armstrong', 'Armstrong', 'ARMSTRONG', 'armstrongs', 'Armstrongs', 'ARMSTRONGS'],
    'bohr' : ['bohr', 'Bohr', 'BOHR', 'bohr', 'Bohr', 'BOHR', 'bohrradii', 'Bohrradii', 'BOHRRADII'],
    'm'    : ['m', 'M', 'meter', 'meters', 'Meter', 'Meters', 'METER', 'METERS'],
    'deg'  : ['deg', 'DEG', 'Deg', 'degree', 'degrees', 'Degree', 'Degrees', 'DEGREE', 'DEGREES'],
    'rad'  : ['rad', 'RAD', 'Rad', 'radian', 'radians', 'Radian', 'Radians', 'RADIAN', 'RADIANS'],
    'bar'  : ['bar', 'Bar', 'BAR', 'bars', 'Bars', 'BARS'],
    'kbar' : ['kbar', 'Kbar', 'KBAR', 'kilobar', 'kilobars', 'Kilobar', 'Kilobars', 'KILOBAR', 'KILOBARS'],
    'Pa'   : ['Pa', 'pa', 'PA', 'Pascal', 'Pascals', 'PASCAL', 'PASCALS'],
    'GPa'  : ['GPa', 'Gpa', 'gpa', 'GPA', 'gigapascal', 'gigapascals', 'Gigapascal', 'Gigapascals', 'GIGAPASCAL', 'GIGAPASCALS'],
    's'    : ['s', 'S', 'second', 'seconds', 'Second', 'Seconds', 'SECOND', 'SECONDS'],
    'H'    : ['H', 'h', 'hour', 'hours', 'Hour', 'Hours', 'HOUR', 'HOURS'],
}
'''
Dict with unit names.
'''

parameters = {
    'height': ['height', 'HEIGHT', 'Height', 'H', 'h'],
    'area'  : ['area', 'Area', 'AREA', 'a', 'A'],
}
'''Dict with different parameters.'''

experiment: dict = {
    'INS'   : ['INS', 'ins', 'Ins', 'InelasticNeutronScattering'],
    'ATR'   : ['ATR', 'atr', 'FTIR', 'ftir', 'AttenuatedTotalReflection'],
    'RAMAN' : ['RAMAN', 'raman', 'Raman'],
}
'''
Dictionary with the available experiment types.
'''

file = {
    'file'  : ['file', 'files', 'File', 'Files', 'FILE', 'FILES', 'f', 'F'],
    'dir'   : ['dir', 'Dir', 'DIR', 'directory', 'Directory', 'DIRECTORY', 'd', 'D', 'folder', 'Folder', 'FOLDER'],
    'Error' : ['Error', 'error', 'ERROR', 'Errors', 'errors', 'ERRORS'],
    }
'''
Strings related to files.
'''

boolean= {
    True  : ['yes', 'YES', 'Yes', 'Y', 'y', 'T', 'True', 'TRUE', 't', 'true', True, 'Si', 'SI', 'si', 'S', 's'],
    False : ['no', 'NO', 'No', 'N', 'n', 'F', 'False', 'FALSE', 'f', 'false', False],
}
'''
Strings with booleans such as 'yes' / 'no'.
'''

