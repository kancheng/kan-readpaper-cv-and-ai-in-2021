# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

Privacy-Preserving Image Features via Adversarial Affine Subspace Embeddings
通過對抗仿射子空間嵌入保護隱私的圖像特徵

Mihai Dusmanu, Johannes L. Schönberger, Sudipta N. Sinha, Marc Pollefeys

1 Department of Computer Science, ETH Zürich 
2 Microsoft

https://arxiv.org/abs/2006.06634
CVPR 2021 Best Paper Candidate


Note

> 該篇研究是想要運用機算計視覺領域來保護個人隱私，簡單來說就是保護隱私的機器學習系統。因為計算機視覺系統需要使用者將自身的圖像特徵上傳到雲端進行處理和存放。
> 
> 研究團隊提出一個新的保護隱私的特徵方式(a new privacy-preserving feature representation)，也就是文中所說的 "the idea of lifting and the technique for matching lifted features"，概念是將每個 feature descriptor 塞進 original feature 和 adversarial feature samples 來刪除 drop constraints，用來預防隱私攻擊跟個人隱私保護上。
> 
> 研究者通過實驗證明他們發方法在視覺、人臉認證應用的有效性，而且讓人想要恢復個人隱私資訊會更困難。
> 
> 研究者使用 Aachen Day-Night long-term visual localization dataset 進行測試，同時也可從該研究的 Figure 3 看到影像重建的品質呈現。

Abstract 摘要

Many computer vision systems require users to upload image features to the cloud for processing and storage. 
許多計算機視覺系統需要用戶將圖像特徵上傳到雲端進行處理和存儲。

These features can be exploited to recover sensitive information about the scene or subjects, e.g., by reconstructing the appearance of the original image. 
可以利用這些特徵來恢復有關場景或主題的敏感信息，例如，通過重建原始圖像的外觀。

To address this privacy concern, we propose a new privacy-preserving feature representation.
為了解決這個隱私問題，我們提出了一種新的隱私保護特徵表示。

The core idea of our work is to drop constraints from each feature descriptor by embedding it within an affine subspace containing the original feature as well as adversarial feature samples. 
我們工作的核心思想是通過將每個特徵描述符嵌入到包含原始特徵和對抗性特徵樣本的仿射子空間中來刪除每個特徵描述符的約束。

Feature matching on the privacy preserving representation is enabled based on the notion of subspace-to-subspace distance. 
基於子空間到子空間距離的概念啟用隱私保護表示上的特徵匹配。

We experimentally demonstrate the effectiveness of our method and its high practical relevance for the applications of visual localization and mapping as well as face authentication. 
我們通過實驗證明了我們的方法的有效性及其與視覺定位和映射以及人臉認證應用的高度實際相關性。

Compared to the original features, our approach makes it significantly more difficult for an adversary to recover private information.
與原始特徵相比，我們的方法使對手恢復私人資訊得更加困難。




## CVPR 2021
https://cvpr2021.thecvf.com/node/290


