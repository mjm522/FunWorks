#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/compression/octree_pointcloud_compression.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/common/transforms.h>
#include <pcl/visualization/pcl_visualizer.h>

#include <stdio.h>
#include <sstream>
#include <stdlib.h>
#include <fstream>

int main (int argc, char** argv)
{
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);

  if (pcl::io::loadPCDFile<pcl::PointXYZ> ("test_pcd.pcd", *cloud) == -1) //* load the file
  {
    PCL_ERROR ("Couldn't read file test_pcd.pcd \n");
    return (-1);
  }

  bool showStatistics = true;
  // for a full list of profiles see: /io/include/pcl/compression/compression_profiles.h
  pcl::io::compression_Profiles_e compressionProfile = pcl::io::HIGH_RES_OFFLINE_COMPRESSION_WITHOUT_COLOR;

  pcl::io::OctreePointCloudCompression<pcl::PointXYZ>* PointCloudEncoder;
  pcl::io::OctreePointCloudCompression<pcl::PointXYZ>* PointCloudDecoder;

  // instantiate point cloud compression for encoding and decoding
  PointCloudEncoder = new pcl::io::OctreePointCloudCompression<pcl::PointXYZ> (compressionProfile, showStatistics);
  PointCloudDecoder = new pcl::io::OctreePointCloudCompression<pcl::PointXYZ> ();

  // stringstream to store compressed point cloud
  std::stringstream compressedData;
  std::stringstream compressedData2;
  
  // output pointcloud
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloudOut (new pcl::PointCloud<pcl::PointXYZ> ());
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloudOut2 (new pcl::PointCloud<pcl::PointXYZ> ());

  // compress point cloud
  // PointCloudEncoder->encodePointCloud (cloud, compressedData);

  // std::ofstream myFile("test_pcd_high.txt");

  // myFile << compressedData.rdbuf();

  // myFile.close();

  // Transformation matrix object, initialized to the identity matrix
      // (a null transformation).
  Eigen::Matrix4f transformation = Eigen::Matrix4f::Identity();

  // Set a rotation around the Z axis (right hand rule).
  float theta = 0.0f * (M_PI / 180.0f); // 90 degrees.
  transformation(0, 0) = cos(theta);
  transformation(0, 1) = -sin(theta);
  transformation(1, 0) = sin(theta);
  transformation(1, 1) = cos(theta);

  // Set a translation on the X axis.
  transformation(0, 3) = 1.0f; // 1 meter (positive direction).

  std::ifstream inFile("test_pcd_high.txt");
  std::ifstream inFile2("test_pcd.txt");
  compressedData << inFile.rdbuf();
  compressedData2 << inFile2.rdbuf();

  // decompress point cloud 
  PointCloudDecoder->decodePointCloud (compressedData, cloudOut);
  PointCloudDecoder->decodePointCloud (compressedData2, cloudOut2);


  // pcl::transformPointCloud(*cloudOut2, *cloudOut2, transformation);


  pcl::visualization::CloudViewer viewer("Simple Cloud Viewer");

  // pcl::visualization::PCLVisualizer viewer(argv[1]);

  // viewer.addPointCloud(cloudOut, "high");
  // viewer.addPointCloud(cloudOut2, "med");

  // show decompressed point cloud
  viewer.showCloud (cloudOut2);

  while (!viewer.wasStopped())
  {
      // viewer.spinOnce();

  }

  return (0);
}