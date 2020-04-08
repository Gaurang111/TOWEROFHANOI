def TOH(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))
        return

    TOH(disks - 1, source, target, auxiliary)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))
    TOH(disks - 1, auxiliary, source, target)


disks = int(input('Enter number of disks: '))
TOH(disks, 'A', 'B', 'C')