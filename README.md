Devcontainer setup for CUDA enabled workloads.   
Includes a specific example for NVIDIA Reinforcement Learning with Verifiable Rewards Fine Tuning example

For this blog post: https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/  
Which linked to this Youtube video: https://www.youtube.com/watch?v=9t-BAjzBWj8   
Which links to this notebook: https://colab.research.google.com/github/openai/gpt-oss/blob/main/examples/reinforcement-fine-tuning.ipynb#scrollTo=CGoDZwcunHEU  

I didn't want to set up CUDA on my dev machine, considering the various combinations of CUDA, PyTorch and driver versions often involved. It was simpler to just set up this environment for easier reuse and isolation. 

