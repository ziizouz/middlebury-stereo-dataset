# MiddleBury Stereo dataset manipulator
Small python script that downloads middlebury stereo dataset 2014, converts PFM file to PNG. Then, it saves gray and depth into 2 pickles for later use with Tensorflow


http://vision.middlebury.edu/stereo/data/

### Prerequisites

```
Linux or Debian OS
```

```
Pickle
openCV
imagemagick
```

## Running the tests


```
python3 dataset_maker.py
```

## References

* [Middlebury dataset](http://vision.middlebury.edu/stereo/data/) - Middlebury stereo dataset
* [Middlebury dataset papers](http://vision.middlebury.edu/stereo/taxonomy-IJCV.pdf) - [1] D. Scharstein and R. Szeliski. A taxonomy and evaluation of dense two-frame stereo correspondence algorithms.
International Journal of Computer Vision, 47(1/2/3):7-42, April-June 2002.
* [Middlebury dataset papers](http://www.cs.middlebury.edu/~schar/papers/structlight/) - [2]	D. Scharstein and R. Szeliski. High-accuracy stereo depth maps using structured light.
In IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2003), volume 1, pages 195-202, Madison, WI, June 2003.
* [Middlebury dataset papers](http://www.cs.middlebury.edu/~schar/papers/LearnCRFstereo_cvpr07.pdf) - [3]	D. Scharstein and C. Pal. Learning conditional random fields for stereo.
In IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2007), Minneapolis, MN, June 2007.
* [Middlebury dataset papers](http://www.cs.middlebury.edu/~schar/papers/evalCosts_cvpr07.pdf) - [4]	H. Hirschmüller and D. Scharstein. Evaluation of cost functions for stereo matching.
In IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2007), Minneapolis, MN, June 2007.
* [Middlebury dataset papers](http://www.cs.middlebury.edu/~schar/papers/datasets-gcpr2014.pdf) - [5]	D. Scharstein, H. Hirschmüller, Y. Kitajima, G. Krathwohl, N. Nesic, X. Wang, and P. Westling. High-resolution stereo datasets with subpixel-accurate ground truth.
In German Conference on Pattern Recognition (GCPR 2014), Münster, Germany, September 2014.


## License
Check [Middleburry dataset](http://vision.middlebury.edu/stereo/data/) - License
