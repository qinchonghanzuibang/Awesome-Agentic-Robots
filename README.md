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

Works can span several categories. Such associations describe the survey's organization; they do not imply that every component operates jointly in one configuration. Venue labels include the conference event or journal publication year; arXiv labels use the first posting year.

## Taxonomy

| Domain | Categories |
| --- | --- |
| **Model** | [Training](#training) · [Perception](#perception) · [Planning](#planning) · [Robot Control](#robot-control) · [Adaptation](#adaptation) |
| **Data** | [Collection](#collection) · [Annotation](#annotation) · [Refinement](#refinement) |
| **Environment** | [Reconstruction](#reconstruction) · [Task Generation](#task-generation) · [Benchmarking](#benchmarking) |
| **Harness** | [Orchestration](#orchestration) · [Memory](#memory) · [Monitoring and Recovery](#monitoring-and-recovery) · [Skills](#skills) · [Infrastructure](#infrastructure) · [Layered Systems](#layered-systems) |

## Papers

Entries follow the visible literature tables of the current manuscript, ordered by publication year (newest first) within each category. Metadata is stored once in [data/papers.yaml](data/papers.yaml), with all visible category placements retained. A dash in Code means no relevant public implementation was verified in the manuscript. A superscript * follows the manuscript's marking of acceptance pending verification of formal publication.

<!-- BEGIN AUTO-GENERATED PAPER LIST -->

### Model

#### Training

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2603.27416">Agent-Driven Autonomous Reinforcement Learning Research: Iterative Policy Improvement for Quadruped Locomotion</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.23280">Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/ZJU4EmbodiedAI/EmbodiedSkills">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.19980">ENPIRE: Agentic Robot Policy Self-Improvement in the Real World</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/NVlabs/ENPIRE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.11859">EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.17210">FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence</a></td><td>arXiv 26</td><td><a href="https://github.com/FluxVLA/FluxVLA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.00083">From Demonstrations to Rewards: Test-Time Prompt Optimization for VLM Reward Models</a></td><td>RLJ 26</td><td><a href="https://github.com/cgumbsch/Demo2Reward">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.08610">HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning</a></td><td>arXiv 26</td><td><a href="https://github.com/supersglzc/harbor-rl">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.00416">Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.11665">Nautilus: From One Prompt to Plug-and-Play Robot Learning</a></td><td>NeurIPS 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.09630">ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.01672">Reward Design Agent for Reinforcement Learning</a></td><td>RLJ 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv 26</td><td><a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.07555">You Don&#x27;t Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2310.12931">Eureka: Human-Level Reward Design via Coding Large Language Models</a></td><td>ICLR 24</td><td><a href="https://github.com/eureka-research/Eureka">Code</a></td></tr>
</tbody>
</table>

#### Perception

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2606.06061">A Conversational Framework for Human-Robot Collaborative Manipulation with Distributed Generative AI models</a></td><td>RO-MAN 26<sup>*</sup></td><td><a href="https://github.com/cogrob-tuni/franka-llm">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.04157">A Modern System Recipe for Situated Embodied Human-Robot Conversation with Real-Time Multimodal LLMs and Tool-Calling</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.10383">ABot-N1: Toward a General Visual Language Navigation Foundation Model</a></td><td>arXiv 26</td><td><a href="https://github.com/amap-cvlab/ABot-Navigation">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.10577">AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.12285">AnchorVLN: Geometry-Anchored Vision-Language Grounding Reasoning for Open-Vocabulary Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/aryanmangal769/embodied-nav-mcp">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.14681">FARE: Fast-Slow Agentic Robotic Exploration</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.18210">GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.02653">HINT: Human-Intent Inception for Long-Horizon Robot Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/robot-hint/HINT">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.20615">INSPECT: Learning Robot View Selection from Assistant Use</a></td><td>arXiv 26</td><td><a href="https://github.com/Kratos-Wen/INSPECT">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.17129">MG-VQA: Manipulation Grounded Visual Question Answering with VLMs</a></td><td>arXiv 26</td><td><a href="https://github.com/vineet2104/MG-VQA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.05377">OpenFrontier: General Navigation with Visual-Language Grounded Frontiers</a></td><td>RSS 26</td><td><a href="https://github.com/cvg/OpenFrontier">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv 26</td><td><a href="https://github.com/Robo-Harness/k1">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.26988">Robot Planning and Situation Handling with Active Perception</a></td><td>IROS 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.04610">RoboVista: Evaluating Vision Language Models for Diverse Robot Applications</a></td><td>RSS 26</td><td><a href="https://github.com/ehehee/robovista">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.02951">SCOPE: Real-Time Natural Language Camera Agent at the Edge</a></td><td>HRI 26</td><td><a href="https://github.com/HindsboNikolaj/SCOPE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.13193">Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control</a></td><td>RSS 26</td><td><a href="https://github.com/steerable-policies/steerable-policies-bridge">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.13143">SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation</a></td><td>NeurIPS 25</td><td><a href="https://github.com/qizekun/SoFar">Code</a></td></tr>
</tbody>
</table>

#### Planning

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2609.05985">A Brain-inspired Hierarchical Framework for Zero-Shot Robot Task Reasoning and Execution</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td><a href="https://www.mdpi.com/1424-8220/26/17/5595">Adaptive Task Planning for Long-Horizon Robotic Manipulation Based on Video Priors and Dynamic Scene Graphs</a></td><td>Sensors 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.13081">Agentic AI for Robot Control: Flexible but still Fragile</a></td><td>AAAI-SS 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.13591">AgentRob: From Virtual Forum Agents to Hijacked Physical Robots</a></td><td>arXiv 26</td><td><a href="https://github.com/PKU-LLM-DS-LAB/AgentRob">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.13335">Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.18492">DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/PlumJun/DV-VLN">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.11063">EmboTeam: Grounding LLM Reasoning into Reactive Behavior Trees via PDDL for Embodied Multi-Robot Collaboration</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.13533">Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization</a></td><td>IJCNN 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.03148">From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?</a></td><td>ICRA 26<sup>*</sup></td><td><a href="https://github.com/ShinasShaji/llm-robot-cognition">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19315">GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.26360">Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering</a></td><td>arXiv 26</td><td><a href="https://github.com/ntnu-arl/hflex_eqa">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.21670">Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning</a></td><td>ICRA 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.06501">Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning</a></td><td>RSS 26</td><td><a href="https://github.com/threefruits/HUME">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02669">IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models</a></td><td>ICRA 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv 26</td><td><a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.27871">LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.28300">MaCoPlanner: LLM-Assisted Manual-Compiled Task Planning with Proactive Safety Verification for Robotic Industrial Panel Operation</a></td><td>arXiv 26</td><td><a href="https://github.com/XinGP/MaCoPlanner">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.11561">Memory as Plans: World-Action Modeling with Memory-Grounded Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27526">NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/liujy25/NavProbe">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08444">Safe Task Planning with Long-Term Graph Memory for Embodied Agents</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.30396">Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02772">Self-Evolutionary Replanning for Failure-Aware Motion Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1848830/full">STARS: extending interactive task learning with large language models</a></td><td>Front. Comput. Sci. 26</td><td><a href="https://github.com/Center-for-Integrated-Cognition/STARS">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.22999">WCM: World-Cognition Model for Generalizable Human-Robot Interaction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2510.03342">Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td><td>ICML 25</td><td>—</td></tr>
<tr><td><a href="https://proceedings.mlr.press/v305/feng25b.html">Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation</a></td><td>CoRL 25</td><td><a href="https://github.com/yunhaif/reflect-vlm">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.04738">RoCo: Dialectic Multi-Robot Collaboration with Large Language Models</a></td><td>ICRA 24</td><td><a href="https://github.com/MandiZhao/robot-collab">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.01928">Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners</a></td><td>CoRL 23</td><td><a href="https://github.com/google-research/google-research/tree/master/language_model_uncertainty">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.06135">SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning</a></td><td>CoRL 23</td><td>—</td></tr>
</tbody>
</table>

#### Robot Control

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2607.10383">ABot-N1: Toward a General Visual Language Navigation Foundation Model</a></td><td>arXiv 26</td><td><a href="https://github.com/amap-cvlab/ABot-Navigation">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.29379">Bridging Semantics and Physics with Constrained LLMs for Safe and Trustworthy Robotic Manipulation</a></td><td>ECCV-W 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.28247">Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.02600">CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation</a></td><td>RSS 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.20334">Demonstration-Free Robotic Control via LLM Agents</a></td><td>IROS 26<sup>*</sup></td><td><a href="https://github.com/robiemusketeer/faea-sim">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.26148">Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/jianzhou0420/AgentCanvas/tree/archive/mip-embodied-agents-take-control">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.03924">ETA: A New Agentic Paradigm for Embodied Tasks</a></td><td>arXiv 26</td><td><a href="https://github.com/OpenMOSS/OpenETA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.14047">Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use</a></td><td>CVPR Findings 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19138">In-Context Robot Learning with VLM Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/cheng-haha/GPT-Policy">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19347">Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.18869">KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.12299">Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.16331">ManiSkillFormer: Demonstration-Free Compositional Manipulation via Geometric Contracts and Agentic Skill Graph</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.22832">MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution</a></td><td>arXiv 26</td><td><a href="https://github.com/sygkounas/MEMENTO">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv 26</td><td><a href="https://github.com/Robo-Harness/k1">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.02951">SCOPE: Real-Time Natural Language Camera Agent at the Edge</a></td><td>HRI 26</td><td><a href="https://github.com/HindsboNikolaj/SCOPE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.10522">Show-Harness: Just a VLM Agent Can Play Robots</a></td><td>arXiv 26</td><td><a href="https://github.com/showlab/Show-Harness">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.22966">Transferring the Intelligence of VLMs to Robotic Control</a></td><td>arXiv 26</td><td><a href="https://github.com/Hugo-AGI/RoboDawn">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.11119">VIA: Visual Interface Agent for Robot Control</a></td><td>arXiv 26</td><td><a href="https://github.com/hengyuan-hu/via">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.28429">Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29964">World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2409.01652">ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation</a></td><td>CoRL 24</td><td><a href="https://github.com/huangwl18/ReKep">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td><td>CoRL 23</td><td><a href="https://github.com/huangwl18/VoxPoser">Code</a></td></tr>
</tbody>
</table>

#### Adaptation

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2603.07997">CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/ZJU4EmbodiedAI/EmbodiedSkills">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19138">In-Context Robot Learning with VLM Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/cheng-haha/GPT-Policy">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv 26</td><td><a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.00416">Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.20323">PhysMem: Scaling Test-Time Memory for Embodied Physical Reasoning</a></td><td>arXiv 26</td><td><a href="https://github.com/haoyangli16/PhysMem">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.26809">Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02772">Self-Evolutionary Replanning for Failure-Aware Motion Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.22966">Transferring the Intelligence of VLMs to Robotic Control</a></td><td>arXiv 26</td><td><a href="https://github.com/Hugo-AGI/RoboDawn">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.18247">Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement</a></td><td>RSS 26</td><td><a href="https://github.com/princeton-prism/veritas">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.12063">VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model</a></td><td>ICML 26</td><td><a href="https://github.com/Robert-gyj/Ctrl-World">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.22474">When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering</a></td><td>RSS 26</td><td><a href="https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2509.15155">Self-Improving Embodied Foundation Models</a></td><td>NeurIPS 25</td><td><a href="https://github.com/self-improving-efms/self-improving-efms.github.io/blob/main/pointmass_notebook.ipynb">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2511.14759">π*₀.₆: A VLA That Learns From Experience</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2311.10678">Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections</a></td><td>ICRA 24</td><td><a href="https://github.com/Stanford-ILIAD/droc">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2402.11450">Learning to Learn Faster from Human Feedback with Language Model Predictive Control</a></td><td>RSS 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2403.12910">Yell At Your Robot: Improving On-the-Fly from Language Corrections</a></td><td>RSS 24</td><td><a href="https://github.com/yay-robot/yay_robot">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2310.17555">Interactive Robot Learning from Verbal Correction</a></td><td>LangRob Workshop 23<sup>*</sup></td><td><a href="https://github.com/UT-Austin-RPL/olaf">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2212.07398">Policy Adaptation from Foundation Model Feedback</a></td><td>CVPR 23</td><td><a href="https://github.com/geyuying/PAFF_code">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2306.11706">RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation</a></td><td>TMLR 23</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2305.05658">TidyBot: Personalized Robot Assistance with Large Language Models</a></td><td>Auton. Robots 23</td><td><a href="https://github.com/jimmyyhwu/tidybot">Code</a></td></tr>
</tbody>
</table>

### Data

#### Collection

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.38905">EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.32069">Find Something You Can&#x27;t Do: Agentic Real-World Reinforcement Learning for Self-Improving VLA Models</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.18742">RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv 26</td><td><a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.23997">RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.03278">Tether: Autonomous Functional Play with Correspondence-Driven Trajectory Warping</a></td><td>ICLR 26</td><td><a href="https://github.com/tether-research/tether">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.18811">V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.22136">Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data</a></td><td>arXiv 26</td><td><a href="https://github.com/chenyt31/Wh0">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.22474">When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering</a></td><td>RSS 26</td><td><a href="https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv 26</td><td><a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2507.00833">HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning</a></td><td>NeurIPS 25</td><td><a href="https://github.com/TeleHuman/HumanoidGen">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2503.16408">RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints</a></td><td>ICCV 25</td><td><a href="https://github.com/MARS-EAI/RoboFactory">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2407.20635">Autonomous Improvement of Instruction Following Skills via Foundation Models</a></td><td>CoRL 24</td><td><a href="https://github.com/rail-berkeley/soar">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2311.01455">RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation</a></td><td>ICML 24</td><td><a href="https://github.com/Genesis-Embodied-AI/RoboGen">Code</a></td></tr>
</tbody>
</table>

#### Annotation

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2512.14442">A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning</a></td><td>ECCV 26</td><td><a href="https://github.com/EnVision-Research/A4-Agent">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.00663">Affordance Agent Harness: Verification-Gated Skill Orchestration</a></td><td>arXiv 26</td><td><a href="https://github.com/tenplusgood/A-Harness">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.04172">Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/arc-l/a2a">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.17446">AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.34484">ARS: Agentic Reward System for Robot Learning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.16046">DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning</a></td><td>CVPR 26</td><td><a href="https://github.com/junha-l/dexter">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.39378">EgoTools: Towards Tool-Centric Reasoning in Real-World Egocentric Videos</a></td><td>EMNLP 26<sup>*</sup></td><td><a href="https://github.com/Ropedia/EgoTools">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.07459">EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI</a></td><td>arXiv 26</td><td><a href="https://github.com/HorizonRobotics/EmbodiedGen">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.37655">Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding</a></td><td>NeurIPS 26<sup>*</sup></td><td><a href="https://github.com/yingjiayu12/Exemplar2VQA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.13653">Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation</a></td><td>ECCV 26</td><td><a href="https://github.com/InternRobotics/REAL">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2505.08548">From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation</a></td><td>ICLR 26</td><td><a href="https://github.com/pickxiguapi/Embodied-FSD">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.13497">SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/intuitive-robots/sparc">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.00438">Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv 26</td><td><a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
<tr><td><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Kou_RoboAnnotatorX_A_Comprehensive_and_Universal_Annotation_Framework_for_Accurate_Understanding_ICCV_2025_paper.html">RoboAnnotatorX: A Comprehensive and Universal Annotation Framework for Accurate Understanding of Long-horizon Robot Demonstration</a></td><td>ICCV 25</td><td><a href="https://github.com/LongXinKou/RoboannotatorX">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2411.16537">RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics</a></td><td>CVPR 25</td><td><a href="https://github.com/NVlabs/RoboSpatial">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2508.01943">ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks</a></td><td>NeurIPS 25</td><td><a href="https://github.com/Philip-MIT/rover-vlm">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2407.08693">Robotic Control via Embodied Chain-of-Thought Reasoning</a></td><td>CoRL 24</td><td><a href="https://github.com/MichalZawalski/embodied-CoT">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.17772">Scaling Robot Policy Learning via Zero-Shot Labeling with Foundation Models</a></td><td>CoRL 24</td><td><a href="https://github.com/intuitive-robots/NILS">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2401.12168">SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities</a></td><td>CVPR 24</td><td>—</td></tr>
</tbody>
</table>

#### Refinement

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2609.34484">ARS: Agentic Reward System for Robot Learning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.21198">Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</a></td><td>arXiv 26</td><td><a href="https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.22142">RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations</a></td><td>arXiv 26</td><td><a href="https://github.com/robolineage/robolineage">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.14047">Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment</a></td><td>arXiv 26</td><td><a href="https://github.com/open-gigaai/Zero2Skill">Code</a></td></tr>
</tbody>
</table>

### Environment

#### Reconstruction

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2610.03715">4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes</a></td><td>arXiv 26</td><td><a href="https://github.com/4DCodeBench/4DCodeBench">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.19190">Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/agentic-real2sim/agentic_real2sim">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.15187">Articraft: An Agentic System for Scalable Articulated 3D Asset Generation</a></td><td>NeurIPS 26<sup>*</sup></td><td><a href="https://github.com/mattzh72/articraft">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2610.02274">Awomo-SimDataEngine: Agentic Simulation-Ready World Generation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.14398">ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.36777">Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.36024">CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.35318">DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.05241">DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.23103">DiagGen: Agentic Generation of Deformable Assets with Sim-based Diagnostics for Robotic Simulation</a></td><td>arXiv 26</td><td><a href="https://github.com/diaggen/diaggen">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.07459">EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI</a></td><td>arXiv 26</td><td><a href="https://github.com/HorizonRobotics/EmbodiedGen">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.02078">Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot</a></td><td>arXiv 26</td><td><a href="https://github.com/AgibotTech/genie_sim">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.05927">GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.36380">LEGO-Anything: Coding Agents for 3D Scene Reconstruction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.30249">RAPID: Robot Agentic Programming from Demonstrations</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS 26</td><td><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.10116">SAGE: Scalable Agentic 3D Scene Generation for Embodied AI</a></td><td>CVPR 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.09153">SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes</a></td><td>ICML 26</td><td><a href="https://github.com/nepfaff/scenesmith">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.28276">SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation</a></td><td>arXiv 26</td><td><a href="https://github.com/NVlabs/SimFoundry">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.09423">SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2610.04432">Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos</a></td><td>arXiv 26</td><td><a href="https://github.com/AetherLabsAI/Video2World">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.13882">Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model</a></td><td>ICLR 25</td><td><a href="https://github.com/vlongle/articulate-anything">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv 25</td><td>—</td></tr>
</tbody>
</table>

#### Task Generation

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2609.24563">ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2610.07969">EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.01505">FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.08664">GenPHRI: Agentic Generative Simulation for Physical Human-Robot Interaction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.08610">HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning</a></td><td>arXiv 26</td><td><a href="https://github.com/supersglzc/harbor-rl">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.19419">Playful Agentic Robot Learning</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/Playful-RATs/RATs">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS 26</td><td><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.12065">Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.09423">SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2409.18382">CurricuLLM: Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models</a></td><td>ICRA 25</td><td><a href="https://github.com/labicon/CurricuLLM">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2411.00081">PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks</a></td><td>ICLR 25</td><td><a href="https://github.com/facebookresearch/partnr-planner">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.09886">Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2310.01361">GenSim: Generating Robotic Simulation Tasks via Large Language Models</a></td><td>ICLR 24</td><td><a href="https://github.com/liruiw/GenSim">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2311.01455">RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation</a></td><td>ICML 24</td><td><a href="https://github.com/Genesis-Embodied-AI/RoboGen">Code</a></td></tr>
</tbody>
</table>

#### Benchmarking

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2602.01640">A2Eval: Agentic and Automated Evaluation for Embodied Brain</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2610.00854">Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena</a></td><td>arXiv 26</td><td><a href="https://github.com/embodied-agent-arena/embodied-agent-arena">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.00272">ASPIRE: Agentic /Skills Discovery for Robotics</a></td><td>arXiv 26</td><td><a href="https://github.com/NVlabs/ASPIRE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.22435">CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation</a></td><td>ICML 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.08036">Compiling and Benchmarking Task-State Horizons for Embodied Agents</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.13082">Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv 26</td><td><a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.26637">Enabling Extensible Embodied Capabilities with Tools</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08292">EvoNav-Bench: Benchmarking Lifelong Navigation in Evolving Environments</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.08448">Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/RLinf/RPent">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.25788">KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning</a></td><td>RSS 26</td><td><a href="https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden">Code</a></td></tr>
<tr><td><a href="https://proceedings.iclr.cc/paper_files/paper/2026/hash/8833c8aa10542d24d693bbaf6a4598f5-Abstract-Conference.html">ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies</a></td><td>ICLR 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.10895">ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.18060">RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning</a></td><td>ECCV-W 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS 26</td><td><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.10921">RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark</a></td><td>arXiv 26</td><td><a href="https://github.com/OpenHelix-Team/RoboMemArena">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.05226">RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19554">VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.22014">Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/FraunhoferIVI/MissionBench">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.09560">EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents</a></td><td>ICML 25</td><td><a href="https://github.com/EmbodiedBench/EmbodiedBench">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2411.00081">PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks</a></td><td>ICLR 25</td><td><a href="https://github.com/facebookresearch/partnr-planner">Code</a></td></tr>
</tbody>
</table>

### Harness

#### Orchestration

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2607.10350">ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.21725">Addressing the Orchestration Gap in Generalist Robots via Physical Agency</a></td><td>arXiv 26</td><td><a href="https://github.com/lianegalanti/Pigey">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.18520">AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution</a></td><td>arXiv 26</td><td><a href="https://github.com/Admire-ljb/AeroWeaver">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.05377">Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/InternRobotics/Cortex">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.01281">EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/ZJU4EmbodiedAI/EmbodiedSkills">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.26637">Enabling Extensible Embodied Capabilities with Tools</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.18363">Guava: Distilling Frontier VLMs into a Compact Agent through a Robotic Manipulation Harness</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.09516">HarnessWAM: Bridging Prediction and Deliberation in World Action Models</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.11975">M2HRI: An LLM-Driven Multimodal Multi-Agent Framework for Personalized Human-Robot Interaction</a></td><td>arXiv 26</td><td><a href="https://github.com/project-m2hri/m2hri">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.15549">MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration</a></td><td>ECCV-W 26<sup>*</sup></td><td><a href="https://github.com/WangXiaoShawn/MistyPilot">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.22657">Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs</a></td><td>arXiv 26</td><td><a href="https://github.com/Liuuuxy/physical-agentic-ai">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.17213">Retriever: Composing the Perception-Reasoning-Action Loop for Long-Horizon Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/openretriever/retriever">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.18060">RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning</a></td><td>ECCV-W 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.07892">RoboRouter: Training-Free Policy Routing for Robotic Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.23997">RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.26997">ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08402">Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.13119">Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.11246">Towards the Harness of Embodied Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/EIT-HAI/Thea">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.07723">VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/NVlabs/VoLoAgent">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.22662">EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents</a></td><td>ICLR 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.04738">RoCo: Dialectic Multi-Robot Collaboration with Large Language Models</a></td><td>ICRA 24</td><td><a href="https://github.com/MandiZhao/robot-collab">Code</a></td></tr>
</tbody>
</table>

#### Memory

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2609.11308">2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.24124">ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation</a></td><td>arXiv 26</td><td><a href="https://github.com/leeibo/ActiveArena">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.00551">APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation</a></td><td>CVPR 26</td><td><a href="https://github.com/4amGodvzx/apex">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.13335">Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.07997">CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27720">CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.16889">Don&#x27;t Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.18271">EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents</a></td><td>IROS 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.10332">EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/air-embodied-brain/EmbodiSkill">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.13533">Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization</a></td><td>IJCNN 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.29600">HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.26360">Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering</a></td><td>arXiv 26</td><td><a href="https://github.com/ntnu-arl/hflex_eqa">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.03449">HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control</a></td><td>ICML 26</td><td><a href="https://github.com/HappyWaterXP/HiMe">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.23565">HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.20577">MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization</a></td><td>AAMAS 26</td><td><a href="https://github.com/TomWang-NPU/MeCo">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.14252">MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning</a></td><td>EMNLP 26<sup>*</sup></td><td><a href="https://github.com/yuzihaowashu/MEMORA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.15976">MessyMem: Learning-from-Doing Memory for Mobile Manipulation</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.04933">Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27526">NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/liujy25/NavProbe">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.12872">OVAL: Open-Vocabulary Augmented Memory Model for Lifelong Object Goal Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.18729">Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29389">Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation</a></td><td>arXiv 26</td><td><a href="https://github.com/Robo-Harness/k1">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.12939">RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics</a></td><td>ECCV 26</td><td><a href="https://github.com/yu2hi13/RoboStream">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.08444">Safe Task Planning with Long-Term Graph Memory for Embodied Agents</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.30396">Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.09410">Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.28429">Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams</a></td><td>CoRL 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29964">World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal</a></td><td>arXiv 26</td><td>—</td></tr>
</tbody>
</table>

#### Monitoring and Recovery

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2607.06990">A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation</a></td><td>RSS 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.07395">A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.04162">ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.13081">Agentic AI for Robot Control: Flexible but still Fragile</a></td><td>AAAI-SS 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.26349">Closing the Loop in Teleoperation: Episode-Level Data Quality Assessment and Feedback for High-Quality Demonstration Collection</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.20822">Coding Agents with Harness for Safe Robot Control</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.06256">Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition</a></td><td>RSS-W 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2601.18492">DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation</a></td><td>arXiv 26</td><td><a href="https://github.com/PlumJun/DV-VLN">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.26645">FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation</a></td><td>CVPR 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2605.11951">From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation</a></td><td>RSS 26</td><td><a href="https://github.com/EDEM-AI/AgentChord">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19413">From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.13942">Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.15195">HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.13578">LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories</a></td><td>arXiv 26</td><td><a href="https://github.com/zjunlp/LabVLA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.13528">Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.05178">LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models</a></td><td>arXiv 26</td><td><a href="https://github.com/liulin815/LIBERO-Recovery">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.23532">Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.10682">OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency</a></td><td>IROS 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.00104">PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs</a></td><td>ICRA-W 26<sup>*</sup></td><td><a href="https://github.com/erdemuysalx/PEACE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.16636">PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution</a></td><td>arXiv 26</td><td><a href="https://github.com/PhyAgentOS/PhyAgentOS-core">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.09630">ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.09860">RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies</a></td><td>RSS 26</td><td><a href="https://github.com/NVlabs/RoboLab">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02115">Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons</a></td><td>RSS 26</td><td><a href="https://github.com/robometer/robometer">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.12281">Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment</a></td><td>ECCV 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02772">Self-Evolutionary Replanning for Failure-Aware Motion Planning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.13049">SPINE: Bridging the Cyber-Physical Gap with Agentic AI</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.02318">Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.06508">VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.22999">WCM: World-Cognition Model for Generalizable Human-Robot Interaction</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.00371">AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation</a></td><td>ICLR 25</td><td><a href="https://github.com/NVlabs/AHA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2412.04455">Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection</a></td><td>CVPR 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.00329">DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment</a></td><td>IROS 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2306.15724">REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction</a></td><td>CoRL 23</td><td><a href="https://github.com/real-stanford/reflect">Code</a></td></tr>
</tbody>
</table>

#### Skills

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2607.23784">A Few Words Go a Long Way: Language Guided Robot Policy Synthesis</a></td><td>arXiv 26</td><td><a href="https://github.com/robo-architect/architect-franka">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.04466">Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.12541">Agent as Policy for Robotic Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2405.15019">Agentic Skill Discovery</a></td><td>RAS 26</td><td><a href="https://github.com/xf-zhao/Agentic-Skill-Discovery">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.00272">ASPIRE: Agentic /Skills Discovery for Robotics</a></td><td>arXiv 26</td><td><a href="https://github.com/NVlabs/ASPIRE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.22435">CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation</a></td><td>ICML 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.27308">EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</a></td><td>arXiv 26</td><td><a href="https://github.com/EmbodiedSWE/EmbodiedSWE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.19980">ENPIRE: Agentic Robot Policy Self-Improvement in the Real World</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/NVlabs/ENPIRE">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.37810">Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/SII-dannyXSC/RoboSkill">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29166">HarnessPAI: An Evolving Harness for Physical AI</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02669">IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models</a></td><td>ICRA 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.19906">Learning and Transferring Closed-Loop Robot Software</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.22832">MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution</a></td><td>arXiv 26</td><td><a href="https://github.com/sygkounas/MEMENTO">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.19419">Playful Agentic Robot Learning</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/Playful-RATs/RATs">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.29394">RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning</a></td><td>arXiv 26</td><td><a href="https://github.com/Robo-Harness/racap">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.30249">RAPID: Robot Agentic Programming from Demonstrations</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2610.02204">Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.16458">RHO: Your Coding Agent is Secretly a Roboticist</a></td><td>arXiv 26</td><td><a href="https://github.com/KE7/HELIX">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.11558">RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks</a></td><td>arXiv 26</td><td><a href="https://github.com/RoboClaw-Robotics/RoboClaw">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.11350">Self-Evolving Embodied Agents via Skill-Harness Evolution</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.14944">SkillComposer: Learning Reusable Skills for Natural-Language Robot Programming</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.17209">Teach and Grow: An Agent-Centered Architecture for General Robot Learning</a></td><td>arXiv 26</td><td><a href="https://github.com/IRMVLab/TGL">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.02623">Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation</a></td><td>ICRA 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.05395">VASO: Formally Verifiable Self-Evolving Skills for Physical AI Agents</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.31760">What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.07555">You Don&#x27;t Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.16590">Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence</a></td><td>arXiv 26</td><td><a href="https://github.com/air-embodied-brain/Zetta-Embodiment">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2509.18597">Robotic Ultra-Long-Horizon Manipulation Skills via Human-guided Lifelong Code Generation</a></td><td>arXiv 25</td><td><a href="https://github.com/Ghiara/LYRA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2311.10678">Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections</a></td><td>ICRA 24</td><td><a href="https://github.com/Stanford-ILIAD/droc">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2406.18746">Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models</a></td><td>ICRA 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2406.03757">RoboCoder: Robotic Learning from Basic Skills to General Tasks with Large Language Models</a></td><td>arXiv 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2402.16117">RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis</a></td><td>ICML 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2305.16291">Voyager: An Open-Ended Embodied Agent with Large Language Models</a></td><td>TMLR 24</td><td><a href="https://github.com/MineDojo/Voyager">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2209.07753">Code as Policies: Language Model Programs for Embodied Control</a></td><td>ICRA 23</td><td><a href="https://github.com/google-research/google-research/tree/master/code_as_policies">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2209.11302">ProgPrompt: Generating Situated Robot Task Plans using Large Language Models</a></td><td>ICRA 23</td><td><a href="https://github.com/NVlabs/progprompt-vh">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.05973">VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models</a></td><td>CoRL 23</td><td><a href="https://github.com/huangwl18/VoxPoser">Code</a></td></tr>
</tbody>
</table>

#### Infrastructure

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2608.00337">Action Chunk Scheduling for Batched Robot Policy Serving</a></td><td>arXiv 26</td><td><a href="https://github.com/GaTech-RL2/armory">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2506.07530">BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation</a></td><td>CoRL 26<sup>*</sup></td><td><a href="https://github.com/ustcwhy/BitVLA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.29379">Bridging Semantics and Physics with Constrained LLMs for Safe and Trustworthy Robotic Manipulation</a></td><td>ECCV-W 26<sup>*</sup></td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.19983">Contextual Safety Reasoning and Grounding for Open-World Robots</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.12075">Efficient Vision-Language-Action Management and Serving for Robot Factories</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2608.03924">ETA: A New Agentic Paradigm for Embodied Tasks</a></td><td>arXiv 26</td><td><a href="https://github.com/OpenMOSS/OpenETA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.05369">GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks</a></td><td>arXiv 26</td><td><a href="https://github.com/graph-robots/graph-as-policy">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.11225">Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.18397">How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf</a></td><td>arXiv 26</td><td><a href="https://github.com/NVlabs/vla-perf">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2602.22818">LeRobot: An Open-Source Library for End-to-End Robot Learning</a></td><td>ICLR 26</td><td><a href="https://github.com/huggingface/lerobot">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.14371">OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism</a></td><td>NeurIPS 26<sup>*</sup></td><td><a href="https://github.com/air-embodied-brain/OxyGen">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2604.05427">Pre-Execution Safety Gate &amp; Task Safety Contracts for LLM-Controlled Robot Systems</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2603.20711">RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models</a></td><td>IJCNN 26<sup>*</sup></td><td><a href="https://github.com/zhengzihaoPKU/RoboECC">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2512.21220">RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic</a></td><td>ICLR 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.01088">ROSA: A Robotics Foundation Model Serving System for Robot Factories</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2503.07885">Safety Guardrails for LLM-Enabled Robots</a></td><td>RA-L 26</td><td><a href="https://github.com/KumarRobotics/RoboGuard">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2609.10522">Show-Harness: Just a VLM Agent Can Play Robots</a></td><td>arXiv 26</td><td><a href="https://github.com/showlab/Show-Harness">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.08094">vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models</a></td><td>arXiv 26</td><td><a href="https://github.com/VinRobotics/vla.cpp">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2503.20020">Gemini Robotics: Bringing AI into the Physical World</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.13691">Jailbreaking LLM-Controlled Robots</a></td><td>ICRA 25</td><td><a href="https://github.com/arobey1/robopair">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2506.07339">Real-Time Execution of Action Chunking Flow Policies</a></td><td>NeurIPS 25</td><td><a href="https://github.com/Physical-Intelligence/real-time-chunking-kinetix">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2512.10394">RoboNeuron: A Middle-Layer Infrastructure for Agent-Driven Orchestration in Embodied AI</a></td><td>arXiv 25</td><td><a href="https://github.com/guanweifan/RoboNeuron">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2510.26742">Running VLAs at Real-time Speed</a></td><td>arXiv 25</td><td><a href="https://github.com/Dexmal/realtime-vla">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2506.01844">SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics</a></td><td>arXiv 25</td><td><a href="https://github.com/huggingface/lerobot">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2512.05964">Training-Time Action Conditioning for Efficient Real-Time Chunking</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2512.01031">VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference</a></td><td>arXiv 25</td><td><a href="https://github.com/mit-han-lab/vlash">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2401.12202">OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics</a></td><td>RSS 24</td><td><a href="https://github.com/ok-robot/ok-robot">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2309.09919">Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents</a></td><td>ICRA 24</td><td><a href="https://github.com/YzyLmc/ltl_safety">Code</a></td></tr>
</tbody>
</table>

#### Layered Systems

<table width="100%">
<thead><tr>
<th width="75%" align="left">Paper</th>
<th width="15%" align="left">Venue</th>
<th width="10%" align="left">Code</th>
</tr></thead>
<tbody>
<tr><td><a href="https://arxiv.org/abs/2603.05185">Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2512.08186">Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation</a></td><td>ICLR 26</td><td><a href="https://github.com/InternRobotics/InternNav">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2607.08448">Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents</a></td><td>arXiv 26</td><td><a href="https://github.com/RLinf/RPent">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2606.10267">What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents</a></td><td>arXiv 26</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2510.03342">Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer</a></td><td>arXiv 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2503.14734">GR00T N1: An Open Foundation Model for Generalist Humanoid Robots</a></td><td>arXiv 25</td><td><a href="https://github.com/NVIDIA/Isaac-GR00T">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.05485">HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation</a></td><td>ICLR 25</td><td><a href="https://github.com/liyi14/HAMSTER_beta">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2502.19417">Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models</a></td><td>ICML 25</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2412.04453">NaVILA: Legged Robot Vision-Language-Action Model for Navigation</a></td><td>RSS 25</td><td><a href="https://github.com/AnjieCheng/NaVILA">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2506.17561">VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models</a></td><td>NeurIPS 25</td><td><a href="https://github.com/HeegerGao/VLA-OS">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2504.16054">π₀.₅: a Vision-Language-Action Model with Open-World Generalization</a></td><td>CoRL 25</td><td><a href="https://github.com/Physical-Intelligence/openpi">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.05273">HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers</a></td><td>CoRL 24</td><td>—</td></tr>
<tr><td><a href="https://arxiv.org/abs/2402.06529">Introspective Planning: Aligning Robots&#x27; Uncertainty with Inherent Task Ambiguity</a></td><td>NeurIPS 24</td><td><a href="https://github.com/kevinliang888/IntroPlan">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2403.03174">MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting</a></td><td>RSS 24</td><td><a href="https://github.com/moka-manipulation/moka">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2409.01652">ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation</a></td><td>CoRL 24</td><td><a href="https://github.com/huangwl18/ReKep">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2410.08001">Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation</a></td><td>arXiv 24</td><td><a href="https://github.com/OpenDriveLab/RoboDual">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2305.11176">Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model</a></td><td>arXiv 23</td><td><a href="https://github.com/OpenGVLab/Instruct2Act">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2307.01928">Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners</a></td><td>CoRL 23</td><td><a href="https://github.com/google-research/google-research/tree/master/language_model_uncertainty">Code</a></td></tr>
<tr><td><a href="https://arxiv.org/abs/2204.01691">Do As I Can, Not As I Say: Grounding Language in Robotic Affordances</a></td><td>CoRL 22</td><td><a href="https://github.com/google-research/google-research/tree/master/saycan">Code</a></td></tr>
</tbody>
</table>

<!-- END AUTO-GENERATED PAPER LIST -->

<!-- ## Citation -->

<!-- The survey's final publication identifier and BibTeX citation are pending. Please use the official citation once released. -->

<!-- Replace this notice with the author-confirmed survey BibTeX upon release. -->

## Contributing

Paper suggestions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and submission details.
