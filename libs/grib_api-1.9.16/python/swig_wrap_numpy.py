# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gribapi_swig', [dirname(__file__)])
        except ImportError:
            import _gribapi_swig
            return _gribapi_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_gribapi_swig', fp, pathname, description)
            finally:
                fp.close()
                return _mod
    _gribapi_swig = swig_import_helper()
    del swig_import_helper
else:
    import _gribapi_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def cdata(*args):
  return _gribapi_swig.cdata(*args)
cdata = _gribapi_swig.cdata

def memmove(*args):
  return _gribapi_swig.memmove(*args)
memmove = _gribapi_swig.memmove
GRIB_SUCCESS = _gribapi_swig.GRIB_SUCCESS
GRIB_END_OF_FILE = _gribapi_swig.GRIB_END_OF_FILE
GRIB_INTERNAL_ERROR = _gribapi_swig.GRIB_INTERNAL_ERROR
GRIB_BUFFER_TOO_SMALL = _gribapi_swig.GRIB_BUFFER_TOO_SMALL
GRIB_NOT_IMPLEMENTED = _gribapi_swig.GRIB_NOT_IMPLEMENTED
GRIB_7777_NOT_FOUND = _gribapi_swig.GRIB_7777_NOT_FOUND
GRIB_ARRAY_TOO_SMALL = _gribapi_swig.GRIB_ARRAY_TOO_SMALL
GRIB_FILE_NOT_FOUND = _gribapi_swig.GRIB_FILE_NOT_FOUND
GRIB_CODE_NOT_FOUND_IN_TABLE = _gribapi_swig.GRIB_CODE_NOT_FOUND_IN_TABLE
GRIB_WRONG_ARRAY_SIZE = _gribapi_swig.GRIB_WRONG_ARRAY_SIZE
GRIB_NOT_FOUND = _gribapi_swig.GRIB_NOT_FOUND
GRIB_IO_PROBLEM = _gribapi_swig.GRIB_IO_PROBLEM
GRIB_INVALID_MESSAGE = _gribapi_swig.GRIB_INVALID_MESSAGE
GRIB_DECODING_ERROR = _gribapi_swig.GRIB_DECODING_ERROR
GRIB_ENCODING_ERROR = _gribapi_swig.GRIB_ENCODING_ERROR
GRIB_NO_MORE_IN_SET = _gribapi_swig.GRIB_NO_MORE_IN_SET
GRIB_GEOCALCULUS_PROBLEM = _gribapi_swig.GRIB_GEOCALCULUS_PROBLEM
GRIB_OUT_OF_MEMORY = _gribapi_swig.GRIB_OUT_OF_MEMORY
GRIB_READ_ONLY = _gribapi_swig.GRIB_READ_ONLY
GRIB_INVALID_ARGUMENT = _gribapi_swig.GRIB_INVALID_ARGUMENT
GRIB_NULL_HANDLE = _gribapi_swig.GRIB_NULL_HANDLE
GRIB_INVALID_SECTION_NUMBER = _gribapi_swig.GRIB_INVALID_SECTION_NUMBER
GRIB_VALUE_CANNOT_BE_MISSING = _gribapi_swig.GRIB_VALUE_CANNOT_BE_MISSING
GRIB_WRONG_LENGTH = _gribapi_swig.GRIB_WRONG_LENGTH
GRIB_INVALID_TYPE = _gribapi_swig.GRIB_INVALID_TYPE
GRIB_WRONG_STEP = _gribapi_swig.GRIB_WRONG_STEP
GRIB_WRONG_STEP_UNIT = _gribapi_swig.GRIB_WRONG_STEP_UNIT
GRIB_INVALID_FILE = _gribapi_swig.GRIB_INVALID_FILE
GRIB_INVALID_GRIB = _gribapi_swig.GRIB_INVALID_GRIB
GRIB_INVALID_INDEX = _gribapi_swig.GRIB_INVALID_INDEX
GRIB_INVALID_ITERATOR = _gribapi_swig.GRIB_INVALID_ITERATOR
GRIB_INVALID_KEYS_ITERATOR = _gribapi_swig.GRIB_INVALID_KEYS_ITERATOR
GRIB_INVALID_NEAREST = _gribapi_swig.GRIB_INVALID_NEAREST
GRIB_INVALID_ORDERBY = _gribapi_swig.GRIB_INVALID_ORDERBY
GRIB_MISSING_KEY = _gribapi_swig.GRIB_MISSING_KEY
GRIB_OUT_OF_AREA = _gribapi_swig.GRIB_OUT_OF_AREA
GRIB_CONCEPT_NO_MATCH = _gribapi_swig.GRIB_CONCEPT_NO_MATCH
GRIB_NO_DEFINITIONS = _gribapi_swig.GRIB_NO_DEFINITIONS
GRIB_WRONG_TYPE = _gribapi_swig.GRIB_WRONG_TYPE
GRIB_END = _gribapi_swig.GRIB_END
GRIB_NO_VALUES = _gribapi_swig.GRIB_NO_VALUES
GRIB_WRONG_GRID = _gribapi_swig.GRIB_WRONG_GRID
GRIB_END_OF_INDEX = _gribapi_swig.GRIB_END_OF_INDEX
GRIB_NULL_INDEX = _gribapi_swig.GRIB_NULL_INDEX
GRIB_PREMATURE_END_OF_FILE = _gribapi_swig.GRIB_PREMATURE_END_OF_FILE
GRIB_INTERNAL_ARRAY_TOO_SMALL = _gribapi_swig.GRIB_INTERNAL_ARRAY_TOO_SMALL
GRIB_MESSAGE_TOO_LARGE = _gribapi_swig.GRIB_MESSAGE_TOO_LARGE
GRIB_CONSTANT_FIELD = _gribapi_swig.GRIB_CONSTANT_FIELD
GRIB_SWITCH_NO_MATCH = _gribapi_swig.GRIB_SWITCH_NO_MATCH
GRIB_UNDERFLOW = _gribapi_swig.GRIB_UNDERFLOW
GRIB_MESSAGE_MALFORMED = _gribapi_swig.GRIB_MESSAGE_MALFORMED
GRIB_CORRUPTED_INDEX = _gribapi_swig.GRIB_CORRUPTED_INDEX
GRIB_INVALID_BPV = _gribapi_swig.GRIB_INVALID_BPV
GRIB_DIFFERENT_EDITION = _gribapi_swig.GRIB_DIFFERENT_EDITION
GRIB_VALUE_DIFFERENT = _gribapi_swig.GRIB_VALUE_DIFFERENT
GRIB_INVALID_KEY_VALUE = _gribapi_swig.GRIB_INVALID_KEY_VALUE
class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gribapi_swig.new_intp()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gribapi_swig.delete_intp
    __del__ = lambda self : None;
    def assign(self, *args): return _gribapi_swig.intp_assign(self, *args)
    def value(self): return _gribapi_swig.intp_value(self)
    def cast(self): return _gribapi_swig.intp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gribapi_swig.intp_frompointer
    if _newclass:frompointer = staticmethod(_gribapi_swig.intp_frompointer)
