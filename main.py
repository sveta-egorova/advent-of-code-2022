import time


def find_max_calories(filename='data/day1_short'):
    with open(filename) as file:
        cur_elf_sum = 0
        max_elf_sum = 0
        for line in file:
            if line == '\n':
                cur_elf_sum = 0
            else:
                cur_elf_sum += int(line)
                max_elf_sum = max(cur_elf_sum, max_elf_sum)
    return max_elf_sum


def find_sum_of_top_k_calories(filename='data/day1_short', k=3):
    calories_list = []
    with open(filename) as file:
        cur_elf_sum = 0
        for line in file:
            if line == '\n':
                prev_elf_sum = cur_elf_sum
                calories_list.append(prev_elf_sum)
                cur_elf_sum = 0
            else:
                cur_elf_sum += int(line)
        calories_list.append(cur_elf_sum)
    return sum(sorted(calories_list, reverse=True)[:k])


def count_points_strategy1(filename):

    shape_points = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    strategy_mapping = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    outcome_points = {
        'win': 6,
        'draw': 3,
        'lose': 0
    }

    points_total = 0

    with open(filename) as file:
        for line in file:
            his_turn = line[0]
            my_turn = line[2]
            points_total += shape_points[strategy_mapping[my_turn]]
            if strategy_mapping[my_turn] == his_turn:
                points_total += outcome_points['draw']
            elif ((his_turn == 'A' and strategy_mapping[my_turn] == 'B') or
                  (his_turn == 'B' and strategy_mapping[my_turn] == 'C') or
                  (his_turn == 'C' and strategy_mapping[my_turn] == 'A')):
                points_total += outcome_points['win']
            else:
                points_total += outcome_points['lose']

    return points_total


def count_points_strategy2(filename):

    shape_points = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    win_combos = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    lose_combos = {
        'B': 'A',
        'C': 'B',
        'A': 'C'
    }

    outcome_points = {
        'win': 6,
        'draw': 3,
        'lose': 0
    }

    points_total = 0

    with open(filename) as file:
        for line in file:
            his_turn = line[0]
            my_turn = line[2]
            if my_turn == 'X': # lose
                my_shape = lose_combos[his_turn]
                points_total += outcome_points['lose']
            elif my_turn == 'Y': # draw
                my_shape = his_turn
                points_total += outcome_points['draw']
            else: # win
                my_shape = win_combos[his_turn]
                points_total += outcome_points['win']
            points_total += shape_points[my_shape]

    return points_total


def count_rucksack_failures(filename):

    total_penalties = 0
    penalties = {}
    for i in range(1, 53):
        if i <= 26:
            offset = i + 96
        else:
            offset = i + 38
        penalties[chr(offset)] = i

    with open(filename) as file:
        for line in file:
            size = len(line.strip())
            if size > 0:
                first_compartment = line[:int(size/2)]
                second_compartment = line[int(size/2):]
                for item in first_compartment:
                    if item in second_compartment:
                        total_penalties += penalties[item]
                        break

    return total_penalties


def find_badges(filename):

    total_penalties = 0
    penalties = {}
    for i in range(1, 53):
        if i <= 26:
            offset = i + 96
        else:
            offset = i + 38
        penalties[chr(offset)] = i

    cur_pointer = 0
    cur_group = []

    with open(filename) as file:
        for line in file:
            cur_group.append(line.strip())
            if len(cur_group) == 3:
                for item in cur_group[0]:
                    if item in cur_group[1] and item in cur_group[2]:
                        common_element = item
                        total_penalties += penalties[common_element]
                        break
                # print(common_element)
                cur_pointer = 0
                cur_group = []
            else:
                cur_pointer += 1
                continue

    return total_penalties


def find_section_full_overlaps(filename):
    overlap_count = 0
    with open(filename) as file:
        for line in file:
            two_sections = line.strip().split(',')
            start_first = int(two_sections[0].split('-')[0])
            end_first = int(two_sections[0].split('-')[1])
            start_second = int(two_sections[1].split('-')[0])
            end_second = int(two_sections[1].split('-')[1])
            if ((start_first <= start_second and end_first >= end_second) or
                (start_second <= start_first and end_second >= end_first)):
                overlap_count += 1

    return overlap_count


def find_section_partial_overlaps(filename):
    overlap_count = 0
    with open(filename) as file:
        for line in file:
            two_sections = line.strip().split(',')
            start_first = int(two_sections[0].split('-')[0])
            end_first = int(two_sections[0].split('-')[1])
            start_second = int(two_sections[1].split('-')[0])
            end_second = int(two_sections[1].split('-')[1])
            if ((start_first <= start_second and end_first >= start_second) or
                (start_second <= start_first and end_second >= start_first)):
                overlap_count += 1

    return overlap_count


def find_top_blocks_old(filename, type='long'):

    current_state = {
        1: 'zjg',
        2: 'qlrpwfvc',
        3: 'fpmclgr',
        4: 'lfbwphm',
        5: 'gcfsvq',
        6: 'whjzmqtl',
        7: 'hfsbv',
        8: 'fjzs',
        9: 'mcdpfhbt'
    }

    if type == 'short':
        current_state = {
            1: 'zn',
            2: 'mcd',
            3: 'p'
        }

    with open(filename) as file:
        for line in file:
            line_tokens = line.split()
            # print(line_tokens)
            if line_tokens:
                if line_tokens[0] == 'move':
                    how_many = int(line_tokens[1])
                    from_where = int(line_tokens[3])
                    to_where = int(line_tokens[5])
                    # print(how_many, from_where, to_where)

                    for step in range(how_many):
                        new_state_dest = current_state[to_where] + current_state[from_where][-1:]
                        current_state[to_where] = new_state_dest
                        new_state_origin = current_state[from_where][:-1]
                        current_state[from_where] = new_state_origin
                        # original_state[to_where] += original_state[from_where][-1:]
                        # original_state[from_where] = original_state[from_where][:-1]

    top_blocks = ''
    for key, value in current_state.items():
        top_blocks += value[-1:]
    return top_blocks


