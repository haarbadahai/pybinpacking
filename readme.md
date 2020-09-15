# 3D bin packing

Small modifications to [Janet-19's solution to the 3d bin packing problem](https://github.com/Janet-19/3d-bin-packing-problem): 

- Small optimizations (checking for volume and remaining weight before placing)
- Removed the bin variable, as it's a built-in python function
- Added a complete packing function, for trying to pack everything in given bins/boxes
- Added packing criteira (Items/Volume)
    1. If Items is selected, the smallest box with the most items is picked
    2. If Volume is selected, the box with the highest packing ratio is picked


## Basic Explanation


Boxes and Items have a similar structure:

```
box = Box(name, width, height, depth, max_weight)
item = Item(name, width, height, depth, weight)
```

Packer has these functions:

```
packer = Packer() #initialize packer
packer.add_box(box) #add boxes
packer.add_item(item) #add items

packer.pack(bigger_first, number_of_decimals, criteria) #by default bigger_first = True, numbe_of_decimals = 3, and criteria=Volume
```

After normal packing, items can be seen using: 

```
packer.boxes            # All boxes in the packer
box.items               # All items which fit the box
box.unfitted_items      # All items which cannot fit into the box
```

For the complete packing solution, the following function can be used:

```
packer.pack_complete(bigger_first,
 number_of_decimals, criteria, 
 remove_boxes) #by default, bigger_first = True, number_of_decimals = 3, criteria= Volume and remove_boxes = False

```

This function runs the packer recursively till: 
- all items are packed, or
- no boxes are left, or
- none of the items can be packed into the remaining boxes

The outputs of this function can be seen using:
```
packer.packing          # This lists all the boxes used to pack the items
packer.unfit_items      # This lists the items that could not be packed in the boxes given as an input
```

## Usage

For the packer.pack() function: 

```
from pybinpacking import Packer, Box, Item

packer = Packer()

packer.add_box(Box('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_box(Box('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_box(Box('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_box(Box('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_box(Box('medium-2-box', 13.625, 11.875, 3.375, 70.0))
packer.add_box(Box('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_box(Box('large-2-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))

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
```

For the complete packing problem:

```
from pybinpacking import Packer, Box, Item

packer = Packer()

packer.add_box(Box('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_box(Box('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_box(Box('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_box(Box('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_box(Box('medium-2-box', 13.625, 11.875, 3.375, 70.0))
packer.add_box(Box('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_box(Box('large-2-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))

packer.pack_complete()

print("########### Packed Items ##########")
for box in packer.packing:
    print("Selected Boxes: \n")
    print(box.string())
    print("\n")
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

```
