# kan-readpaper-homework
期刊閱讀筆記與作業

## 人工智慧

1. A game-theoretic analysis of networked system control for common-pool resource management(公共池資源管理) using multi-agent reinforcement learning
使用多智能體強化學習進行公共池資源管理的網絡系統控制的博弈論分析

https://arxiv.org/abs/2010.07777
Comments: 17 pages, 16 Figures, to appear in Advances of Neural Information Processing Systems (NeurIPS) conference, 2020
Subjects:	Machine Learning (cs.LG); Computer Science and Game Theory (cs.GT); Multiagent Systems (cs.MA)

Abstract 摘要

多智能體強化學習(Multi-agent reinforcement learning)最近顯示出作為網絡系統控制方法的巨大希望。
可以說，適用於大規模網絡系統控制的最困難和最重要的任務之一是公共池資源管理。

重要的公共池資源包括耕地、淡水、濕地、野生動物、魚類種群、森林和大氣，其中的適當管理與社會面臨的一些最大挑戰有關，例如糧食安全、不平等和氣候變化。在這裡，我們從最近的一項研究項目中汲取靈感，該項目調查了人類在社會困境（例如眾所周知的公地悲劇）中的博弈論激勵。

然而，與其專注於生物進化的類人代理(human-like agents)，我們更關心的是更好地理解包含通用強化學習代理的工程網絡系統的學習和操作行為，僅受非生物約束，如內存、計算和通信帶寬(communication bandwidth)。

利用經驗博弈論(game-theoretic analysis)分析中的工具，我們分析了由於在網絡多代理系統(multi-agent systems)設計中採用不同信息結構而產生的解決方案概念的差異。這些信息結構(information structure)與代理之間共享的信息類型以及採用的通信協議和網絡拓撲(network topology)有關。

我們的分析為與某些設計選擇相關的後果提供了新的見解，並提供了超越效率、穩健性、可擴展性和平均控制性能的系統之間比較的額外維度。

2. Performance Effectiveness of Multimedia Information Search Using the Epsilon-Greedy Algorithm
使用 Epsilon-Greedy 演算法進行多媒體資訊搜尋的表現上的效能 
(研究者想要看這玩意會不會比較棒)

https://ieeexplore.ieee.org/document/8999097
Published in: 2019 18th IEEE International Conference On Machine Learning And Applications (ICMLA)

Abstract 摘要
在對多媒體物件的搜尋(search)和取得(retrieval)， 用手動或自動化方式去取得內容來給索引的用，是一件很不實際的事情，因為多數多媒體內容無法用機器去取得。而手动提取往往非常费力和费时。然而，藉由系統化方式去捕捉和分析，人類使用者的反饋模式。也就是說人類使用者反應所組成的模式。跟這些多媒體內容的有關的重要資訊，是可以被取得來做有效率的索引和後續搜尋使用。藉由學習使用者人類判斷與大腦評估。可以逐步开发和建立有效的搜索索引，然后利用它来查找最相关的多媒体对象。

为了避免在局部最大值附近徘徊，我们应用 Є-greedy 方法来系统化地來探索搜索空间。藉由通过这种有条不紊的探索，我们證實所提出的方法能够保证始终可以发现最相关的对象，即使一開始的時候，這些搜尋結果或方法可能被忽视或不被认为是相关的。
* it 寫錯，應該用 they.
為了執行 Є-greedy algorithm 的兩個變數值，也就是EGSE-A和EGSE-B，我們現在的搜尋方法的搜尋行為是被量化分析(quantitatively analyzed)，而且還得取得封闭形式表达式(closed-form expressions)。
我們已經進行了對實際數據的模擬和實驗，其結果與理論上的數據有非常大的一致。現有的這個方法可以很有效的增強搜尋來大幅的提升多媒體資訊搜尋的表現，而且可以確切地發現原本找不到的一些相關的物件。
Index Terms—multimedia search, exploration, performance analysis, content indexing
索引—多媒體搜尋、勘探、性能分析、内容索引

3. Planning in Markov Decision Processes with Gap-Dependent Sample Complexity
用間隙相關樣本複雜性來做出利用馬爾可夫決策過程所做出的規劃

https://arxiv.org/abs/2006.05879
https://proceedings.neurips.cc/paper/2020
https://proceedings.neurips.cc/paper/2020/hash/0d85eb24e2add96ff1a7021f83c1abc9-Abstract.html
Part of Advances in Neural Information Processing Systems 33 (NeurIPS 2020)

Abstract 摘要

We propose MDP-GapE, a new trajectory-based Monte-Carlo Tree Search algorithm for planning in a Markov Decision Process in which transitions have a finite support.
我們提出了 MDP-GapE，這是一種新的基於軌跡的蒙特卡洛樹搜索算法(trajectory-based Monte-Carlo Tree Search algorithm)，此算法用於在馬爾可夫決策過程中進行規劃，在過程中進行規畫，而這個過程的轉換具有有限支持(a finite support)。
* trajectory 彈道, 軌道
We prove an upper bound on the number of calls to the generative models needed for MDP-GapE to identify a near-optimal action with high probability. 
我們證明了對 MDP-GapE 所需的生成模型調用次數的上限，以用最高產生的可能性(高概率識別)，從而找出接近最好的動作。

This problem dependent sample complexity result is expressed in terms of the sub-optimality gaps of the state-action pairs that are visited during exploration. 
這種問題相關的樣本複雜性結果 是以 在我們尋找最高可能性的期間考慮過(探索期間訪問)的狀態-動作對的次優差距(the sub-optimality gaps of the state-action pairs)來被產生出來。

