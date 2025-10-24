import periodictable
import pyfiglet

text=pyfiglet.print_figlet(text='Periodic table',colors='red',font='slant')

Atomic_No=int(input('Enter the Atomic number: '))
element=periodictable.elements[Atomic_No]

print('Name: ',element.name)
print('Symbol: ',element.symbol)
print('Atomic mass: ',element.mass)
print('Density: ',element.density)