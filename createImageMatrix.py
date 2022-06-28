import numpy as np
import itertools


def createImageMatrix(corner_points:list, image_dimensions: tuple):

    # Checks if the number of corner points is correct
    if len(corner_points ) !=4 :
        print('Wrong number of coordinates provided')
        return

    if len(image_dimensions) != 2:
        print('Wrong shape of image_dimensions')
        return

    # Initial values are set base on the first coordinates provided
    height_max = corner_points[0][1]
    height_min = corner_points[0][1]
    width_max = corner_points[0][0]
    width_min = corner_points[0][0]

    # iterate through all of the coordinates to find the outter parameters of the image
    for i in range(1,len(corner_points)):
        height_max = max(height_max, corner_points[i][1])
        height_min = min(height_min, corner_points[i][1])
        width_max = max(width_max,corner_points[i][0])
        width_min = min(width_min, corner_points[i][0])


    # Generate a evenly distributed line of numbers based on the 
    # min and max values, and the number of points desire in between
    complete_width = list(np.linspace(width_min, width_max, image_dimensions[0]))
    complete_height = list(np.linspace(height_min,height_max, image_dimensions[1]))

    # Create a list of all possible coordinates 
    all_coordinates = list(itertools.product(complete_width, complete_height))

    # initialize lists
    row_ans = list()
    final_ans = list()

    # append the first entry from the list of coordinates
    row_ans.append([all_coordinates[0][0], all_coordinates[0][1]])
    for i in range(1,len(all_coordinates)):

        # if a new row is detected, add the current row of coordinates to the final
        # answer and reset the row
        if all_coordinates[i][0] != row_ans[-1][0]:
            final_ans.append(row_ans)
            row_ans = list()
        
        # add the pair of coordinates to the row
        row_ans.append([all_coordinates[i][0], all_coordinates[i][1]])
    
    # add the row to the final answer
    final_ans.append(row_ans)
    return final_ans


