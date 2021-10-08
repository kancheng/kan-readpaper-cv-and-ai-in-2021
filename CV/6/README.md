# kan-readpaper-homework

期刊閱讀筆記與作業

## 計算機視覺

SCANimate: Weakly Supervised Learning of Skinned Clothed Avatar Networks

SCANimate: Skinned Clothing Avatar Networks 的弱監督學習

Shunsuke Saito, Jinlong Yang, Qianli Ma, Michael J. Black

Max Planck Institute for Intelligent Systems, Tubingen, Germany
ETH Zurich

CVPR 2021 Best Paper Candidate

https://arxiv.org/abs/2104.03313

https://scanimate.is.tue.mpg.de/



Note

> 研究團隊展示了名為 SCANimate 的一個端到端的可訓練框架，該框架可以對一個穿著衣服的人進行原始 3D 掃描，並將其變成一個可動畫的角色。而且這些角色由姿勢參數來驅動，並同時擁有可自然移動和變形的逼真服裝。
> 
> 研究者通過觀察發現將參數化 3D 身體模型，將其擬合到穿著衣服的人體掃描是容易處理的，反之則身體結構與掃描的表面配准通常則不行，因為衣服可能會顯著偏離身體形狀。這一連串的觀察使研究者找到一種弱監督學習方法，該方法可通過沒有模型的表面配準的情況下就能進行掃描，同時對齊到規範姿勢中。
> 


Abstract 摘要

We present SCANimate, an end-to-end trainable framework that takes raw 3D scans of a clothed human and turns them into an animatable avatar. 
我們展示了 SCANimate，這是一個端到端的可訓練框架，它對一個穿著衣服的人進行原始 3D 掃描並將它們變成一個可動畫的化身。

These avatars are driven by pose parameters and have realistic clothing that moves and deforms naturally. 
這些化身由姿勢參數驅動，並擁有可自然移動和變形的逼真服裝。

SCANimate does not rely on a customized mesh template or surface mesh registration. 
SCANimate 不依賴於自定義網格模板或表面網格註冊。

We observe that fitting a parametric 3D body model, like SMPL, to a clothed human scan is tractable while surface registration of the body topology to the scan is often not, because clothing can deviate significantly from the body shape.
我們觀察到，將參數化 3D 身體模型（如 SMPL）擬合到穿著衣服的人體掃描是容易處理的，而身體拓撲結構與掃描的表面配准通常則不然，因為衣服可能會顯著偏離身體形狀。

We also observe that articulated transformations are invertible, resulting in geometric cycle-consistency in the posed and unposed shapes.
我們還觀察到鉸接變換是可逆的，從而導致擺姿勢和未擺姿勢的形狀的幾何循環一致性。

These observations lead us to a weakly supervised learning method that aligns scans into a canonical pose by disentangling articulated deformations without templatebased surface registration. 
這些觀察使我們找到了一種弱監督學習方法，該方法通過在沒有基於模板的表面配準的情況下解開鉸接變形來將掃描對齊到規範姿勢。

Furthermore, to complete missing regions in the aligned scans while modeling posedependent deformations, we introduce a locally pose-aware implicit function that learns to complete and model geometry with learned pose correctives.
此外，為了在對姿態相關變形建模的同時完成對齊掃描中的缺失區域，我們引入了一個局部姿態感知隱式函數，該函數學習使用學習的姿態校正來完成和建模幾何。

In contrast to commonly used global pose embeddings, our local pose conditioning significantly reduces long-range spurious correlations and improves generalization to unseen poses, especially when training data is limited. Our method can be applied to poseaware appearance modeling to generate a fully textured avatar. 
與常用的全局姿勢嵌入相比，我們的局部姿勢調節顯著降低了遠程虛假相關性，並提高了對未知姿勢的泛化能力，尤其是在訓練數據有限的情況下。 我們的方法可以應用於姿態感知外觀建模以生成完全紋理化的頭像。

We demonstrate our approach on various clothing types with different amounts of training data, outperforming existing solutions and other variants in terms of fidelity and generality in every setting. 
我們在具有不同訓練數據量的各種服裝類型上展示了我們的方法，在每種設置的保真度和通用性方面均優於現有解決方案和其他變體。

The code is available at https://scanimate.is.tue.mpg.de.



## CVPR 2021

https://cvpr2021.thecvf.com/node/290


