cmake_minimum_required(VERSION 3.12)

include(pico_sdk_import.cmake)

include(pico_extras_import.cmake)

project(DrumMachine C CXX)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_subdirectory(src)
