# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interfacing/Velocity.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Velocity(genpy.Message):
  _md5sum = "50ef263368455a7e4548bab29e60b833"
  _type = "interfacing/Velocity"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 Check
float32 leftwheel
float32 rightwheel
"""
  __slots__ = ['Check','leftwheel','rightwheel']
  _slot_types = ['int8','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Check,leftwheel,rightwheel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Velocity, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.Check is None:
        self.Check = 0
      if self.leftwheel is None:
        self.leftwheel = 0.
      if self.rightwheel is None:
        self.rightwheel = 0.
    else:
      self.Check = 0
      self.leftwheel = 0.
      self.rightwheel = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_b2f().pack(_x.Check, _x.leftwheel, _x.rightwheel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.Check, _x.leftwheel, _x.rightwheel,) = _get_struct_b2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_b2f().pack(_x.Check, _x.leftwheel, _x.rightwheel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.Check, _x.leftwheel, _x.rightwheel,) = _get_struct_b2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b2f = None
def _get_struct_b2f():
    global _struct_b2f
    if _struct_b2f is None:
        _struct_b2f = struct.Struct("<b2f")
    return _struct_b2f
