class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.n = len(balance)

    def _verify_num(self, num):
        return 0 < num <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._verify_num(account1) and self._verify_num(account2) and self.withdraw(account1, money):
            self.deposit(account2, money)
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self._verify_num(account): return False
        self.balances[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._verify_num(account) or self.balances[account - 1] < money: return False
        self.balances[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)