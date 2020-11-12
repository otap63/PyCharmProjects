# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import Cars

from Cars import Bmw
from Cars import Audi
from Cars import Nissan


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('In main().............')

    # Import classes from your brand new package

    # Create an object of Bmw class & call its method
    ModBMW = Bmw.Bmw()
    ModBMW.outModels()

    # Create an object of Audi class & call its method
    ModAudi = Audi.Audi()
    ModAudi.outModels()

    # Create an object of Nissan class & call its method
    ModNissan = Nissan.Nissan()
    ModNissan.outModels()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