def find_top_blocks_new(filename, type='long'):

    current_state = {
        1: 'zjg',
        2: 'qlrpwfvc',
        3: 'fpmclgr',
        4: 'lfbwphm',
        5: 'gcfsvq',
        6: 'whjzmqtl',
        7: 'hfsbv',
        8: 'fjzs',
        9: 'mcdpfhbt'
    }

    if type == 'short':
        current_state = {
            1: 'zn',
            2: 'mcd',
            3: 'p'
        }

    with open(filename) as file:
        for line in file:
            line_tokens = line.split()
            # print(line_tokens)
            if line_tokens:
                if line_tokens[0] == 'move':
                    how_many = int(line_tokens[1])
                    from_where = int(line_tokens[3])
                    to_where = int(line_tokens[5])
                    # print(how_many, from_where, to_where)
                    new_state_dest = current_state[to_where] + current_state[from_where][-how_many:]
                    current_state[to_where] = new_state_dest
                    new_state_origin = current_state[from_where][:-how_many]
                    current_state[from_where] = new_state_origin

    top_blocks = ''
    for key, value in current_state.items():
        top_blocks += value[-1:]
    return top_blocks


def find_start_marker(filename):
    with open(filename) as file:
        for line in file:
            cur_position = 0
            for ix in range(len(line)):
                candidate_marker = line[ix:ix+4]
                # print(candidate_marker)
                occurrences = {}
                for char in candidate_marker:
                    if char in occurrences:
                        occurrences[char] += 1
                    else:
                        occurrences[char] = 1
                if len(occurrences) == 4 and max(occurrences.values()) == 1:
                    return ix + 4
                else:
                    occurrences = {}


def find_start_message(filename):
    with open(filename) as file:
        for line in file:
            cur_position = 0
            for ix in range(len(line)):
                candidate_marker = line[ix:ix+14]
                # print(candidate_marker)
                occurrences = {}
                for char in candidate_marker:
                    if char in occurrences:
                        occurrences[char] += 1
                    else:
                        occurrences[char] = 1
                if len(occurrences) == 14 and max(occurrences.values()) == 1:
                    return ix + 14
                else:
                    occurrences = {}


def find_directory_sizes(filename):
    parents = {}
    dir_size = {}

    with open(filename) as file:
        for line in file:
            if line.startswith('$ cd /'):
                cur_directory = 'root'
            elif line.startswith('$ cd ..'):
                cur_directory = parents[cur_directory]
            elif line.startswith('$ cd '):
                child_folder_name = line.split()[2]
                cur_directory = cur_directory + '/' + child_folder_name
            elif line.startswith('$ ls') or not line:
                pass
            else:
                folder_items = line.split()
                item_details = folder_items[0]
                item_name = folder_items[1]
                if item_details == 'dir':
                    full_path = cur_directory + '/' + item_name
                    parents[full_path] = cur_directory
                else:
                    if cur_directory not in dir_size:
                        dir_size[cur_directory] = int(item_details)
                    else:
                        dir_size[cur_directory] = dir_size[cur_directory] + int(item_details)
                    # add to the immediate parent
                    dir_for_parent_search = cur_directory
                    while True:
                        if dir_for_parent_search == 'root':
                            break
                        immediate_parent = parents[dir_for_parent_search]
                        if immediate_parent not in dir_size:
                            dir_size[immediate_parent] = int(item_details)
                        else:
                            dir_size[immediate_parent] = dir_size[immediate_parent] + int(item_details)
                        dir_for_parent_search = immediate_parent

    # print(parents)
    # print(children)
    # print(dir_size)

    sizes = dir_size.values()
    elements_below_100 = [el for el in sizes if el < 100000]

    return sum(elements_below_100)


def find_which_to_remove(filename):
    parents = {}
    dir_size = {}

    with open(filename) as file:
        for line in file:
            if line.startswith('$ cd /'):
                cur_directory = 'root'
            elif line.startswith('$ cd ..'):
                cur_directory = parents[cur_directory]
            elif line.startswith('$ cd '):
                child_folder_name = line.split()[2]
                cur_directory = cur_directory + '/' + child_folder_name
            elif line.startswith('$ ls') or not line:
                pass
            else:
                folder_items = line.split()
                item_details = folder_items[0]
                item_name = folder_items[1]
                if item_details == 'dir':
                    full_path = cur_directory + '/' + item_name
                    parents[full_path] = cur_directory
                else:
                    if cur_directory not in dir_size:
                        dir_size[cur_directory] = int(item_details)
                    else:
                        dir_size[cur_directory] = dir_size[cur_directory] + int(item_details)
                    # add to the immediate parent
                    dir_for_parent_search = cur_directory
                    while True:
                        if dir_for_parent_search == 'root':
                            break
                        immediate_parent = parents[dir_for_parent_search]
                        if immediate_parent not in dir_size:
                            dir_size[immediate_parent] = int(item_details)
                        else:
                            dir_size[immediate_parent] = dir_size[immediate_parent] + int(item_details)
                        dir_for_parent_search = immediate_parent

    space_left = 70000000 - dir_size['root']
    need_to_free_up = 30000000 - space_left
    deletion_candidates = []
    for key, value in dir_size.items():
        if value >= need_to_free_up:
            deletion_candidates.append(value)

    return sorted(deletion_candidates)[0]


def find_visible_trees(filename):

    grid = []
    with open(filename) as file:
        for line in file:
            cur_row = []
            for char in line.strip():
                cur_row.append(int(char))
            grid.append(cur_row)
    grid_width = len(cur_row)
    grid_height = len(grid)

    count_visible = 2 * grid_width + 2 * grid_height - 4

    for y in range(1, grid_height-1): # vertical axis of the cur element
        for x in range(1, grid_width-1): # horizontal axis of the cur element
            neighbors_left = []
            neighbors_right = []
            neighbors_up = []
            neighbors_down = []
            for i in range(grid_width): # check horizontal neighbors
                if i < x:
                    neighbors_left.append(grid[y][i])
                elif i == x:
                    pass
                else:
                    neighbors_right.append(grid[y][i])
            for k in range(grid_height): # check horizontal neighbors
                if k < y:
                    neighbors_up.append(grid[k][x])
                elif k == y:
                    pass
                else:
                    neighbors_down.append(grid[k][x])
            if grid[y][x] > max(neighbors_left) \
                    or grid[y][x] > max(neighbors_right) \
                    or grid[y][x] > max(neighbors_up) \
                    or grid[y][x] > max(neighbors_down):
                count_visible += 1

    return count_visible


