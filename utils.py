class utils:
    def reversed (x:int):
        if isinstance(x, int):
            return int(str(x)[::-1]) 
    def formatter (x:int):
        if isinstance(x, int):
            return bin(x), oct(x)
    
