# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

Binary TTC: A Temporal Geofence for Autonomous Navigation

二進制 TTC：自主導航的時間地理圍欄

Abhishek Badki, Orazio Gallo, Jan Kautz, Pradeep Sen

1 NVIDIA

2 UC Santa Barbara 

CVPR 2021 Best Paper Candidate

https://arxiv.org/abs/2101.04777

https://github.com/NVlabs/BiTTC

https://www.youtube.com/watch?v=uUQJcjyerM4




Note

> 該篇為路經規劃的研究，即研究者提出一個新的方法，可以在 6.4 毫秒內提供一個 temporal geofence ，快過現今的方法 25 倍。
>
> 這當中的關鍵在於 接觸時間 (TTC; Time-to-contact)，即物體與觀察者平面碰撞的時間，是路徑規劃的強大工具，可以比影像場景中的深度、速度、加速度等給出更多的資訊。
> 
> 當然處理 TTC 有困難度，所以研究者使用更簡單的二元分類估計 TTC 來解決此困境。
> 
> 然後會用低延遲預測的方式，來判斷測觀察者是否會在特定時間內與障礙物發生碰撞，這通常比知道精確的每像素 TTC 更重要。


Abstract 摘要

Time-to-contact (TTC), the time for an object to collide with the observer’s plane, is a powerful tool for path planning:
接觸時間 (TTC)，即物體與觀察者平面碰撞的時間，是路徑規劃的強大工具：

it is potentially more informative than the depth, velocity, and acceleration of objects in the scene—even for humans.
它可能比場景中物體的深度、速度和加速度提供更多信息——即使對於人類也是如此。

TTC presents several advantages, including requiring only a monocular, uncalibrated camera. 
TTC 具有多種優勢，包括只需要一個單目、未校準的相機。

However, regressing TTC for each pixel is not straightforward, and most existing methods make over-simplifying assumptions about the scene. 
然而，回歸每個像素的 TTC 並不簡單，大多數現有方法對場景做出了過度簡化的假設。

We address this challenge by estimating TTC via a series of simpler, binary classifications. 
我們通過一系列更簡單的二元分類估計 TTC 來解決這一挑戰。

We predict with low latency whether the observer will collide with an obstacle within a certain time, which is often more critical than knowing exact, per-pixel TTC. 
我們以低延遲預測觀察者是否會在特定時間內與障礙物發生碰撞，這通常比知道精確的每像素 TTC 更重要。

For such scenarios, our method offers a temporal geofence in 6.4 ms—over 25faster than existing methods.
對於這種情況，我們的方法在 6.4 毫秒內提供了時間地理圍欄——比現有方法快 25 倍。

Our approach can also estimate per-pixel TTC with arbitrarily fine quantization (including continuous values), when the computational budget allows for it. 
當計算預算允許時，我們的方法還可以通過任意精細的量化（包括連續值）來估計每像素 TTC。

To the best of our knowledge, our method is the first to offer TTC information (binary or coarsely quantized) at sufficiently high frame-rates for practical use.
據我們所知，我們的方法是第一個以足夠高的幀速率提供 TTC 信息（二進製或粗量化）以供實際使用的方法。

This work was done while A. Badki was interning at NVIDIA.
這項工作是在 A. Badki 在 NVIDIA 實習期間完成的。

Project page: https://github.com/NVlabs/BiTTC



## CVPR 2021

https://cvpr2021.thecvf.com/node/290


