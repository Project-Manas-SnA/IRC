# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "interfacing: 2 messages, 0 services")

set(MSG_I_FLAGS "-Iinterfacing:/home/blackbox/catkin_ws/src/interfacing/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(interfacing_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_custom_target(_interfacing_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "interfacing" "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" ""
)

get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_custom_target(_interfacing_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "interfacing" "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interfacing
)
_generate_msg_cpp(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interfacing
)

### Generating Services

### Generating Module File
_generate_module_cpp(interfacing
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interfacing
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(interfacing_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(interfacing_generate_messages interfacing_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_cpp _interfacing_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_cpp _interfacing_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interfacing_gencpp)
add_dependencies(interfacing_gencpp interfacing_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interfacing_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interfacing
)
_generate_msg_eus(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interfacing
)

### Generating Services

### Generating Module File
_generate_module_eus(interfacing
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interfacing
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(interfacing_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(interfacing_generate_messages interfacing_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_eus _interfacing_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_eus _interfacing_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interfacing_geneus)
add_dependencies(interfacing_geneus interfacing_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interfacing_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interfacing
)
_generate_msg_lisp(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interfacing
)

### Generating Services

### Generating Module File
_generate_module_lisp(interfacing
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interfacing
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(interfacing_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(interfacing_generate_messages interfacing_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_lisp _interfacing_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_lisp _interfacing_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interfacing_genlisp)
add_dependencies(interfacing_genlisp interfacing_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interfacing_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interfacing
)
_generate_msg_nodejs(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interfacing
)

### Generating Services

### Generating Module File
_generate_module_nodejs(interfacing
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interfacing
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(interfacing_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(interfacing_generate_messages interfacing_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_nodejs _interfacing_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_nodejs _interfacing_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interfacing_gennodejs)
add_dependencies(interfacing_gennodejs interfacing_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interfacing_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing
)
_generate_msg_py(interfacing
  "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing
)

### Generating Services

### Generating Module File
_generate_module_py(interfacing
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(interfacing_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(interfacing_generate_messages interfacing_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/Velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_py _interfacing_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/blackbox/catkin_ws/src/interfacing/msg/velocity.msg" NAME_WE)
add_dependencies(interfacing_generate_messages_py _interfacing_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interfacing_genpy)
add_dependencies(interfacing_genpy interfacing_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interfacing_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interfacing)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interfacing
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(interfacing_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interfacing)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interfacing
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(interfacing_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interfacing)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interfacing
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(interfacing_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interfacing)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interfacing
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(interfacing_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interfacing
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(interfacing_generate_messages_py std_msgs_generate_messages_py)
endif()
