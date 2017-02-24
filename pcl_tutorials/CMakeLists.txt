cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pcd_read)

find_package(PCL 1.2 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (./bin/pcd_read pcd_read.cpp)
target_link_libraries (./bin/pcd_read ${PCL_LIBRARIES})

#add_executable (./bin/openni_grabber openni_grabber.cpp)
#target_link_libraries (./bin/openni_grabber ${PCL_LIBRARIES})

add_executable (./bin/min_cut min_cut.cpp)
target_link_libraries (./bin/min_cut ${PCL_LIBRARIES})