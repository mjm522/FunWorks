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
include CMakeFiles/./bin/openni_grabber.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/./bin/openni_grabber.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/./bin/openni_grabber.dir/flags.make

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o: CMakeFiles/./bin/openni_grabber.dir/flags.make
CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o: openni_grabber.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mjm/Projects/FunProjects/pcl_tutorials/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o -c /home/mjm/Projects/FunProjects/pcl_tutorials/openni_grabber.cpp

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/mjm/Projects/FunProjects/pcl_tutorials/openni_grabber.cpp > CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.i

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/mjm/Projects/FunProjects/pcl_tutorials/openni_grabber.cpp -o CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.s

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.requires:
.PHONY : CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.requires

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.provides: CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.requires
	$(MAKE) -f CMakeFiles/./bin/openni_grabber.dir/build.make CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.provides.build
.PHONY : CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.provides

CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.provides.build: CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o

# Object files for target ./bin/openni_grabber
_/bin/openni_grabber_OBJECTS = \
"CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o"

# External object files for target ./bin/openni_grabber
_/bin/openni_grabber_EXTERNAL_OBJECTS =

./bin/openni_grabber: CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o
./bin/openni_grabber: CMakeFiles/./bin/openni_grabber.dir/build.make
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_system.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_thread.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libpthread.so
./bin/openni_grabber: /usr/lib/libpcl_common.so
./bin/openni_grabber: /usr/lib/libpcl_octree.so
./bin/openni_grabber: /usr/lib/libOpenNI.so
./bin/openni_grabber: /usr/lib/libvtkCommon.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkRendering.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkHybrid.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkCharts.so.5.8.0
./bin/openni_grabber: /usr/lib/libpcl_io.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
./bin/openni_grabber: /usr/lib/libpcl_kdtree.so
./bin/openni_grabber: /usr/lib/libpcl_search.so
./bin/openni_grabber: /usr/lib/libpcl_sample_consensus.so
./bin/openni_grabber: /usr/lib/libpcl_filters.so
./bin/openni_grabber: /usr/lib/libpcl_features.so
./bin/openni_grabber: /usr/lib/libpcl_keypoints.so
./bin/openni_grabber: /usr/lib/libpcl_segmentation.so
./bin/openni_grabber: /usr/lib/libpcl_visualization.so
./bin/openni_grabber: /usr/lib/libpcl_outofcore.so
./bin/openni_grabber: /usr/lib/libpcl_registration.so
./bin/openni_grabber: /usr/lib/libpcl_recognition.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libqhull.so
./bin/openni_grabber: /usr/lib/libpcl_surface.so
./bin/openni_grabber: /usr/lib/libpcl_people.so
./bin/openni_grabber: /usr/lib/libpcl_tracking.so
./bin/openni_grabber: /usr/lib/libpcl_apps.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_system.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_thread.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libpthread.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libqhull.so
./bin/openni_grabber: /usr/lib/libOpenNI.so
./bin/openni_grabber: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
./bin/openni_grabber: /usr/lib/libvtkCommon.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkRendering.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkHybrid.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkCharts.so.5.8.0
./bin/openni_grabber: /usr/lib/libpcl_common.so
./bin/openni_grabber: /usr/lib/libpcl_octree.so
./bin/openni_grabber: /usr/lib/libpcl_io.so
./bin/openni_grabber: /usr/lib/libpcl_kdtree.so
./bin/openni_grabber: /usr/lib/libpcl_search.so
./bin/openni_grabber: /usr/lib/libpcl_sample_consensus.so
./bin/openni_grabber: /usr/lib/libpcl_filters.so
./bin/openni_grabber: /usr/lib/libpcl_features.so
./bin/openni_grabber: /usr/lib/libpcl_keypoints.so
./bin/openni_grabber: /usr/lib/libpcl_segmentation.so
./bin/openni_grabber: /usr/lib/libpcl_visualization.so
./bin/openni_grabber: /usr/lib/libpcl_outofcore.so
./bin/openni_grabber: /usr/lib/libpcl_registration.so
./bin/openni_grabber: /usr/lib/libpcl_recognition.so
./bin/openni_grabber: /usr/lib/libpcl_surface.so
./bin/openni_grabber: /usr/lib/libpcl_people.so
./bin/openni_grabber: /usr/lib/libpcl_tracking.so
./bin/openni_grabber: /usr/lib/libpcl_apps.so
./bin/openni_grabber: /usr/lib/libvtkViews.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkInfovis.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkWidgets.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkHybrid.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkParallel.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkVolumeRendering.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkRendering.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkGraphics.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkImaging.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkIO.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkFiltering.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtkCommon.so.5.8.0
./bin/openni_grabber: /usr/lib/libvtksys.so.5.8.0
./bin/openni_grabber: CMakeFiles/./bin/openni_grabber.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ./bin/openni_grabber"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/./bin/openni_grabber.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/./bin/openni_grabber.dir/build: ./bin/openni_grabber
.PHONY : CMakeFiles/./bin/openni_grabber.dir/build

CMakeFiles/./bin/openni_grabber.dir/requires: CMakeFiles/./bin/openni_grabber.dir/openni_grabber.cpp.o.requires
.PHONY : CMakeFiles/./bin/openni_grabber.dir/requires

CMakeFiles/./bin/openni_grabber.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/./bin/openni_grabber.dir/cmake_clean.cmake
.PHONY : CMakeFiles/./bin/openni_grabber.dir/clean

CMakeFiles/./bin/openni_grabber.dir/depend:
	cd /home/mjm/Projects/FunProjects/pcl_tutorials && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials /home/mjm/Projects/FunProjects/pcl_tutorials/CMakeFiles/bin/openni_grabber.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/./bin/openni_grabber.dir/depend
