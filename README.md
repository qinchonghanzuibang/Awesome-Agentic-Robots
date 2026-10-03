<h1 align="center">Awesome Agentic Robots</h1>

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/qinchonghanzuibang/Awesome-Agentic-Robots/stargazers"><img src="https://img.shields.io/github/stars/qinchonghanzuibang/Awesome-Agentic-Robots?style=social" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/arXiv-pending-b31b1b.svg?logo=arxiv" alt="arXiv identifier pending">
</p>

<!-- Add the author-confirmed arXiv link to its badge upon release. -->

A curated collection of papers and resources accompanying **Towards Agentic Robots: Model, Data, Environment, and Harness**.

This official companion repository follows the survey's taxonomy, organizing work by the object of intervention in a robotic system: model capabilities and decisions, experience records, worlds and tasks, and the software connecting them.

[Taxonomy](#taxonomy) · [Papers](#papers) · [Contributing](CONTRIBUTING.md)

## Overview

**Model · Data · Environment · Harness**

The survey asks: *What should the agent decide, what should the robot execute, and what should experience change?* It connects robot-facing interfaces, execution feedback, and reusable capabilities across these four domains. The collection includes methods alongside the datasets, platforms, and evaluation resources used to develop and assess them.

Works can span several categories. Such associations describe the survey's organization; they do not imply that every component operates jointly in one configuration. Dates indicate first release, while venues reflect the publication information recorded in the survey.

## Taxonomy

| Domain | Categories |
| --- | --- |
| **Model** | [Training](#training) · [Perception](#perception) · [Planning](#planning) · [Robot Control](#robot-control) · [Adaptation](#adaptation) |
| **Data** | [Collection](#collection) · [Filtering](#filtering) · [Correction](#correction) |
| **Environment** | [Reconstruction](#reconstruction) · [Task Generation](#task-generation) · [Benchmarking](#benchmarking) |
| **Harness** | [Orchestration](#orchestration) · [Memory](#memory) · [Monitoring](#monitoring) · [Recovery](#recovery) · [Skill Synthesis](#skill-synthesis) · [Evolution](#evolution) |

## Papers

Entries are ordered newest first within each category. A work appears in every category assigned by the survey; metadata is stored once in [data/papers.yaml](data/papers.yaml). A dash in Resources means no verified link is recorded in this collection.

<!-- BEGIN AUTO-GENERATED PAPER LIST -->

### Model

#### Training

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.17210">FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence</a></td><td>arXiv</td><td nowrap><a href="https://github.com/FluxVLA/FluxVLA">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.07555">You Don&#x27;t Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.23280">Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation</a></td><td>arXiv</td><td nowrap><a href="https://yy12136.github.io/CRWM">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.19980">ENPIRE: Agentic Robot Policy Self-Improvement in the Real World</a></td><td>arXiv</td><td nowrap><a href="https://github.com/NVlabs/ENPIRE">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.08610">HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.01672">RDA: Reward Design Agent for Reinforcement Learning</a></td><td>RLJ</td><td nowrap><a href="https://nitinkamra1992.github.io/reward-design-agent">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.09630">ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv</td><td nowrap><a href="https://robolineage.github.io/">Project</a> · <a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.11859">EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2606.00083">From Demonstrations to Rewards: Test-Time Prompt Optimization for VLM Reward Models</a></td><td>arXiv</td><td nowrap><a href="https://github.com/cgumbsch/Demo2Reward">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.11665">Nautilus: From One Prompt to Plug-and-Play Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.27416">Agent-Driven Autonomous Reinforcement Learning Research: Iterative Policy Improvement for Quadruped Locomotion</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2023/10</td><td><a href="https://arxiv.org/abs/2310.12931">Eureka: Human-Level Reward Design via Coding Large Language Models</a></td><td>ICLR</td><td nowrap><a href="https://eureka-research.github.io">Project</a> · <a href="https://github.com/eureka-research/Eureka">Code</a></td></tr>
</tbody>
</table>

#### Perception

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.12285">AnchorVLN: Geometry-Anchored Vision-Language Grounding Reasoning for Open-Vocabulary Navigation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/aryanmangal769/embodied-nav-mcp">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.02653">HINT: Human-Intent Inception for Long-Horizon Robot Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://robot-hint.github.io/">Project</a> · <a href="https://github.com/robot-hint/HINT">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.17129">Probe: Manipulation-Grounded Visual Question Answering with VLM Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10383">ABot-N1: Toward a General Visual Language Navigation Foundation Model</a></td><td>arXiv</td><td nowrap><a href="https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/">Project</a> · <a href="https://github.com/amap-cvlab/ABot-Navigation">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.04610">RoboVista: Evaluating Vision Language Models for Diverse Robot Applications</a></td><td>RSS</td><td nowrap><a href="https://berkeleyautomation.github.io/robovista">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.06061">A Conversational Framework for Human-Robot Collaborative Manipulation with Distributed Generative AI models</a></td><td>RO-MAN</td><td nowrap><a href="https://github.com/cogrob-tuni/franka-llm">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.10577">AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.02951">SCOPE: Real-Time Natural Language Camera Agent at the Edge</a></td><td>HRI</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.26988">Robot Planning and Situation Handling with Active Perception</a></td><td>arXiv</td><td nowrap><a href="https://vap-tamp.github.io/vap-tamp/">Project</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.18210">GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.05377">OpenFrontier: General Navigation with Visual-Language Grounded Frontiers</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.04157">A Modern System Recipe for Situated Embodied Human-Robot Conversation with Real-Time Multimodal LLMs and Tool-Calling</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.13193">Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control</a></td><td>arXiv</td><td nowrap><a href="https://steerable-policies.github.io">Project</a> · <a href="https://github.com/steerable-policies/steerable-policies-bridge">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.14681">FARE: Fast-Slow Agentic Robotic Exploration</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.13143">SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation</a></td><td>NeurIPS</td><td nowrap><a href="https://qizekun.github.io/sofar/">Project</a> · <a href="https://github.com/qizekun/SoFar">Code</a></td></tr>
</tbody>
</table>

#### Planning

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05985">A Brain-inspired Hierarchical Framework for Zero-Shot Robot Task Reasoning and Execution</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://leeibo.github.io/ActiveArena">Project</a> · <a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://www.mdpi.com/1424-8220/26/17/5595">Adaptive Task Planning for Long-Horizon Robotic Manipulation Based on Video Priors and Dynamic Scene Graphs</a></td><td>Sensors</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.13335">Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19315">GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.26360">Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.11561">Memory as Plans: World-Action Modeling with Memory-Grounded Planning</a></td><td>arXiv</td><td nowrap><a href="https://sizhezhao.github.io/projects/MaP-WAM/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27526">NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08444">Safe Task Planning with Long-Term Graph Memory for Embodied Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.28300">MaCoPlanner: LLM-Assisted Manual-Compiled Task Planning with Proactive Safety Verification for Robotic Industrial Panel Operation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/XinGP/MaCoPlanner">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.30396">Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1848830/full">STARS: extending interactive task learning with large language models</a></td><td>Front. Comput. Sci.</td><td nowrap><a href="https://github.com/Center-for-Integrated-Cognition/STARS">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.06501">Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.22999">WCM: World-Cognition Model for Generalizable Human-Robot Interaction</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.27871">LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.13533">Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02772">Agentic Self-Evolutionary Replanning for Embodied Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.03148">From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?</a></td><td>arXiv</td><td nowrap><a href="https://github.com/ShinasShaji/llm-robot-cognition">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02669">IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.13081">Agentic AI for Robot Control: Flexible but still Fragile</a></td><td>AAAI-SS</td><td nowrap><a href="https://dfki-ni.github.io/AGENTS-MAKE-2026">Project</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.13591">AgentRob: From Virtual Forum Agents to Hijacked Physical Robots</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.21670">Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv</td><td nowrap><a href="https://reflective-test-time-planning.github.io">Project</a> · <a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.19510">ALRM: Agentic LLM for Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://tiiuae.github.io/ALRM">Project</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.18492">DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/PlumJun/DV-VLN">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.11063">EmboTeam: Grounding LLM Reasoning into Reactive Behavior Trees via PDDL for Embodied Multi-Robot Collaboration</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/10</td><td><a href="https://arxiv.org/abs/2510.03342">Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td><td>ICML</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.16707">Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation</a></td><td>CoRL</td><td nowrap><a href="https://reflect-vlm.github.io">Project</a> · <a href="https://github.com/yunhaif/reflect-vlm">Code</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.01928">Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners</a></td><td>CoRL</td><td nowrap><a href="https://robot-help.github.io">Project</a> · <a href="https://github.com/google-research/google-research/tree/master/language_model_uncertainty">Code</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.04738">RoCo: Dialectic Multi-Robot Collaboration with Large Language Models</a></td><td>ICRA</td><td nowrap><a href="https://project-roco.github.io">Project</a> · <a href="https://github.com/MandiZhao/robot-collab">Code</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.06135">SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning</a></td><td>CoRL</td><td nowrap><a href="https://sayplan.github.io">Project</a></td></tr>
</tbody>
</table>

#### Robot Control

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.28247">Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.26499">Generalizing Manipulation Skills with a Local Coding Agent</a></td><td>arXiv</td><td nowrap><a href="https://rtalwar2.github.io/agentic-coding-for-robot-manipulation/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19138">In-Context Robot Learning with VLM Agents</a></td><td>arXiv</td><td nowrap><a href="https://cheng-haha.github.io/GPT-Policy/">Project</a> · <a href="https://github.com/cheng-haha/GPT-Policy">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19347">Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.18869">KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.16331">ManiSkillFormer: Demonstration-Free Compositional Manipulation via Geometric Contracts and Agentic Skill Graph</a></td><td>arXiv</td><td nowrap><a href="https://patricia1019.github.io/ManiSkillFormer/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.10522">Show-Harness: Just a VLM Agent Can Play Robots</a></td><td>arXiv</td><td nowrap><a href="https://showlab.github.io/Show-Harness">Project</a> · <a href="https://github.com/showlab/Show-Harness">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.22966">Transferring the Intelligence of VLMs to Robotic Control</a></td><td>arXiv</td><td nowrap><a href="https://robodawn.top/">Project</a> · <a href="https://github.com/Hugo-AGI/RoboDawn">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.28429">Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29964">World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.03924">ETA: A New Agentic Paradigm for Embodied Tasks</a></td><td>arXiv</td><td nowrap><a href="https://github.com/OpenMOSS/OpenETA">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.14047">Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use</a></td><td>CVPR Findings</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10383">ABot-N1: Toward a General Visual Language Navigation Foundation Model</a></td><td>arXiv</td><td nowrap><a href="https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/">Project</a> · <a href="https://github.com/amap-cvlab/ABot-Navigation">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.26148">Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.22832">MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/sygkounas/MEMENTO">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.11119">VIA: Visual Interface Agent for Robot Control</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.12299">Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.02951">SCOPE: Real-Time Natural Language Camera Agent at the Edge</a></td><td>HRI</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.02600">CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.20334">Demonstration-Free Robotic Control via LLM Agents</a></td><td>arXiv</td><td nowrap><a href="https://github.com/robiemusketeer/faea-sim">Code</a></td></tr>
<tr><td nowrap>2024/09</td><td><a href="https://arxiv.org/abs/2409.01652">ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation</a></td><td>CoRL</td><td nowrap><a href="https://rekep-robot.github.io/">Project</a> · <a href="https://github.com/huangwl18/ReKep">Code</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td><td>CoRL</td><td nowrap><a href="https://voxposer.github.io">Project</a> · <a href="https://github.com/huangwl18/VoxPoser">Code</a></td></tr>
</tbody>
</table>

#### Adaptation

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19138">In-Context Robot Learning with VLM Agents</a></td><td>arXiv</td><td nowrap><a href="https://cheng-haha.github.io/GPT-Policy/">Project</a> · <a href="https://github.com/cheng-haha/GPT-Policy">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.22966">Transferring the Intelligence of VLMs to Robotic Control</a></td><td>arXiv</td><td nowrap><a href="https://robodawn.top/">Project</a> · <a href="https://github.com/Hugo-AGI/RoboDawn">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.26809">Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations</a></td><td>arXiv</td><td nowrap><a href="https://hero-agent.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.18247">Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement</a></td><td>RSS</td><td nowrap><a href="https://veritas-improvement.github.io">Project</a> · <a href="https://github.com/princeton-prism/veritas">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.00416">Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies</a></td><td>arXiv</td><td nowrap><a href="https://learning-while-deploying.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02772">Agentic Self-Evolutionary Replanning for Embodied Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.07997">CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv</td><td nowrap><a href="https://reflective-test-time-planning.github.io">Project</a> · <a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.12063">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td><td>arXiv</td><td nowrap><a href="https://sites.google.com/view/vlaw-arxiv">Project</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.22474">When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering</a></td><td>RSS</td><td nowrap><a href="https://jessie-yuan.github.io/ups/">Project</a> · <a href="https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering">Code</a></td></tr>
<tr><td nowrap>2025/09</td><td><a href="https://arxiv.org/abs/2509.15155">Self-Improving Embodied Foundation Models</a></td><td>NeurIPS</td><td nowrap><a href="https://self-improving-efms.github.io">Project</a></td></tr>
</tbody>
</table>

### Data

#### Collection

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv</td><td nowrap><a href="https://boweili666.github.io/ARSTAG/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv</td><td nowrap><a href="https://embodiedswe.github.io/">Project</a> · <a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05927">GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.23997">RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.17209">Teach and Grow: An Agent-Centered Architecture for General Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.13653">Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation</a></td><td>ECCV</td><td nowrap><a href="https://github.com/InternRobotics/REAL">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.26809">Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations</a></td><td>arXiv</td><td nowrap><a href="https://hero-agent.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv</td><td nowrap><a href="https://open-gigaai.github.io/Zero2Skill">Project</a> · <a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.19419">Playful Agentic Robot Learning</a></td><td>arXiv</td><td nowrap><a href="https://Playful-RATs.github.io">Project</a> · <a href="https://github.com/Playful-RATs/RATs">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv</td><td nowrap><a href="https://robolineage.github.io/">Project</a> · <a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.11558">RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks</a></td><td>arXiv</td><td nowrap><a href="https://github.com/RoboClaw-Robotics/RoboClaw">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.18811">V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/09</td><td><a href="https://arxiv.org/abs/2509.20070">LLM Trainer: Automated Robotic Data Generation via Demonstration Augmentation using LLMs</a></td><td>arXiv</td><td nowrap><a href="https://sites.google.com/andrew.cmu.edu/llm-trainer">Project</a></td></tr>
<tr><td nowrap>2025/09</td><td><a href="https://arxiv.org/abs/2509.15155">Self-Improving Embodied Foundation Models</a></td><td>NeurIPS</td><td nowrap><a href="https://self-improving-efms.github.io">Project</a></td></tr>
<tr><td nowrap>2025/07</td><td><a href="https://arxiv.org/abs/2507.00833">HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning</a></td><td>NeurIPS</td><td nowrap><a href="https://openhumanoidgen.github.io">Project</a> · <a href="https://github.com/TeleHuman/HumanoidGen">Code</a></td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv</td><td nowrap><a href="https://yewr.github.io/video2policy">Project</a></td></tr>
<tr><td nowrap>2023/11</td><td><a href="https://arxiv.org/abs/2311.01455">RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation</a></td><td>ICML</td><td nowrap><a href="https://robogen-ai.github.io/">Project</a> · <a href="https://github.com/Genesis-Embodied-AI/RoboGen">Code</a></td></tr>
</tbody>
</table>

#### Filtering

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv</td><td nowrap><a href="https://boweili666.github.io/ARSTAG/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv</td><td nowrap><a href="https://embodiedswe.github.io/">Project</a> · <a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05927">GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.20056">MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution</a></td><td>arXiv</td><td nowrap><a href="https://magma-rob.github.io/magma-gen">Project</a> · <a href="https://github.com/MAGMA-rob/magma-gen">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.02580">Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data</a></td><td>arXiv</td><td nowrap><a href="https://www-ye.github.io/ego2robot_blog/">Project</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.04196">SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://lin-nie.github.io/SiMDex/">Project</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.09776">HELP: Human-Efficient Large-Scale Robot Post-Training with Rollout Segmentation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv</td><td nowrap><a href="https://open-gigaai.github.io/Zero2Skill">Project</a> · <a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.25115">Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv</td><td nowrap><a href="https://robolineage.github.io/">Project</a> · <a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.13497">SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale</a></td><td>arXiv</td><td nowrap><a href="https://intuitive-robots.github.io/sparc-labeling/">Project</a> · <a href="https://github.com/intuitive-robots/sparc">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.18247">Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement</a></td><td>RSS</td><td nowrap><a href="https://veritas-improvement.github.io">Project</a> · <a href="https://github.com/princeton-prism/veritas">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.26349">Closing the Loop in Teleoperation: Episode-Level Data Quality Assessment and Feedback for High-Quality Demonstration Collection</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.13528">Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis</a></td><td>arXiv</td><td nowrap><a href="https://dream2fix.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.00675">RoboReward: General-Purpose Vision-Language Reward Models for Robotics</a></td><td>arXiv</td><td nowrap>—</td></tr>
</tbody>
</table>

#### Correction

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv</td><td nowrap><a href="https://boweili666.github.io/ARSTAG/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.20056">MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution</a></td><td>arXiv</td><td nowrap><a href="https://magma-rob.github.io/magma-gen">Project</a> · <a href="https://github.com/MAGMA-rob/magma-gen">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.02580">Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data</a></td><td>arXiv</td><td nowrap><a href="https://www-ye.github.io/ego2robot_blog/">Project</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.26645">FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation</a></td><td>CVPR</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv</td><td nowrap><a href="https://open-gigaai.github.io/Zero2Skill">Project</a> · <a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.13528">Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis</a></td><td>arXiv</td><td nowrap><a href="https://dream2fix.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv</td><td nowrap><a href="https://reflective-test-time-planning.github.io">Project</a> · <a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.22474">When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering</a></td><td>RSS</td><td nowrap><a href="https://jessie-yuan.github.io/ups/">Project</a> · <a href="https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.00675">RoboReward: General-Purpose Vision-Language Reward Models for Robotics</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/09</td><td><a href="https://arxiv.org/abs/2509.20070">LLM Trainer: Automated Robotic Data Generation via Demonstration Augmentation using LLMs</a></td><td>arXiv</td><td nowrap><a href="https://sites.google.com/andrew.cmu.edu/llm-trainer">Project</a></td></tr>
</tbody>
</table>

### Environment

#### Reconstruction

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv</td><td nowrap><a href="https://boweili666.github.io/ARSTAG/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05927">GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.30249">RAPID: Robot Agentic Programming from Demonstrations</a></td><td>arXiv</td><td nowrap><a href="https://yuyaoliu.me/projects/rapid">Project</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.19190">Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents</a></td><td>arXiv</td><td nowrap><a href="https://agentic-real2sim.github.io/">Project</a> · <a href="https://github.com/agentic-real2sim/agentic_real2sim">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.07459">EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI</a></td><td>arXiv</td><td nowrap><a href="https://horizonrobotics.github.io/EmbodiedGen">Project</a> · <a href="https://github.com/HorizonRobotics/EmbodiedGen">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.28276">SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.14398">ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction</a></td><td>arXiv</td><td nowrap><a href="https://uwsbel.github.io/chrono-agentic-website/">Project</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.05241">DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.09423">SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS</td><td nowrap><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv</td><td nowrap><a href="https://roboplayground.github.io">Project</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.10116">SAGE: Scalable Agentic 3D Scene Generation for Embodied AI</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.09153">SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes</a></td><td>ICML</td><td nowrap><a href="https://scenesmith.github.io/">Project</a> · <a href="https://github.com/nepfaff/scenesmith">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.02078">Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot</a></td><td>arXiv</td><td nowrap><a href="https://github.com/AgibotTech/genie_sim">Code</a></td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv</td><td nowrap><a href="https://yewr.github.io/video2policy">Project</a></td></tr>
</tbody>
</table>

#### Task Generation

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv</td><td nowrap><a href="https://boweili666.github.io/ARSTAG/">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.08610">HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.19419">Playful Agentic Robot Learning</a></td><td>arXiv</td><td nowrap><a href="https://Playful-RATs.github.io">Project</a> · <a href="https://github.com/Playful-RATs/RATs">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.09423">SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.08664">Generative Simulation for Policy Learning in Physical Human-Robot Interaction</a></td><td>arXiv</td><td nowrap><a href="https://rchi-lab.github.io/gen_phri/">Project</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS</td><td nowrap><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv</td><td nowrap><a href="https://roboplayground.github.io">Project</a></td></tr>
<tr><td nowrap>2025/02</td><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv</td><td nowrap><a href="https://yewr.github.io/video2policy">Project</a></td></tr>
<tr><td nowrap>2024/10</td><td><a href="https://arxiv.org/abs/2411.00081">PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks</a></td><td>ICLR</td><td nowrap><a href="https://github.com/facebookresearch/partnr-planner">Code</a></td></tr>
<tr><td nowrap>2023/11</td><td><a href="https://arxiv.org/abs/2311.01455">RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation</a></td><td>ICML</td><td nowrap><a href="https://robogen-ai.github.io/">Project</a> · <a href="https://github.com/Genesis-Embodied-AI/RoboGen">Code</a></td></tr>
</tbody>
</table>

#### Benchmarking

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://leeibo.github.io/ActiveArena">Project</a> · <a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv</td><td nowrap><a href="https://embodiedswe.github.io/">Project</a> · <a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08292">EvoNav-Bench: Benchmarking Lifelong Navigation in Evolving Environments</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19413">From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation</a></td><td>arXiv</td><td nowrap><a href="https://yy-gx.github.io/HALTER/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05178">LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models</a></td><td>arXiv</td><td nowrap><a href="https://liulin815.github.io/LIBERO-Recovery/">Project</a> · <a href="https://github.com/liulin815/LIBERO-Recovery">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.07047">MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Collab-Gen/MEMOBench">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.06424">OVMAN: A Task and Benchmark for Open-Vocabulary Motion-Aware Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.10895">ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19554">VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.08036">Compiling and Benchmarking Task-State Horizons for Embodied Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.17386">ManiGuard: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.04434">RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies</a></td><td>arXiv</td><td nowrap><a href="https://XPolicyLab.github.io">Project</a> · <a href="https://github.com/RoboDojo-Benchmark/RoboDojo">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.04610">RoboVista: Evaluating Vision Language Models for Diverse Robot Applications</a></td><td>RSS</td><td nowrap><a href="https://berkeleyautomation.github.io/robovista">Project</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.22014">Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents</a></td><td>arXiv</td><td nowrap><a href="https://gomtae.github.io/publications/missionbench">Project</a> · <a href="https://github.com/FraunhoferIVI/MissionBench">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.04811">Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?</a></td><td>arXiv</td><td nowrap><a href="https://github.com/showlab/Dream.exe">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.31993">OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.18610">SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation</a></td><td>arXiv</td><td nowrap><a href="https://weichengtseng.github.io/sc3-eval/">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.04233">What Are We Actually Benchmarking in Robot Manipulation?</a></td><td>arXiv</td><td nowrap><a href="https://ripl.github.io/manipulation_benchmark_audit/">Project</a> · <a href="https://github.com/ripl/ManipulationBenchmarkAudit">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.26637">Enabling Extensible Embodied Capabilities with Tools</a></td><td>arXiv</td><td nowrap><a href="https://racingemperor.github.io/manip-tool-hub/">Project</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.10921">RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark</a></td><td>arXiv</td><td nowrap><a href="https://robomemarena.github.io">Project</a> · <a href="https://github.com/OpenHelix-Team/RoboMemArena">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.25788">KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://proceedings.iclr.cc/paper_files/paper/2026/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf">ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies</a></td><td>ICLR</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS</td><td nowrap><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv</td><td nowrap><a href="https://roboplayground.github.io">Project</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.22435">CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation</a></td><td>ICML</td><td nowrap><a href="https://capgym.github.io">Project</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.04356">RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots</a></td><td>arXiv</td><td nowrap><a href="https://github.com/robocasa/robocasa">Code</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.06556">LIBERO-X: Robustness Litmus for Vision-Language-Action Models</a></td><td>RSS</td><td nowrap><a href="https://zackhxn.github.io/LIBERO-X/">Project</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.02078">Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot</a></td><td>arXiv</td><td nowrap><a href="https://github.com/AgibotTech/genie_sim">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.00675">RoboReward: General-Purpose Vision-Language Reward Models for Robotics</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/10</td><td><a href="https://arxiv.org/abs/2510.03827">LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2025/06</td><td><a href="https://arxiv.org/abs/2506.18088">RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation</a></td><td>ICML</td><td nowrap><a href="https://github.com/RoboTwin-Platform/RoboTwin">Code</a></td></tr>
<tr><td nowrap>2024/10</td><td><a href="https://arxiv.org/abs/2411.00081">PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks</a></td><td>ICLR</td><td nowrap><a href="https://github.com/facebookresearch/partnr-planner">Code</a></td></tr>
<tr><td nowrap>2024/06</td><td><a href="https://arxiv.org/abs/2406.02523">RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots</a></td><td>RSS</td><td nowrap><a href="https://github.com/robocasa/robocasa">Code</a></td></tr>
<tr><td nowrap>2024/03</td><td><a href="https://arxiv.org/abs/2403.09227">BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation</a></td><td>arXiv</td><td nowrap><a href="https://behavior.stanford.edu">Project</a> · <a href="https://github.com/StanfordVL/BEHAVIOR-1K">Code</a></td></tr>
<tr><td nowrap>2023/06</td><td><a href="https://arxiv.org/abs/2306.03310">LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning</a></td><td>NeurIPS</td><td nowrap><a href="https://libero-project.github.io/main.html">Project</a> · <a href="https://github.com/Lifelong-Robot-Learning/LIBERO">Code</a></td></tr>
<tr><td nowrap>2020/09</td><td><a href="https://arxiv.org/abs/2009.12293">robosuite: A Modular Simulation Framework and Benchmark for Robot Learning</a></td><td>arXiv</td><td nowrap><a href="https://github.com/ARISE-Initiative/robosuite">Code</a></td></tr>
<tr><td nowrap>2019/09</td><td><a href="https://arxiv.org/abs/1909.12271">RLBench: The Robot Learning Benchmark &amp; Learning Environment</a></td><td>RA-L</td><td nowrap><a href="https://github.com/stepjam/RLBench">Code</a></td></tr>
</tbody>
</table>

### Harness

#### Orchestration

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29204">AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.18520">AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Admire-ljb/AeroWeaver">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29166">HarnessPAI: An Evolving Harness for Physical AI</a></td><td>arXiv</td><td nowrap><a href="https://darwin-agent.github.io/HarnessPAI">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29394">RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.23997">RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.09516">HarnessWAM: Bridging Prediction and Deliberation in World Action Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.15549">MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration</a></td><td>arXiv</td><td nowrap><a href="https://wangxiaoshawn.github.io/MistyPilot.html">Project</a> · <a href="https://github.com/WangXiaoShawn/MistyPilot">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.22657">Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Liuuuxy/physical-agentic-ai">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.30396">Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.11246">Towards the Harness of Embodied Agents</a></td><td>arXiv</td><td nowrap><a href="https://eit-hai.github.io/thea">Project</a> · <a href="https://github.com/EIT-HAI/Thea">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.11377">A Glimpse into Long-term Physical Coexistence with Intelligent Robots</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10350">ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.21725">Addressing the Orchestration Gap in Generalist Robots via Physical Agency</a></td><td>arXiv</td><td nowrap><a href="https://lianegalanti.github.io/Pigey/">Project</a> · <a href="https://github.com/lianegalanti/Pigey">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.05377">Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://steinate.github.io/cortex.github.io">Project</a> · <a href="https://github.com/InternRobotics/Cortex">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.08448">Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents</a></td><td>arXiv</td><td nowrap><a href="https://harnessvla.github.io/">Project</a> · <a href="https://github.com/RLinf/RPent">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.17213">Retriever: Composing the Perception-Reasoning-Action Loop for Long-Horizon Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/openretriever/retriever">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.18060">RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.18363">Guava: An Effective and Universal Harness for Embodied Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://guava-harness.github.io">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.07723">VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://chicychen.github.io/VoLo/">Project</a> · <a href="https://github.com/NVlabs/VoLoAgent">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.10267">What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents</a></td><td>arXiv</td><td nowrap><a href="http://jiahenghu.github.io/hi-vla">Project</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.26637">Enabling Extensible Embodied Capabilities with Tools</a></td><td>arXiv</td><td nowrap><a href="https://racingemperor.github.io/manip-tool-hub/">Project</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.13119">Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.11975">M2HRI: An LLM-Driven Multimodal Multi-Agent Framework for Personalized Human-Robot Interaction</a></td><td>arXiv</td><td nowrap><a href="https://project-m2hri.github.io/">Project</a> · <a href="https://github.com/project-m2hri/m2hri">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.04664">ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration</a></td><td>arXiv</td><td nowrap><a href="https://www.rosclaw.io/">Project</a> · <a href="https://github.com/ros-claw/rosclaw">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.07892">RoboRouter: Training-Free Policy Routing for Robotic Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.26997">ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.19510">ALRM: Agentic LLM for Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://tiiuae.github.io/ALRM">Project</a></td></tr>
<tr><td nowrap>2024/10</td><td><a href="https://arxiv.org/abs/2410.22662">EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents</a></td><td>ICLR</td><td nowrap><a href="https://emos-project.github.io/">Project</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.04738">RoCo: Dialectic Multi-Robot Collaboration with Large Language Models</a></td><td>ICRA</td><td nowrap><a href="https://project-roco.github.io">Project</a> · <a href="https://github.com/MandiZhao/robot-collab">Code</a></td></tr>
</tbody>
</table>

#### Memory

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.11308">2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://leeibo.github.io/ActiveArena">Project</a> · <a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29204">AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.13335">Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29166">HarnessPAI: An Evolving Harness for Physical AI</a></td><td>arXiv</td><td nowrap><a href="https://darwin-agent.github.io/HarnessPAI">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.26360">Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.15976">MessyMem: Learning-from-Doing Memory for Mobile Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://messymem.github.io">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27526">NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08444">Safe Task Planning with Long-Term Graph Memory for Embodied Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.28429">Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29964">World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.16889">Don&#x27;t Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.04933">Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.30396">Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.09410">Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.23784">A Few Words Go a Long Way: Language Guided Robot Policy Synthesis</a></td><td>arXiv</td><td nowrap><a href="https://robo-architect.github.io/">Project</a> · <a href="https://github.com/robo-architect/architect-franka">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10350">ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.29600">HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.03449">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td><td>ICML</td><td nowrap><a href="https://github.com/HappyWaterXP/HiMe">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.14252">MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning</a></td><td>arXiv</td><td nowrap><a href="https://yuzihaowashu.github.io/MEMORA/">Project</a> · <a href="https://github.com/yuzihaowashu/MEMORA">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.23565">HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2607.13049">SPINE: Bridging the Cyber-Physical Gap with Agentic AI</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.10332">EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents</a></td><td>arXiv</td><td nowrap><a href="https://github.com/air-embodied-brain/EmbodiSkill">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.18729">Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction</a></td><td>arXiv</td><td nowrap><a href="https://robocortex66.github.io/robo-cortex/">Project</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.18271">EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.13533">Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.12872">OVAL: Open-Vocabulary Augmented Memory Model for Lifelong Object Goal Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02772">Agentic Self-Evolutionary Replanning for Embodied Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.07997">CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.12939">RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics</a></td><td>ECCV</td><td nowrap><a href="https://robostream123.github.io/">Project</a> · <a href="https://github.com/yu2hi13/RoboStream">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2602.00551">APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation</a></td><td>CVPR</td><td nowrap><a href="https://github.com/4amGodvzx/apex">Code</a></td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.20577">MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization</a></td><td>AAMAS</td><td nowrap><a href="https://github.com/TomWang-NPU/MeCo">Code</a></td></tr>
</tbody>
</table>

#### Monitoring

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.20822">Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19413">From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation</a></td><td>arXiv</td><td nowrap><a href="https://yy-gx.github.io/HALTER/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.08444">Safe Task Planning with Long-Term Graph Memory for Embodied Agents</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10350">ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.06256">Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.23532">Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.26349">Closing the Loop in Teleoperation: Episode-Level Data Quality Assessment and Feedback for High-Quality Demonstration Collection</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2605.11951">From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS</td><td nowrap><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.10682">OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02115">Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons</a></td><td>RSS</td><td nowrap><a href="https://robometer.github.io/">Project</a> · <a href="https://github.com/robometer/robometer">Code</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.12281">Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.18492">DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation</a></td><td>arXiv</td><td nowrap><a href="https://github.com/PlumJun/DV-VLN">Code</a></td></tr>
<tr><td nowrap>2024/12</td><td><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td><td>CVPR</td><td nowrap><a href="https://zhoues.github.io/Code-as-Monitor">Project</a></td></tr>
<tr><td nowrap>2024/10</td><td><a href="https://arxiv.org/abs/2410.00371">AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation</a></td><td>ICLR</td><td nowrap><a href="https://aha-vlm.github.io/">Project</a> · <a href="https://github.com/NVlabs/AHA">Code</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.00329">DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment</a></td><td>IROS</td><td nowrap><a href="https://sites.google.com/view/doremi-paper">Project</a></td></tr>
<tr><td nowrap>2023/06</td><td><a href="https://arxiv.org/abs/2306.15724">REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction</a></td><td>CoRL</td><td nowrap><a href="https://robot-reflect.github.io/">Project</a> · <a href="https://github.com/real-stanford/reflect">Code</a></td></tr>
</tbody>
</table>

#### Recovery

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19413">From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation</a></td><td>arXiv</td><td nowrap><a href="https://yy-gx.github.io/HALTER/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.15195">HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.05178">LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models</a></td><td>arXiv</td><td nowrap><a href="https://liulin815.github.io/LIBERO-Recovery/">Project</a> · <a href="https://github.com/liulin815/LIBERO-Recovery">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.06508">VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.03924">ETA: A New Agentic Paradigm for Embodied Tasks</a></td><td>arXiv</td><td nowrap><a href="https://github.com/OpenMOSS/OpenETA">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.26645">FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation</a></td><td>CVPR</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.09516">HarnessWAM: Bridging Prediction and Deliberation in World Action Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.06990">A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation</a></td><td>RSS</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.04162">ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.21725">Addressing the Orchestration Gap in Generalist Robots via Physical Agency</a></td><td>arXiv</td><td nowrap><a href="https://lianegalanti.github.io/Pigey/">Project</a> · <a href="https://github.com/lianegalanti/Pigey">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.16636">PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/PhyAgentOS/PhyAgentOS-core">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.22999">WCM: World-Cognition Model for Generalizable Human-Robot Interaction</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.13578">LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories</a></td><td>arXiv</td><td nowrap><a href="https://zjunlp.github.io/LabVLA">Project</a> · <a href="https://github.com/zjunlp/LabVLA">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.09630">ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.07723">VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://chicychen.github.io/VoLo/">Project</a> · <a href="https://github.com/NVlabs/VoLoAgent">Code</a></td></tr>
<tr><td nowrap>2026/05</td><td><a href="https://arxiv.org/abs/2606.00104">PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs</a></td><td>arXiv</td><td nowrap><a href="https://github.com/erdemuysalx/PEACE">Code</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.07395">A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring</a></td><td>arXiv</td><td nowrap><a href="https://wenzewwz123.github.io/Agentic-Loop/">Project</a></td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.13942">Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.02318">Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02772">Agentic Self-Evolutionary Replanning for Embodied Navigation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.13528">Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis</a></td><td>arXiv</td><td nowrap><a href="https://dream2fix.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/02</td><td><a href="https://arxiv.org/abs/2602.13081">Agentic AI for Robot Control: Flexible but still Fragile</a></td><td>AAAI-SS</td><td nowrap><a href="https://dfki-ni.github.io/AGENTS-MAKE-2026">Project</a></td></tr>
<tr><td nowrap>2023/07</td><td><a href="https://arxiv.org/abs/2307.00329">DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment</a></td><td>IROS</td><td nowrap><a href="https://sites.google.com/view/doremi-paper">Project</a></td></tr>
<tr><td nowrap>2023/06</td><td><a href="https://arxiv.org/abs/2306.15724">REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction</a></td><td>CoRL</td><td nowrap><a href="https://robot-reflect.github.io/">Project</a> · <a href="https://github.com/real-stanford/reflect">Code</a></td></tr>
</tbody>
</table>

#### Skill Synthesis

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.12541">Agent as Policy for Robotic Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.16346">Auto-HSI: Personalized human control of a robot swarm on demand by using LLMs for online automatic code generation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv</td><td nowrap><a href="https://embodiedswe.github.io/">Project</a> · <a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.26499">Generalizing Manipulation Skills with a Local Coding Agent</a></td><td>arXiv</td><td nowrap><a href="https://rtalwar2.github.io/agentic-coding-for-robot-manipulation/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.09808">GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes</a></td><td>arXiv</td><td nowrap><a href="https://gta2-project.github.io/">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29394">RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.30249">RAPID: Robot Agentic Programming from Demonstrations</a></td><td>arXiv</td><td nowrap><a href="https://yuyaoliu.me/projects/rapid">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.18435">WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories</a></td><td>arXiv</td><td nowrap><a href="https://github.com/tsudalab/WetRobo">Code</a></td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.17209">Teach and Grow: An Agent-Centered Architecture for General Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.23784">A Few Words Go a Long Way: Language Guided Robot Policy Synthesis</a></td><td>arXiv</td><td nowrap><a href="https://robo-architect.github.io/">Project</a> · <a href="https://github.com/robo-architect/architect-franka">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.05369">GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks</a></td><td>arXiv</td><td nowrap><a href="https://graph-robots.github.io/gap">Project</a> · <a href="https://github.com/graph-robots/graph-as-policy">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.22832">MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/sygkounas/MEMENTO">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2607.00272">ASPIRE: Agentic /Skills Discovery for Robotics</a></td><td>arXiv</td><td nowrap><a href="https://research.nvidia.com/labs/gear/aspire/">Project</a> · <a href="https://github.com/NVlabs/ASPIRE">Code</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.19419">Playful Agentic Robot Learning</a></td><td>arXiv</td><td nowrap><a href="https://Playful-RATs.github.io">Project</a> · <a href="https://github.com/Playful-RATs/RATs">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.22435">CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation</a></td><td>ICML</td><td nowrap><a href="https://capgym.github.io">Project</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02669">IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.02623">Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/01</td><td><a href="https://arxiv.org/abs/2601.19510">ALRM: Agentic LLM for Robotic Manipulation</a></td><td>arXiv</td><td nowrap><a href="https://tiiuae.github.io/ALRM">Project</a></td></tr>
<tr><td nowrap>2022/09</td><td><a href="https://arxiv.org/abs/2209.07753">Code as Policies: Language Model Programs for Embodied Control</a></td><td>ICRA</td><td nowrap><a href="https://code-as-policies.github.io">Project</a> · <a href="https://github.com/google-research/google-research/tree/master/code_as_policies">Code</a></td></tr>
</tbody>
</table>

#### Evolution

<table width="100%">
<thead><tr>
<th width="10%" align="left">Date</th>
<th width="65%" align="left">Paper</th>
<th width="10%" align="left">Venue</th>
<th width="15%" align="left">Resources</th>
</tr></thead>
<tbody>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29204">AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution</a></td><td>arXiv</td><td nowrap><a href="https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA">Code</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29166">HarnessPAI: An Evolving Harness for Physical AI</a></td><td>arXiv</td><td nowrap><a href="https://darwin-agent.github.io/HarnessPAI">Project</a></td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.19906">Learning and Transferring Closed-Loop Robot Software</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/09</td><td><a href="https://arxiv.org/abs/2609.29394">RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.18227">Revisiting the &quot;Push-T&quot; Robot Manipulation Task with Agentic Robotics</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.11350">Self-Evolving Embodied Agents via Skill-Harness Evolution</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.09410">Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.07555">You Don&#x27;t Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/08</td><td><a href="https://arxiv.org/abs/2608.16590">Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence</a></td><td>arXiv</td><td nowrap><a href="https://air-embodied-brain.github.io/zetta">Project</a> · <a href="https://github.com/air-embodied-brain/Zetta-Embodiment">Code</a></td></tr>
<tr><td nowrap>2026/07</td><td><a href="https://arxiv.org/abs/2607.10350">ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2606.16458">RHO: Your Coding Agent is Secretly a Roboticist</a></td><td>arXiv</td><td nowrap><a href="https://rho-robotics.github.io">Project</a></td></tr>
<tr><td nowrap>2026/06</td><td><a href="https://arxiv.org/abs/2607.13049">SPINE: Bridging the Cyber-Physical Gap with Agentic AI</a></td><td>arXiv</td><td nowrap>—</td></tr>
<tr><td nowrap>2026/04</td><td><a href="https://arxiv.org/abs/2604.10096">ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents</a></td><td>arXiv</td><td nowrap><a href="https://github.com/amap-cvlab/ABot-Claw">Code</a></td></tr>
<tr><td nowrap>2026/03</td><td><a href="https://arxiv.org/abs/2603.04466">Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation</a></td><td>arXiv</td><td nowrap>—</td></tr>
</tbody>
</table>

<!-- END AUTO-GENERATED PAPER LIST -->

<!-- ## Citation -->

<!-- The survey's final publication identifier and BibTeX citation are pending. Please use the official citation once released. -->

<!-- Replace this notice with the author-confirmed survey BibTeX upon release. -->

## Contributing

Paper suggestions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and submission details.