def find_visibility_score(filename):

    grid = []
    with open(filename) as file:
        for line in file:
            cur_row = []
            for char in line.strip():
                cur_row.append(int(char))
            grid.append(cur_row)
    grid_width = len(cur_row)
    grid_height = len(grid)

    visibility_scores = []

    for y in range(1, grid_height-1): # vertical axis of the cur element
        for x in range(1, grid_width-1): # horizontal axis of the cur element
            neighbors_left = []
            neighbors_right = []
            neighbors_up = []
            neighbors_down = []
            for i in range(grid_width): # check horizontal neighbors
                if i < x:
                    neighbors_left.append(grid[y][i])
                elif i == x:
                    pass
                else:
                    neighbors_right.append(grid[y][i])
            for k in range(grid_height): # check horizontal neighbors
                if k < y:
                    neighbors_up.append(grid[k][x])
                elif k == y:
                    pass
                else:
                    neighbors_down.append(grid[k][x])
            score_left = 0
            score_right = 0
            score_top = 0
            score_bottom = 0
            for l in reversed(neighbors_left):
                if l >= grid[y][x]:
                    score_left += 1
                    break
                else:
                    score_left += 1
            for m in neighbors_right:
                if m >= grid[y][x]:
                    score_right += 1
                    break
                else:
                    score_right += 1
            for n in reversed(neighbors_up):
                if n >= grid[y][x]:
                    score_top += 1
                    break
                else:
                    score_top += 1
            for o in neighbors_down:
                if o >= grid[y][x]:
                    score_bottom += 1
                    break
                else:
                    score_bottom += 1

            overall_score = score_left * score_right * score_top * score_bottom
            visibility_scores.append(overall_score)

    return max(visibility_scores)


def find_tail_positions_one_knot(filename):

    cur_pos_head_x = 0
    cur_pos_head_y = 0
    cur_pos_tail_x = 0
    cur_pos_tail_y = 0

    # position is marked as (y-axis, x-axis)

    head_positions = [(cur_pos_head_y,cur_pos_head_x)]
    tail_positions = [(cur_pos_tail_y,cur_pos_tail_x)]

    with open(filename) as file:
        for line in file:
            direction, steps = line.strip().split()

            for step in range(int(steps)):
                # change head positions
                if direction == 'R':
                    cur_pos_head_x += 1
                elif direction == 'L':
                    cur_pos_head_x -= 1
                elif direction == 'U':
                    cur_pos_head_y += 1
                elif direction == 'D':
                    cur_pos_head_y -= 1
                else:
                    pass
                # change tail positions

                # if vertically aligned and horizontally not
                if cur_pos_head_y == cur_pos_tail_y and cur_pos_head_x > cur_pos_tail_x + 1:
                    cur_pos_tail_x += 1
                elif cur_pos_head_y == cur_pos_tail_y and cur_pos_head_x < cur_pos_tail_x - 1:
                    cur_pos_tail_x -= 1
                # if horizontally aligned and vertically not
                elif cur_pos_head_x == cur_pos_tail_x and cur_pos_head_y > cur_pos_tail_y + 1:
                    cur_pos_tail_y += 1
                elif cur_pos_head_x == cur_pos_tail_x and cur_pos_head_y < cur_pos_tail_y - 1:
                    cur_pos_tail_y -= 1
                # print(abs(cur_pos_head_y - cur_pos_tail_y))
                # print(abs(cur_pos_head_y - cur_pos_tail_y))
                # if misaligned both vertically and horizontally and at lease one of the dimensions by more than one
                elif (cur_pos_head_y != cur_pos_tail_y and cur_pos_head_x != cur_pos_tail_x
                      and (abs(cur_pos_head_y - cur_pos_tail_y) > 1 or abs(cur_pos_head_x - cur_pos_tail_x) > 1)):
                    # print('jump now')
                    # higher misalignment vertically
                    if abs(cur_pos_head_y - cur_pos_tail_y) > abs(cur_pos_head_x - cur_pos_tail_x):
                        if cur_pos_head_y > cur_pos_tail_y + 1:
                            cur_pos_tail_y += 1
                        elif cur_pos_head_y < cur_pos_tail_y - 1:
                            cur_pos_tail_y -= 1
                        cur_pos_tail_x = cur_pos_head_x
                    # higher misalignment horizontally
                    if abs(cur_pos_head_y - cur_pos_tail_y) < abs(cur_pos_head_x - cur_pos_tail_x):
                        if cur_pos_head_x > cur_pos_tail_x + 1:
                            cur_pos_tail_x += 1
                        elif cur_pos_head_x < cur_pos_tail_x - 1:
                            cur_pos_tail_x -= 1
                        cur_pos_tail_y = cur_pos_head_y
                else:
                    pass
                head_positions.append((cur_pos_head_y,cur_pos_head_x))
                # print((cur_pos_head_y,cur_pos_head_x))
                tail_positions.append((cur_pos_tail_y,cur_pos_tail_x))
                # print((cur_pos_tail_y,cur_pos_tail_x))
                # print('----')

    # print(tail_positions)

    unique_tail_positions = []
    for position in tail_positions:
        if position not in unique_tail_positions:
            unique_tail_positions.append(position)
    # print(unique_tail_positions)
    # print(len(unique_tail_positions))
    return len(unique_tail_positions)


def update_tail_position(new_head_pos, old_tail_pos):
    cur_pos_head_y = new_head_pos[0]
    cur_pos_head_x = new_head_pos[1]
    cur_pos_tail_y = old_tail_pos[0]
    cur_pos_tail_x = old_tail_pos[1]

    # if vertically aligned and horizontally not
    if cur_pos_head_y == cur_pos_tail_y and cur_pos_head_x > cur_pos_tail_x + 1:
        cur_pos_tail_x += 1
    elif cur_pos_head_y == cur_pos_tail_y and cur_pos_head_x < cur_pos_tail_x - 1:
        cur_pos_tail_x -= 1
    # if horizontally aligned and vertically not
    elif cur_pos_head_x == cur_pos_tail_x and cur_pos_head_y > cur_pos_tail_y + 1:
        cur_pos_tail_y += 1
    elif cur_pos_head_x == cur_pos_tail_x and cur_pos_head_y < cur_pos_tail_y - 1:
        cur_pos_tail_y -= 1
    # if misaligned both vertically and horizontally and at lease one of the dimensions by more than one
    elif (cur_pos_head_y != cur_pos_tail_y and cur_pos_head_x != cur_pos_tail_x
          and (abs(cur_pos_head_y - cur_pos_tail_y) > 1 or abs(cur_pos_head_x - cur_pos_tail_x) > 1)):
        # higher misalignment vertically
        if abs(cur_pos_head_y - cur_pos_tail_y) > abs(cur_pos_head_x - cur_pos_tail_x):
            if cur_pos_head_y > cur_pos_tail_y + 1:
                cur_pos_tail_y += 1
            elif cur_pos_head_y < cur_pos_tail_y - 1:
                cur_pos_tail_y -= 1
            cur_pos_tail_x = cur_pos_head_x
        # higher misalignment horizontally
        if abs(cur_pos_head_y - cur_pos_tail_y) < abs(cur_pos_head_x - cur_pos_tail_x):
            if cur_pos_head_x > cur_pos_tail_x + 1:
                cur_pos_tail_x += 1
            elif cur_pos_head_x < cur_pos_tail_x - 1:
                cur_pos_tail_x -= 1
            cur_pos_tail_y = cur_pos_head_y
        # equal misalignment horizontally and vertically
        if abs(cur_pos_head_y - cur_pos_tail_y) == abs(cur_pos_head_x - cur_pos_tail_x):
            if cur_pos_head_x > cur_pos_tail_x + 1:
                cur_pos_tail_x += 1
            elif cur_pos_head_x < cur_pos_tail_x - 1:
                cur_pos_tail_x -= 1
            if cur_pos_head_y > cur_pos_tail_y + 1:
                cur_pos_tail_y += 1
            elif cur_pos_head_y < cur_pos_tail_y - 1:
                cur_pos_tail_y -= 1
    else:
        pass

    return cur_pos_tail_y, cur_pos_tail_x


def find_tail_positions_ten_knots(filename):

    cur_pos_head_x = 0
    cur_pos_head_y = 0
    cur_pos_tail_x = 0
    cur_pos_tail_y = 0

    tail_knots = [(cur_pos_head_y,cur_pos_head_x)] + [(cur_pos_tail_y,cur_pos_tail_x)] * 9

    # position is marked as (y-axis, x-axis)

    all_head_positions = [tail_knots[0]]
    all_tail_positions = [tail_knots[9]]

    with open(filename) as file:
        for line in file:
            direction, steps = line.strip().split()

            for step in range(int(steps)):
                # change head positions
                if direction == 'R':
                    cur_pos_head_x += 1
                elif direction == 'L':
                    cur_pos_head_x -= 1
                elif direction == 'U':
                    cur_pos_head_y += 1
                elif direction == 'D':
                    cur_pos_head_y -= 1
                else:
                    pass
                tail_knots[0] = (cur_pos_head_y,cur_pos_head_x)

                # change tail positions
                for i in range(1,10):
                    tail_knots[i] = update_tail_position(tail_knots[i-1], tail_knots[i])

                all_head_positions.append((cur_pos_head_y,cur_pos_head_x))
                all_tail_positions.append(tail_knots[9])

    unique_tail_positions = []
    for position in all_tail_positions:
        if position not in unique_tail_positions:
            unique_tail_positions.append(position)
    return len(unique_tail_positions)


def compute_signal_strengths(filename):

    x_cycle_start = 1
    current_cycle = 1
    x_values = {}

    with open(filename) as file:
        for line in file:
            if line.strip() == 'noop':
                x_values[current_cycle] = x_cycle_start
                current_cycle += 1
            elif line.strip().split()[0] == 'addx':
                value_to_add = int(line.strip().split()[1])
                x_values[current_cycle] = x_cycle_start
                current_cycle += 1
                x_values[current_cycle] = x_cycle_start
                current_cycle += 1
                x_cycle_start += value_to_add
            else:
                pass

    signal_sum = 0
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    for cycle in cycles_of_interest:
        signal_sum += cycle * x_values[cycle]

    return signal_sum


def draw_image(filename):

    x_cycle_start = 1
    current_cycle = 0
    image = ''
    x_values = {}
    stripes = {}
    cur_row = 0

    with open(filename) as file:
        for line in file:
            if line.strip() == 'noop':
                x_values[current_cycle] = x_cycle_start
                stripe_covers = [x_cycle_start -1, x_cycle_start, x_cycle_start + 1]
                stripes[current_cycle] = stripe_covers
                if current_cycle - cur_row * 40 in stripe_covers:
                    image += '#'
                else:
                    image += '.'
                if current_cycle in [39, 79, 119, 159, 199, 39]:
                    image += '\n'
                    cur_row += 1
                current_cycle += 1
            elif line.strip().split()[0] == 'addx':
                value_to_add = int(line.strip().split()[1])
                x_values[current_cycle] = x_cycle_start
                stripe_covers = [x_cycle_start -1, x_cycle_start, x_cycle_start + 1]
                stripes[current_cycle] = stripe_covers
                if current_cycle - cur_row * 40 in stripe_covers:
                    image += '#'
                else:
                    image += '.'
                if current_cycle in [39, 79, 119, 159, 199, 39]:
                    image += '\n'
                    cur_row += 1
                current_cycle += 1
                x_values[current_cycle] = x_cycle_start
                stripes[current_cycle] = stripe_covers
                if current_cycle - cur_row * 40 in stripe_covers:
                    image += '#'
                else:
                    image += '.'
                if current_cycle in [39, 79, 119, 159, 199, 39]:
                    image += '\n'
                    cur_row += 1
                current_cycle += 1
                x_cycle_start += value_to_add
            else:
                pass

    print(image)
    # print(stripes)


