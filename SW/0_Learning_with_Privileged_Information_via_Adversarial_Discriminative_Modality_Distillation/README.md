# kan-readpaper-homework

期刊閱讀筆記與作業

## 科技論文寫作 Scientific Writing

1. IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) (SCI IF 16.389), 2021

2. IEEE Journal on Selected Areas in Communications (SCI IF 9.114), 2021

## Note

> IMRAD - Introduction, Methods, Results And Discussion

### Introduction

### Methods

### Results

### Discussion


## About

Learning with Privileged Information via Adversarial Discriminative Modality Distillation

通過對抗性判別模態蒸餾(Adversarial Discriminative Modality Distillation) 學習特權資訊 (Privileged Information)

Nuno C. Garcia, Pietro Morerio, and Vittorio Murino, Senior Member, IEEE


https://arxiv.org/abs/1810.08437

Comments: Accepted to IEEE Transactions on Pattern Analysis and Machine Intelligence

Subjects:	Computer Vision and Pattern Recognition (cs.CV)


https://ieeexplore.ieee.org/document/8764498

Published in: IEEE Transactions on Pattern Analysis and Machine Intelligence ( Volume: 42, Issue: 10, Oct. 1 2020)

Page(s): 2581 - 2593

Date of Publication: 16 July 2019 

ISSN Information:

 - Print ISSN: 0162-8828

 - CD: 2160-9292

 - Electronic ISSN: 1939-3539

PubMed ID: 31331879

INSPEC Accession Number: 19931889

DOI: 10.1109/TPAMI.2019.2929038

Publisher: IEEE



## Code

Code is available at
https://github.com/pmorerio/admd


## Abstract 摘要

Heterogeneous data modalities can provide complementary cues for several tasks, usually leading to more robust algorithms and better performance. 

異構資料模式可以為多個任務提供補充線索，通常會導致更強大的演算法和更好的性能。

However, while training data can be accurately collected to include a variety of sensory modalities, it is often the case that not all of them are available in real life (testing) scenarios, where a model has to be deployed. 

然而，雖然可以準確地收集訓練資料以包括各種感官模式，但在現實生活（測試）場景中，通常情況下並非所有這些都可用，在這些場景中必須部署模型。

This raises the challenge of how to extract information from multimodal data in the training stage, in a form that can be exploited at test time, considering limitations such as noisy or missing modalities. 

這對來自訓練階段的多模態資料中如何提出訊息提出了挑戰，以一種可以在測試時利用的形式，考慮到諸如嘈雜或缺失模態等限制。

This paper presents a new approach in this direction for RGB-D vision tasks, developed within the adversarial learning and privileged information frameworks. 

本文提出了一種針對 RGB-D 視覺任務的新方法，該方法是在對抗性學習和特權資訊框架內開發的。

We consider the practical case of learning representations from depth and RGB videos, while relying only on RGB data at test time. 

我們考慮從深度和 RGB 影像中學習表示的實際案例，而在測試時僅依賴於 RGB 資料。

We propose a new approach to train a hallucination network that learns to distill depth information via adversarial learning, resulting in a clean approach without several losses to balance or hyperparameters. 

我們提出了一種訓練幻覺網絡的新方法，該方法通過對抗性學習來學習提取深度資訊，從而產生一種乾淨的方法，而不會出現一些平衡或超參數損失。

We report state-of-the-art results for object classification on the NYUD dataset, and video action recognition on the largest multimodal dataset available for this task, the NTU RGB+D, as well as on the Northwestern-UCLA.

我們報告了 NYUD 資料集上對象分類的最新結果，以及可用於此任務的最大多模式資料集 NTU RGB+D 以及 Northwestern-UCLA 上的影像動作識別結果。

Index Terms—Multimodal deep learning, adversarial learning, privileged information, network distillation, modality hallucination.
