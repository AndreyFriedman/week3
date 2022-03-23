class FR:
    def __init__(self, f):
        self.func = f
        self.name = f.__name__
        self.doc = f.__doc__

        if self.doc is None:
            self.doc = ""
        else:
            self.doc = self.doc.replace("\n", "<br>")

        self.annotations = f.__annotations__

        if "return" in self.annotations:
            del self.annotations["return"]

        self.annotations = str([i + "<br>"
                                for i in self.annotations]).replace("'", "").replace(",", "")[1:-1]

    def create(self):
        blockOfData = \
            f'''    
                <p>
                    <h1> Function {self.name}: </h1>
                    {self.doc} <br>
                    {self.annotations}  
                </p>
            '''
        return blockOfData
