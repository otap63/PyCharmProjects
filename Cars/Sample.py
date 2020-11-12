from Cars import Bmw
from Cars import Audi
from Cars import Nissan



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('In Sample.py........')

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