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

    print('Total number of b: ', len(b_list))

    time_start = time.time()

    end_node = (end_row, end_col, 'E')
    grid_height = len(grid)
    grid_width = len((grid[0]))

    initial_neighbor_input = set()
    neighbors_df = [[initial_neighbor_input for i in range(grid_width)] for i in range(grid_height)]

    for row_ix in range(grid_height):
        for el_ix in range(grid_width):
            cur_node = (row_ix, el_ix, grid[row_ix][el_ix])
            neighbors_df[row_ix][el_ix] = find_valid_neighbours(cur_node, grid)


    movement = ''
    step_history = []
    default_input = (9999, step_history)

    steps_and_history_to_reach_ix_general = [[default_input for i in range(grid_width)] for i in range(grid_height)]

    solutions = []
    b_counter = 0

    time_start = time.time()

    for start_node in b_list:
        b_counter += 1

        start_history = step_history.copy()
        start_history.append(start_node)

        steps_and_history_to_reach_ix = steps_and_history_to_reach_ix_general.copy()
        steps_and_history_to_reach_ix[start_row][start_col] = (0, start_history)

        cur_level = 0
        found_solution = False
        neighbors = [start_node]

        while neighbors and not found_solution:
            next_level_neighbors = []
            cur_level += 1

            for old_el in neighbors:
                optimal_history_to_this_point = steps_and_history_to_reach_ix[old_el[0]][old_el[1]][1]
                valid_neighbors = [el for el in neighbors_df[old_el[0]][old_el[1]] if el not in optimal_history_to_this_point]
                for proposed_neighbour in valid_neighbors:
                    previous_optimal_level = steps_and_history_to_reach_ix[proposed_neighbour[0]][proposed_neighbour[1]][0]
                    if previous_optimal_level > cur_level:
                        proposed_history = optimal_history_to_this_point.copy()
                        proposed_history.append(proposed_neighbour)
                        steps_and_history_to_reach_ix[proposed_neighbour[0]][proposed_neighbour[1]] = (cur_level, proposed_history)
                    if proposed_neighbour == end_node:
                        found_solution = True
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



import json


def get_list(char):
    return json.loads(char)


def compare_elements(list1, list2):

    if isinstance(list1, int) and isinstance(list2, list):
        list1 = [list1]
    elif isinstance(list1, list) and isinstance(list2, int):
        list2 = [list2]
    elif isinstance(list1, int) and isinstance(list2, int):
        if list1 > list2:
            return 'Incorrect'
        elif list1 < list2:
            return 'Correct'
        elif list1 == list2:
            return 'Equal'

    if len(list1) == 0 and len(list2) == 0:
        return 'Equal'
    if len(list1) == 0:
        return 'Correct'
    if len(list2) == 0:
        return 'Incorrect'

    left_head = list1[0]
    right_head = list2[0]

    compare_result = compare_elements(left_head, right_head)
    if compare_result in ['Incorrect', 'Correct']:
        return compare_result
    else:
        return compare_elements(list1[1:], list2[1:])


def compare_pairs_of_arrays(filename):

    results = {}
    cur_pair = 1

    with open(filename) as file:
        first_array = []
        second_array = []
        first_given = False
        second_given = False
        for line in file:
            if line == '\n':
                first_given = False
                second_given = False
                continue
            if not first_given:
                first_array = get_list(line.strip())
                first_given = True
                continue
            if not second_given:
                second_array = get_list(line.strip())
                second_given = True
            if first_given and second_given:
                # print(first_array)
                # print(second_array)
                results[cur_pair] = compare_elements(first_array, second_array)
                cur_pair += 1
                continue

    # print(results)
    indices_true = [ix for ix, value in results.items() if value == 'Correct']
    return sum(indices_true)


def sort_packages(filename):

    all_packages = []

    with open(filename) as file:
        for line in file:
            if line == '\n':
                continue
            else:
                array = get_list(line.strip())
                all_packages.append(array)

    divider_package_1 = [[2]]
    divider_package_2 = [[6]]
    all_packages.append(divider_package_1)
    all_packages.append(divider_package_2)
    new_index_1 = None
    new_index_2 = None

    for i in range(1, len(all_packages)):
        cur_package = all_packages[i]
        j = i-1
        while j >= 0 and compare_elements(cur_package, all_packages[j]) == 'Correct':
            all_packages[j+1] = all_packages[j]
            j -= 1
        all_packages[j + 1] = cur_package
        if i == len(all_packages) - 2:
            new_index_1 = j + 1 + 1
        if i == len(all_packages) - 1:
            new_index_2 = j + 1 + 1

    return new_index_1 * new_index_2


