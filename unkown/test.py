class ab:
    def test(self):
        print "ab.test"

class bc(ab):
    def test(self):
        print "bc.test"

v = ab()
v.test()