def find_monkey_business_test():

    monkey_state = [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74]
    ]

    monkey_test = [
        (lambda x: x * 19, 23, 2, 3),
        (lambda x: x + 6, 19, 2, 0),
        (lambda x: x * x, 13, 1, 3),
        (lambda x: x + 3, 17, 0, 1)
    ]

    monkey_items_inspected = [
        0,
        0,
        0,
        0
    ]

    cur_round = 0

    while cur_round < 20:
        for monkey in range(len(monkey_state)):
            cur_state = monkey_state[monkey]
            cur_test = monkey_test[monkey]
            for item in cur_state:
                monkey_items_inspected[monkey] += 1
                new_worry_level = cur_test[0](item)
                new_worry_level = int(new_worry_level / 3)
                who_receives = cur_test[2] if new_worry_level % cur_test[1] == 0 else cur_test[3]
                monkey_state[who_receives].append(new_worry_level)
            monkey_state[monkey] = []
        cur_round += 1

    # print(monkey_items_inspected)

    top_monkey_businesses = sorted(monkey_items_inspected)[-2:]

    return top_monkey_businesses[0] * top_monkey_businesses[1]


def find_monkey_business():

    monkey_state = [
        [83, 97, 95, 67],
        [71, 70, 79, 88, 56, 70],
        [98, 51, 51, 63, 80, 85, 84, 95],
        [77, 90, 82, 80, 79],
        [68],
        [60, 94],
        [81, 51, 85],
        [98, 81, 63, 65, 84, 71, 84]
    ]

    monkey_test = [
        (lambda x: x * 19, 17, 2, 7),
        (lambda x: x + 2, 19, 7, 0),
        (lambda x: x + 7, 7, 4, 3),
        (lambda x: x + 1, 11, 6, 4),
        (lambda x: x * 5, 13, 6, 5),
        (lambda x: x + 5, 3, 1, 0),
        (lambda x: x * x, 5, 5, 1),
        (lambda x: x + 3, 2, 2, 3)

    ]

    monkey_items_inspected = [0] * 8

    cur_round = 0

    while cur_round < 20:
        for monkey in range(len(monkey_state)):
            cur_state = monkey_state[monkey]
            cur_test = monkey_test[monkey]
            for item in cur_state:
                monkey_items_inspected[monkey] += 1
                new_worry_level = cur_test[0](item)
                new_worry_level = int(new_worry_level / 3)
                who_receives = cur_test[2] if new_worry_level % cur_test[1] == 0 else cur_test[3]
                monkey_state[who_receives].append(new_worry_level)
            monkey_state[monkey] = []
        cur_round += 1

    # print(monkey_items_inspected)

    top_monkey_businesses = sorted(monkey_items_inspected)[-2:]

    return top_monkey_businesses[0] * top_monkey_businesses[1]


def find_monkey_business_extra():

    monkey_state = [
        [83, 97, 95, 67],
        [71, 70, 79, 88, 56, 70],
        [98, 51, 51, 63, 80, 85, 84, 95],
        [77, 90, 82, 80, 79],
        [68],
        [60, 94],
        [81, 51, 85],
        [98, 81, 63, 65, 84, 71, 84]
    ]

    monkey_test = [
        (lambda x: x * 19, 17, 2, 7),
        (lambda x: x + 2, 19, 7, 0),
        (lambda x: x + 7, 7, 4, 3),
        (lambda x: x + 1, 11, 6, 4),
        (lambda x: x * 5, 13, 6, 5),
        (lambda x: x + 5, 3, 1, 0),
        (lambda x: x * x, 5, 5, 1),
        (lambda x: x + 3, 2, 2, 3)

    ]

    reduction_factor = 1
    for factor in [test[1] for test in monkey_test]:
        reduction_factor *= factor
    # print('reduction factor is: ', reduction_factor)

    num_monkeys = len(monkey_state)
    monkey_items_inspected = [0] * num_monkeys
    cur_round = 0

    time_start = time.time()
    while cur_round < 10000:
        for monkey in range(num_monkeys):
            cur_state = monkey_state[monkey]
            cur_test = monkey_test[monkey]
            for item in cur_state:
                monkey_items_inspected[monkey] += 1
                new_worry_level = cur_test[0](item)
                while new_worry_level > reduction_factor: # this is all factors multiplied by each other
                    new_worry_level -= reduction_factor
                # new_worry_level = int(new_worry_level / 3)
                who_receives = cur_test[2] if new_worry_level % cur_test[1] == 0 else cur_test[3]
                monkey_state[who_receives].append(new_worry_level)
            monkey_state[monkey] = []
        cur_round += 1
        if cur_round % 500 == 0:
            time_taken = time.time() - time_start
            # print(f'500 rounds up to {cur_round} took {time_taken} s')
            # print('cur_state: ', str(monkey_state))
            # print('items_inspected: ', monkey_items_inspected)
            time_start = time.time()
            # print(cur_round)
            # print(monkey_items_inspected)

    # print(monkey_items_inspected)

    top_monkey_businesses = sorted(monkey_items_inspected)[-2:]

    return top_monkey_businesses[0] * top_monkey_businesses[1]


from collections import deque

