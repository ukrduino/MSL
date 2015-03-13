# возвращает количество комбинаций (например количество комбинаций 6 шаров из 42 шаров)
def ball_combinations(balls=6, from_all_balls=42):

    if balls > 0 or from_all_balls > 0:
        mult_balls = 1
        mult_from_all_balls = 1
        from_all_balls_ = from_all_balls
        for b in range(1, balls+1):
            mult_balls *= b

        for ab in range(0, balls):
            mult_from_all_balls *= from_all_balls_
            from_all_balls_ -= 1

        return int(mult_from_all_balls/mult_balls)
comb = ball_combinations(6, 42)
win_5 = ball_combinations(5, 6) * ball_combinations(1, 36)
win_4 = ball_combinations(4, 6) * ball_combinations(2, 36)
win_3 = ball_combinations(3, 6) * ball_combinations(3, 36)
win_2 = ball_combinations(2, 6) * ball_combinations(4, 36)
win_1 = ball_combinations(1, 6) * ball_combinations(5, 36)
win_0 = ball_combinations(0, 6) * ball_combinations(6, 36)
odd_even = ball_combinations(6, 21)
odd5_even1 = ball_combinations(5, 21) * ball_combinations(1, 21)
odd4_even2 = ball_combinations(4, 21) * ball_combinations(2, 21)
odd3_even3 = ball_combinations(3, 21) * ball_combinations(3, 21)
# http://loto-time.ru/математика-спортлото-часть-2/
# http://loto-time.ru/математика-спортлото-часть-5-чет-нечет/

# print("В лотере 6 из 42:")
# print("Количество комбинаций по 6 шаров из 42 шаров %s" % comb)
# print("Количество выиграшных комбинаций из 6 шаров - 1")
# print("Количество выиграшных комбинаций из 5 шаров - %s" % win_5)
# print("Количество выиграшных комбинаций из 4 шаров - %s" % win_4)
# print("Количество выиграшных комбинаций из 3 шаров - %s" % win_3)
# print("Количество выиграшных комбинаций из 2 шаров - %s" % win_2)
# print("Количество выиграшных комбинаций из 1 шаров - %s" % win_1)
# print("Количество выиграшных комбинаций из 0 шаров - %s" % win_0)
# print("Количество выиграшных комбинаций из всех четных/нечетных шаров - %s (%s)" % (odd_even, int(odd_even/comb*100)))
# print("Количество выиграшных комбинаций из 5 четных / 1 нечетных шаров - %s (%s)" % (odd5_even1, int(odd5_even1/comb*100)))
# print("Количество выиграшных комбинаций из 4 четных / 2 нечетных шаров - %s (%s)" % (odd4_even2, int(odd4_even2/comb*100)))
# print("Количество выиграшных комбинаций из 3 четных / 3 нечетных шаров - %s (%s)" % (odd3_even3, int(odd3_even3/comb*100)))
#
# print("Проверка %s = %s" % (comb, 1 + win_5 + win_4 + win_3 + win_2 + win_1 + win_0))
# print("Проверка 2 %s = %s" % (comb, odd3_even3 + (odd_even + odd5_even1 + odd4_even2) * 2))



#TODO - четные и нечетные (30%)
#TODO - большие и малые группы чисел (1:21 22:42)(2:4, 4:2)
#TODO - повторяющиеся числа (47%)
#TODO - последовательные числа (нет в 89%)
#TODO - одинаковый интервал (не более 3)
#TODO - комбинации 2х, 3х, 4х