import numpy as np
from day12classes import Region, Present


if __name__ == '__main__':
    with open('day12/day12.txt', 'r') as f:
        data = f.read()

    data = data.split('-')
    shapes = data[0]
    region_lines = data[-1].split('\n')

    shapes = shapes.split('\n')
    
    presents = []
    for i in range(len(shapes)):
        start = i * 5
        end = (i * 5) + 4

        if end > len(shapes):
            break
        
        shape = shapes[start+1:end]
        present = Present(i, shape)
        presents.append(present)

    
    regions: list[Region] = []

    for line in region_lines:
        dims = line.split(":")[0].split("x")
        if len(dims) == 2:
            w = int(dims[0])
            h = int(dims[1])
            
            requirements = line.split(":")[-1].strip().split(" ")
            requirements = [int(i) for i in requirements]

            region = Region(w, h, requirements)
            regions.append(region)
    
    valid_regions = []
    for region in regions:
        total_area = 0
        maximum_area = region.w * region.h
        requirements = region.requirements
        for i, requirement in enumerate(requirements):
            total_area += requirement * presents[i].area
        
        if total_area <= maximum_area:
           valid_regions.append(region)


    regions[0].place_present(presents[0], 1, 1)
    print(regions[0])
    print(len(valid_regions))


