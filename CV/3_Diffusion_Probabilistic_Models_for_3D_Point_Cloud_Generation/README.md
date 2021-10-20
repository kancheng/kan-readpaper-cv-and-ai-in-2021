# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

Diffusion Probabilistic Models for 3D Point Cloud Generation
用於 3D 點雲生成的擴散概率模型

Shitong Luo, Wei Hu *
Wangxuan Institute of Computer Technology
Peking University
{luost, forhuwei}@pku.edu.cn

CVPR 2021 Best Paper Candidate
https://arxiv.org/abs/2103.01458



Note

> 該研究提出了一個用於點雲生成的概率模型(probabilistic model for point cloud generation)，負責各種如形狀完成、上採樣、合成和數據增強(shape completion, upsampling, synthesis and data augmentation)等 3D 視覺任務等的基礎。
>
> 該研究描述早期研究處理方式，同時研究者們受非平衡熱力學中擴散過程的啟發(the diffusion process in nonequilibrium thermodynamics)，然後他們將將點雲(point clouds)中的每一個點視為與熱浴接觸的熱力學系統中的粒子，使它們從原始分佈(original distribution)擴散到噪聲分佈(noise distribution)。
>
> 而這個點雲生成相當於是一個學習將噪聲分佈轉換為所需形狀分佈的反向擴散過程。具體來說，該研究建議將點雲的反向擴散過程建模為以特定形狀為條件的馬爾可夫鏈，同時研究推導出封閉形式的變分界用於訓練並提供模型的實現，並且研究者證明，其研究的模型在點雲生成和自動編碼方面取得很好的效能。
>


Abstract 摘要

We present a probabilistic model for point cloud generation, which is fundamental for various 3D vision tasks such as shape completion, upsampling, synthesis and data augmentation. 
我們提出了一個用於點雲生成的概率模型，它是各種 3D 視覺任務（例如形狀完成、上採樣、合成和數據增強）的基礎。

Inspired by the diffusion process in nonequilibrium thermodynamics, we view points in point clouds as particles in a thermodynamic system in contact with a heat bath, which diffuse from the original distribution to a noise distribution.
受非平衡熱力學中擴散過程的啟發，我們將點雲中的點視為與熱浴接觸的熱力學系統中的粒子，它們從原始分佈擴散到噪聲分佈。

Point cloud generation thus amounts to learning the reverse diffusion process that transforms the noise distribution to the distribution of a desired shape. 
因此，點雲生成相當於學習將噪聲分佈轉換為所需形狀分佈的反向擴散過程。

Specifically, we propose to model the reverse diffusion process for point clouds as a Markov chain conditioned on certain shape latent. 
具體來說，我們建議將點雲的反向擴散過程建模為以特定形狀為條件的馬爾可夫鏈。

We derive the variational bound in closed form for training and provide implementations of the model. 
我們推導出封閉形式的變分界用於訓練並提供模型的實現。

Experimental results demonstrate that our model achieves competitive performance in point cloud generation and auto-encoding. 
實驗結果表明，我們的模型在點雲生成和自動編碼方面取得了有競爭力的性能。

The code is available at https://github.com/luost26/diffusionpoint-cloud.

https://github.com/luost26/diffusion-point-cloud


## CVPR 2021
https://cvpr2021.thecvf.com/node/290


