'''
Author: star428
Date: 2020-08-15 16:04:04
LastEditTime: 2020-08-15 16:45:36
LastEditors: Please set LastEditors
Description: 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
FilePath: \python_learn_X2\Recursion\frag.py
'''

save_steps = [-1] * 201  # 记录计算过的台阶，并不是动态规划而是值表


def climb_steps(steps):
    if steps <= 2:  # 寻找递归终结条件
        return steps
    if save_steps[steps] != -1:
        return save_steps[steps]

    else:  # 递归函数等价关系式
        save_steps[steps] = climb_steps(steps - 1) + climb_steps(steps - 2)
        return save_steps[steps]


# test
for steps in range(10):
    print(climb_steps(steps))
print(climb_steps(200))
