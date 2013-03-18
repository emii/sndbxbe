Date: 2013-01-30
Title: Tissue Segmentation using Voronoi tesselation
Summary: An attempt for tissue segmentation using bounded triangulations in MATLAB 
Abstract: Tissue segmentation of single cells is a hard problem to solve by automatic procedures (i.e. watershed and level set methods), here I use semi-automatic segmentation using Delaunay triangulations of manually selected points corresponding to single cells which  
Tags: matlab, image processing
Category: experiments

##Main code##########
	
	:::matlab
	%select the slice for the dapi and edge info

	sliceno=18;


	%Reading the files for the image stacks

	%EDGE
	filename='ch2_02.tif';
	info=imfinfo(filename);
	ims=double(parse_stack(filename,1,numel(info)));
	h=-utilities.fspecial3('log',[15 15 11],[1.3,1.3,1.1]);
	ims=imfilter(ims,h,'replicate');
	im=ims(:,:,sliceno);
	im=im/max(im(:));

	%DAPI
	filename='ch3_02.tif';
	info=imfinfo(filename);
	ims=double(parse_stack(filename,sliceno,sliceno));
	ims=ims/max(ims(:));


	%DOTS
	filename='ch1_02.tif';
	info=imfinfo(filename);
	ims2=double(parse_stack(filename,1,numel(info)));
	ims2=imfilter(ims2,h,'replicate');
	ims2=zproject(ims2);
	ims2=ims2/max(ims2(:));

##Viewing the image overlay###

	:::matlab
	m=zeros(size(ims,1),size(ims,2),3);
	m(:,:,2)=im;
	m(:,:,3)=ims;
	m(:,:,1)=ims2;

	h=utilities.im(m);