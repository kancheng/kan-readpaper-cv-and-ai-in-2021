# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

PoseAug: A Differentiable Pose Augmentation Framework for 3D Human Pose Estimation

PoseAug：用於 3D 人體姿勢估計的可微姿勢增強框架

Kehong Gong, Jianfeng Zhang, Jiashi Feng

National University of Singapore

CVPR 2021 Best Paper Candidate
https://arxiv.org/abs/2105.02465

https://github.com/jfzhang95/PoseAug



Note

> 就研究結果而言 PoseAug 一種即將出現的估計數據增強方法，在場景內和跨場景數據集上都帶來了明顯的用法。舉例來說，在跨數據集評估設置下，它在 MPI-INF-3DHP 上實現了 88.6 % 的 3D PCK，比之前的最佳方法提高了 9.1%。
> 
>　因為目前研究中的3D 人體姿態估計器對新數據集的泛化性能較差，這主要原因是訓練數據中 2D-3D 姿態對的多樣性有限。
>
>　為了面對此問題，研究者提出了一個名為 PoseAug 的自動增強框架，此框架可以學習更多可用的訓練姿勢，並增加到更多動作的多樣性，從而提高經過訓練的 2D 到 3D 姿勢估計器的性能。
>
> 簡單來說，這個名為 PoseAug 使用一種新穎的姿勢增強器，這個增強器可以通過可微分操作來學習調整姿勢的各種幾何因素（例如，姿勢、身體大小、視點和位置）。
>
> 再有這個優勢的情況下，增強器可以與 3D 姿態估計器一起最佳化成果，並將估計誤差反饋回來，好用在線方式生成更多樣和更複雜的姿態與動作。


Abstract 摘要

Existing 3D human pose estimators suffer poor generalization performance to new datasets, largely due to the limited diversity of 2D-3D pose pairs in the training data.
現有的 3D 人體姿態估計器對新數據集的泛化性能較差，這主要是由於訓練數據中 2D-3D 姿態對的多樣性有限。

To address this problem, we present PoseAug, a new autoaugmentation framework that learns to augment the available training poses towards a greater diversity and thus improve generalization of the trained 2D-to-3D pose estimator.
為了解決這個問題，我們提出了 PoseAug，這是一種新的自動增強框架，它可以學習將可用的訓練姿勢增加到更大的多樣性，從而提高經過訓練的 2D 到 3D 姿勢估計器的泛化。

Specifically, PoseAug introduces a novel pose augmentor that learns to adjust various geometry factors (e.g., posture, body size, view point and position) of a pose through differentiable operations. 
具體來說，PoseAug 引入了一種新穎的姿勢增強器，它可以通過可微分操作來學習調整姿勢的各種幾何因素（例如，姿勢、身體大小、視點和位置）。

With such differentiable capacity, the augmentor can be jointly optimized with the 3D pose estimator and take the estimation error as feedback to generate more diverse and harder poses in an online manner.
有了這種可區分的容量，增強器可以與 3D 姿態估計器聯合優化，並將估計誤差作為反饋，以在線方式生成更多樣和更難的姿態。

Moreover, PoseAug introduces a novel part-aware Kinematic Chain Space for evaluating local joint-angle plausibility and develops a discriminative module accordingly to ensure the plausibility of the augmented poses. 
此外，PoseAug 引入了一種新穎的部分感知運動鏈空間來評估局部關節角度的合理性，並相應地開發了一個判別模塊以確保增強姿勢的合理性。

These elaborate designs enable PoseAug to generate more diverse yet plausible poses than existing offline augmentation methods, and thus yield better generalization of the pose estimator.
這些精心設計的設計使 PoseAug 能夠生成比現有離線增強方法更多樣化但更合理的姿勢，從而更好地泛化姿勢估計器。

PoseAug is generic and easy to be applied to various 3D pose estimators. 
PoseAug 是通用的，易於應用於各種 3D 姿勢估計器。

Extensive experiments demonstrate that PoseAug brings clear improvements on both intra-scenario and cross-scenario datasets. 
大量實驗表明，PoseAug 在場景內和跨場景數據集上都帶來了明顯的改進。

Notably, it achieves 88.6% 3D PCK on MPI-INF-3DHP under cross-dataset evaluation setup, improving upon the previous best data augmentation based method [22] by 9.1%. 
值得注意的是，它在跨數據集評估設置下在 MPI-INF-3DHP 上實現了 88.6% 的 3D PCK，比之前基於數據增強的最佳方法 [22] 提高了 9.1%。

Code can be found at: https://github.com/jfzhang95/PoseAug.



## CVPR 2021

https://cvpr2021.thecvf.com/node/290


