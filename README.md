This repo contains a sample Devcontainer configuration for CUDA workloads in VS Code. It accompanies [this blog post](https://code.mendhak.com/run-cuda-machine-learning-environment-in-docker/). 


Includes a specific example for NVIDIA Reinforcement Learning with Verifiable Rewards Fine Tuning example. 

Originally spurred by this blog post: https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/  

Which linked to this Youtube video: https://www.youtube.com/watch?v=9t-BAjzBWj8   


Which links to this notebook: https://colab.research.google.com/github/openai/gpt-oss/blob/main/examples/reinforcement-fine-tuning.ipynb#scrollTo=CGoDZwcunHEU  

I didn't want to set up CUDA on my dev machine, considering the various combinations of CUDA, PyTorch and driver versions often involved and mess things up. 

It was simpler to just set up this environment for easier reuse and isolation. 

