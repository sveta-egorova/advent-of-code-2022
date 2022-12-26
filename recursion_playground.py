class Solution1:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(left_index, right_index):
            if left_index < right_index:
                s[left_index], s[right_index] = s[right_index], s[left_index]
                helper(left_index + 1, right_index - 1)

        helper(0, len(s) - 1)


class Solution2:
    def climb_stairs(self, n):
        def climb_stairs_rec(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            variants_after_one_step = climb_stairs_rec(i + 1, n)
            variants_after_two_steps = climb_stairs_rec(i + 2, n)
            return variants_after_one_step + variants_after_two_steps

        return climb_stairs_rec(0, n)


if __name__ == '__main__':
    # solution = Solution1()
    # input_data = [x for x in 'abcdefghijkl']
    # solution.reverseString(input_data)
    # print(input_data)

    solution = Solution2()
    num_ways = solution.climb_stairs(5)
    print(num_ways)