intp_swigregister = _gribapi_swig.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(*args):
  return _gribapi_swig.intp_frompointer(*args)
intp_frompointer = _gribapi_swig.intp_frompointer

class longp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, longp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, longp, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gribapi_swig.new_longp()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gribapi_swig.delete_longp
    __del__ = lambda self : None;
    def assign(self, *args): return _gribapi_swig.longp_assign(self, *args)
    def value(self): return _gribapi_swig.longp_value(self)
    def cast(self): return _gribapi_swig.longp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gribapi_swig.longp_frompointer
    if _newclass:frompointer = staticmethod(_gribapi_swig.longp_frompointer)
longp_swigregister = _gribapi_swig.longp_swigregister
longp_swigregister(longp)

def longp_frompointer(*args):
  return _gribapi_swig.longp_frompointer(*args)
longp_frompointer = _gribapi_swig.longp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _gribapi_swig.new_doublep()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gribapi_swig.delete_doublep
    __del__ = lambda self : None;
    def assign(self, *args): return _gribapi_swig.doublep_assign(self, *args)
    def value(self): return _gribapi_swig.doublep_value(self)
    def cast(self): return _gribapi_swig.doublep_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gribapi_swig.doublep_frompointer
    if _newclass:frompointer = staticmethod(_gribapi_swig.doublep_frompointer)
