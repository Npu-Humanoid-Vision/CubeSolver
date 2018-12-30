#ifndef KMEANS_H
#define KMEANS_H

#include "./Father.h"

class KmeansProc : public FatherProc {
public:
    KmeansProc() ;
    ~KmeansProc() ;
    std::vector<cv::Mat> Image2Mat(std::vector<cv::Mat> images) ;
};

#undef KMEANS_H
#endif // KMEANS_H