from bisect import bisect


def find_sand_units_before_void(filename):

    all_rock_coordinates = set()
    with open(filename) as file:
        for line in file:
            corner_elements = line.strip().split(' -> ')
            cur_x = int(corner_elements[0].split(',')[0])
            cur_y = int(corner_elements[0].split(',')[1])
            all_rock_coordinates.add((cur_x, cur_y))
            for next_element in corner_elements[1:]:
                next_x = int(next_element.split(',')[0])
                next_y = int(next_element.split(',')[1])
                all_rock_coordinates.add((next_x, next_y))
                if next_x == cur_x:
                    y_range = range(min(cur_y, next_y), max(cur_y, next_y))
                    for one_y in y_range:
                        all_rock_coordinates.add((cur_x, one_y))
                if next_y == cur_y:
                    x_range = range(min(cur_x, next_x), max(cur_x, next_x))
                    for one_x in x_range:
                        all_rock_coordinates.add((one_x, cur_y))
                cur_x = next_x
                cur_y = next_y

    all_blocks = {}
    for x,y in all_rock_coordinates:
        if x not in all_blocks:
            all_blocks[x] = [y]
        else:
            all_blocks[x].insert(bisect(all_blocks[x], y), y)

    cur_sand = 0
    fell_into_the_void = False

    while True:
        # print(cur_sand)
        if fell_into_the_void:
            return cur_sand - 1
        cur_sand += 1
        start_x = 500
        start_y = 0
        x_cur, y_cur = start_x, min(all_blocks[start_x]) - 1
        left_available = True
        right_available = True
        while (left_available or right_available) and not fell_into_the_void:
            # GO DOWN LEFT
            x_down_left, y_down_left = x_cur - 1, y_cur + 1
            if x_down_left in all_blocks:
                # means it is not complete void
                if y_down_left not in all_blocks[x_down_left]:
                    # means that the down left is available
                    # see where it moves

                    position_to_insert = bisect(all_blocks[x_down_left], y_down_left)
                    if position_to_insert == len(all_blocks[x_down_left]):
                        fell_into_the_void = True
                    else:
                        y_closest_down = all_blocks[x_down_left][position_to_insert] - 1
                        x_cur, y_cur = x_down_left, y_closest_down
                    continue
                else:
                    left_available = False
            else:
                # this falls into the void
                fell_into_the_void = True

            # GO DOWN RIGHT
            x_down_right, y_down_right = x_cur + 1, y_cur + 1
            if x_down_right in all_blocks:
                # means it is not complete void
                if y_down_right not in all_blocks[x_down_right]:
                    # means that the down right is available
                    # see where it moves
                    position_to_insert = bisect(all_blocks[x_down_right], y_down_right)
                    if position_to_insert == len(all_blocks[x_down_right]):
                        fell_into_the_void = True
                    else:
                        y_closest_down = all_blocks[x_down_right][position_to_insert] - 1
                        x_cur, y_cur = x_down_right, y_closest_down
                    continue
                else:
                    right_available = False
            else:
                # this falls into the void
                fell_into_the_void = True

        all_blocks[x_cur].insert(bisect(all_blocks[x_cur], y_cur), y_cur)


