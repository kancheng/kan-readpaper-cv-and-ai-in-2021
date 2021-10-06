# kan-readpaper-homework
期刊閱讀筆記與作業

## 計算機視覺

Learning Calibrated Medical Image Segmentation via Multi-rater Agreement Modeling
通過多評估者協議建模學習校準的醫學圖像分割

Wei Ji, Shuang Yu, Junde Wu, Kai Ma, Cheng Bian, Qi Bi, Jingjing Li, Hanruo Liu, Li Cheng, Yefeng Zheng

1 Tencent Jarvis Lab, Shenzhen, China 
2 University of Alberta, Canada
3 Beijing Tongren Hospital, Capital Medical University, Beijing, China

{wji3, lcheng5}@ualberta.ca, {shirlyyu, kylekma, yefengzheng}@tencent.com


CVPR 2021 Best Paper Candidate
Paper(Best Paper Candidate): https://openaccess.thecvf.com/content/CVPR2021/html/Ji_Learning_Calibrated_Medical_Image_Segmentation_via_Multi-Rater_Agreement_Modeling_CVPR_2021_paper.html
Code: https://github.com/jiwei0921/MRNet/


Note

> 該研究為醫學圖像分割領域，研究者考量到在醫學圖像分析中，通常會收集來自不同的臨床專家或評估者們的多個註釋，希望能夠減少會發生的診斷錯誤。
>
> 但若從計算機視覺領域視角來說，多數決跟首選評估者是一種常見方法。同時此法又會省略這個過程中很多有價值的資訊。
> 
>所以研究者為了避免這個問題，他們提出一個所謂的多評價協議模型(ex-plicitly model the multi-rater (dis-)agreement)，該模型被稱之為 MR-Net。而從文獻中的圖 2 可以看到 MRNet 框架的組成與不同的模組。 
>
> 這個模型有兩大貢獻 :
>
> 其一是將各個評分者的傳業知識水平做成一個高級語意特徵 (high-level semantic features)的專業知識模組。
>
> 其二則是概略預測中重建多評分者的評分，將其利用提高表現。
>
> 該研究該網絡使用 PyTorch 平台實現，並在具有 24GB 記憶體的 Tesla P40 GPU 上進行訓練與測試。所有訓練和測試影像都被研究者統一調整為 256×256 像素的尺寸。而且可以在研究中的表 2中，看到實驗的 RIGA 測試，並在當中觀察到在不同專業水平和真實情況下，使用不同策略的定量結果。
>
> 這篇研究的價值在於是第一篇在不同專業水名下進行專業醫學圖像分割預測的工作(the first in producing cali-brated predictions under different expertise levels for medical image segmentatio)。
>
> 研究利用不同呈現的五個醫學分割的方式進行實驗，而且也驗證了該研究所提出的 MRNet，有其優越、有效性與適用性。


Abstract 摘要

In medical image analysis, it is typical to collect multiple annotations, each from a different clinical expert or rater, in the expectation that possible diagnostic errors could be mitigated. 
在醫學圖像分析中，通常會收集多個註釋，每個註釋來自不同的臨床專家或評估者，以期減少可能的診斷錯誤。

Meanwhile, from the computer vision practi-tioner viewpoint, it has been a common practice to adopt the ground-truth labels obtained via either the majority-vote or simply one annotation from a preferred rater. 
同時，從計算機視覺從業者的角度來看，採用通過多數票或來自首選評估者的簡單註釋獲得的真實標籤已成為一種常見做法。

This process, however, tends to overlook the rich information of agreement or disagreement ingrained in the raw multi-rater annotations.
然而，這個過程往往會忽略在原始多評估者註釋中根深蒂固的同意或不同意的豐富資訊。

To address this issue, we propose to ex-plicitly model the multi-rater (dis-)agreement, dubbed MR-Net, which has two main contributions.
為了解決這個問題，我們建議對多評價者（不）協議進行顯式建模，稱為 MR-Net，它有兩個主要貢獻。

First, an expertise-aware inferring module or EIM is devised to embed the expertise level of individual raters as prior knowledge, to form high-level semantic features. 
首先，設計了一個專業知識推斷模塊或 EIM，將各個評分者的專業知識水平作為先驗知識嵌入，以形成高級語義特徵。

Second, our approach is capable of reconstructing multi-rater gradings from coarse predictions, with the multi-rater (dis-)agreement cues being further exploited to improve the segmentation performance.
其次，我們的方法能夠從粗略預測中重建多評分者的評分，並進一步利用多評分者（不一致）線索來提高分割性能。

To our knowledge, our work is the first in producing cali-brated predictions under different expertise levels for medical image segmentation. 
據我們所知，我們的工作是第一個在不同專業水平下為醫學圖像分割生成校準預測的工作。

Extensive empirical experiments are conducted across five medical segmentation tasks of diverse imaging modalities.
在不同成像方式的五個醫學分割任務中進行了廣泛的實證實驗。

In these experiments, superior performance of our MRNet is observed comparing to the state-of-the-arts, indicating the effectiveness and applicability of our MRNet toward a wide range of medical segmentation tasks.
在這些實驗中，與現有技術相比，我們觀察到了我們的 MRNet 的優越性能，表明我們的 MRNet 對廣泛的醫學分割任務的有效性和適用性。

Source code is publicly available.



## CVPR 2021
https://cvpr2021.thecvf.com/node/290


