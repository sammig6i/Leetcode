class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))

        for i in range(len(num_list) - 1):
            if num_list[i] < num_list[i + 1]:
                break
        else:
            return num

        max_idx, max_val = i + 1, num_list[i + 1]
        for j in range(i + 1, len(num_list)):
            if max_val <= num_list[j]:
                max_idx, max_val = j, num_list[j]

        left_idx = i
        for j in range(i, -1, -1):
            if num_list[j] < max_val:
                left_idx = j

        num_list[max_idx], num_list[left_idx] = num_list[left_idx], num_list[max_idx]
        return int(''.join(num_list))
        
        # 2736 -> 7236
        # 98368 -> 98863
        # 120 -> 210

        # 9973
        # max_num = 9
        # max index = 1