def find_sand_units_before_it_stops_falling(filename):

    all_rock_coordinates = set()
    with open(filename) as file:
        for line in file:
            corner_elements = line.strip().split(' -> ')
            cur_x = int(corner_elements[0].split(',')[0])
            cur_y = int(corner_elements[0].split(',')[1])
            all_rock_coordinates.add((cur_x, cur_y))
            for next_element in corner_elements[1:]:
                next_x = int(next_element.split(',')[0])
                next_y = int(next_element.split(',')[1])
                all_rock_coordinates.add((next_x, next_y))
                if next_x == cur_x:
                    y_range = range(min(cur_y, next_y), max(cur_y, next_y))
                    for one_y in y_range:
                        all_rock_coordinates.add((cur_x, one_y))
                if next_y == cur_y:
                    x_range = range(min(cur_x, next_x), max(cur_x, next_x))
                    for one_x in x_range:
                        all_rock_coordinates.add((one_x, cur_y))
                cur_x = next_x
                cur_y = next_y

    all_blocks = {}
    for x,y in all_rock_coordinates:
        if x not in all_blocks:
            all_blocks[x] = [y]
        else:
            all_blocks[x].insert(bisect(all_blocks[x], y), y)

    # add floor

    lowest_formation = 0
    for x,y in all_rock_coordinates:
        if y > lowest_formation:
            lowest_formation = y

    floor_level_y = lowest_formation + 2
    floor_level_x_min = 500 - floor_level_y - 1
    floor_level_x_max = 500 + floor_level_y + 1

    for x in range(floor_level_x_min, floor_level_x_max):
        if x not in all_blocks:
            all_blocks[x] = [floor_level_y]
        else:
            all_blocks[x].insert(bisect(all_blocks[x], floor_level_y), floor_level_y)

    cur_sand = 0
    source_blocked = False

    while True:
        if source_blocked:
            return cur_sand
        cur_sand += 1
        start_x = 500
        start_y = 0
        x_cur, y_cur = start_x, min(all_blocks[start_x]) - 1
        left_available = True
        right_available = True
        while (left_available or right_available) and not source_blocked:
            # GO DOWN LEFT
            x_down_left, y_down_left = x_cur - 1, y_cur + 1
            if x_down_left in all_blocks:
                # in theory, should always be True
                if y_down_left not in all_blocks[x_down_left]:
                    # means that the down left is available
                    # see where it moves

                    position_to_insert = bisect(all_blocks[x_down_left], y_down_left)
                    y_closest_down = all_blocks[x_down_left][position_to_insert] - 1
                    x_cur, y_cur = x_down_left, y_closest_down
                    continue
                else:
                    left_available = False
            else:
                print('This is not expected')

            # GO DOWN RIGHT
            x_down_right, y_down_right = x_cur + 1, y_cur + 1
            if x_down_right in all_blocks:
                # means it is not complete void
                if y_down_right not in all_blocks[x_down_right]:
                    # means that the down right is available
                    # see where it moves
                    position_to_insert = bisect(all_blocks[x_down_right], y_down_right)
                    y_closest_down = all_blocks[x_down_right][position_to_insert] - 1
                    x_cur, y_cur = x_down_right, y_closest_down
                    continue
                else:
                    right_available = False
            else:
                print('This is not expected')

        all_blocks[x_cur].insert(bisect(all_blocks[x_cur], y_cur), y_cur)

        if x_cur == 500 and y_cur == 0:
            source_blocked = True


import re


def find_list_intersection(lists_with_borders):

    global_min = 99999999
    global_max = -99999999
    intersection_gaps = []
    # num_gaps = 0
    previous_list = None
    for one_list in sorted(lists_with_borders):
        if previous_list:
            previous_max = max(previous_list[1], global_max)
            if one_list[0] > previous_max:
                # num_gaps += 1
                gap_start = previous_max
                gap_end = one_list[0]
                intersection_gaps.append((gap_start, gap_end))
        if one_list[0] < global_min:
            global_min = one_list[0]
        if one_list[1] > global_max:
            global_max = one_list[1]

        previous_list = one_list
    return intersection_gaps, global_min, global_max


def get_sensors_and_beacons(filename):

    all_beacons = set()
    all_sensors = []
    pattern = '-?[0-9]+'
    current_sensor = 0
    with open(filename) as file:
        for line in file:
            current_sensor += 1
            coordinates = re.findall(pattern, line)
            x_sensor = int(coordinates[0])
            y_sensor = int(coordinates[1])
            x_beacon = int(coordinates[2])
            y_beacon = int(coordinates[3])
            distance_covered = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
            all_sensors.append((x_sensor, y_sensor, distance_covered))
            all_beacons.add((x_beacon, y_beacon))

    return all_sensors, all_beacons


