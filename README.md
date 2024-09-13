# Large Langague Model Monte Carlo Search Tree (LLM-MCST)

Basic implementation of a monte carlo search tree with the goal of improving smaller LLM's reasoning performance

Based on [this](https://arxiv.org/abs/2408.06195) paper
Stealing some code from their attached repo [here](https://github.com/zhentingqi/rStar)

## Background

The paper above claims very impressive performance, boosting 7b models to near GPT-4 level on logic benchmarks. There's 2 main components

 * Generator LLM: Take a problem and creates possible reasoning trajectories, essentially different possible steps that can be taken to solve the problem
 * Discriminator LLM: Evaluates reasoning trajectories, double checks generator's thinking
