# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mjm/Projects/FunProjects/pcl_tutorials

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mjm/Projects/FunProjects/pcl_tutorials

# Include any dependencies generated for this target.
include CMakeFiles/./bin/point_cloud_to_mesh.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/./bin/point_cloud_to_mesh.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/./bin/point_cloud_to_mesh.dir/flags.make

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o: CMakeFiles/./bin/point_cloud_to_mesh.dir/flags.make
CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o: point_cloud_to_mesh.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mjm/Projects/FunProjects/pcl_tutorials/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o -c /home/mjm/Projects/FunProjects/pcl_tutorials/point_cloud_to_mesh.cpp

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/mjm/Projects/FunProjects/pcl_tutorials/point_cloud_to_mesh.cpp > CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.i

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/mjm/Projects/FunProjects/pcl_tutorials/point_cloud_to_mesh.cpp -o CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.s

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.requires:
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.requires

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.provides: CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.requires
	$(MAKE) -f CMakeFiles/./bin/point_cloud_to_mesh.dir/build.make CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.provides.build
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.provides

CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.provides.build: CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o

# Object files for target ./bin/point_cloud_to_mesh
_/bin/point_cloud_to_mesh_OBJECTS = \
"CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o"

# External object files for target ./bin/point_cloud_to_mesh
_/bin/point_cloud_to_mesh_EXTERNAL_OBJECTS =

./bin/point_cloud_to_mesh: CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o
./bin/point_cloud_to_mesh: CMakeFiles/./bin/point_cloud_to_mesh.dir/build.make
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_system.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_thread.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libpthread.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_common.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_octree.so
./bin/point_cloud_to_mesh: /usr/lib/libOpenNI.so
./bin/point_cloud_to_mesh: /usr/lib/libvtkCommon.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkRendering.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkHybrid.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkCharts.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libpcl_io.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
./bin/point_cloud_to_mesh: /usr/lib/libpcl_kdtree.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_search.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_sample_consensus.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_filters.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_features.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_keypoints.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_segmentation.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_visualization.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_outofcore.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_registration.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_recognition.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libqhull.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_surface.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_people.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_tracking.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_apps.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_system.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_thread.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libpthread.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libqhull.so
./bin/point_cloud_to_mesh: /usr/lib/libOpenNI.so
./bin/point_cloud_to_mesh: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
./bin/point_cloud_to_mesh: /usr/lib/libvtkCommon.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkRendering.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkHybrid.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkCharts.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libpcl_common.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_octree.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_io.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_kdtree.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_search.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_sample_consensus.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_filters.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_features.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_keypoints.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_segmentation.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_visualization.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_outofcore.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_registration.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_recognition.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_surface.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_people.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_tracking.so
./bin/point_cloud_to_mesh: /usr/lib/libpcl_apps.so
./bin/point_cloud_to_mesh: /usr/lib/libvtkViews.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkInfovis.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkWidgets.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkHybrid.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkParallel.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkVolumeRendering.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkRendering.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkGraphics.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkImaging.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkIO.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkFiltering.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtkCommon.so.5.8.0
./bin/point_cloud_to_mesh: /usr/lib/libvtksys.so.5.8.0
./bin/point_cloud_to_mesh: CMakeFiles/./bin/point_cloud_to_mesh.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ./bin/point_cloud_to_mesh"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/./bin/point_cloud_to_mesh.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/./bin/point_cloud_to_mesh.dir/build: ./bin/point_cloud_to_mesh
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/build

CMakeFiles/./bin/point_cloud_to_mesh.dir/requires: CMakeFiles/./bin/point_cloud_to_mesh.dir/point_cloud_to_mesh.cpp.o.requires
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/requires

CMakeFiles/./bin/point_cloud_to_mesh.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/./bin/point_cloud_to_mesh.dir/cmake_clean.cmake
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/clean

CMakeFiles/./bin/point_cloud_to_mesh.dir/depend:
	cd /home/mjm/Projects/FunProjects/pcl_tutorials && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials/CMakeFiles/bin/point_cloud_to_mesh.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/./bin/point_cloud_to_mesh.dir/depend

