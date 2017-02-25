cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(pcd_read)

find_package(PCL 1.2 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (./bin/pcd_read pcd_read.cpp)
target_link_libraries (./bin/pcd_read ${PCL_LIBRARIES})

add_executable (./bin/openni_grabber openni_grabber.cpp)
target_link_libraries (./bin/openni_grabber ${PCL_LIBRARIES})

add_executable (./bin/min_cut min_cut.cpp)
target_link_libraries (./bin/min_cut ${PCL_LIBRARIES})

add_executable (./bin/point_cloud_to_mesh point_cloud_to_mesh.cpp)
target_link_libraries (./bin/point_cloud_to_mesh ${PCL_LIBRARIES})

add_executable (./bin/region_growing_segmentation region_growing_segmentation.cpp)
target_link_libraries (./bin/region_growing_segmentation ${PCL_LIBRARIES})

add_executable (./bin/cylinder_model_segmentation cylinder_model_segmentation.cpp)
target_link_libraries (./bin/cylinder_model_segmentation ${PCL_LIBRARIES})

add_executable (./bin/points_not_in_plane points_not_in_plane.cpp)
target_link_libraries (./bin/points_not_in_plane ${PCL_LIBRARIES})

add_executable (./bin/outlier_removal outlier_removal.cpp)
target_link_libraries (./bin/outlier_removal ${PCL_LIBRARIES})