def find_area_without_beacons(filename, requested_y):

    y_coverage_borders = []
    all_sensors, all_beacons = get_sensors_and_beacons(filename)

    for x_sensor, y_sensor, distance_covered in all_sensors:
        distance_to_y_sensor = abs(requested_y - y_sensor)
        if distance_to_y_sensor < distance_covered:
            coverage_width_one_side = distance_covered - distance_to_y_sensor
            coverage_start_local = x_sensor - coverage_width_one_side
            coverage_end_local = x_sensor + coverage_width_one_side
            y_coverage_borders.append([coverage_start_local, coverage_end_local])

    _, coverage_start_global, coverage_end_global = find_list_intersection(y_coverage_borders)
    coverage_length = coverage_end_global - coverage_start_global + 1
    for x_beacon, y_beacon in all_beacons:
        if y_beacon == requested_y:
            coverage_length -= 1

    return coverage_length


def find_distress_beacon(filename, grid_size=20):

    all_sensors, all_beacons = get_sensors_and_beacons(filename)
    for y_candidate in range(0, grid_size + 1):
        if y_candidate % 100000 == 0:
            print('analyzing y candidate: ', y_candidate)
        y_coverage_borders = []
        for x_sensor, y_sensor, distance_covered in all_sensors:
            distance_to_y_sensor = abs(y_candidate - y_sensor)
            if distance_to_y_sensor < distance_covered:
                coverage_width_one_side = distance_covered - distance_to_y_sensor
                coverage_start_local = x_sensor - coverage_width_one_side
                coverage_end_local = x_sensor + coverage_width_one_side
                y_coverage_borders.append([coverage_start_local, coverage_end_local])

        intersection_gaps, _, _ = find_list_intersection(y_coverage_borders)
        # print(intersection_gaps)
        if len(intersection_gaps) > 0:
            gap_y = y_candidate
            gap_x = intersection_gaps[0][0] + 1
            # print(y_candidate)
            # print(intersection_gaps[0][0] + 1)
            tuning_freq = gap_x * 4000000 + gap_y
            return tuning_freq


def draw_sensor_diagram(filename):

    area_covered = {}
    all_sensors = {}
    pattern = '-?[0-9]+'
    current_sensor = 0
    with open(filename) as file:
        for line in file:
            current_sensor += 1
            coordinates = re.findall(pattern, line)
            x_sensor = int(coordinates[0])
            y_sensor = int(coordinates[1])
            x_beacon = int(coordinates[2])
            y_beacon = int(coordinates[3])
            if y_sensor not in all_sensors:
                all_sensors[y_sensor] = [x_sensor]
            else:
                all_sensors[y_sensor].append(x_sensor)
            distance_covered = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
            for y in range(y_sensor - distance_covered, y_sensor + distance_covered + 1):

                cover_width_one_side = distance_covered - abs(y_sensor - y)
                coverage_per_line = [x for x in range(x_sensor - cover_width_one_side,
                                                      x_sensor + cover_width_one_side + 1)]

                if y not in area_covered:
                    area_covered[y] = set(coverage_per_line)
                else:
                    area_covered[y].update(set(coverage_per_line))

    coverage_diagram = ''

    for y in range(-12,30):
        for x in range(-10,35):
            if y not in area_covered:
                coverage_diagram += '.'
            elif y in area_covered and y not in all_sensors:
                if x in area_covered[y]:
                    coverage_diagram += '#'
                else:
                    coverage_diagram += '.'
            elif y in area_covered and y in all_sensors:
                if x in all_sensors[y]:
                    coverage_diagram += 'S'
                elif x in area_covered[y]:
                    coverage_diagram += '#'
                else:
                    coverage_diagram += '.'

            if x == 34:
                coverage_diagram += '\n'

    print(coverage_diagram)



def get_valve_structure(filename):
    pattern = r'Valve ([A-Z]+) has flow rate=([0-9]+); tunnel[s]? lead[s]? to valve[s]? ([A-Z, ]*)'

    valve_directions = {}
    valve_flow_rates = {}

    with open(filename) as file:
        for line in file:
            regex_match = re.findall(pattern, line.strip())[0]
            # print(regex_match)

            valve = regex_match[0]
            flow_rate = regex_match[1]
            leads_to = regex_match[2].split(', ')
            valve_directions[valve] = leads_to
            valve_flow_rates[valve] = int(flow_rate)

    return valve_directions, valve_flow_rates


def traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                         valve_flow_rates, points_reached, max_points_reached, location):
    # while minutes_remaining > 0:
    if minutes_remaining == 0:
        # print(cur_path)
        if points_reached > max_points_reached:
            max_points_reached = points_reached
            print(cur_path)
            print(max_points_reached)

    elif minutes_remaining > 0:
        for next_node in valve_directions[location]:
            cur_path.append(next_node)
            minutes_remaining -= 1
            cur_path.append(minutes_remaining)

            if minutes_remaining >= 1:
                for action in ['open', 'ignore']:

                    if not valve_states[next_node] and valve_flow_rates[next_node] > 0:
                        if action == 'open':
                            cur_path.append('open')
                            valve_states[next_node] = True
                            points_gained = minutes_remaining * valve_flow_rates[next_node]
                            points_reached += points_gained
                            minutes_remaining -= 1
                            cur_path.append(minutes_remaining)
                            traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                                                 valve_flow_rates, points_reached, max_points_reached, next_node)
                        else:
                            traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                                                 valve_flow_rates, points_reached, max_points_reached, next_node)
                    else:
                        traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                                             valve_flow_rates, points_reached, max_points_reached, next_node)

            else:
                traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                                     valve_flow_rates, points_reached, max_points_reached, next_node)



def find_valve_opening_routes(filename):

    valve_directions, valve_flow_rates = get_valve_structure(filename)
    # cur_point = 'AA'
    minutes_remaining = 30
    max_points_reached = 0
    possible_steps = valve_directions['AA']
    valve_states = {}
    for valve in valve_flow_rates:
        valve_states[valve] = False

    print(valve_states)
    cur_path = ['AA']
    cur_path.append(minutes_remaining)
    points_reached = 0

    traverse_valve_graph(cur_path, minutes_remaining, valve_directions, valve_states,
                         valve_flow_rates, points_reached, max_points_reached, 'AA')

    # while minutes_remaining > 0:
    #     next_possible_steps = []
    #     for location in possible_steps:
    #         # step into that location
    #         cur_path.append(location)
    #         minutes_remaining -= 1
    #         cur_path.append(minutes_remaining)
    #
    #         # do something with the valve
    #         if minutes_remaining >= 1:
    #             for action in ['open', 'ignore']:
    #                 if not valve_states[location] and valve_flow_rates[location] > 0:
    #                     if action == 'open':
    #                         cur_path.append('open')
    #                         valve_states[location] = True
    #                         points_gained = minutes_remaining * valve_flow_rates[location]
    #                         points_reached += points_gained
    #                         minutes_remaining -= 1
    #                         cur_path.append(minutes_remaining)
    #                     else:
    #                         pass
    #                 else:
    #                     pass
    #
    #         for next_step in valve_directions[location]:
    #             next_possible_steps.append(next_step)
    #
    #         possible_steps = next_possible_steps
    #
    #         if minutes_remaining == 0:
    #             # print(cur_path)
    #             if points_reached > max_points_reached:
    #                 max_points_reached = points_reached

    print(max_points_reached)





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

    # TASK 12
    # res = find_quickest_route('data/day12')
    # print(min(res))

    # TASK 13.1
    # indices_true = compare_pairs_of_arrays('data/day13')
    # print(indices_true)

    # TASK 13.2
    # divider_indices = sort_packages('data/day13')
    # print(divider_indices)

    # TASK 14.1
    # sand_before_void = find_sand_units_before_void('data/day14')
    # print(sand_before_void)

    # TASK 14.2
    # sand_before_blockage = find_sand_units_before_it_stops_falling('data/day14')
    # print(sand_before_blockage)

    # TASK 15.1
    # start_time = time.time()
    # num_elements = find_area_without_beacons('data/day15', 2000000)
    # print(num_elements)
    # print(f'it took: {time.time() - start_time}s')

    # TASK 15.2
    # draw_sensor_diagram('data/day15_short')
    # tuning_freq = find_distress_beacon('data/day15', 4000000)
    # print(tuning_freq)

    # TASK 16.1
    find_valve_opening_routes('data/day16_short')