doublep_swigregister = _gribapi_swig.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(*args):
  return _gribapi_swig.doublep_frompointer(*args)
doublep_frompointer = _gribapi_swig.doublep_frompointer


def new_doubleArray(*args):
  return _gribapi_swig.new_doubleArray(*args)
new_doubleArray = _gribapi_swig.new_doubleArray

def delete_doubleArray(*args):
  return _gribapi_swig.delete_doubleArray(*args)
delete_doubleArray = _gribapi_swig.delete_doubleArray

def doubleArray_getitem(*args):
  return _gribapi_swig.doubleArray_getitem(*args)
doubleArray_getitem = _gribapi_swig.doubleArray_getitem

def doubleArray_setitem(*args):
  return _gribapi_swig.doubleArray_setitem(*args)
doubleArray_setitem = _gribapi_swig.doubleArray_setitem

def new_longArray(*args):
  return _gribapi_swig.new_longArray(*args)
new_longArray = _gribapi_swig.new_longArray

def delete_longArray(*args):
  return _gribapi_swig.delete_longArray(*args)
delete_longArray = _gribapi_swig.delete_longArray

def longArray_getitem(*args):
  return _gribapi_swig.longArray_getitem(*args)
longArray_getitem = _gribapi_swig.longArray_getitem

def longArray_setitem(*args):
  return _gribapi_swig.longArray_setitem(*args)
longArray_setitem = _gribapi_swig.longArray_setitem

def new_intArray(*args):
  return _gribapi_swig.new_intArray(*args)
new_intArray = _gribapi_swig.new_intArray

def delete_intArray(*args):
  return _gribapi_swig.delete_intArray(*args)
delete_intArray = _gribapi_swig.delete_intArray

def intArray_getitem(*args):
  return _gribapi_swig.intArray_getitem(*args)
intArray_getitem = _gribapi_swig.intArray_getitem

def intArray_setitem(*args):
  return _gribapi_swig.intArray_setitem(*args)
intArray_setitem = _gribapi_swig.intArray_setitem

def grib_c_new_from_file(*args):
  return _gribapi_swig.grib_c_new_from_file(*args)
grib_c_new_from_file = _gribapi_swig.grib_c_new_from_file

def grib_c_iterator_new(*args):
  return _gribapi_swig.grib_c_iterator_new(*args)
grib_c_iterator_new = _gribapi_swig.grib_c_iterator_new

def grib_c_keys_iterator_new(*args):
  return _gribapi_swig.grib_c_keys_iterator_new(*args)
grib_c_keys_iterator_new = _gribapi_swig.grib_c_keys_iterator_new

def grib_c_new_from_samples(*args):
  return _gribapi_swig.grib_c_new_from_samples(*args)
grib_c_new_from_samples = _gribapi_swig.grib_c_new_from_samples

def grib_c_index_new_from_file(*args):
  return _gribapi_swig.grib_c_index_new_from_file(*args)
grib_c_index_new_from_file = _gribapi_swig.grib_c_index_new_from_file

def grib_c_index_add_file(*args):
  return _gribapi_swig.grib_c_index_add_file(*args)
grib_c_index_add_file = _gribapi_swig.grib_c_index_add_file

def grib_c_new_from_index(*args):
  return _gribapi_swig.grib_c_new_from_index(*args)
grib_c_new_from_index = _gribapi_swig.grib_c_new_from_index

def grib_c_index_write(*args):
  return _gribapi_swig.grib_c_index_write(*args)
grib_c_index_write = _gribapi_swig.grib_c_index_write

def grib_c_index_read(*args):
  return _gribapi_swig.grib_c_index_read(*args)
grib_c_index_read = _gribapi_swig.grib_c_index_read

def grib_c_new_from_message(*args):
  return _gribapi_swig.grib_c_new_from_message(*args)
grib_c_new_from_message = _gribapi_swig.grib_c_new_from_message

def grib_c_count_in_file(*args):
  return _gribapi_swig.grib_c_count_in_file(*args)
grib_c_count_in_file = _gribapi_swig.grib_c_count_in_file

def grib_c_release(*args):
  return _gribapi_swig.grib_c_release(*args)
grib_c_release = _gribapi_swig.grib_c_release

def grib_c_write(*args):
  return _gribapi_swig.grib_c_write(*args)
grib_c_write = _gribapi_swig.grib_c_write

def grib_c_get_size_long(*args):
  return _gribapi_swig.grib_c_get_size_long(*args)
grib_c_get_size_long = _gribapi_swig.grib_c_get_size_long

def grib_c_clone(*args):
  return _gribapi_swig.grib_c_clone(*args)
grib_c_clone = _gribapi_swig.grib_c_clone

def grib_c_copy_namespace(*args):
  return _gribapi_swig.grib_c_copy_namespace(*args)
grib_c_copy_namespace = _gribapi_swig.grib_c_copy_namespace

def grib_c_get_message_size(*args):
  return _gribapi_swig.grib_c_get_message_size(*args)
grib_c_get_message_size = _gribapi_swig.grib_c_get_message_size

def grib_c_get_native_type(*args):
  return _gribapi_swig.grib_c_get_native_type(*args)
grib_c_get_native_type = _gribapi_swig.grib_c_get_native_type

def grib_c_multi_new():
  return _gribapi_swig.grib_c_multi_new()
grib_c_multi_new = _gribapi_swig.grib_c_multi_new

def grib_c_multi_support_on():
  return _gribapi_swig.grib_c_multi_support_on()
grib_c_multi_support_on = _gribapi_swig.grib_c_multi_support_on

def grib_c_multi_write(*args):
  return _gribapi_swig.grib_c_multi_write(*args)
grib_c_multi_write = _gribapi_swig.grib_c_multi_write

def grib_c_multi_support_off():
  return _gribapi_swig.grib_c_multi_support_off()
grib_c_multi_support_off = _gribapi_swig.grib_c_multi_support_off

def grib_c_multi_release(*args):
  return _gribapi_swig.grib_c_multi_release(*args)
grib_c_multi_release = _gribapi_swig.grib_c_multi_release

def grib_c_multi_append(*args):
  return _gribapi_swig.grib_c_multi_append(*args)
grib_c_multi_append = _gribapi_swig.grib_c_multi_append

def grib_c_gribex_mode_on():
  return _gribapi_swig.grib_c_gribex_mode_on()
grib_c_gribex_mode_on = _gribapi_swig.grib_c_gribex_mode_on

def grib_c_gribex_mode_off():
  return _gribapi_swig.grib_c_gribex_mode_off()
grib_c_gribex_mode_off = _gribapi_swig.grib_c_gribex_mode_off

def grib_c_keys_iterator_next(*args):
  return _gribapi_swig.grib_c_keys_iterator_next(*args)
grib_c_keys_iterator_next = _gribapi_swig.grib_c_keys_iterator_next

def grib_c_keys_iterator_delete(*args):
  return _gribapi_swig.grib_c_keys_iterator_delete(*args)
grib_c_keys_iterator_delete = _gribapi_swig.grib_c_keys_iterator_delete

def grib_c_skip_computed(*args):
  return _gribapi_swig.grib_c_skip_computed(*args)
grib_c_skip_computed = _gribapi_swig.grib_c_skip_computed

def grib_c_skip_coded(*args):
  return _gribapi_swig.grib_c_skip_coded(*args)
grib_c_skip_coded = _gribapi_swig.grib_c_skip_coded

def grib_c_skip_edition_specific(*args):
  return _gribapi_swig.grib_c_skip_edition_specific(*args)
grib_c_skip_edition_specific = _gribapi_swig.grib_c_skip_edition_specific

def grib_c_skip_duplicates(*args):
  return _gribapi_swig.grib_c_skip_duplicates(*args)
grib_c_skip_duplicates = _gribapi_swig.grib_c_skip_duplicates

def grib_c_skip_read_only(*args):
  return _gribapi_swig.grib_c_skip_read_only(*args)
grib_c_skip_read_only = _gribapi_swig.grib_c_skip_read_only

def grib_c_skip_function(*args):
  return _gribapi_swig.grib_c_skip_function(*args)
grib_c_skip_function = _gribapi_swig.grib_c_skip_function

def grib_c_keys_iterator_rewind(*args):
  return _gribapi_swig.grib_c_keys_iterator_rewind(*args)
grib_c_keys_iterator_rewind = _gribapi_swig.grib_c_keys_iterator_rewind

def grib_c_keys_iterator_get_name(*args):
  return _gribapi_swig.grib_c_keys_iterator_get_name(*args)
grib_c_keys_iterator_get_name = _gribapi_swig.grib_c_keys_iterator_get_name

def grib_c_index_get_size_long(*args):
  return _gribapi_swig.grib_c_index_get_size_long(*args)
grib_c_index_get_size_long = _gribapi_swig.grib_c_index_get_size_long

def grib_c_index_get_long(*args):
  return _gribapi_swig.grib_c_index_get_long(*args)
grib_c_index_get_long = _gribapi_swig.grib_c_index_get_long

def grib_c_index_get_real8(*args):
  return _gribapi_swig.grib_c_index_get_real8(*args)
grib_c_index_get_real8 = _gribapi_swig.grib_c_index_get_real8

def grib_c_index_get_string(*args):
  return _gribapi_swig.grib_c_index_get_string(*args)
grib_c_index_get_string = _gribapi_swig.grib_c_index_get_string

def grib_c_index_select_long(*args):
  return _gribapi_swig.grib_c_index_select_long(*args)
grib_c_index_select_long = _gribapi_swig.grib_c_index_select_long

def grib_c_index_select_real8(*args):
  return _gribapi_swig.grib_c_index_select_real8(*args)
grib_c_index_select_real8 = _gribapi_swig.grib_c_index_select_real8

def grib_c_index_select_string(*args):
  return _gribapi_swig.grib_c_index_select_string(*args)
grib_c_index_select_string = _gribapi_swig.grib_c_index_select_string

def grib_c_index_release(*args):
  return _gribapi_swig.grib_c_index_release(*args)
grib_c_index_release = _gribapi_swig.grib_c_index_release

def grib_c_iterator_delete(*args):
  return _gribapi_swig.grib_c_iterator_delete(*args)
grib_c_iterator_delete = _gribapi_swig.grib_c_iterator_delete

def grib_c_iterator_next(*args):
  return _gribapi_swig.grib_c_iterator_next(*args)
grib_c_iterator_next = _gribapi_swig.grib_c_iterator_next

def grib_c_get_string(*args):
  return _gribapi_swig.grib_c_get_string(*args)
grib_c_get_string = _gribapi_swig.grib_c_get_string

def grib_c_set_string(*args):
  return _gribapi_swig.grib_c_set_string(*args)
grib_c_set_string = _gribapi_swig.grib_c_set_string

def grib_c_get_long(*args):
  return _gribapi_swig.grib_c_get_long(*args)
grib_c_get_long = _gribapi_swig.grib_c_get_long

def grib_c_set_long(*args):
  return _gribapi_swig.grib_c_set_long(*args)
grib_c_set_long = _gribapi_swig.grib_c_set_long

def grib_c_get_double(*args):
  return _gribapi_swig.grib_c_get_double(*args)
grib_c_get_double = _gribapi_swig.grib_c_get_double

def grib_c_set_double(*args):
  return _gribapi_swig.grib_c_set_double(*args)
grib_c_set_double = _gribapi_swig.grib_c_set_double

def grib_c_set_real8_array(*args):
  return _gribapi_swig.grib_c_set_real8_array(*args)
grib_c_set_real8_array = _gribapi_swig.grib_c_set_real8_array

def grib_c_get_real8_array(*args):
  return _gribapi_swig.grib_c_get_real8_array(*args)
grib_c_get_real8_array = _gribapi_swig.grib_c_get_real8_array

def grib_c_get_long_array(*args):
  return _gribapi_swig.grib_c_get_long_array(*args)
grib_c_get_long_array = _gribapi_swig.grib_c_get_long_array

def grib_c_set_long_array(*args):
  return _gribapi_swig.grib_c_set_long_array(*args)
grib_c_set_long_array = _gribapi_swig.grib_c_set_long_array

def grib_c_get_real8_element(*args):
  return _gribapi_swig.grib_c_get_real8_element(*args)
grib_c_get_real8_element = _gribapi_swig.grib_c_get_real8_element

def grib_c_get_real8_elements(*args):
  return _gribapi_swig.grib_c_get_real8_elements(*args)
grib_c_get_real8_elements = _gribapi_swig.grib_c_get_real8_elements

def grib_c_set_missing(*args):
  return _gribapi_swig.grib_c_set_missing(*args)
grib_c_set_missing = _gribapi_swig.grib_c_set_missing

def grib_c_is_missing(*args):
  return _gribapi_swig.grib_c_is_missing(*args)
grib_c_is_missing = _gribapi_swig.grib_c_is_missing

def with_numpy():
  return _gribapi_swig.with_numpy()
with_numpy = _gribapi_swig.with_numpy

def grib_set_double_ndarray(*args):
  return _gribapi_swig.grib_set_double_ndarray(*args)
grib_set_double_ndarray = _gribapi_swig.grib_set_double_ndarray

def grib_set_long_ndarray(*args):
  return _gribapi_swig.grib_set_long_ndarray(*args)
grib_set_long_ndarray = _gribapi_swig.grib_set_long_ndarray

def grib_get_double_ndarray(*args):
  return _gribapi_swig.grib_get_double_ndarray(*args)
grib_get_double_ndarray = _gribapi_swig.grib_get_double_ndarray

def grib_get_long_ndarray(*args):
  return _gribapi_swig.grib_get_long_ndarray(*args)
grib_get_long_ndarray = _gribapi_swig.grib_get_long_ndarray

def grib_get_double_ndelements(*args):
  return _gribapi_swig.grib_get_double_ndelements(*args)
grib_get_double_ndelements = _gribapi_swig.grib_get_double_ndelements

def grib_c_find_nearest_single(*args):
  return _gribapi_swig.grib_c_find_nearest_single(*args)
grib_c_find_nearest_single = _gribapi_swig.grib_c_find_nearest_single

def grib_c_find_nearest_four_single(*args):
  return _gribapi_swig.grib_c_find_nearest_four_single(*args)
grib_c_find_nearest_four_single = _gribapi_swig.grib_c_find_nearest_four_single

def grib_c_get_message(*args):
  return _gribapi_swig.grib_c_get_message(*args)
grib_c_get_message = _gribapi_swig.grib_c_get_message

def grib_c_get_error_string(*args):
  return _gribapi_swig.grib_c_get_error_string(*args)
grib_c_get_error_string = _gribapi_swig.grib_c_get_error_string

def no_fail_on_wrong_length(*args):
  return _gribapi_swig.no_fail_on_wrong_length(*args)
no_fail_on_wrong_length = _gribapi_swig.no_fail_on_wrong_length

def grib_c_get_api_version():
  return _gribapi_swig.grib_c_get_api_version()
grib_c_get_api_version = _gribapi_swig.grib_c_get_api_version

def grib_c_gts_header_on():
  return _gribapi_swig.grib_c_gts_header_on()
grib_c_gts_header_on = _gribapi_swig.grib_c_gts_header_on

def grib_c_gts_header_off():
  return _gribapi_swig.grib_c_gts_header_off()
grib_c_gts_header_off = _gribapi_swig.grib_c_gts_header_off


