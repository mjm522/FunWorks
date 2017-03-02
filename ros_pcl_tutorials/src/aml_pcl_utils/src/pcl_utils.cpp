#include <ros/ros.h>
#include <iostream>
#include <string>
// PCL specific includes
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <pcl/filters/voxel_grid.h>


class PCLUtils
{
private:

  ros::NodeHandle _nh;
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud;

public:
  PCLUtils(ros::NodeHandle nh);
  void recieve_cloud_callback(const sensor_msgs::PointCloud2ConstPtr& cloud_msg);
  void read_pcd_file(std::string filename);
  void save_point_cloud_file(std::string filename, const pcl::PointCloud2::Ptr cloud, std::string format);
  void down_sample_pcd_file(pcl::PointCloud2::Ptr cloud_filtered, const pcl::PointCloud2::Ptr cloud);

};

PCLUtils::PCLUtils(ros::NodeHandle nh): 
_nh(nh), cloud (new pcl::PointCloud<pcl::PointXYZ>)
{}

void  PCLUtils::recieve_cloud_callback(const sensor_msgs::PointCloud2ConstPtr& cloud_msg)
{
  // Container for original & filtered data
  pcl::PCLPointCloud2* cloud = new pcl::PCLPointCloud2; 
  pcl::PCLPointCloud2ConstPtr cloudPtr(cloud);
  pcl::PCLPointCloud2 cloud_filtered;

  // Convert to PCL data type
  pcl_conversions::toPCL(*cloud_msg, *cloud);

  // Perform the actual filtering
  pcl::VoxelGrid<pcl::PCLPointCloud2> sor;
  sor.setInputCloud (cloudPtr);
  sor.setLeafSize (0.1, 0.1, 0.1);
  sor.filter (cloud_filtered);

  // Convert to ROS data type
  sensor_msgs::PointCloud2 output;
  pcl_conversions::moveFromPCL(cloud_filtered, output);

  // pcl::PointCloud<pcl::PointXYZ>::Ptr temp_cloud(new pcl::PointCloud<pcl::PointXYZ>);
  pcl::PointCloud<pcl::PointXYZRGB> temp_cloud;
  pcl::fromROSMsg(*cloud_msg, temp_cloud);

  // pcl::io::savePCDFileASCII ("test_pcd.pcd", temp_cloud);

  // Publish the data
  // pub.publish (output);
}

void PCLUtils::save_point_cloud_file(std::string filename, const pcl::PointCloud2::Ptr cloud, std::string format)
{
  if (format.compare("pcd_ascii"))
  {
    //pcl::io::savePCDFileASCII(filename.c_str(), cloud);
  }
  pcl::PCDWriter writer;
  writer.write (filename.c_str(), *cloud, 
    Eigen::Vector4f::Zero (), Eigen::Quaternionf::Identity (), false);
}

void PCLUtils::read_pcd_file(std::string filename)
{
  if (pcl::io::loadPCDFile<pcl::PointXYZ> (filename.c_str(), *cloud) == -1) //* load the file
  {
    PCL_ERROR("Couldn't read file %s \n", filename.c_str());
    return;
  }
}

void PCLUtils::down_sample_pcd_file(pcl::PCLPointCloud2::Ptr cloud_filtered, const pcl::PCLPointCloud2::Ptr cloud)
{
  // Create the filtering object
  pcl::VoxelGrid<pcl::PCLPointCloud2> sor;
  sor.setInputCloud (cloud);
  sor.setLeafSize (0.008f, 0.008f, 0.008f);
  sor.filter (*cloud_filtered);

}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "aml_pcl_utils");
  ros::NodeHandle nh("");;

  PCLUtils pcl_util_obj(nh);

  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe<sensor_msgs::PointCloud2> ("point_cloud_data", 1, &PCLUtils::recieve_cloud_callback, &pcl_util_obj);

  // Create a ROS publisher for the output point cloud
  // ros::Publisher pub = nh.advertise<sensor_msgs::PointCloud2> ("output", 1);

  // Spin
  while(ros::ok()) 
  {
    ros::spinOnce();
  }

  return 0;
  
}