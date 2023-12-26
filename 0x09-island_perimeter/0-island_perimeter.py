#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''returns the island perimeter described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # Last list index of the grid
    lst_max = len(grid[0]) - 1  # Last square index in the list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1


                    counter += 1
                else:

                    if lst[land_idx - 1] == 0:
                        counter += 1


                    if lst[land_idx + 1] == 0:
                        counter += 1


                if lst_idx == 0:

                    counter += 1


                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:

                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1


                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter