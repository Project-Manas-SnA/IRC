// Auto-generated. Do not edit!

// (in-package interfacing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Velocity {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Check = null;
      this.leftwheel = null;
      this.rightwheel = null;
    }
    else {
      if (initObj.hasOwnProperty('Check')) {
        this.Check = initObj.Check
      }
      else {
        this.Check = 0;
      }
      if (initObj.hasOwnProperty('leftwheel')) {
        this.leftwheel = initObj.leftwheel
      }
      else {
        this.leftwheel = 0.0;
      }
      if (initObj.hasOwnProperty('rightwheel')) {
        this.rightwheel = initObj.rightwheel
      }
      else {
        this.rightwheel = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Velocity
    // Serialize message field [Check]
    bufferOffset = _serializer.int8(obj.Check, buffer, bufferOffset);
    // Serialize message field [leftwheel]
    bufferOffset = _serializer.float32(obj.leftwheel, buffer, bufferOffset);
    // Serialize message field [rightwheel]
    bufferOffset = _serializer.float32(obj.rightwheel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Velocity
    let len;
    let data = new Velocity(null);
    // Deserialize message field [Check]
    data.Check = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [leftwheel]
    data.leftwheel = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rightwheel]
    data.rightwheel = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'interfacing/Velocity';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '50ef263368455a7e4548bab29e60b833';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 Check
    float32 leftwheel
    float32 rightwheel
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Velocity(null);
    if (msg.Check !== undefined) {
      resolved.Check = msg.Check;
    }
    else {
      resolved.Check = 0
    }

    if (msg.leftwheel !== undefined) {
      resolved.leftwheel = msg.leftwheel;
    }
    else {
      resolved.leftwheel = 0.0
    }

    if (msg.rightwheel !== undefined) {
      resolved.rightwheel = msg.rightwheel;
    }
    else {
      resolved.rightwheel = 0.0
    }

    return resolved;
    }
};

module.exports = Velocity;
