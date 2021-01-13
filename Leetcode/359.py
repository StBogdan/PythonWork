class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.store and timestamp - self.store[message] < 10:
            return False
        else:
            self.store[message] = timestamp
            return True


        
if __name__ == "__main__":
    # Your Logger object will be instantiated and called as such:
    obj = Logger()
    msgs = [ [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
    for timestamp, message in msgs:
        print(obj.shouldPrintMessage(timestamp,message))