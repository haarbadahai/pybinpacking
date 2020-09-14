from pybinpacking import Packer, Box, Item
import argparse
import sys

packer = Packer()
# packer.add_box(Box('small-envelope', 11.5, 6.125, 0.25, 10))
# packer.add_box(Box('large-envelope', 15.0, 12.0, 0.75, 15))
# packer.add_box(Box('small-box', 8.625, 5.375, 1.625, 70.0))
# packer.add_box(Box('medium-box', 11.0, 8.5, 5.5, 70.0))
# packer.add_box(Box('medium-2-box', 13.625, 11.875, 3.375, 70.0))
# packer.add_box(Box('large-box', 12.0, 12.0, 5.5, 70.0))
# packer.add_box(Box('large-2-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))


def pack_normal():
    packer.pack()

    for b in packer.boxes:
        print(":::::::::::", b.string())

        print("FITTED ITEMS:")
        for item in b.items:
            print("====> ", item.string())

        print("UNFITTED ITEMS:")
        for item in b.unfitted_items:
            print("====> ", item.string())

        print("***************************************************")
        print("***************************************************")

def pack_all():

    packer.pack_complete()
    print("########### Packed Boxes ##########")
    for box in packer.packing:
        print("Selected Box: \n")
        print(box.string())
        print("\n Items: \n")
        for item in box.items:
            print(item.string())
            print("\n")

    print("########## Unfit items ###########")
    if packer.unfit_items:
        for item in packer.unfit_items:
            print(item.string())
            print("\n")

    else:
        print("None")

def parseArgs (args = None):
    """ Parsing the arguments in the command line - this is used to get the parameters using this script"""
    method = {1: 'Pack items in all boxes',
              2: 'Recursively pack and give optimal boxes for items'  }
    parser = argparse.ArgumentParser(description='Solve bin packing problem')
    parser.add_argument('-m', '--method', help = f'Method: {method}', required = 'False', default= 1, type = int)     
    return parser.parse_args(args)

if __name__ == '__main__':
    val = parseArgs(sys.argv[1:])
    if (val.method == 1):
        pack_normal()
    elif (val.method == 2):
        pack_all()
    else:
        method = {1: 'Pack items in all boxes',
              2: 'Recursively pack and give optimal boxes for items'  }
        print(f"Please provide the method. Available methods:{method}")
