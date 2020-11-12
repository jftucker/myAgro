import unittest


class TestGetDaysOfPower(unittest.TestCase):

    def test_example(self):
        self.assertEqual(get_days_of_power(1000, 3, 500, 10, 1500, 7, 21000), 10)

    def test_all_0_returns_0(self):
        self.assertEqual(get_days_of_power(0, 0, 0, 0, 0, 0, 0), 0)

    def test_1000_per_day_runs_out_in_10_days_with_k_of_10000(self):
        self.assertEqual(get_days_of_power(1000, 0, 0, 0, 0, 0, 10000), 10)
        self.assertEqual(get_days_of_power(0, 0, 0, 0, 1000, 0, 10000), 10)
        self.assertEqual(get_days_of_power(0, 0, 1000, 0, 0, 0, 10000), 10)

    def test_case1_answer_is_141_days(self):
        self.assertEqual(get_days_of_power(3000, 3, 500, 10, 1500, 7, 700000), 141)

    def test_case2_answer_is_17_days(self):
        self.assertEqual(get_days_of_power(500, 3, 500, 10, 500, 7, 21000), 17)

    def test_case3_answer_is_5_days(self):
        self.assertEqual(get_days_of_power(1300, 0, 500, 0, 1500, 7, 10000), 5)

    def test_case4_answer_is_1_day(self):
        self.assertEqual(get_days_of_power(10000, 3, 500, 10, 1500, 7, 11000), 1)


def get_days_of_power(r1, d1, r2, d2, r3, d3, remaining_balance):
    today = 0
    rates = [r1, r2, r3]
    start_days = [d1, d2, d3]
    balance_sheet = []

    while remaining_balance > 0:
        todays_rate = 0
        for rate, start_day in zip(rates, start_days):
            if today >= start_day:
                todays_rate += rate

        if todays_rate > remaining_balance:
            break

        if todays_rate > 0:
            balance_sheet.append([todays_rate, remaining_balance])

        remaining_balance -= todays_rate
        today += 1

    return len(balance_sheet)


if __name__ == '__main__':
    unittest.main()
