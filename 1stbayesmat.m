  clc
clear all
close all

% BAYESMAT  Calculates alpha matting for the given image and trimap.

im=imread('lighthouse input.png');
trimap=imread('lighthouse trimap.png');

p=makeParameters;
%function [F,B,alpha]=bayesmat(im,trimap,p)
im=im2double(im);
trimap=im2double(trimap);


bgmask=trimap==0; % background region mask
fgmask=trimap==1; % foreground region mask
unkmask=~bgmask&~fgmask; % unknow region mask

% initialize F,B,alpha
F=im; F(repmat(~fgmask,[1,1,3]))=0;
B=im; B(repmat(~bgmask,[1,1,3]))=0;

alpha=zeros(size(trimap));
alpha(fgmask)=1;
alpha(unkmask)=NaN;

nUnknown=sum(unkmask(:)); 

% guassian falloff. will be used for weighting each pixel neighborhood
g=fspecial('gaussian', p.N, p.sigma); g=g/max(g(:));

% square structuring element for eroding the unknown region(s)
se=strel('square',3);

n=1;
unkreg=unkmask;
aa = 0; cc = 0;

while n<nUnknown
    % get unknown pixels to process at this iteration
    unkreg=imerode(unkreg,se);
    unkpixels=~unkreg&unkmask;
    [Y,X]=find(unkpixels); 

    for i=1:length(Y)
        
        % report progress
        if mod(n,50)==0
            if p.guiMode
                stop=progressbar(n/nUnknown);
                if stop
                    return;
                end
            else
                fprintf('processing %d/%d\n',n,nUnknown);
            end
        end
        
        % take current pixel
        x=X(i); y=Y(i);
        
%         if X(i)== X(i-1) && Y(i) == Y(i-1)
%             x = X(i+1) ;
%             y = Y(i+1) ;
%         end

        c = reshape(im(y,x,:),[3,1]);

        % take surrounding alpha values
        a=getN(alpha,x,y,p.N);
        
        % take surrounding foreground pixels
        f_pixels=getN(F,x,y,p.N);
        f_weights=(a.^2).*g;
        f_pixels=reshape(f_pixels,p.N*p.N,3);
        f_pixels=f_pixels(f_weights>0,:);
        f_weights=f_weights(f_weights>0);
        
        % take surrounding background pixels
        b_pixels=getN(B,x,y,p.N);
        b_weights=((1-a).^2).*g;
        b_pixels=reshape(b_pixels,p.N*p.N,3);
        b_pixels=b_pixels(b_weights>0,:);
        b_weights=b_weights(b_weights>0);
        

        % if not enough data, return to it later...
%         if (aa < 250000)
%          if n<nUnknown-500
%              if length(X)>p.minN || length(Y)>p.minN
%             if length(f_weights)<p.minN || length(b_weights)<p.minN
%                 aa = aa + 1;
%                 continue;
%            else 
%             end
%             end
%         end
%          end
        
        % partition foreground and background pixels to clusters (in a
        % weighted manner)
        [mu_f,Sigma_f]=p.clustFunc(f_pixels,f_weights,p.clust.minVar);
        [mu_b,Sigma_b]=p.clustFunc(b_pixels,b_weights,p.clust.minVar);
        
        % update covariances with camera variance, as mentioned in their
        % addendum
        Sigma_f=addCamVar(Sigma_f,p.sigma_C);
        Sigma_b=addCamVar(Sigma_b,p.sigma_C);
        
        % set initial alpha value to mean of surrounding pixels
        alpha_init=nanmean(a(:));
        
        % solve for current pixel
        [f,b,a]=solve(mu_f,Sigma_f,mu_b,Sigma_b,c,p.sigma_C,alpha_init,p.opt.maxIter,p.opt.minLike);
        
        F(y,x,:)=f;
        B(y,x,:)=b;
        alpha(y,x)=a;
        unkmask(y,x)=0; % remove from unkowns
        cc = cc + 1;
        n=n+1;
    end
end

% release progress bar
if p.guiMode
    progressbar(1);
end


figure;
imshow(im);
title('Input');

figure;
imshow(trimap);
title('Trimap');

figure;
imshow(alpha);
title('Alpha');

% retruns the surrounding N-rectangular neighborhood of matrix m, centered
% at pixel (x,y) 
function r=getN(m,x,y,N)

[h,w,c]=size(m);
halfN = floor(N/2);
n1=halfN; n2=N-halfN-1;
r=nan(N,N,c);
xmin=max(1,x-n1);
xmax=min(w,x+n2);
ymin=max(1,y-n1);
ymax=min(h,y+n2);
pxmin=halfN-(x-xmin)+1; pxmax=halfN+(xmax-x)+1;
pymin=halfN-(y-ymin)+1; pymax=halfN+(ymax-y)+1;
r(pymin:pymax,pxmin:pxmax,:)=m(ymin:ymax,xmin:xmax,:);
end
% finds the orientation of the covariance matrices, and adds the camera
% variance to each axis
function Sigma=addCamVar(Sigma,sigma_C)

Sigma=zeros(size(Sigma));
for i=1:size(Sigma,3)
    Sigma_i=Sigma(:,:,i);
    [U,S,V]=svd(Sigma_i);
    Sp=S+diag([sigma_C^2,sigma_C^2,sigma_C^2]);
    Sigma(:,:,i)=U*Sp*V';
end
end
% end