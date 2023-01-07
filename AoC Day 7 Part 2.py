import re

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')


def get_number(str):

    m = re.match('\d+', str)

    if m:
        return int(m.group())
    
    return None


def get_dir_mapping():

    current_dir = ''

    for instruc in input:

        if instruc.find('$ cd') == 0 and instruc != '$ cd ..':
            
            parent_dir = current_dir
            current_dir = instruc[5:]
            
            if current_dir in dirs:
                current_dir = current_dir + f'_{parent_dir}'
            
            dirs[current_dir] = {'size': 0, 'parent_dir': parent_dir, 'child_dir': []}

        elif instruc == '$ cd ..':
            
            current_dir = dirs[current_dir]['parent_dir']

        elif instruc.find('dir') == 0:
            
            child_dir = instruc[4:]
            duplicate_name = False
            
            for info in dirs.values():
                if child_dir in info['child_dir']:
                    duplicate_name = True
                    break

            if duplicate_name:
                dirs[current_dir]['child_dir'].append(child_dir + f'_{current_dir}')
            else: dirs[current_dir]['child_dir'].append(child_dir)

        elif get_number(instruc) != None:
            dirs[current_dir]['size'] += get_number(instruc)
    
    return


def get_parent_child_rels(info):

    children = info['child_dir']

    if children == []:
        return

    parent_child[dir_to_modify].extend(children)

    for dir, values in dirs.items():
        if dir in children:
            get_parent_child_rels(values)

    return


# script
dirs = {}

get_dir_mapping()

parent_child = {}
dir_to_modify = ''

for dir, info in dirs.items():
    parent_child[dir] = []
    dir_to_modify = dir
    get_parent_child_rels(info)

dir_sizes = {}

for dir, children in parent_child.items():
    dir_sizes[dir] = dirs[dir]['size']
    for child_dir in children:
        dir_sizes[dir] += dirs[child_dir]['size']

space_needed = 30000000 - (70000000 - dir_sizes['/'])

candidates = []

for dir, size in dir_sizes.items():
    if size >= space_needed:
        candidates.append(size)

candidates.sort()

print(candidates[0])