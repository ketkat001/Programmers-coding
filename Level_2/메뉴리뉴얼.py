from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        menu_dict = {}
        for order in orders:
            for comb in combinations(order, c):
                comb = ''.join(sorted(list(comb)))
                if comb in menu_dict:
                    menu_dict[comb] += 1
                else:
                    menu_dict[comb] = 1
        max_value = 0
        menus = []
        for menu, value in menu_dict.items():
            if value > max_value and value > 1:
                max_value = value
                menus = [menu]
            elif value == max_value:
                menus.append(menu)
        answer.extend(menus)
    answer.sort()
    return answer


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))