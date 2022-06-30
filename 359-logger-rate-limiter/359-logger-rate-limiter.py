class Logger:

    def __init__(self):
        self.msg_hs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.msg_hs:
            self.msg_hs[message] = timestamp
            return True
        if timestamp - self.msg_hs[message] >= 10:
            self.msg_hs[message] = timestamp
            return True
        else:
            return False
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)