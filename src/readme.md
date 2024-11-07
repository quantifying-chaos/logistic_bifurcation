# Calculate delta_hat

The key is to find the point r_n such that the bifurcation occurs. 

## Method 1: point of non-differentiability in the graph of standard deviation  

Means and standard deviations. 

When bifurcation occurs, the standard deviation of x is likely to change rapidly.

If we plot r versus standard deviation of x, we should see a sharp change at the bifurcation point (point of non differentiability).

## Box Counting

Just count the box (like a histogram).

TODO: use [mpmath](https://mpmath.org/doc/current/mpmath.pdf) package for higher precision. 

## The A_i values

The A_i values for logistic function (the points of superstability) are 

```python
A_List = [2, 3.23606797749979, 3.4985479775008543, 3.554637435512696, 3.5666663858959753, 3.569243282100676, 3.569795227423478, 3.5699134489582596, 3.5699387708186654, 3.5699441935758296, 3.5699453551991143]
```
