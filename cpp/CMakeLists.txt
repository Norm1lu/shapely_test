cmake_minimum_required(VERSION 3.5)
set (CMAKE_CXX_STANDARD 11)
project(hitbot)

add_library(hitbot_interface SHARED IMPORTED)
message(STATUS "CMAKE_SOURCE_DIR: ${CMAKE_SOURCE_DIR}")

set_property(TARGET hitbot_interface PROPERTY IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/lib/libsmall_scara_interface.so)

add_executable(demo ${CMAKE_SOURCE_DIR}/example/demo.cpp)
target_include_directories(demo PRIVATE ${CMAKE_SOURCE_DIR}/include/)
target_link_libraries(demo hitbot_interface)
