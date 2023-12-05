class InputError(Exception):
    pass

class InputLib:
    @staticmethod
    def fopen(infile):
        if infile == "-":
            return sys.stdin
        else:
            try:
                return open(infile, 'r')
            except IOError as e:
                raise InputError(str(e))

    @staticmethod
    def fclose(inbuf):
        try:
            inbuf.close()
        except IOError as e:
            raise InputError(str(e))

    @staticmethod
    def get_line(inbuf):
        try:
            return inbuf.readline().rstrip('\n')
        except IOError as e:
            raise InputError(str(e))
