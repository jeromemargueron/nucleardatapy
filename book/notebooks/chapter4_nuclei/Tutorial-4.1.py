# Import numpy
import numpy as np
# Import nucleardatapy package
import nucleardatapy as nuda

# -------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[1], line 5
#       2 import numpy as np
#       4 # Import nucleardatapy package
# ----> 5 import nucleardatapy as nuda

# File ~/git/github/nucleardatapy/version-0.2/nucleardatapy/__init__.py:23
#      21 from nucleardatapy.hnuc    import *
#      22 #
# ---> 23 from nucleardatapy.fig     import *

# File ~/git/github/nucleardatapy/version-0.2/nucleardatapy/fig/__init__.py:4
#       1 """
#       2 This module provides microscopic, phenomenological and experimental data constraints.
#       3 """
# ----> 4 from nucleardatapy.fig.matter_setupFFGNuc_fig        import *
#       5 from nucleardatapy.fig.matter_setupMicro_fig         import *
#       6 from nucleardatapy.fig.matter_setupMicro_err_NM_fig  import *

# File ~/git/github/nucleardatapy/version-0.2/nucleardatapy/fig/matter_setupFFGNuc_fig.py:3
#       2 import numpy as np
# ----> 3 import matplotlib.pyplot as plt
#       5 import nucleardatapy as nuda
#       7 def matter_setupFFGNuc_EP_fig( pname, mss = [ 1.0 ], den = np.linspace(0.01,0.35,10), kfn = np.linspace(0.5,2.0,10) ):

# File ~/.local/lib/python3.10/site-packages/matplotlib/__init__.py:1273
#    1269     rcParams['backend_fallback'] = False
#    1272 if os.environ.get('MPLBACKEND'):
# -> 1273     rcParams['backend'] = os.environ.get('MPLBACKEND')
#    1276 def get_backend():
#    1277     """
#    1278     Return the name of the current backend.
#    1279 
#    (...)
#    1282     matplotlib.use
#    1283     """

# File ~/.local/lib/python3.10/site-packages/matplotlib/__init__.py:739, in RcParams.__setitem__(self, key, val)
#     737             return
#     738 try:
# --> 739     cval = self.validate[key](val)
#     740 except ValueError as ve:
#     741     raise ValueError(f"Key {key}: {ve}") from None

# File ~/.local/lib/python3.10/site-packages/matplotlib/rcsetup.py:273, in validate_backend(s)
#     272 def validate_backend(s):
# --> 273     if s is _auto_backend_sentinel or backend_registry.is_valid_backend(s):
#     274         return s
#     275     else:

# File ~/.local/lib/python3.10/site-packages/matplotlib/backends/registry.py:250, in BackendRegistry.is_valid_backend(self, backend)
#     247     return True
#     249 # Only load entry points if really need to and not already done so.
# --> 250 self._ensure_entry_points_loaded()
#     251 if backend in self._backend_to_gui_framework:
#     252     return True

# File ~/.local/lib/python3.10/site-packages/matplotlib/backends/registry.py:116, in BackendRegistry._ensure_entry_points_loaded(self)
#     113 def _ensure_entry_points_loaded(self):
#     114     # Load entry points, if they have not already been loaded.
#     115     if not self._loaded_entry_points:
# --> 116         entries = self._read_entry_points()
#     117         self._validate_and_store_entry_points(entries)
#     118         self._loaded_entry_points = True

# File ~/.local/lib/python3.10/site-packages/matplotlib/backends/registry.py:140, in BackendRegistry._read_entry_points(self)
#     138 group = "matplotlib.backend"
#     139 if sys.version_info >= (3, 10):
# --> 140     entry_points = im.entry_points(group=group)
#     141 else:
#     142     entry_points = im.entry_points().get(group, ())

# File /usr/lib/python3.10/importlib/metadata/__init__.py:1021, in entry_points(**params)
#    1017 unique = functools.partial(unique_everseen, key=norm_name)
#    1018 eps = itertools.chain.from_iterable(
#    1019     dist.entry_points for dist in unique(distributions())
#    1020 )
# -> 1021 return SelectableGroups.load(eps).select(**params)

# File /usr/lib/python3.10/importlib/metadata/__init__.py:459, in SelectableGroups.load(cls, eps)
#     456 @classmethod
#     457 def load(cls, eps):
#     458     by_group = operator.attrgetter('group')
# --> 459     ordered = sorted(eps, key=by_group)
#     460     grouped = itertools.groupby(ordered, by_group)
#     461     return cls((group, EntryPoints(eps)) for group, eps in grouped)

# File /usr/lib/python3.10/importlib/metadata/__init__.py:1018, in <genexpr>(.0)
#    1016 norm_name = operator.attrgetter('_normalized_name')
#    1017 unique = functools.partial(unique_everseen, key=norm_name)
# -> 1018 eps = itertools.chain.from_iterable(
#    1019     dist.entry_points for dist in unique(distributions())
#    1020 )
#    1021 return SelectableGroups.load(eps).select(**params)

# File /usr/lib/python3.10/importlib/metadata/_itertools.py:15, in unique_everseen(iterable, key)
#      13         yield element
#      14 else:
# ---> 15     for element in iterable:
#      16         k = key(element)
#      17         if k not in seen:

# File /usr/lib/python3.10/importlib/metadata/__init__.py:904, in <genexpr>(.0)
#     901 """Find metadata directories in paths heuristically."""
#     902 prepared = Prepared(name)
#     903 return itertools.chain.from_iterable(
# --> 904     path.search(prepared) for path in map(FastPath, paths)
#     905 )

# File /usr/lib/python3.10/importlib/metadata/__init__.py:802, in FastPath.search(self, name)
#     801 def search(self, name):
# --> 802     return self.lookup(self.mtime).search(name)

# File /usr/lib/python3.10/importlib/metadata/__init__.py:807, in FastPath.mtime(self)
#     804 @property
#     805 def mtime(self):
#     806     with suppress(OSError):
# --> 807         return os.stat(self.root).st_mtime
#     808     self.lookup.cache_clear()

# TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType
