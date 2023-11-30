# copyright ############################### #
# This file is part of the Xdeps Package.   #
# Copyright (c) CERN, 2023.                 #
# ######################################### #

class Print:
    suppress = False

    def __call__(self, *args, **kwargs):
        if not self.suppress:
            print(*args, **kwargs)


_print = Print()
