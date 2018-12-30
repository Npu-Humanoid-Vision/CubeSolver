#ifndef FATHER_H
#define FATHER_H

#include <bits/stdc++.h>
#include <opencv2/opencv.hpp>
using namespace std;

class FatherProc {
public:
    virtual std::vector<cv::Mat> Image2Mat(std::vector<cv::Mat> images) = 0;
};

#undef FATHER_H
#endif