class TreeNode:
    def __init__(self, pos, grid, cur_level, visited_by_parent, grid_completion):
        self.position = pos
        self.val = grid[pos[0]][pos[1]]
        self.grid = grid
        self.cur_level = cur_level
        self.visited_by_parent = visited_by_parent
        self.grid_completion = grid_completion
        self.left, self.right, self.up, self.down = None, None, None, None
        print('level being done: ', self.cur_level)
        # this keeps only the level number for the shortest path
        if self.grid_completion[pos[0]][pos[1]] >= self.cur_level:
            if (self.grid_completion[pos[0]][pos[1]] < 50 and self.grid_completion[pos[0]][pos[1]] > self.cur_level):
                print(f'Congrats, you have just found a faster route to {pos}, '
                      f'it can be reached in {self.cur_level} levels and not {self.grid_completion[pos[0]][pos[1]]}')
            self.grid_completion[pos[0]][pos[1]] = self.cur_level
        else:
            print(f'Oh, this is a long route to {pos}, '
                  f'it can be reached in {self.grid_completion[pos[0]][pos[1]]} levels and not {self.cur_level}')
            self.cur_level = self.grid_completion[pos[0]][pos[1]]
        print('grid_completion: ', grid_completion)
        if self.val == 26:
            print('GOTCHA!')
        grid_height = len(grid)
        grid_width = len(grid[0])
        if self.cur_level < 100:
            if self.position[0] > 0:
                position_up = (self.position[0] - 1, self.position[1])
                new_value = grid[position_up[0]][position_up[1]]
                # This prevents stepping on the same blocks as used before in that path, and keeps only valid moves
                if position_up not in self.visited_by_parent and new_value <= self.val + 1:
                    print(f'{chr(self.val+97)} on {pos} go up to {chr(new_value+97)}')
                    new_visits = self.visited_by_parent + [position_up]
                    self.up = TreeNode(position_up, self.grid, self.cur_level + 1, new_visits, self.grid_completion)
            if self.position[0] < grid_height - 1:
                position_down = (self.position[0] + 1, self.position[1])
                new_value = grid[position_down[0]][position_down[1]]
                if position_down not in self.visited_by_parent and new_value <= self.val + 1:
                    print(f'{chr(self.val+97)} on {pos} go down to {chr(new_value+97)}')
                    new_visits = self.visited_by_parent + [position_down]
                    self.down = TreeNode(position_down, self.grid, self.cur_level + 1, new_visits, self.grid_completion)
            if self.position[1] > 0:
                position_left = (self.position[0], self.position[1] - 1)
                new_value = grid[position_left[0]][position_left[1]]
                if position_left not in self.visited_by_parent and new_value <= self.val + 1:
                    print(f'{chr(self.val+97)} on {pos} go left to {chr(new_value+97)}')
                    new_visits = self.visited_by_parent + [position_left]
                    self.left = TreeNode(position_left, self.grid, self.cur_level + 1, new_visits, self.grid_completion)
            if self.position[1] < grid_width - 1:
                position_right = (self.position[0], self.position[1] + 1)
                new_value = grid[position_right[0]][position_right[1]]
                if position_right not in self.visited_by_parent and new_value <= self.val + 1:
                    print(f'{chr(self.val+97)} on {pos} go right to {chr(new_value+97)}')
                    new_visits = self.visited_by_parent + [position_right]
                    self.right = TreeNode(position_right, self.grid, self.cur_level + 1, new_visits, self.grid_completion)



def find_neighbours(cur_node, grid, visited, movement):
    grid_height = len(grid)
    grid_width = len(grid[0])
    cur_value = cur_node[2]
    # print('cur_node: ', cur_node)
    # print('visited: ', visited)

    # visited.add(cur_node)
    if cur_value == 'S':
        cur_value = 'a'
    if cur_value == 'E':
        return None
    neighbors = []
    if cur_node[0] > 0:
        up_value = grid[cur_node[0] - 1][cur_node[1]]
        up_node = (cur_node[0] - 1, cur_node[1], up_value)
        new_history = visited.copy()
        new_history.add(up_node)
        up_node_with_history = (up_node, movement + '^', new_history)
        if up_value == 'E':
            if ord('z') - 1 <= ord(cur_value) and up_node not in visited:
                neighbors.append(up_node_with_history) # up
        else:
            if ord(up_value) - 1 <= ord(cur_value) and up_node not in visited:
                neighbors.append(up_node_with_history) # up
    if cur_node[0] < grid_height - 1:
        down_value = grid[cur_node[0] + 1][cur_node[1]]
        down_node = (cur_node[0] + 1, cur_node[1], down_value)
        new_history = visited.copy()
        new_history.add(down_node)
        down_node_with_history = (down_node, movement + 'v', new_history)
        if down_value == 'E':
            if ord('z') - 1 <= ord(cur_value) and down_value not in visited:
                neighbors.append(down_node_with_history) # down
        else:
            if ord(down_value) - 1 <= ord(cur_value) and down_node not in visited:
                neighbors.append(down_node_with_history) # down
    if cur_node[1] > 0:
        left_value = grid[cur_node[0]][cur_node[1] - 1]
        left_node = (cur_node[0], cur_node[1] - 1, left_value)
        new_history = visited.copy()
        new_history.add(left_node)
        left_node_with_history = (left_node, movement + '<', new_history)
        if left_value == 'E':
            if ord('z') - 1 <= ord(cur_value) and left_value not in visited:
                neighbors.append(left_node_with_history) # left
        else:
            if ord(left_value) - 1 <= ord(cur_value) and left_node not in visited:
                neighbors.append(left_node_with_history) # left
    if cur_node[1] < grid_width - 1:
        right_value = grid[cur_node[0]][cur_node[1] + 1]
        right_node = (cur_node[0], cur_node[1] + 1, right_value)
        new_history = visited.copy()
        new_history.add(right_node)
        right_node_with_history = (right_node, movement + '>', new_history)
        if right_value == 'E':
            if ord('z') - 1 <= ord(cur_value) and right_value not in visited:
                neighbors.append(right_node_with_history) # right
        else:
            if ord(right_value) - 1 <= ord(cur_value) and right_node not in visited:
                neighbors.append(right_node_with_history) # right
    # print('neighbors: ', neighbors)
    return neighbors


