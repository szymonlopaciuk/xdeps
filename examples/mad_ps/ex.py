import xdeps
from cpymad.madx import Madx

mad = Madx()
mad.call("job.madx")

m = xdeps.madxutils.MadxEnv(mad)

m._vref.brho._info()
