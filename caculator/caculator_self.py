#coding=utf-8
class Buffer(object):
    def __init__(self,data):
        self.data = data
        self.offset = 0

    def peek(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]

    def advance(self):
        self.offset += 1

class Token(object):
    def consume(self,buffer):
        pass

class IntToken(Token):
    def consume(self,buffer):
        accume = ''
        while True:
            ch = buffer.peek()
            if ch is None or ch not in "0123456789":
                break
            else:
                accume += ch
                buffer.advance()
        if accume != "":
            return ("int",int(accume))
        else:
            return None

class OperatorToken(Token):
    def consume(self,buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-":
            buffer.advance()
            return ("ope",ch)
        return None

def Tokenize(string):
    buffer = Buffer(string)
    tk_int = IntToken()
    tk_ope = OperatorToken()
    tokens = []

    while buffer.peek():
        token = None
        for tk in (tk_int,tk_ope):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        if not token:
            raise ValueError("value error!")

    return tokens




if __name__ == "__main__":
    a = Tokenize("66+78")
    print(a)