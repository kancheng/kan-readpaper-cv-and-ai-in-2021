# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

On Self-Contact and Human Pose

關於自我接觸和人體姿勢

Lea Müller, Ahmed A. A. Osman, Siyu Tang, Chun-Hao P. Huang, Michael J. Black

Max Planck Institute for Intelligent Systems, Tubingen

ETH Zurich

{lea.mueller, ahmed.osman, stang, paul.huang, black}@tuebingen.mpg.de

https://arxiv.org/abs/2104.03176

https://tuch.is.tue.mpg.de/




Note

> 此研究針對人體姿態估計去進行突破，研究團隊做了一個新的 3D 數據集，還面對 3D 掃描的過程中複雜的肢體接觸，因為目前的方法很難去估計這個領域，同時該團隊也提出一個新的優化方法，可以讓 3D 人體更接近真實人的姿勢。
> 
> 同時研究者們所做的數據集，還用來訓練一個新的名為 Towards Understanding Contact in Humans(TUCH) 的 3D 人體姿勢回歸器(3D human pose regressor)。
>
> 就研究結果來說，該研究讓改善了自接觸姿勢的結果，而且還提高了非接觸姿勢的準確性。


Abstract 摘要

People touch their face 23 times an hour, they cross their arms and legs, put their hands on their hips, etc.
人們每小時摸臉 23 次，他們交叉雙臂和雙腿，把手放在臀部等。

While many images of people contain some form of selfcontact, current 3D human pose and shape (HPS) regression methods typically fail to estimate this contact. 
雖然許多人的圖像包含某種形式的自我接觸，但當前的 3D 人體姿勢和形狀 (HPS) 回歸方法通常無法估計這種接觸。

To address this, we develop new datasets and methods that significantly improve human pose estimation with self-contact.
為了解決這個問題，我們開發了新的數據集和方法，通過自我接觸顯著改善人體姿勢估計。

First, we create a dataset of 3D Contact Poses (3DCP) containing SMPL-X bodies fit to 3D scans as well as poses from AMASS, which we refine to ensure good contact. 
首先，我們創建了一個 3D 接觸姿勢 (3DCP) 數據集，其中包含適合 3D 掃描的 SMPL-X 身體以及來自 AMASS 的姿勢，我們對其進行改進以確保良好的接觸。

Second, we leverage this to create the Mimic-The-Pose (MTP) dataset of images, collected via Amazon Mechanical Turk, containing people mimicking the 3DCP poses with selfcontact.
其次，我們利用它來創建通過 Amazon Mechanical Turk 收集的 Mimic-The-Pose (MTP) 圖像數據集，其中包含通過自我接觸模仿 3DCP 姿勢的人。

Third, we develop a novel HPS optimization method, SMPLify-XMC, that includes contact constraints and uses the known 3DCP body pose during fitting to create near ground-truth poses for MTP images. 
第三，我們開發了一種新穎的 HPS 優化方法 SMPLify-XMC，它包括接觸約束並在擬合期間使用已知的 3DCP 身體姿勢為 MTP 圖像創建接近真實的姿勢。

Fourth, for more image variety, we label a dataset of in-the-wild images with Discrete Self-Contact (DSC) information and use another new optimization method, SMPLify-DC, that exploits discrete contacts during pose optimization. 
第四，為了獲得更多的圖像多樣性，我們使用離散自接觸 (DSC) 信息標記野外圖像數據集，並使用另一種新的優化方法 SMPLify-DC，該方法在姿勢優化過程中利用離散接觸。

Finally, we use our datasets during SPIN training to learn a new 3D human pose regressor, called TUCH (Towards Understanding Contact in Humans). 
最後，我們在 SPIN 訓練期間使用我們的數據集來學習一個新的 3D 人體姿勢回歸器，稱為 TUCH（Towards Understanding Contact in Humans）。

We show that the new selfcontact training data significantly improves 3D human pose estimates on withheld test data and existing datasets like 3DPW. 
我們表明，新的自我接觸訓練數據顯著改善了對保留測試數據和現有數據集（如 3DPW）的 3D 人體姿勢估計。

Not only does our method improve results for selfcontact poses, but it also improves accuracy for non-contact poses. 
我們的方法不僅改善了自接觸姿勢的結果，而且還提高了非接觸姿勢的準確性。

The code and data are available for research purposes at https://tuch.is.tue.mpg.de.
程式碼和數據可用於研究目的，網址為 https://touch.is.the.mpg.de。




## CVPR 2021

https://cvpr2021.thecvf.com/node/290


