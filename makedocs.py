'''
This script is used to update Maat documentation automatically.
Requires pdoc, install it with `pip install pdoc`.
It also requires Aton, get it here: https://github.com/pablogila/Aton
Run this script as `python3 makedocs.py`.
'''

try:
    import aton
except:
    print("Aborting... You need Aton to compile the documentation! https://github.com/pablogila/Aton")

readme = './README.md'
temp_readme = './_README_temp.md'
version_path = './maatpy/constants.py'

fix_dict ={
    '[alias](https://pablogila.github.io/MaatPy/maatpy/alias.html)'             : '`maatpy.alias`',
    '[classes](https://pablogila.github.io/MaatPy/maatpy/classes.html)'         : '`maatpy.classes`',
    '[constants](https://pablogila.github.io/MaatPy/maatpy/constants.html)'     : '`maatpy.constants`',
    '[atoms](https://pablogila.github.io/MaatPy/maatpy/atoms.html)'             : '`maatpy.atoms`',
    '[elements](https://pablogila.github.io/MaatPy/maatpy/elements.html)'       : '`maatpy.elements`',
    '[fit](https://pablogila.github.io/MaatPy/maatpy/fit.html)'                 : '`maatpy.fit`',
    '[normalize](https://pablogila.github.io/MaatPy/maatpy/normalize.html)'     : '`maatpy.normalize`',
    '[plot](https://pablogila.github.io/MaatPy/maatpy/plot.html)'               : '`maatpy.plot`',
    '[deuteration](https://pablogila.github.io/MaatPy/maatpy/deuteration.html)' : '`maatpy.deuteration`',
    '[sample](https://pablogila.github.io/MaatPy/maatpy/sample.html)'           : '`maatpy.sample`',
}

version = aton.text.find.lines(version_path, r"version\s*=", -1, 0, False, True)[0]
version = aton.text.extract.string(version, 'version', None, True)

print(f'Updating README to {version}...')
aton.text.edit.replace_line(readme, '# MaatPy v', f'# MaatPy {version}', 1)

print('Updating docs with Pdoc...')
aton.text.edit.from_template(readme, temp_readme, fix_dict)
aton.call.bash(f"pdoc ./maatpy/ -o ./docs --mermaid --math --footer-text='MaatPy {version} documentation'")
aton.file.remove(temp_readme)
print('Done!')

