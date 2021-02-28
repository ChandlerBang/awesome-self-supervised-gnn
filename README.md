# awesome-self-supervised-gnn
Papers about self-supervised learning on Graph Neural Networks (GNNs).
If you feel there are papers with related topics missing, do not hesitate to let us know (via issues or pull requests).

<!---
### Contents
Since GNN pretraining and some unsupervised methods often involve self-supervised learning, here we also include them in this repository.
* [1. GNN Self-Supervised learning](#1-gnn-self-supervised-learning)
* [2. GNN Pretraining](#2-gnn-pre-training)
* [3. Other Related Papers](#3-other-related-papers) (implicitly using self-supersvied learning or applying graph neural networks in other domains)
-->

1. [arXiv 2021] **Towards Robust Graph Contrastive Learning** [[paper]](https://arxiv.org/pdf/2102.13085.pdf)
2. [arXiv 2021] **Pre-Training on Dynamic Graph Neural Networks** [[paper]](https://arxiv.org/abs/2102.12380)
4. [arXiv 2021] **Self-Supervised Learning of Graph Neural Networks: A Unified Review** [[paper]](https://arxiv.org/abs/2102.10757)
5. [WWW 2021 Workshop] **Iterative Graph Self-Distillation** [[paper]](https://arxiv.org/abs/2010.12609)
6. [WWW 2021] **SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised Mutual Information Mechanism** [[paper]](https://arxiv.org/abs/2101.08170) [[code]](https://github.com/RingBDStack/SUGAR)
7. [Arxiv 2021] **Self-Supervised Multi-Channel Hypergraph Convolutional Network for Social Recommendation** [[paper]](https://arxiv.org/abs/2101.06448) [[code]](https://github.com/Coder-Yu/RecQ)
8. [ICLR 2021] **How to Find Your Friendly Neighborhood: Graph Attention Design with Self-Supervision** [[paper]](https://openreview.net/forum?id=Wi5KUNlqWty)
9. [WSDM 2021] **Pre-Training Graph Neural Networks for Cold-Start Users and Items Representation** [[paper]](https://arxiv.org/abs/2012.07064) [[code]](https://github.com/jerryhao66/Pretrain-Recsys)
10. [Arxiv 2020] **COAD: Contrastive Pre-training with Adversarial Fine-tuning for Zero-shot Expert Linking** [[paper]](https://arxiv.org/abs/2012.11336) [[code]](https://github.com/BoChen-Daniel/Expert-Linking)
11. [Arxiv 2020] **Distance-wise Graph Contrastive Learning** [[paper]](https://arxiv.org/abs/2012.07437)
12. [Arxiv 2020] **Graph Contrastive Learning with Adaptive Augmentation** [[paper]](https://arxiv.org/abs/2010.14945)
13. [Openreview 2020] **Motif-Driven Contrastive Learning of Graph Representations** [[paper]](https://openreview.net/forum?id=qcKh_Msv1GP)
14. [Openreview 2020] **SLAPS: Self-Supervision Improves Structure Learning for Graph Neural Networks** [[paper]](https://openreview.net/forum?id=a5KvtsZ14ev)
15. [Openreview 2020] **TopoTER: Unsupervised Learning of Topology Transformation Equivariant Representations** [[paper]](https://openreview.net/forum?id=9az9VKjOx00)
16. [Openreview 2020] **Graph-Based Neural Network Models with Multiple Self-Supervised Auxiliary Tasks** [[paper]](https://openreview.net/forum?id=hnJSgY7p33a)
17. [Openreview 2020] **Self-supervised Graph-level Representation Learning with Local and Global Structure** [[paper]](https://openreview.net/forum?id=DAaaaqPv9-q)
18. [NeurIPS 2020] **Self-Supervised Graph Transformer on Large-Scale Molecular Data** [[paper]](https://drug.ai.tencent.com/publications/GROVER.pdf)
19. [NeurIPS 2020] **Self-supervised Auxiliary Learning with Meta-paths for Heterogeneous Graphs** [[paper]](https://arxiv.org/abs/2007.08294) [[code]](https://github.com/mlvlab/SELAR)
20. [NeurIPS 2020] **Graph Contrastive Learning with Augmentations** [[paper]](https://arxiv.org/abs/2010.13902) [[code]](https://github.com/Shen-Lab/GraphCL)
21. [Arxiv 2020] **Self-supervised Learning on Graphs: Deep Insights and New Direction.** [[paper]](https://arxiv.org/abs/2006.10141) [[code]](https://github.com/ChandlerBang/SelfTask-GNN)
22. [Arxiv 2020] **Deep Graph Contrastive Representation Learning** [[paper]](https://arxiv.org/abs/2006.04131)
23. [ICML 2020] **When Does Self-Supervision Help Graph Convolutional Networks?** [[paper]](https://arxiv.org/abs/2006.09136) [[code]](https://github.com/Shen-Lab/SS-GCNs)
24. [ICML 2020] **Graph-based, Self-Supervised Program Repair from Diagnostic Feedback.** [[paper]](https://arxiv.org/abs/2005.10636)
25. [ICML 2020] **Contrastive Multi-View Representation Learning on Graphs.** [[paper]](https://arxiv.org/abs/2006.05582) [[code]](https://github.com/kavehhassani/mvgrl)
26. [ICML 2020 Workshop] **Self-supervised edge features for improved Graph Neural Network training.** [[paper]](https://arxiv.org/abs/2007.04777)
27. [Arxiv 2020] **Self-supervised Training of Graph Convolutional Networks.** [[paper]](https://arxiv.org/abs/2006.02380)
28. [Arxiv 2020] **Self-Supervised Graph Representation Learning via Global Context Prediction.** [[paper]](https://arxiv.org/abs/2003.01604)
29. [KDD 2020] **GPT-GNN: Generative Pre-Training of Graph Neural Networks.** [[pdf]](https://arxiv.org/abs/2006.15437) [[code]](https://github.com/acbull/GPT-GNN)
30. [KDD 2020] **GCC: Graph Contrastive Coding for Graph Neural Network Pre-Training.** [[pdf]](https://arxiv.org/abs/2006.09963) [[code]](https://github.com/THUDM/GCC) 
31. [Arxiv 2020] **Graph-Bert: Only Attention is Needed for Learning Graph Representations.** [[paper]](https://arxiv.org/abs/2001.05140) [[code]](https://github.com/anonymous-sourcecode/Graph-Bert)
32. [ICLR 2020] **Strategies for Pre-training Graph Neural Networks.** [[paper]](https://arxiv.org/abs/1905.12265) [[code]](https://github.com/snap-stanford/pretrain-gnns)
33. [AAAI 2020] **Multi-Stage Self-Supervised Learning for Graph Convolutional Networks on Graphs with Few Labels.** [[paper]](https://arxiv.org/abs/1902.11038)
34. [KDD 2019 Workshop] **SGR: Self-Supervised Spectral Graph Representation Learning.** [[paper]](https://arxiv.org/abs/1811.06237)
35. [ICLR 2019 Workshop] **Can Graph Neural Networks Go "Online"? An Analysis of Pretraining and Inference.** [[paper]](https://arxiv.org/abs/1905.06018)
36. [ICLR 2019 workshop] **Pre-Training Graph Neural Networks for Generic Structural Feature Extraction.** [[paper]](https://arxiv.org/abs/1905.13728)


## Other related papers
 (implicitly using self-supersvied learning or applying graph neural networks in other domains)
1. [Arxiv 2020] **Self-supervised Learning: Generative or Contrastive.** [[paper]](https://arxiv.org/abs/2006.08218)
1. [KDD 2020] **Octet: Online Catalog Taxonomy Enrichment with Self-Supervision.** [[paper]](https://arxiv.org/pdf/2006.10276.pdf)
1. [WWW 2020] **Structural Deep Clustering Network.** [[paper]](https://dl.acm.org/doi/abs/10.1145/3366423.3380214
) [[code]](https://github.com/bdy9527/SDCN)
1. [ICLR 2020] **InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation Learning via Mutual Information Maximization.** [[paper]](https://arxiv.org/abs/1908.01000) [[code]](https://github.com/fanyun-sun/InfoGraph)
1. [ICLR 2019] **Deep Graph Informax.** [[paper]](https://arxiv.org/abs/1809.10341) [[code]](https://github.com/PetarV-/DGI)
1. [IJCAI 2019] **Pre-training of Graph Augmented Transformers for Medication Recommendation.** [[paper]](https://arxiv.org/abs/1906.00346) [[code]](https://github.com/jshang123/G-Bert)
1. [Arxiv 2019] **Heterogeneous Deep Graph Infomax** [[paper]](https://arxiv.org/abs/1911.08538) [[code]](https://github.com/YuxiangRen/Heterogeneous-Deep-Graph-Infomax)
1. [AAAI 2020] **Unsupervised Attributed Multiplex Network Embedding** [[paper]](https://arxiv.org/abs/1911.06750) [[code]](https://github.com/pcy1302/DMGI)
1. [WWW 2020] **Graph representation learning via graphical mutual information maximization** [[paper]](https://dl.acm.org/doi/abs/10.1145/3366423.3380112)
1. [NeurIPS 2017] **Inductive Representation Learning on Large Graphs** [[paper]](https://papers.nips.cc/paper/2017/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html) [[code]](https://github.com/williamleif/GraphSAGE)
1. [NeurIPS 2016 Workshop] **Variational Graph Auto-Encoders** [[paper]](https://arxiv.org/abs/1611.07308) [[code]](https://github.com/tkipf/gae)
1. [WWW 2015] **LINE: Large-scale Information Network Embedding** [[paper]](https://dl.acm.org/doi/abs/10.1145/2736277.2741093) [[code]](https://github.com/tangjianpku/LINE)
1. [KDD 2014] **DeepWalk: Online Learning of Social Representations** [[paper]](https://dl.acm.org/doi/abs/10.1145/2623330.2623732) [[code]](https://github.com/phanein/deepwalk)


