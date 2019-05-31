# railsreactor-mlschool-test-task
Test task for Rails Reactor ML Summer School by Andrii Pavlenko
In this task i used color histograms of images to find similarity.
color_histogram.py gets a normalized histogram for each image and calculates Chebyshev distance for similarity.
Results tested on 64-bit Windows 7 on Python 3.7.3 shown in the png screenshot.
I also tried a different approach using Complex Wavelet Structural Similarity Index Method
https://en.wikipedia.org/wiki/Structural_similarity#Complex_Wavelet_SSIM
It doesnt't work at the moment, although it should be more accurate. The problem I've experienced is that it gives every pair a score of 1 and I haven't figured out why yet.
