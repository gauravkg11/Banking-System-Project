class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance for this transaction"):
        self.message = message
        super().__init__(self.message)
