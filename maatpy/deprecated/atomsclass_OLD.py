'''
## Description
This module contains the classes for the `maat.atomsdict.atom` megadictionary,
which carries the information of all elements: isotope mass, cross section, etc.
The `atom` megadict is managed and updated with `maat.atoms`.

## Index
- `Isotope`
- `Element`

---
'''


class Isotope:
    def __init__(self, mass=None, abundance=None, mass_number=None, cross_section=None):
        self.mass = mass
        '''Atomic mass of the isotope, in atomic mass units (amu)'''
        self.abundance = abundance
        '''Relative abundance of the isotope'''
        self.mass_number = mass_number
        '''Mass number (A) of the isotope. Corresponds to the total number of protons + neutrons in the core'''
        self.cross_section = cross_section
        '''Total bound scattering cross section of the isotope'''


class Element:
    def __init__(self=None, symbol=None, name=None, mass=None, number=None, cross_section=None, isotope=None):
        self.symbol = symbol
        '''Standard symbol of the element'''
        self.name = name
        '''Full name'''
        self.mass = mass
        '''Atomic mass, in atomic mass units (amu)'''
        self.number = number
        '''Atomic number (Z). Corresponds to the number of protons / electrons'''
        self.cross_section = cross_section
        '''Total bound scattering cross section'''
        self.isotope = isotope
        '''Dictionary containing the different `Isotope` of the element. The keys are the mass number (A).'''

