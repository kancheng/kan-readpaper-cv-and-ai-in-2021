# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

Task Programming: Learning Data Efficient Behavior Representations
任務編程：學習數據高效行為表徵

Jennifer J. Sun, Ann Kennedy, Eric Zhan, David J. Anderson, Yisong Yue, Pietro Perona

Caltech 
Northwestern University

CVPR 2021 Best Paper Candidate
https://arxiv.org/abs/2011.13917
Comments: To appear in as an Oral in CVPR 2021.
Code & Project Website: https://sites.google.com/view/task-programming

## Links

https://github.com/neuroethology/TREBA

https://sites.google.com/view/task-programming

https://arxiv.org/abs/2011.13917


Note

> 研究團隊為減少標註工作量，提出一個名為 TREBA 的一種基於多任務自監督學習(multi-task self-supervised learning)的學習註釋樣本有效軌跡嵌入以進行行為分析的方法(a method to learn annotation-sample efficient trajectory embedding for behavior analysis)。
>
> 研究團隊之所以會提出此方法，因為專業領域知識通常是需要準確註釋訓練集以進行深入分析，但從該領域專家那裡獲取的過程，有可能既繁瑣又耗時，為了要降低人工等工作量而提出。
>
> 這些工作多像是在自動化行為分析的過程中，從影像與跟蹤數據去尋找 agent 的移動或者想要找出感興趣的動作。
> 
> 我們方法中的任務可以由領域專家通過我們稱為“任務編程”的過程有效地設計，該過程使用程序對領域專家的結構化知識進行顯式編碼。
>
> 通過為構建少量編程任務交換數據註釋時間，可以減少領域專家的總工作量。
>
> 我們使用來自行為神經科學的數據來評估這種權衡，其中使用專門的領域知識來識別行為。
>
> 團隊在其在兩個領域的三個數據集中進行實驗，而研究結果實際的呈現，為小鼠的標註減少 10 倍，果蠅標註減少 2 倍。
> 
> 而這些成果與目前方法的特徵相比，將註釋負擔減少了 10 倍，也證明任務編程和自我監督可以成為減少領域專家註釋工作的有效方法。


Abstract 摘要

Specialized domain knowledge is often necessary to accurately annotate training sets for in-depth analysis, but can be burdensome and time-consuming to acquire from domain experts.
專業領域知識通常是準確註釋訓練集以進行深入分析所必需的，但從領域專家那裡獲取可能既繁瑣又耗時。

This issue arises prominently in automated behavior analysis, in which agent movements or actions of interest are detected from video tracking data.
這個問題在自動化行為分析中尤為突出，其中從視頻跟踪數據中檢測到代理移動或感興趣的動作。

To reduce annotation effort, we present TREBA: a method to learn annotation-sample efficient trajectory embedding for behavior analysis, based on multi-task self-supervised learning.
為了減少註釋工作，我們提出了 TREBA：一種基於多任務自監督學習學習註釋樣本有效軌跡嵌入以進行行為分析的方法。

The tasks in our method can be efficiently engineered by domain experts through a process we call “task programming”, which uses programs to explicitly encode structured knowledge from domain experts. 
我們方法中的任務可以由領域專家通過我們稱為“任務編程”的過程有效地設計，該過程使用程序對領域專家的結構化知識進行顯式編碼。

Total domain expert effort can be reduced by exchanging data annotation time for the construction of a small number of programmed tasks. 
通過為構建少量編程任務交換數據註釋時間，可以減少領域專家的總工作量。

We evaluate this trade-off using data from behavioral neuroscience, in which specialized domain knowledge is used to identify behaviors. 
我們使用來自行為神經科學的數據來評估這種權衡，其中使用專門的領域知識來識別行為。

We present experimental results in three datasets across two domains: mice and fruit flies. 
我們在兩個領域的三個數據集中展示了實驗結果：小鼠和果蠅。

Using embeddings from TREBA, we reduce annotation burden by up to a factor of 10 without compromising accuracy compared to state-of-the-art features.
使用來自 TREBA 的嵌入，與最先進的特徵相比，我們在不影響準確性的情況下將註釋負擔減少了 10 倍。

Our results thus suggest that task programming and self-supervision can be an effective way to reduce annotation effort for domain experts.
因此，我們的結果表明，任務編程和自我監督可以成為減少領域專家註釋工作的有效方法。



## CVPR 2021

https://cvpr2021.thecvf.com/node/290


