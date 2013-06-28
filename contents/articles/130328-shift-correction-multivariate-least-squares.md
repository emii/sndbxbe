Title: Shift correction by fitting a least-squares polynomial
Summary: How to solve the problem of the chromatic shift by fitting a polynomial z(x,y)
Abstract: From the image data of fluorescent beads we can estimate the shift (z) depending on the x,y position, like-wise we can estimate the shift w, from its x,y,z position?
Category: projects
Tags: biology, research, hd dna-fish, MATLAB, fitting, image processing
Date: 2013-03-28

## Various useful concepts:

* least squares

## Splines

In mathematics, a spline is a sufficiently smooth polynomial function that is piecewise-defined, and possesses a high degree of smoothness at the places where the polynomial pieces connect (which are known as knots).

## Matrix Decomposition

In the mathematical discipline of linear algebra, a matrix decomposition is a factorization of a matrix into a product of matrices. There are many different matrix decompositions; each finds use among a particular class of problems. They are used tosolve systems of linear equations


## Multivariate polynomial

\\begin{equation}
	P(x,y) = a_{22}x^2y^2 + a_{21}x^2y + a_{12}xy^2 + a_{11}xy + a_{10}x + a_{01}y + a_{00}
\\end{equation}


\\begin{equation\*}
	P(x,y) = a_{n,n}x^ny^n + a_{n,n-1}x^ny^{n-1} + a_{n-1,n}x^{n-1}y^n + \ldots + a_{1,0}x + a_{0,1}y + a_{0,0}
\\end{equation\*}

Searching in internet I found a couple of aproximations to the problem of fitting a function of the type $z = f(x,y)$, like the following:

## Some ramdom PDFs

* [this thesis](http://perso.ensg.ign.fr/mambap-fokouong/cours_lidar/doc_biblio/articles/georef/92.pdf)
* [this other script](http://www.geometrictools.com/Documentation/LeastSquaresFitting.pdf)
* [this article](http://www2.isikun.edu.tr/personel/akca/devrim/2005__ls3d_isprsj59_3.pdf)

## Some discussion threads

* [this discussion](http://www.mathworks.com/matlabcentral/newsreader/view_thread/76384)
* [this thread](http://www.mathworks.com/matlabcentral/newsreader/view_thread/134076)
* [This other thread2](http://www.mathworks.com/matlabcentral/newsreader/view_thread/166596)

## From MATLAB central

* [here1](http://www.mathworks.com/matlabcentral/fileexchange/26336-two-dimensional-surface-fitting-program/content/fit2.m) by using nlinfit
* [here2](http://www.mathworks.com/matlabcentral/fileexchange/24062-3d-least-squares-polynomial-fit-in-x-and-y/content/least_square_polyfit_xyz.m) by decomposition
* [other script](http://www.mathworks.com/matlabcentral/fileexchange/22865-general-least-squares-regression) Multi Dimensional Multivariable Least Squares Regression
* [the one Stefan uses](http://www.mathworks.com/matlabcentral/fileexchange/13719-2d-weighted-polynomial-fitting-and-evaluation/content/polyfitweighted2/polyfitweighted2.m) using decomposition
* [this 4th script](http://www.mathworks.com/matlabcentral/fileexchange/34918-multivariable-polynomial-regression) using regress
* [apparently the one i am going to use](http://www.mathworks.com/matlabcentral/fileexchange/34765-polyfitn/content/PolyfitnTools/polyfitn.m) also by QR decomposition
* [and one also from the previous author](http://www.mathworks.com/matlabcentral/fileexchange/8998-surface-fitting-using-gridfit)

## Built-in MATLAB functions

* [TriScatteredInterp](http://www.mathworks.nl/help/matlab/ref/triscatteredinterp.html)
* [griddata](http://www.mathworks.nl/help/matlab/ref/griddata.html)
* [fit](http://www.mathworks.nl/help/curvefit/fit.html)
	* Visualization
		* [quiver](http://www.mathworks.nl/help/matlab/ref/quiver.html)
		* [quiver3D](https://www.mathworks.com/matlabcentral/fileexchange/28211-quiver3dpatch)
		* [examples](http://www2.math.umd.edu/~immortal/241spring13/matlab/matlab3.html)
		* [slice](http://www.mathworks.nl/help/matlab/ref/slice.html)
* [interp2](http://www.mathworks.nl/help/matlab/ref/interp2.html)
* [interp3](http://www.mathworks.nl/help/matlab/ref/interp3.html)
* [interpn](http://www.mathworks.nl/help/matlab/ref/interpn.html)
* [using curve fitting toolbox](http://www.mathworks.nl/help/curvefit/example-interactive-surface-fitting.html)
* [nlinfit](http://www.mathworks.nl/help/stats/nlinfit.html)
* [interp scattered data](http://www.mathworks.nl/help/matlab/math/interpolating-scattered-data.html)


## Other random scripts

* [this m script](http://www.ime.usp.br/~rt/mmfina/POLYFIT2.M) by using decomposition

## Some material to understand multivariate polynomial interpolation

* [here](https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/05Interpolation/)

## google seaches

* matlab fit function f(x,y,z) 
