# Different interpolation methods for audio restoration

## High-level Description of the project

This assignment builds on Assignment 2. We want to detect an image frontground and background by using trimap.

---

## Installation and Execution                 
```
numpy==1.20.3
opencv_python==4.7.0.72
Pillow==9.4.0
scipy==1.7.1
```

Afer installing all required packages you can run the demo file simply by typing:

`python main.py`

If you need to run the end to end result, you can run test by typing:

`python e2e_Laplacian.py`



## Methodology and Results
**Methodology**
1. Median filtering: 

2. Cubic Spline: 

3. Unit test：

    
    You can clicking this link to see:[unit test](unit_test/test.py)

**Results**

1. 

|**b for 2*n+b**| **MSE** |
|---------|---------------|


<div align=center>
<img src="co.png" width="750">
</div>

1. The original audio signal with clicks and clean audio signal show like this:
<div align=center>
<img src="cl+de.png" width="750" >
</div>



The restored waveform with the optimal filter length is given below:

<div align=center>
<img src="me.png" width="750">
</div>

Using the cubic splines, we observe the restored waveform with the optimal filter length is given below:

<div align=center>
<img src="cu.png" width="750">
</div>

1. 

---
## Credits

This code was developed for purely academic purposes by Xiaoru Liu (github name: XiyunYue) as part of the module EEP55C22-202223: COMPUTATIONAL METHODS.

https://github.com/XiyunYue/computational_lab/tree/main/assignment2_fin