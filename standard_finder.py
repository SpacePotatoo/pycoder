"""
@author: Ayuta
Description: program to find primary standard and secondary standard
input: weight transferred/burette reading
output: strength of primary standard/secondary standard
"""
from datetime import date 

weight = float(input("Enter weight of Oxalic acid transferred (in g.):\n>>"))
choice = input("Find strength of secondary standard?\ny/n\n>>")

if choice == "y":
    volume = float(input("Enter volume of NaOH solution (in ml):\n>>"))
    today = date.today()
    strength1 = round(weight/1.575, 4)
    volume_fraction = strength1*25
    strength2 = round(volume_fraction/volume, 4)
    
    print("\nStrength of your primary standard is", strength1,"(N/10)\nand strength of your secondary standard is",strength2,"(N/10)")
    info = '\n{}, {}, {}'.format(strength1, strength2, today)
    
elif choice == "n":
    today = date.today()
    strength1 = round(weight/1.575, 4)
    print("\nStrength of your primary standard is",strength1,"(N/10)")
    info = '\n{}, NA, {}'.format(strength1, today)    
    
else:
    print("invalid input")

with open('D:\\baban\\pythonworks\\py_outputfiles\\standard_strength.csv',mode='a') as standards:
  standards.write(info)
