#include <iostream>

#include <mutex>
#include <pcl/io/openni_grabber.h>
#include <pcl/visualization/pcl_visualizer.h>

typedef pcl::PointXYZ T;

class SimpleOpenNIViewer 
{
public:
  SimpleOpenNIViewer()
      : viewer(new pcl::visualization::PCLVisualizer("PCL OpenNI Viewer")) {}

  std::mutex mtx;
  pcl::visualization::PCLVisualizer::Ptr viewer;

  void cloud_cb_(const pcl::PointCloud<T>::ConstPtr &cloud) 
  {
    if (!viewer->wasStopped()) 
    {
      mtx.lock();
      viewer->updatePointCloud<T>(cloud, "openni");
      mtx.unlock();
    }
  }

  void run() 
  {
    pcl::Grabber *interface = new pcl::io::OpenNIGrabber(
        "", pcl::io::OpenNI2Grabber::OpenNI_QVGA_30Hz,
        pcl::io::OpenNI2Grabber::OpenNI_QVGA_30Hz);

    pcl::PointCloud<T>::Ptr cloud(new pcl::PointCloud<T>);
    viewer->addPointCloud<T>(cloud, "openni", 0);

    boost::function<void(const pcl::PointCloud<T>::ConstPtr &)> f =
        boost::bind(&SimpleOpenNIViewer::cloud_cb_, this, _1);

    interface->registerCallback(f);

    interface->start();

    while (!viewer->wasStopped()) 
    {
      boost::this_thread::sleep(boost::posix_time::millisec(50));
      mtx.lock();
      viewer->spinOnce();
      mtx.unlock();
    }

    interface->stop();
  }

  
};

int main() 
{
  SimpleOpenNIViewer v;
  v.run();
  return 0;
}