def find_valid_neighbours(cur_node, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    cur_value = cur_node[2]

    if cur_value == 'S':
        cur_value = 'a'
    if cur_value == 'E':
        return None
    neighbors = []
    if cur_node[0] > 0:
        up_value = grid[cur_node[0] - 1][cur_node[1]]
        ord_to_check = ord('z') if up_value == 'E' else ord(up_value)
        up_node = (cur_node[0] - 1, cur_node[1], up_value)
        if ord_to_check - 1 <= ord(cur_value):
            neighbors.append(up_node) # up
    if cur_node[0] < grid_height - 1:
        down_value = grid[cur_node[0] + 1][cur_node[1]]
        ord_to_check = ord('z') if down_value == 'E' else ord(down_value)
        down_node = (cur_node[0] + 1, cur_node[1], down_value)
        if ord_to_check - 1 <= ord(cur_value):
            neighbors.append(down_node) # down
    if cur_node[1] > 0:
        left_value = grid[cur_node[0]][cur_node[1] - 1]
        ord_to_check = ord('z') if left_value == 'E' else ord(left_value)
        left_node = (cur_node[0], cur_node[1] - 1, left_value)
        if ord_to_check - 1 <= ord(cur_value):
            neighbors.append(left_node) # left
    if cur_node[1] < grid_width - 1:
        right_value = grid[cur_node[0]][cur_node[1] + 1]
        ord_to_check = ord('z') if right_value == 'E' else ord(right_value)
        right_node = (cur_node[0], cur_node[1] + 1, right_value)
        if ord_to_check - 1 <= ord(cur_value):
            neighbors.append(right_node) # right
    # print('neighbors: ', neighbors)
    return neighbors


def find_quickest_route(filename):
    grid = []
    cur_row = 0
    # a_counter = 0
    # count_letters = {}
    b_list = []
    min_steps_for_all_a = []
    with open(filename) as file:
        for line in file:
            cur_row_char = list(line.strip())
            # for char in cur_row_char:
                # if char in count_letters:
                #     count_letters[char] += 1
                # else:
                #     count_letters[char] = 1
            if 'S' in cur_row_char:
                start_row = cur_row
                start_col = cur_row_char.index('S')
            if 'E' in cur_row_char:
                end_row = cur_row
                end_col = cur_row_char.index('E')
            for ix in range(len(cur_row_char)):
                if cur_row_char[ix] == 'b':
                    b_list.append((cur_row, ix, 'b'))
            grid.append(cur_row_char)
            cur_row += 1

    # print(count_letters)
    # return
    print('Total number of b: ', len(b_list))

    time_start = time.time()

    end_node = (end_row, end_col, 'E')
    grid_height = len(grid)
    grid_width = len((grid[0]))
    # neighbors = deque()
    # neighbors.append(start_node)
    # neighbors = [start_node]


    # print(steps_to_reach_ix[0][0][1])

    # steps_to_reach_ix = [[9999 for i in range(grid_width)] for i in range(grid_height)]
    # steps_to_reach_ix[start_row][start_col] = 0

    initial_neighbor_input = set()
    neighbors_df = [[initial_neighbor_input for i in range(grid_width)] for i in range(grid_height)]
    # print('start creating neighbors df')

    for row_ix in range(grid_height):
        for el_ix in range(grid_width):
            cur_node = (row_ix, el_ix, grid[row_ix][el_ix])
            neighbors_df[row_ix][el_ix] = find_valid_neighbours(cur_node, grid)
    # print('finish creating neighbors df')


    movement = ''
    step_history = []
    # movement_diagram = ('.'* grid_width + '\n') * grid_height
    # movement_diagram = [['.' for i in range(grid_width)] for i in range(grid_height)]
    # print(movement_diagram)


    # initial_input = (9999, movement, step_history)
    default_input = (9999, step_history)

    steps_and_history_to_reach_ix_general = [[default_input for i in range(grid_width)] for i in range(grid_height)]
    # steps_to_reach_ix = [[initial_input for i in range(grid_width)] for i in range(grid_height)]

    solutions = []
    b_counter = 0

    time_start = time.time()

    for start_node in b_list:
        b_counter += 1
        # start_node = (start_row, start_col, 'S')

        start_history = step_history.copy()
        start_history.append(start_node)

        steps_and_history_to_reach_ix = steps_and_history_to_reach_ix_general.copy()
        steps_and_history_to_reach_ix[start_row][start_col] = (0, start_history)
        # steps_to_reach_ix[start_row][start_col] = (0, movement, step_history)

        level_of_the_end = 9999
        cur_level = 0
        found_solution = False
        neighbors = [start_node]

        while neighbors and not found_solution:
            next_level_neighbors = []
            cur_level += 1
            # print(cur_level)
            # print(neighbors)

            for old_el in neighbors:
                # print(old_el)
                optimal_history_to_this_point = steps_and_history_to_reach_ix[old_el[0]][old_el[1]][1]
                # print('optimal_history_to_this_point', optimal_history_to_this_point)
                valid_neighbors = [el for el in neighbors_df[old_el[0]][old_el[1]] if el not in optimal_history_to_this_point]
                for proposed_neighbour in valid_neighbors:
                    previous_optimal_level = steps_and_history_to_reach_ix[proposed_neighbour[0]][proposed_neighbour[1]][0]
                    if previous_optimal_level > cur_level:
                        proposed_history = optimal_history_to_this_point.copy()
                        proposed_history.append(proposed_neighbour)
                        steps_and_history_to_reach_ix[proposed_neighbour[0]][proposed_neighbour[1]] = (cur_level, proposed_history)
                    if proposed_neighbour == end_node:
                        found_solution = True
                        level_of_the_end = cur_level
                    if proposed_neighbour not in next_level_neighbors:
                        next_level_neighbors.append(proposed_neighbour)

            neighbors = next_level_neighbors
        if b_counter % 5 == 0:
            time_it_took = time.time() - time_start
            print(f'Start positions analysed: {b_counter}')
            print(f'Running for one start position took {time_it_took} s')
            time_start = time.time()
        winning_strategy = steps_and_history_to_reach_ix[end_node[0]][end_node[1]]
        print('took this number of steps:', winning_strategy[0])
        solutions.append(winning_strategy[0])
    return solutions

    # level_of_the_end = 9999
    # cur_level = 0
    # visited = set()
    while neighbors and not found_solution:
        # print('cycle started with neighbors: ', neighbors)
        next_level_neighbors = []
        # print(cur_level)
        cur_level += 1

        for old_el in neighbors:
            optimal_movement_to_this_point = steps_to_reach_ix[old_el[0]][old_el[1]][1]
            optimal_history_to_this_point = steps_to_reach_ix[old_el[0]][old_el[1]][2]
            # print(f'Optimal to level {cur_level-1} and element {old_el} is {optimal_movement_to_this_point}')
            new_neighbors = find_neighbours(old_el, grid, optimal_history_to_this_point, optimal_movement_to_this_point)
            if new_neighbors is None:
                level_of_the_end = cur_level - 1
                break
            # print(new_neighbors)
            for new_el in new_neighbors:
                proposed_node = new_el[0]
                proposed_movement = new_el[1]
                proposed_history = new_el[2]
                previous_optimal_level = steps_to_reach_ix[proposed_node[0]][proposed_node[1]][0]
                if previous_optimal_level > cur_level:
                    steps_to_reach_ix[proposed_node[0]][proposed_node[1]] = (cur_level, proposed_movement, proposed_history)

                if proposed_node == end_node:
                    # print(cur_level)
                    found_solution = True
                    level_of_the_end = cur_level
                if proposed_node not in next_level_neighbors:
                    next_level_neighbors.append(proposed_node)
                # print('neighbors after element was appended', neighbors)

        neighbors = next_level_neighbors
        # print(steps_to_reach_ix)
        # print('neighbors after old element was deleted', neighbors)

    winning_strategy = steps_to_reach_ix[end_node[0]][end_node[1]]
    # print(winning_strategy)
    winning_history = winning_strategy[2]

    time_took = time.time() - time_start
    print(f'One iteration took {time_took} s')

    # for new_a in a_list:

    print('This is the diagram as the sequence of optimal steps:')
    print(proposed_movement)
    # print('\n')

    print(f'It took {len(proposed_movement)} steps, corresponding to {level_of_the_end} level')

    movement_diagram = [['.' for i in range(grid_width)] for i in range(grid_height)]
    cur_pos_for_diagram = (start_row, start_col)
    for i in range(level_of_the_end):
        this_step = proposed_movement[i]
        movement_diagram[cur_pos_for_diagram[0]][cur_pos_for_diagram[1]] = this_step #<>^v
        if this_step == '^':
            cur_pos_for_diagram = (cur_pos_for_diagram[0] - 1, cur_pos_for_diagram[1])
        elif this_step == 'v':
            cur_pos_for_diagram = (cur_pos_for_diagram[0] + 1, cur_pos_for_diagram[1])
        elif this_step == '<':
            cur_pos_for_diagram = (cur_pos_for_diagram[0], cur_pos_for_diagram[1] - 1)
        elif this_step == '>':
            cur_pos_for_diagram = (cur_pos_for_diagram[0], cur_pos_for_diagram[1] + 1)

    movement_diagram_as_str = ''
    for row in movement_diagram:
        cur_row = ''.join(row) + '\n'
        movement_diagram_as_str += cur_row

    print('This is the 2D diagram from start to end:')
    print(movement_diagram_as_str)
    return level_of_the_end


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TASK 1.1
    # max_elf_sum = find_max_calories('data/day1')
    # print(max_elf_sum)

    # TASK 1.2
    # top_k_sum = find_sum_of_top_k_calories('data/day1')
    # print(top_k_sum)

    # TASK 2.1
    # points_total = count_points_strategy1('data/day2')
    # print(points_total)

    # TASK 2.2
    # points_total = count_points_strategy2('data/day2')
    # print(points_total)

    # TASK 3.1
    # total_penalties = count_rucksack_failures('data/day3')
    # print(total_penalties)

    # TASK 3.2
    # total_penalties = find_badges('data/day3')
    # print(total_penalties)

    # TASK 4.1
    # overlaps = find_section_full_overlaps('data/day4')
    # print(overlaps)

    # TASK 4.2
    # overlaps = find_section_partial_overlaps('data/day4')
    # print(overlaps)

    # TASK 5.1
    # top_blocks = find_top_blocks_old('data/day5')
    # print(top_blocks)

    # TASK 5.2
    # top_blocks = find_top_blocks_new('data/day5')
    # print(top_blocks)

    # TASK 6.1
    # start_marker = find_start_marker('data/day6')
    # print(start_marker)

    # TASK 6.2
    # start_marker = find_start_message('data/day6')
    # print(start_marker)

    # TASK 7.1
    # sum_smallest = find_directory_sizes('data/day7')
    # print(sum_smallest) #1243729

    # TASK 7.2
    # size_smallest = find_which_to_remove('data/day7')
    # print(size_smallest)

    # TASK 8.1
    # visible_trees = find_visible_trees('data/day8')
    # print(visible_trees)

    # TASK 8.2
    # max_score = find_visibility_score('data/day8')
    # print(max_score)

    # TASK 9.1
    # unique_positions_num = find_tail_positions_one_knot('data/day9')
    # print(unique_positions_num)

    # TASK 9.2
    # unique_positions_num = find_tail_positions_ten_knots('data/day9')
    # print(unique_positions_num)

    # TASK 10.1
    # signal_sum = compute_signal_strengths('data/day10')
    # print(signal_sum)

    # TASK 10.2
    # draw_image('data/day10')

    # TASK 11.1
    # monkey_business = find_monkey_business()
    # print(monkey_business)

    # TASK 11.2
    # monkey_business = find_monkey_business_extra()
    # print(monkey_business)

    # TASK 12.1
    res = find_quickest_route('data/day12')
    print(min(res))