Our experiments reveal that MDP-GapE is also effective in practice, in contrast with other algorithms with sample complexity guarantees in the fixed-confidence setting, that are mostly theoretical.
我們的實驗表明，在與固定置信度設置(the fixed-confidence setting)中具有樣本複雜性保證的(sample complexity guarantees)其他主要是理論性的算法，相比之下 MDP-GapE 在實踐中也是有效的。
(研究者說他這東西在實踐中有效，其他都是理論性 !!!!)

4. DAGs with No Fears: A Closer Look at Continuous Optimization for Learning Bayesian Networks
無所畏懼的 DAG：深入了解學習貝葉斯網絡的持續優化

https://arxiv.org/abs/2010.09133
Comments:	40 pages, 8 figures, to appear at the 34th Conference on Neural Information Processing Systems (NeurIPS 2020)
Subjects:	Machine Learning (cs.LG); Machine Learning (stat.ML)

Abstract 摘要

This paper re-examines a continuous optimization framework dubbed NOTEARS for learning Bayesian networks. 
本文重新審視了一個名為 NOTEARS 的連續優化框架，用於學習貝葉斯網絡。

We first generalize existing algebraic characterizations of acyclicity to a class of matrix polynomials.
我們首先將非循環性的現有代數特徵推廣到一類矩陣多項式。

Next, focusing on a one-parameter-per-edge setting, it is shown that the Karush-Kuhn-Tucker (KKT) optimality conditions for the NOTEARS formulation cannot be satisfied except in a trivial case, which explains a behavior of the associated algorithm. 
接下來，重點關注每邊一個參數的設置，結果表明，除了在微不足道的情況下，不能滿足 NOTEARS 公式的 Karush-Kuhn-Tucker (KKT) 最優性條件，並解釋該演算法的行為。

We then derive the KKT conditions for an equivalent reformulation, show that they are indeed necessary, and relate them to explicit constraints that certain edges be absent from the graph. 
然後我們推導出等效重構的 KKT 條件，表明它們確實是必要的，並將它們與圖中某些邊不存在的顯式約束相關聯。

If the score function is convex, these KKT conditions are also sufficient for local minimality despite the non-convexity of the constraint. 
如果得分函數是凸的，儘管約束不凸，這些 KKT 條件也足以滿足局部極小性。

Informed by the KKT conditions, a local search post-processing algorithm is proposed and shown to substantially and universally improve the structural Hamming distance of all tested algorithms, typically by a factor of 2 or more.
根據 KKT 條件，提出了一種局部搜索後處理算法，並證明它可以顯著和普遍地改善所有測試算法的結構漢明距離，通常提高 2 倍或更多。

Some combinations with local search are both more accurate and more efficient than the original NOTEARS.
與本地搜索的某些組合比原始 NOTEARS 更準確、更有效。

5. Asynchronous Multitask Reinforcement Learning with Dropout for Continuous Control
具有 Dropout 的異步多任務強化學習以實現持續控制

https://ieeexplore.ieee.org/document/8999228
Published in: 2019 18th IEEE International Conference On Machine Learning And Applications (ICMLA)

Abstract 摘要

Deep reinforcement learning is sample inefficient for solving complex tasks. 
深度強化學習對於解決複雜任務的樣本效率很低。

Recently, multitask reinforcement learning has received increased attention because of its ability to learn general policies with improved sample efficiency.
最近，多任務強化學習因其能夠以提高的樣本效率學習一般策略而受到越來越多的關注。

In multitask reinforcement learning, a single agent must learn multiple related tasks, either sequentially or simultaneously.
在多任務強化學習中，單個代理必須依次或同時學習多個相關任務。

Based on the DDPG algorithm, this paper presents Asyn-DDPG, which asynchronously learns a multitask policy for continuous control with simultaneous worker agents.
本文基於 DDPG 算法，提出了 Asyn-DDPG，它異步學習多任務策略，以實現同時工作代理的連續控制。

We empirically found that sparse policy gradients can significantly reduce interference among conflicting tasks and make multitask learning more stable and sample efficient.
我們憑經驗發現稀疏策略梯度可以顯著減少衝突任務之間的干擾，並使多任務學習更加穩定和样本效率。

To ensure the sparsity of gradients evaluated for each task, Asyn-DDPG represents both actor and critic functions as deep neural networks and regularizes them using Dropout.
為了確保為每個任務評估的梯度的稀疏性，Asyn-DDPG 將演員和評論家函數都表示為深度神經網絡，並使用 Dropout 對其進行正則化。

During training, worker agents share the actor and the critic functions, and asynchronously optimize them using task-specific gradients.
在訓練期間，工作代理(agents)共享actor 和critic 函數，並使用特定於任務的梯度異步優化它們。

For evaluating Asyn-DDPG, we proposed robotic navigation tasks based on realistically simulated robots and physics-enabled maze-like environments.
為了評估 Asyn-DDPG，我們提出了基於真實模擬機器人和支持物理的迷宮般環境的機器人導航任務。

Although the number of tasks used in our experiment is small, each task is conducted based on a real-world setting and posts a challenging environment.
雖然我們實驗中使用的任務數量很少，但每項任務都是基於現實世界的設置進行的，並發布了一個具有挑戰性的環境。

Through extensive evaluation, we demonstrate that Dropout regularization can effectively stabilize asynchronous learning and enable Asyn-DDPG to outperform DDPG significantly.
通過廣泛的評估，我們證明 Dropout 正則化可以有效地穩定異步學習並使 Asyn-DDPG 的性能顯著優於 DDPG。

Also, Asyn-DDPG was able to learn a multitask policy that can be well generalized for handling environments unseen during training.
此外，Asyn-DDPG 能夠學習一種多任務策略，該策略可以很好地泛化以處理訓練期間看不見的環境。

Index Terms—Deep reinforcement learning, Multitask reinforcement learning, Asynchronous method, Continuous control, Partial observability






