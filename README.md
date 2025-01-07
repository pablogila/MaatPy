# MaatPy v3.1.1

## IMPORTANT NOTICE

MaatPy has been imported to [Aton](https://github.com/pablogila/Aton/). All the development will continue in the Aton repo. This MaatPy repo is only left for retrocompatibility and will not be updated.

# MaatPy (Legacy)

Welcome to the spectru**M** **A**n**A**lysis **T**ools for **Py**thon; or just **MaatPy**, as the modern incarnation of the Egyptian goddess of truth, order, and justice, [Maat](https://en.wikipedia.org/wiki/Maat).  

Just as an Egyptian goddess fallen from the sky, this Python package can be used to analyze scientific data, such as experimental INS, FTIR and Raman CSV data files, among others.

> **Also check...**  
> Like the Egyptian goddess, MaatPy is *married* to [ThotPy](https://github.com/pablogila/ThotPy), a comprehensive text management package, with a focus in *ab-initio* calculations.  
> Note that although ThotPy is not required to run MaatPy, it is needed to compile MaatPy documentation.  


# Installation

As always, it is strongly recommended to install your packages inside a Python virtual environment:  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## With pip

To install MaatPy with pip, run:  
```shell
pip install maatpy
```

## From source

Optionally, you can install MaatPy from the last GitHub release. First install the dependencies:  
```shell
pip install numpy pandas matplotlib scipy
```

To install MaatPy, clone the repository from [GitHub](https://github.com/pablogila/MaatPy/) or download the [latest stable release](https://github.com/pablogila/MaatPy/tags) as a ZIP and run inside the `/MaatPy/` directory:  
```shell
pip install .
```


# Documentation

Check the [full MaatPy documentation online](https://pablogila.github.io/MaatPy/).  

An offline version of the documentation is available in `/docs/maatpy.html`.
Code examples are provided in the `/examples/` folder.  

## Submodules

MaatPy has the following submodules:  
- [constants](https://pablogila.github.io/MaatPy/maatpy/constants.html). Universal constants and conversion factors. Use them directly as `maatpy.value`.
- [classes](https://pablogila.github.io/MaatPy/maatpy/classes.html). Classes that allow you to work with the data, such as loading INS spectra, etc.
- [plot](https://pablogila.github.io/MaatPy/maatpy/plot.html). Plotting functions.
- [fit](https://pablogila.github.io/MaatPy/maatpy/fit.html). Fitting operations.
- [normalize](https://pablogila.github.io/MaatPy/maatpy/normalize.html). Normalization operations.
- [elements](https://pablogila.github.io/MaatPy/maatpy/elements.html). Contains the `maatpy.atom` dictionary, with the properties of all the elements (mass, cross section, etc).
- [atoms](https://pablogila.github.io/MaatPy/maatpy/atoms.html). Used to build and manage atomic elements.
- [alias](https://pablogila.github.io/MaatPy/maatpy/alias.html). Common dictionaries to correct user inputs.
- [deuteration](https://pablogila.github.io/MaatPy/maatpy/deuteration.html). Tools to estimate deuteration levels.
- [sample](https://pablogila.github.io/MaatPy/maatpy/sample.html). Sample data for testing purposes.

## Compiling the documentation

The documentation can be compiled automatically with [pdoc](https://pdoc.dev/) and [ThotPy](https://github.com/pablogila/ThotPy), by running:
```shell
python3 makedocs.py
```


# License

Copyright (C) 2024  Pablo Gila-Herranz  
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.  
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the attached GNU Affero General Public License for more details.

