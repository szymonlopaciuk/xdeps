# copyright ############################### #
# This file is part of the Xdeps Package.   #
# Copyright (c) CERN, 2023.                 #
# ######################################### #

import numpy as np

from xdeps import Table

data = {
    "name": np.array(["ip1", "ip2", "ip3"]),
    "s": np.array([1.0, 2.0, 3.0]),
    "betx": np.array([4.0, 5.0, 6.0]),
    "bety": np.array([2.0, 3.0, 4.0]),
}


t = Table(data)

def test_column_selection():
    assert len(t.betx)==len(data['betx'])
    assert t["betx", 0] == data['betx'][0]
    assert t["sqrt(betx)"][1]==np.sqrt(data['betx'][1])
    assert t["betx bety"].betx[0] == t.betx[0]
    assert t[["betx", "bety"]].betx[0] == t.betx[0]
    assert t["sqrt(betx)>3 sqrt(bety)"]['sqrt(betx)>3'][0]==(np.sqrt(data['betx'][0])>3)
    assert isinstance(t.cols['betx'], Table)
    assert t.cols["betx", "bety"].betx[0] == t.betx[0]


def test_row_selection():
    assert t[:, 1].betx==data['betx'][1]
    assert t[:, [0, 2]].betx[1]==data['betx'][2]
    assert t[:, t.s > 1].betx[1]==data['betx'][t.s > 1][1]
    assert t.rows[t.s > 1, 1].betx[0]==data['betx'][t.s > 1][0]

def test_row_selection_names():
    assert t[:, "ip1"].betx[0]==data['betx'][0]
    assert t[:, "ip[23]"].betx[0]==data['betx'][1]
    assert t[:, "ip.*##1"].betx[0]==data['betx'][1]
    assert t[:, "notthere"]._nrows==0
    assert t[:, ["ip1", "ip2"]].betx[0]==data['betx'][0]

def test_row_selection_names_with_rows():
    assert t.rows["ip2"].betx[0]==data['betx'][1]
    assert t.rows["ip[23]"].betx[0]==data['betx'][1]
    assert t.rows["ip.*##1"].betx[0]==data['betx'][1]
    assert t.rows["notthere"]._nrows==0
    assert t.rows[["ip1", "ip2"]].betx[1]==data['betx'][1]

def test_row_selection_ranges():
    assert t[:, 1:4:3].betx[0] == data['betx'][1]
    assert t[:, 1.5:2.5:"s"].betx[0] == data['betx'][1]
    assert t[:, "ip1":"ip3"].betx[2] == data['betx'][2]
    assert t[:, "ip.*##1":"ip.*##2"].betx[0] == data['betx'][1]
    assert t[:, "ip2%%-1":"ip2%%+1"].betx[0] == data['betx'][0]
    assert t[:, "ip1":"ip3":"name"].betx[0]  == data['betx'][0]
    assert t[:, None].betx[0]  == data['betx'][0]
    assert t[:, :].betx[0]  == data['betx'][0]

def test_row_selection_ranges_with_rows():
    assert t.rows[1:4:3].betx[0] == data['betx'][1]
    assert t.rows[1.5:2.5:"s"].betx[0] == data['betx'][1]
    assert t.rows["ip1":"ip3"].betx[2] == data['betx'][2]
    assert t.rows["ip.*##1":"ip.*##2"].betx[0] == data['betx'][1]
    assert t.rows["ip2%%-1":"ip2%%+1"].betx[0] == data['betx'][0]
    assert t.rows["ip1":"ip3":"name"].betx[0]  == data['betx'][0]
    assert t.rows[None].betx[0]  == data['betx'][0]
    assert t.rows[:].betx[0]  == data['betx'][0]
