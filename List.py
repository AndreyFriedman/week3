
class List(list):

    def __getitem__(self, args):
        if type(args) is int:
            return super().__getitem__(args)

        if len(args) > 0:
            bap = super().__getitem__(args[0])

            for i in range(1, len(args)):
                bap = bap[args[i]]
            return bap

    def __setitem__(self, args, value):
        if type(args) is int:
            super().__setitem__(args, value)
        elif len(args) >= 1:
            bap = super().__getitem__(args[0])

            for i in range(1, len(args) - 1):
                bap = bap[args[i]]
            bap[args[-1]] = value
