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

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence](https://arxiv.org/abs/2609.17210) | arXiv | [Code](https://github.com/FluxVLA/FluxVLA) |
| 2026/08 | [You Don't Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement](https://arxiv.org/abs/2608.07555) | arXiv | — |
| 2026/06 | [Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation](https://arxiv.org/abs/2606.23280) | arXiv | [Project](https://yy12136.github.io/CRWM) |
| 2026/06 | [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | arXiv | [Code](https://github.com/NVlabs/ENPIRE) |
| 2026/06 | [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | arXiv | — |
| 2026/06 | [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) | RLJ | [Project](https://nitinkamra1992.github.io/reward-design-agent) |
| 2026/06 | [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](https://arxiv.org/abs/2606.09630) | arXiv | — |
| 2026/06 | [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | arXiv | [Project](https://robolineage.github.io/) · [Code](https://github.com/robolineage/robolineage) |
| 2026/05 | [EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models](https://arxiv.org/abs/2605.11859) | arXiv | — |
| 2026/05 | [From Demonstrations to Rewards: Test-Time Prompt Optimization for VLM Reward Models](https://arxiv.org/abs/2606.00083) | arXiv | [Code](https://github.com/cgumbsch/Demo2Reward) |
| 2026/05 | [Nautilus: From One Prompt to Plug-and-Play Robot Learning](https://arxiv.org/abs/2605.11665) | arXiv | — |
| 2026/03 | [Agent-Driven Autonomous Reinforcement Learning Research: Iterative Policy Improvement for Quadruped Locomotion](https://arxiv.org/abs/2603.27416) | arXiv | — |
| 2023/10 | [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) | ICLR | [Project](https://eureka-research.github.io) · [Code](https://github.com/eureka-research/Eureka) |

#### Perception

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [AnchorVLN: Geometry-Anchored Vision-Language Grounding Reasoning for Open-Vocabulary Navigation](https://arxiv.org/abs/2609.12285) | arXiv | [Code](https://github.com/aryanmangal769/embodied-nav-mcp) |
| 2026/09 | [CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation](https://arxiv.org/abs/2609.27720) | arXiv | — |
| 2026/09 | [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2609.02653) | arXiv | [Project](https://robot-hint.github.io/) · [Code](https://github.com/robot-hint/HINT) |
| 2026/09 | [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389) | arXiv | — |
| 2026/09 | [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](https://arxiv.org/abs/2609.08402) | arXiv | — |
| 2026/08 | [Probe: Manipulation-Grounded Visual Question Answering with VLM Agents](https://arxiv.org/abs/2608.17129) | arXiv | — |
| 2026/07 | [ABot-N1: Toward a General Visual Language Navigation Foundation Model](https://arxiv.org/abs/2607.10383) | arXiv | [Project](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) · [Code](https://github.com/amap-cvlab/ABot-Navigation) |
| 2026/07 | [RoboVista: Evaluating Vision Language Models for Diverse Robot Applications](https://arxiv.org/abs/2607.04610) | RSS | [Project](https://berkeleyautomation.github.io/robovista) |
| 2026/06 | [A Conversational Framework for Human-Robot Collaborative Manipulation with Distributed Generative AI models](https://arxiv.org/abs/2606.06061) | RO-MAN | [Code](https://github.com/cogrob-tuni/franka-llm) |
| 2026/06 | [AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness](https://arxiv.org/abs/2606.10577) | arXiv | — |
| 2026/06 | [SCOPE: Real-Time Natural Language Camera Agent at the Edge](https://arxiv.org/abs/2606.02951) | HRI | — |
| 2026/04 | [Robot Planning and Situation Handling with Active Perception](https://arxiv.org/abs/2604.26988) | arXiv | [Project](https://vap-tamp.github.io/vap-tamp/) |
| 2026/03 | [GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System](https://arxiv.org/abs/2603.18210) | arXiv | — |
| 2026/03 | [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377) | RSS | — |
| 2026/02 | [A Modern System Recipe for Situated Embodied Human-Robot Conversation with Real-Time Multimodal LLMs and Tool-Calling](https://arxiv.org/abs/2602.04157) | arXiv | — |
| 2026/02 | [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/abs/2602.13193) | arXiv | [Project](https://steerable-policies.github.io) · [Code](https://github.com/steerable-policies/steerable-policies-bridge) |
| 2026/01 | [FARE: Fast-Slow Agentic Robotic Exploration](https://arxiv.org/abs/2601.14681) | arXiv | — |
| 2025/02 | [SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation](https://arxiv.org/abs/2502.13143) | NeurIPS | [Project](https://qizekun.github.io/sofar/) · [Code](https://github.com/qizekun/SoFar) |

#### Planning

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [A Brain-inspired Hierarchical Framework for Zero-Shot Robot Task Reasoning and Execution](https://arxiv.org/abs/2609.05985) | arXiv | — |
| 2026/09 | [ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation](https://arxiv.org/abs/2609.24124) | arXiv | [Project](https://leeibo.github.io/ActiveArena) · [Code](https://github.com/leeibo/ActiveArena) |
| 2026/09 | [Adaptive Task Planning for Long-Horizon Robotic Manipulation Based on Video Priors and Dynamic Scene Graphs](https://www.mdpi.com/1424-8220/26/17/5595) | Sensors | — |
| 2026/09 | [Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework](https://arxiv.org/abs/2609.13335) | arXiv | — |
| 2026/09 | [CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation](https://arxiv.org/abs/2609.27720) | arXiv | — |
| 2026/09 | [GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning](https://arxiv.org/abs/2609.19315) | arXiv | — |
| 2026/09 | [Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering](https://arxiv.org/abs/2609.26360) | arXiv | — |
| 2026/09 | [Memory as Plans: World-Action Modeling with Memory-Grounded Planning](https://arxiv.org/abs/2609.11561) | arXiv | [Project](https://sizhezhao.github.io/projects/MaP-WAM/) |
| 2026/09 | [NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation](https://arxiv.org/abs/2609.27526) | arXiv | — |
| 2026/09 | [Safe Task Planning with Long-Term Graph Memory for Embodied Agents](https://arxiv.org/abs/2609.08444) | arXiv | — |
| 2026/08 | [MaCoPlanner: LLM-Assisted Manual-Compiled Task Planning with Proactive Safety Verification for Robotic Industrial Panel Operation](https://arxiv.org/abs/2608.28300) | arXiv | [Code](https://github.com/XinGP/MaCoPlanner) |
| 2026/08 | [Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation](https://arxiv.org/abs/2608.30396) | arXiv | — |
| 2026/08 | [STARS: extending interactive task learning with large language models](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1848830/full) | Front. Comput. Sci. | [Code](https://github.com/Center-for-Integrated-Cognition/STARS) |
| 2026/07 | [Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning](https://arxiv.org/abs/2607.06501) | RSS | — |
| 2026/07 | [WCM: World-Cognition Model for Generalizable Human-Robot Interaction](https://arxiv.org/abs/2607.22999) | arXiv | — |
| 2026/06 | [LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation](https://arxiv.org/abs/2606.27871) | arXiv | — |
| 2026/04 | [Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization](https://arxiv.org/abs/2604.13533) | arXiv | — |
| 2026/03 | [Agentic Self-Evolutionary Replanning for Embodied Navigation](https://arxiv.org/abs/2603.02772) | arXiv | — |
| 2026/03 | [From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?](https://arxiv.org/abs/2603.03148) | arXiv | [Code](https://github.com/ShinasShaji/llm-robot-cognition) |
| 2026/03 | [IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models](https://arxiv.org/abs/2603.02669) | arXiv | — |
| 2026/02 | [Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081) | AAAI-SS | [Project](https://dfki-ni.github.io/AGENTS-MAKE-2026) |
| 2026/02 | [AgentRob: From Virtual Forum Agents to Hijacked Physical Robots](https://arxiv.org/abs/2602.13591) | arXiv | — |
| 2026/02 | [Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning](https://arxiv.org/abs/2602.21670) | arXiv | — |
| 2026/02 | [Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198) | arXiv | [Project](https://reflective-test-time-planning.github.io) · [Code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning) |
| 2026/01 | [ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | arXiv | [Project](https://tiiuae.github.io/ALRM) |
| 2026/01 | [DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation](https://arxiv.org/abs/2601.18492) | arXiv | [Code](https://github.com/PlumJun/DV-VLN) |
| 2026/01 | [EmboTeam: Grounding LLM Reasoning into Reactive Behavior Trees via PDDL for Embodied Multi-Robot Collaboration](https://arxiv.org/abs/2601.11063) | arXiv | — |
| 2025/10 | [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://arxiv.org/abs/2510.03342) | arXiv | — |
| 2025/02 | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | ICML | — |
| 2025/02 | [Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2502.16707) | CoRL | [Project](https://reflect-vlm.github.io) · [Code](https://github.com/yunhaif/reflect-vlm) |
| 2023/07 | [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928) | CoRL | [Project](https://robot-help.github.io) · [Code](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| 2023/07 | [RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://arxiv.org/abs/2307.04738) | ICRA | [Project](https://project-roco.github.io) · [Code](https://github.com/MandiZhao/robot-collab) |
| 2023/07 | [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | CoRL | [Project](https://sayplan.github.io) |

#### Robot Control

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers](https://arxiv.org/abs/2609.28247) | arXiv | — |
| 2026/09 | [Generalizing Manipulation Skills with a Local Coding Agent](https://arxiv.org/abs/2609.26499) | arXiv | [Project](https://rtalwar2.github.io/agentic-coding-for-robot-manipulation/) |
| 2026/09 | [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) | arXiv | [Project](https://cheng-haha.github.io/GPT-Policy/) · [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2026/09 | [Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning](https://arxiv.org/abs/2609.19347) | arXiv | — |
| 2026/09 | [KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.18869) | arXiv | — |
| 2026/09 | [ManiSkillFormer: Demonstration-Free Compositional Manipulation via Geometric Contracts and Agentic Skill Graph](https://arxiv.org/abs/2609.16331) | arXiv | [Project](https://patricia1019.github.io/ManiSkillFormer/) |
| 2026/09 | [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389) | arXiv | — |
| 2026/09 | [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | arXiv | [Project](https://showlab.github.io/Show-Harness) · [Code](https://github.com/showlab/Show-Harness) |
| 2026/09 | [Transferring the Intelligence of VLMs to Robotic Control](https://arxiv.org/abs/2609.22966) | arXiv | [Project](https://robodawn.top/) · [Code](https://github.com/Hugo-AGI/RoboDawn) |
| 2026/09 | [Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams](https://arxiv.org/abs/2609.28429) | arXiv | — |
| 2026/09 | [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964) | arXiv | — |
| 2026/08 | [ETA: A New Agentic Paradigm for Embodied Tasks](https://arxiv.org/abs/2608.03924) | arXiv | [Code](https://github.com/OpenMOSS/OpenETA) |
| 2026/08 | [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | CVPR Findings | — |
| 2026/07 | [ABot-N1: Toward a General Visual Language Navigation Foundation Model](https://arxiv.org/abs/2607.10383) | arXiv | [Project](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) · [Code](https://github.com/amap-cvlab/ABot-Navigation) |
| 2026/07 | [Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation](https://arxiv.org/abs/2607.26148) | arXiv | — |
| 2026/07 | [MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/abs/2607.22832) | arXiv | [Code](https://github.com/sygkounas/MEMENTO) |
| 2026/07 | [VIA: Visual Interface Agent for Robot Control](https://arxiv.org/abs/2607.11119) | arXiv | — |
| 2026/06 | [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/abs/2606.12299) | arXiv | — |
| 2026/06 | [SCOPE: Real-Time Natural Language Camera Agent at the Edge](https://arxiv.org/abs/2606.02951) | HRI | — |
| 2026/05 | [CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation](https://arxiv.org/abs/2605.02600) | RSS | — |
| 2026/01 | [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334) | arXiv | [Code](https://github.com/robiemusketeer/faea-sim) |
| 2024/09 | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | CoRL | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |
| 2023/07 | [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973) | CoRL | [Project](https://voxposer.github.io) · [Code](https://github.com/huangwl18/VoxPoser) |

#### Adaptation

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | arXiv | — |
| 2026/09 | [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) | arXiv | [Project](https://cheng-haha.github.io/GPT-Policy/) · [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2026/09 | [Transferring the Intelligence of VLMs to Robotic Control](https://arxiv.org/abs/2609.22966) | arXiv | [Project](https://robodawn.top/) · [Code](https://github.com/Hugo-AGI/RoboDawn) |
| 2026/07 | [Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations](https://arxiv.org/abs/2607.26809) | arXiv | [Project](https://hero-agent.github.io/) |
| 2026/06 | [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/abs/2606.18247) | RSS | [Project](https://veritas-improvement.github.io) · [Code](https://github.com/princeton-prism/veritas) |
| 2026/05 | [Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://arxiv.org/abs/2605.00416) | arXiv | [Project](https://learning-while-deploying.github.io/) |
| 2026/03 | [Agentic Self-Evolutionary Replanning for Embodied Navigation](https://arxiv.org/abs/2603.02772) | arXiv | — |
| 2026/03 | [CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval](https://arxiv.org/abs/2603.07997) | arXiv | — |
| 2026/02 | [Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198) | arXiv | [Project](https://reflective-test-time-planning.github.io) · [Code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning) |
| 2026/02 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | arXiv | [Project](https://sites.google.com/view/vlaw-arxiv) |
| 2026/02 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) | RSS | [Project](https://jessie-yuan.github.io/ups/) · [Code](https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering) |
| 2025/09 | [Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155) | NeurIPS | [Project](https://self-improving-efms.github.io) |

### Data

#### Collection

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | arXiv | [Project](https://boweili666.github.io/ARSTAG/) |
| 2026/09 | [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | arXiv | [Project](https://embodiedswe.github.io/) · [Code](https://github.com/EmbodiedSWE/EmbodiedSWE) |
| 2026/09 | [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](https://arxiv.org/abs/2609.05927) | arXiv | — |
| 2026/09 | [RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations](https://arxiv.org/abs/2609.23997) | arXiv | — |
| 2026/08 | [Teach and Grow: An Agent-Centered Architecture for General Robot Learning](https://arxiv.org/abs/2608.17209) | arXiv | — |
| 2026/07 | [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13653) | ECCV | [Code](https://github.com/InternRobotics/REAL) |
| 2026/07 | [Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations](https://arxiv.org/abs/2607.26809) | arXiv | [Project](https://hero-agent.github.io/) |
| 2026/07 | [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047) | arXiv | [Project](https://open-gigaai.github.io/Zero2Skill) · [Code](https://github.com/open-gigaai/Zero2Skill) |
| 2026/06 | [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | arXiv | [Project](https://Playful-RATs.github.io) · [Code](https://github.com/Playful-RATs/RATs) |
| 2026/06 | [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | arXiv | [Project](https://robolineage.github.io/) · [Code](https://github.com/robolineage/robolineage) |
| 2026/03 | [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) | arXiv | [Code](https://github.com/RoboClaw-Robotics/RoboClaw) |
| 2026/03 | [V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors](https://arxiv.org/abs/2603.18811) | arXiv | — |
| 2025/09 | [LLM Trainer: Automated Robotic Data Generation via Demonstration Augmentation using LLMs](https://arxiv.org/abs/2509.20070) | arXiv | [Project](https://sites.google.com/andrew.cmu.edu/llm-trainer) |
| 2025/09 | [Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155) | NeurIPS | [Project](https://self-improving-efms.github.io) |
| 2025/07 | [HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://arxiv.org/abs/2507.00833) | NeurIPS | [Project](https://openhumanoidgen.github.io) · [Code](https://github.com/TeleHuman/HumanoidGen) |
| 2025/02 | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | arXiv | [Project](https://yewr.github.io/video2policy) |
| 2023/11 | [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | ICML | [Project](https://robogen-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/RoboGen) |

#### Filtering

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | arXiv | [Project](https://boweili666.github.io/ARSTAG/) |
| 2026/09 | [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | arXiv | [Project](https://embodiedswe.github.io/) · [Code](https://github.com/EmbodiedSWE/EmbodiedSWE) |
| 2026/09 | [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](https://arxiv.org/abs/2609.05927) | arXiv | — |
| 2026/09 | [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](https://arxiv.org/abs/2609.20056) | arXiv | [Project](https://magma-rob.github.io/magma-gen) · [Code](https://github.com/MAGMA-rob/magma-gen) |
| 2026/08 | [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) | arXiv | [Project](https://www-ye.github.io/ego2robot_blog/) |
| 2026/08 | [SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2608.04196) | arXiv | [Project](https://lin-nie.github.io/SiMDex/) |
| 2026/07 | [HELP: Human-Efficient Large-Scale Robot Post-Training with Rollout Segmentation](https://arxiv.org/abs/2607.09776) | arXiv | — |
| 2026/07 | [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047) | arXiv | [Project](https://open-gigaai.github.io/Zero2Skill) · [Code](https://github.com/open-gigaai/Zero2Skill) |
| 2026/06 | [Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory](https://arxiv.org/abs/2606.25115) | arXiv | — |
| 2026/06 | [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | arXiv | [Project](https://robolineage.github.io/) · [Code](https://github.com/robolineage/robolineage) |
| 2026/06 | [SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale](https://arxiv.org/abs/2606.13497) | arXiv | [Project](https://intuitive-robots.github.io/sparc-labeling/) · [Code](https://github.com/intuitive-robots/sparc) |
| 2026/06 | [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/abs/2606.18247) | RSS | [Project](https://veritas-improvement.github.io) · [Code](https://github.com/princeton-prism/veritas) |
| 2026/05 | [Closing the Loop in Teleoperation: Episode-Level Data Quality Assessment and Feedback for High-Quality Demonstration Collection](https://arxiv.org/abs/2605.26349) | arXiv | — |
| 2026/03 | [Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) | arXiv | [Project](https://dream2fix.github.io/) |
| 2026/01 | [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](https://arxiv.org/abs/2601.00675) | arXiv | — |

#### Correction

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | arXiv | [Project](https://boweili666.github.io/ARSTAG/) |
| 2026/09 | [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](https://arxiv.org/abs/2609.20056) | arXiv | [Project](https://magma-rob.github.io/magma-gen) · [Code](https://github.com/MAGMA-rob/magma-gen) |
| 2026/08 | [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) | arXiv | [Project](https://www-ye.github.io/ego2robot_blog/) |
| 2026/08 | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | CVPR | — |
| 2026/07 | [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047) | arXiv | [Project](https://open-gigaai.github.io/Zero2Skill) · [Code](https://github.com/open-gigaai/Zero2Skill) |
| 2026/03 | [Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) | arXiv | [Project](https://dream2fix.github.io/) |
| 2026/02 | [Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198) | arXiv | [Project](https://reflective-test-time-planning.github.io) · [Code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning) |
| 2026/02 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) | RSS | [Project](https://jessie-yuan.github.io/ups/) · [Code](https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering) |
| 2026/01 | [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](https://arxiv.org/abs/2601.00675) | arXiv | — |
| 2025/09 | [LLM Trainer: Automated Robotic Data Generation via Demonstration Augmentation using LLMs](https://arxiv.org/abs/2509.20070) | arXiv | [Project](https://sites.google.com/andrew.cmu.edu/llm-trainer) |

### Environment

#### Reconstruction

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | arXiv | [Project](https://boweili666.github.io/ARSTAG/) |
| 2026/09 | [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](https://arxiv.org/abs/2609.05927) | arXiv | — |
| 2026/09 | [RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249) | arXiv | [Project](https://yuyaoliu.me/projects/rapid) |
| 2026/07 | [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190) | arXiv | [Project](https://agentic-real2sim.github.io/) · [Code](https://github.com/agentic-real2sim/agentic_real2sim) |
| 2026/07 | [EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI](https://arxiv.org/abs/2607.07459) | arXiv | [Project](https://horizonrobotics.github.io/EmbodiedGen) · [Code](https://github.com/HorizonRobotics/EmbodiedGen) |
| 2026/06 | [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](https://arxiv.org/abs/2606.28276) | arXiv | — |
| 2026/05 | [ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction](https://arxiv.org/abs/2605.14398) | arXiv | [Project](https://uwsbel.github.io/chrono-agentic-website/) |
| 2026/05 | [DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2605.05241) | arXiv | — |
| 2026/05 | [SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning](https://arxiv.org/abs/2605.09423) | arXiv | — |
| 2026/04 | [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) | RSS | [Code](https://github.com/NVlabs/RoboLab) |
| 2026/04 | [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226) | arXiv | [Project](https://roboplayground.github.io) |
| 2026/02 | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | arXiv | — |
| 2026/02 | [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153) | ICML | [Project](https://scenesmith.github.io/) · [Code](https://github.com/nepfaff/scenesmith) |
| 2026/01 | [Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078) | arXiv | [Code](https://github.com/AgibotTech/genie_sim) |
| 2025/02 | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | arXiv | [Project](https://yewr.github.io/video2policy) |

#### Task Generation

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | arXiv | [Project](https://boweili666.github.io/ARSTAG/) |
| 2026/06 | [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | arXiv | — |
| 2026/06 | [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | arXiv | [Project](https://Playful-RATs.github.io) · [Code](https://github.com/Playful-RATs/RATs) |
| 2026/05 | [SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning](https://arxiv.org/abs/2605.09423) | arXiv | — |
| 2026/04 | [Generative Simulation for Policy Learning in Physical Human-Robot Interaction](https://arxiv.org/abs/2604.08664) | arXiv | [Project](https://rchi-lab.github.io/gen_phri/) |
| 2026/04 | [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) | RSS | [Code](https://github.com/NVlabs/RoboLab) |
| 2026/04 | [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226) | arXiv | [Project](https://roboplayground.github.io) |
| 2025/02 | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | arXiv | [Project](https://yewr.github.io/video2policy) |
| 2024/10 | [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://arxiv.org/abs/2411.00081) | ICLR | [Code](https://github.com/facebookresearch/partnr-planner) |
| 2023/11 | [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | ICML | [Project](https://robogen-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/RoboGen) |

#### Benchmarking

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation](https://arxiv.org/abs/2609.24124) | arXiv | [Project](https://leeibo.github.io/ActiveArena) · [Code](https://github.com/leeibo/ActiveArena) |
| 2026/09 | [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | arXiv | [Project](https://embodiedswe.github.io/) · [Code](https://github.com/EmbodiedSWE/EmbodiedSWE) |
| 2026/09 | [EvoNav-Bench: Benchmarking Lifelong Navigation in Evolving Environments](https://arxiv.org/abs/2609.08292) | arXiv | — |
| 2026/09 | [From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413) | arXiv | [Project](https://yy-gx.github.io/HALTER/) |
| 2026/09 | [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178) | arXiv | [Project](https://liulin815.github.io/LIBERO-Recovery/) · [Code](https://github.com/liulin815/LIBERO-Recovery) |
| 2026/09 | [MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation](https://arxiv.org/abs/2609.07047) | arXiv | [Code](https://github.com/Collab-Gen/MEMOBench) |
| 2026/09 | [OVMAN: A Task and Benchmark for Open-Vocabulary Motion-Aware Navigation](https://arxiv.org/abs/2609.06424) | arXiv | — |
| 2026/09 | [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](https://arxiv.org/abs/2609.10895) | arXiv | — |
| 2026/09 | [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](https://arxiv.org/abs/2609.08402) | arXiv | — |
| 2026/09 | [VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control](https://arxiv.org/abs/2609.19554) | arXiv | — |
| 2026/08 | [Compiling and Benchmarking Task-State Horizons for Embodied Agents](https://arxiv.org/abs/2608.08036) | arXiv | — |
| 2026/08 | [ManiGuard: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](https://arxiv.org/abs/2608.17386) | arXiv | — |
| 2026/07 | [RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](https://arxiv.org/abs/2607.04434) | arXiv | [Project](https://XPolicyLab.github.io) · [Code](https://github.com/RoboDojo-Benchmark/RoboDojo) |
| 2026/07 | [RoboVista: Evaluating Vision Language Models for Diverse Robot Applications](https://arxiv.org/abs/2607.04610) | RSS | [Project](https://berkeleyautomation.github.io/robovista) |
| 2026/07 | [Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents](https://arxiv.org/abs/2607.22014) | arXiv | [Project](https://gomtae.github.io/publications/missionbench) · [Code](https://github.com/FraunhoferIVI/MissionBench) |
| 2026/06 | [Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?](https://arxiv.org/abs/2606.04811) | arXiv | [Code](https://github.com/showlab/Dream.exe) |
| 2026/06 | [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](https://arxiv.org/abs/2606.31993) | RSS | — |
| 2026/06 | [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610) | arXiv | [Project](https://weichengtseng.github.io/sc3-eval/) |
| 2026/06 | [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) | arXiv | [Project](https://ripl.github.io/manipulation_benchmark_audit/) · [Code](https://github.com/ripl/ManipulationBenchmarkAudit) |
| 2026/05 | [Enabling Extensible Embodied Capabilities with Tools](https://arxiv.org/abs/2605.26637) | arXiv | [Project](https://racingemperor.github.io/manip-tool-hub/) |
| 2026/05 | [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921) | arXiv | [Project](https://robomemarena.github.io) · [Code](https://github.com/OpenHelix-Team/RoboMemArena) |
| 2026/04 | [KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning](https://arxiv.org/abs/2604.25788) | RSS | — |
| 2026/04 | [ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies](https://proceedings.iclr.cc/paper_files/paper/2026/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf) | ICLR | — |
| 2026/04 | [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) | RSS | [Code](https://github.com/NVlabs/RoboLab) |
| 2026/04 | [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226) | arXiv | [Project](https://roboplayground.github.io) |
| 2026/03 | [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | ICML | [Project](https://capgym.github.io) |
| 2026/03 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356) | arXiv | [Code](https://github.com/robocasa/robocasa) |
| 2026/02 | [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](https://arxiv.org/abs/2602.06556) | RSS | [Project](https://zackhxn.github.io/LIBERO-X/) |
| 2026/01 | [Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078) | arXiv | [Code](https://github.com/AgibotTech/genie_sim) |
| 2026/01 | [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](https://arxiv.org/abs/2601.00675) | arXiv | — |
| 2025/10 | [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827) | arXiv | — |
| 2025/06 | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088) | ICML | [Code](https://github.com/RoboTwin-Platform/RoboTwin) |
| 2024/10 | [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://arxiv.org/abs/2411.00081) | ICLR | [Code](https://github.com/facebookresearch/partnr-planner) |
| 2024/06 | [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523) | RSS | [Code](https://github.com/robocasa/robocasa) |
| 2024/03 | [BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation](https://arxiv.org/abs/2403.09227) | arXiv | [Project](https://behavior.stanford.edu) · [Code](https://github.com/StanfordVL/BEHAVIOR-1K) |
| 2023/06 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | NeurIPS | [Project](https://libero-project.github.io/main.html) · [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| 2020/09 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](https://arxiv.org/abs/2009.12293) | arXiv | [Code](https://github.com/ARISE-Initiative/robosuite) |
| 2019/09 | [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271) | RA-L | [Code](https://github.com/stepjam/RLBench) |

### Harness

#### Orchestration

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](https://arxiv.org/abs/2609.29204) | arXiv | [Code](https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA) |
| 2026/09 | [AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution](https://arxiv.org/abs/2609.18520) | arXiv | [Code](https://github.com/Admire-ljb/AeroWeaver) |
| 2026/09 | [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | arXiv | — |
| 2026/09 | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | arXiv | [Project](https://darwin-agent.github.io/HarnessPAI) |
| 2026/09 | [RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394) | arXiv | — |
| 2026/09 | [RoboTalk: Learning Multi-Robot Communication and Coordination from Multimodal Demonstrations](https://arxiv.org/abs/2609.23997) | arXiv | — |
| 2026/09 | [Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method](https://arxiv.org/abs/2609.08402) | arXiv | — |
| 2026/08 | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | arXiv | — |
| 2026/08 | [MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration](https://arxiv.org/abs/2608.15549) | arXiv | [Project](https://wangxiaoshawn.github.io/MistyPilot.html) · [Code](https://github.com/WangXiaoShawn/MistyPilot) |
| 2026/08 | [Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs](https://arxiv.org/abs/2608.22657) | arXiv | [Code](https://github.com/Liuuuxy/physical-agentic-ai) |
| 2026/08 | [Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation](https://arxiv.org/abs/2608.30396) | arXiv | — |
| 2026/08 | [Towards the Harness of Embodied Agents](https://arxiv.org/abs/2608.11246) | arXiv | [Project](https://eit-hai.github.io/thea) · [Code](https://github.com/EIT-HAI/Thea) |
| 2026/07 | [A Glimpse into Long-term Physical Coexistence with Intelligent Robots](https://arxiv.org/abs/2607.11377) | arXiv | — |
| 2026/07 | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) | arXiv | — |
| 2026/07 | [Addressing the Orchestration Gap in Generalist Robots via Physical Agency](https://arxiv.org/abs/2607.21725) | arXiv | [Project](https://lianegalanti.github.io/Pigey/) · [Code](https://github.com/lianegalanti/Pigey) |
| 2026/07 | [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377) | arXiv | [Project](https://steinate.github.io/cortex.github.io) · [Code](https://github.com/InternRobotics/Cortex) |
| 2026/07 | [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448) | arXiv | [Project](https://harnessvla.github.io/) · [Code](https://github.com/RLinf/RPent) |
| 2026/07 | [Retriever: Composing the Perception-Reasoning-Action Loop for Long-Horizon Manipulation](https://arxiv.org/abs/2607.17213) | arXiv | [Code](https://github.com/openretriever/retriever) |
| 2026/07 | [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | arXiv | — |
| 2026/06 | [Guava: An Effective and Universal Harness for Embodied Manipulation](https://arxiv.org/abs/2606.18363) | arXiv | [Project](https://guava-harness.github.io) |
| 2026/06 | [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](https://arxiv.org/abs/2606.07723) | arXiv | [Project](https://chicychen.github.io/VoLo/) · [Code](https://github.com/NVlabs/VoLoAgent) |
| 2026/06 | [What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents](https://arxiv.org/abs/2606.10267) | arXiv | [Project](http://jiahenghu.github.io/hi-vla) |
| 2026/05 | [Enabling Extensible Embodied Capabilities with Tools](https://arxiv.org/abs/2605.26637) | arXiv | [Project](https://racingemperor.github.io/manip-tool-hub/) |
| 2026/05 | [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](https://arxiv.org/abs/2605.13119) | arXiv | — |
| 2026/04 | [M2HRI: An LLM-Driven Multimodal Multi-Agent Framework for Personalized Human-Robot Interaction](https://arxiv.org/abs/2604.11975) | arXiv | [Project](https://project-m2hri.github.io/) · [Code](https://github.com/project-m2hri/m2hri) |
| 2026/04 | [ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration](https://arxiv.org/abs/2604.04664) | arXiv | [Project](https://www.rosclaw.io/) · [Code](https://github.com/ros-claw/rosclaw) |
| 2026/03 | [RoboRouter: Training-Free Policy Routing for Robotic Manipulation](https://arxiv.org/abs/2603.07892) | arXiv | — |
| 2026/03 | [ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction](https://arxiv.org/abs/2603.26997) | arXiv | — |
| 2026/01 | [ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | arXiv | [Project](https://tiiuae.github.io/ALRM) |
| 2024/10 | [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | ICLR | [Project](https://emos-project.github.io/) |
| 2023/07 | [RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://arxiv.org/abs/2307.04738) | ICRA | [Project](https://project-roco.github.io) · [Code](https://github.com/MandiZhao/robot-collab) |

#### Memory

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](https://arxiv.org/abs/2609.11308) | arXiv | — |
| 2026/09 | [ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation](https://arxiv.org/abs/2609.24124) | arXiv | [Project](https://leeibo.github.io/ActiveArena) · [Code](https://github.com/leeibo/ActiveArena) |
| 2026/09 | [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](https://arxiv.org/abs/2609.29204) | arXiv | [Code](https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA) |
| 2026/09 | [Bridging Thought and Action: Taming Long-Horizon Instability in Open-Source LLM Agents with a MetaTool-Enhanced ROS Framework](https://arxiv.org/abs/2609.13335) | arXiv | — |
| 2026/09 | [CoRelNav: Collaborative Relational Navigation for Multi-Robot Spatially Constrained Semantic Navigation](https://arxiv.org/abs/2609.27720) | arXiv | — |
| 2026/09 | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | arXiv | [Project](https://darwin-agent.github.io/HarnessPAI) |
| 2026/09 | [Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering](https://arxiv.org/abs/2609.26360) | arXiv | — |
| 2026/09 | [MessyMem: Learning-from-Doing Memory for Mobile Manipulation](https://arxiv.org/abs/2609.15976) | arXiv | [Project](https://messymem.github.io) |
| 2026/09 | [NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation](https://arxiv.org/abs/2609.27526) | arXiv | — |
| 2026/09 | [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389) | arXiv | — |
| 2026/09 | [Safe Task Planning with Long-Term Graph Memory for Embodied Agents](https://arxiv.org/abs/2609.08444) | arXiv | — |
| 2026/09 | [Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams](https://arxiv.org/abs/2609.28429) | arXiv | — |
| 2026/09 | [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964) | arXiv | — |
| 2026/08 | [Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory](https://arxiv.org/abs/2608.16889) | arXiv | — |
| 2026/08 | [Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments](https://arxiv.org/abs/2608.04933) | arXiv | — |
| 2026/08 | [Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation](https://arxiv.org/abs/2608.30396) | arXiv | — |
| 2026/08 | [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](https://arxiv.org/abs/2608.09410) | arXiv | — |
| 2026/07 | [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784) | arXiv | [Project](https://robo-architect.github.io/) · [Code](https://github.com/robo-architect/architect-franka) |
| 2026/07 | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) | arXiv | — |
| 2026/07 | [HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2607.29600) | arXiv | — |
| 2026/07 | [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](https://arxiv.org/abs/2607.03449) | ICML | [Code](https://github.com/HappyWaterXP/HiMe) |
| 2026/07 | [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](https://arxiv.org/abs/2607.14252) | arXiv | [Project](https://yuzihaowashu.github.io/MEMORA/) · [Code](https://github.com/yuzihaowashu/MEMORA) |
| 2026/06 | [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](https://arxiv.org/abs/2606.23565) | arXiv | — |
| 2026/06 | [SPINE: Bridging the Cyber-Physical Gap with Agentic AI](https://arxiv.org/abs/2607.13049) | arXiv | — |
| 2026/05 | [EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents](https://arxiv.org/abs/2605.10332) | arXiv | [Code](https://github.com/air-embodied-brain/EmbodiSkill) |
| 2026/05 | [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729) | arXiv | [Project](https://robocortex66.github.io/robo-cortex/) |
| 2026/04 | [EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents](https://arxiv.org/abs/2604.18271) | arXiv | — |
| 2026/04 | [Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization](https://arxiv.org/abs/2604.13533) | arXiv | — |
| 2026/04 | [OVAL: Open-Vocabulary Augmented Memory Model for Lifelong Object Goal Navigation](https://arxiv.org/abs/2604.12872) | arXiv | — |
| 2026/03 | [Agentic Self-Evolutionary Replanning for Embodied Navigation](https://arxiv.org/abs/2603.02772) | arXiv | — |
| 2026/03 | [CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval](https://arxiv.org/abs/2603.07997) | arXiv | — |
| 2026/03 | [RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics](https://arxiv.org/abs/2603.12939) | ECCV | [Project](https://robostream123.github.io/) · [Code](https://github.com/yu2hi13/RoboStream) |
| 2026/01 | [APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation](https://arxiv.org/abs/2602.00551) | CVPR | [Code](https://github.com/4amGodvzx/apex) |
| 2026/01 | [MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization](https://arxiv.org/abs/2601.20577) | AAMAS | [Code](https://github.com/TomWang-NPU/MeCo) |

#### Monitoring

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](https://arxiv.org/abs/2609.20822) | arXiv | — |
| 2026/09 | [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | arXiv | — |
| 2026/09 | [From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413) | arXiv | [Project](https://yy-gx.github.io/HALTER/) |
| 2026/09 | [Safe Task Planning with Long-Term Graph Memory for Embodied Agents](https://arxiv.org/abs/2609.08444) | arXiv | — |
| 2026/07 | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) | arXiv | — |
| 2026/07 | [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | arXiv | — |
| 2026/07 | [Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric](https://arxiv.org/abs/2607.23532) | arXiv | — |
| 2026/05 | [Closing the Loop in Teleoperation: Episode-Level Data Quality Assessment and Feedback for High-Quality Demonstration Collection](https://arxiv.org/abs/2605.26349) | arXiv | — |
| 2026/05 | [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/abs/2605.11951) | RSS | — |
| 2026/04 | [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) | RSS | [Code](https://github.com/NVlabs/RoboLab) |
| 2026/03 | [OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency](https://arxiv.org/abs/2603.10682) | arXiv | — |
| 2026/03 | [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](https://arxiv.org/abs/2603.02115) | RSS | [Project](https://robometer.github.io/) · [Code](https://github.com/robometer/robometer) |
| 2026/02 | [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281) | arXiv | — |
| 2026/01 | [DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation](https://arxiv.org/abs/2601.18492) | arXiv | [Code](https://github.com/PlumJun/DV-VLN) |
| 2024/12 | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | CVPR | [Project](https://zhoues.github.io/Code-as-Monitor) |
| 2024/10 | [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://arxiv.org/abs/2410.00371) | ICLR | [Project](https://aha-vlm.github.io/) · [Code](https://github.com/NVlabs/AHA) |
| 2023/07 | [DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329) | IROS | [Project](https://sites.google.com/view/doremi-paper) |
| 2023/06 | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | CoRL | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |

#### Recovery

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413) | arXiv | [Project](https://yy-gx.github.io/HALTER/) |
| 2026/09 | [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](https://arxiv.org/abs/2609.15195) | arXiv | — |
| 2026/09 | [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178) | arXiv | [Project](https://liulin815.github.io/LIBERO-Recovery/) · [Code](https://github.com/liulin815/LIBERO-Recovery) |
| 2026/09 | [VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies](https://arxiv.org/abs/2609.06508) | arXiv | — |
| 2026/08 | [ETA: A New Agentic Paradigm for Embodied Tasks](https://arxiv.org/abs/2608.03924) | arXiv | [Code](https://github.com/OpenMOSS/OpenETA) |
| 2026/08 | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | CVPR | — |
| 2026/08 | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | arXiv | — |
| 2026/07 | [A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation](https://arxiv.org/abs/2607.06990) | RSS | — |
| 2026/07 | [ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning](https://arxiv.org/abs/2607.04162) | arXiv | — |
| 2026/07 | [Addressing the Orchestration Gap in Generalist Robots via Physical Agency](https://arxiv.org/abs/2607.21725) | arXiv | [Project](https://lianegalanti.github.io/Pigey/) · [Code](https://github.com/lianegalanti/Pigey) |
| 2026/07 | [PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution](https://arxiv.org/abs/2607.16636) | arXiv | [Code](https://github.com/PhyAgentOS/PhyAgentOS-core) |
| 2026/07 | [WCM: World-Cognition Model for Generalizable Human-Robot Interaction](https://arxiv.org/abs/2607.22999) | arXiv | — |
| 2026/06 | [LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories](https://arxiv.org/abs/2606.13578) | arXiv | [Project](https://zjunlp.github.io/LabVLA) · [Code](https://github.com/zjunlp/LabVLA) |
| 2026/06 | [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](https://arxiv.org/abs/2606.09630) | arXiv | — |
| 2026/06 | [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](https://arxiv.org/abs/2606.07723) | arXiv | [Project](https://chicychen.github.io/VoLo/) · [Code](https://github.com/NVlabs/VoLoAgent) |
| 2026/05 | [PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs](https://arxiv.org/abs/2606.00104) | arXiv | [Code](https://github.com/erdemuysalx/PEACE) |
| 2026/04 | [A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring](https://arxiv.org/abs/2604.07395) | arXiv | [Project](https://wenzewwz123.github.io/Agentic-Loop/) |
| 2026/04 | [Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection](https://arxiv.org/abs/2604.13942) | arXiv | — |
| 2026/04 | [Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning](https://arxiv.org/abs/2604.02318) | arXiv | — |
| 2026/03 | [Agentic Self-Evolutionary Replanning for Embodied Navigation](https://arxiv.org/abs/2603.02772) | arXiv | — |
| 2026/03 | [Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) | arXiv | [Project](https://dream2fix.github.io/) |
| 2026/02 | [Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081) | AAAI-SS | [Project](https://dfki-ni.github.io/AGENTS-MAKE-2026) |
| 2023/07 | [DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329) | IROS | [Project](https://sites.google.com/view/doremi-paper) |
| 2023/06 | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | CoRL | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |

#### Skill Synthesis

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541) | arXiv | — |
| 2026/09 | [Auto-HSI: Personalized human control of a robot swarm on demand by using LLMs for online automatic code generation](https://arxiv.org/abs/2609.16346) | arXiv | — |
| 2026/09 | [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | arXiv | [Project](https://embodiedswe.github.io/) · [Code](https://github.com/EmbodiedSWE/EmbodiedSWE) |
| 2026/09 | [Generalizing Manipulation Skills with a Local Coding Agent](https://arxiv.org/abs/2609.26499) | arXiv | [Project](https://rtalwar2.github.io/agentic-coding-for-robot-manipulation/) |
| 2026/09 | [GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808) | arXiv | [Project](https://gta2-project.github.io/) |
| 2026/09 | [RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394) | arXiv | — |
| 2026/09 | [RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249) | arXiv | [Project](https://yuyaoliu.me/projects/rapid) |
| 2026/09 | [WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories](https://arxiv.org/abs/2609.18435) | arXiv | [Code](https://github.com/tsudalab/WetRobo) |
| 2026/08 | [Teach and Grow: An Agent-Centered Architecture for General Robot Learning](https://arxiv.org/abs/2608.17209) | arXiv | — |
| 2026/07 | [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784) | arXiv | [Project](https://robo-architect.github.io/) · [Code](https://github.com/robo-architect/architect-franka) |
| 2026/07 | [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369) | arXiv | [Project](https://graph-robots.github.io/gap) · [Code](https://github.com/graph-robots/graph-as-policy) |
| 2026/07 | [MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/abs/2607.22832) | arXiv | [Code](https://github.com/sygkounas/MEMENTO) |
| 2026/06 | [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272) | arXiv | [Project](https://research.nvidia.com/labs/gear/aspire/) · [Code](https://github.com/NVlabs/ASPIRE) |
| 2026/06 | [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | arXiv | [Project](https://Playful-RATs.github.io) · [Code](https://github.com/Playful-RATs/RATs) |
| 2026/03 | [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | ICML | [Project](https://capgym.github.io) |
| 2026/03 | [IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models](https://arxiv.org/abs/2603.02669) | arXiv | — |
| 2026/03 | [Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation](https://arxiv.org/abs/2603.02623) | arXiv | — |
| 2026/01 | [ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | arXiv | [Project](https://tiiuae.github.io/ALRM) |
| 2022/09 | [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | ICRA | [Project](https://code-as-policies.github.io) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |

#### Evolution

| Date | Paper | Venue | Resources |
| --- | --- | --- | --- |
| 2026/09 | [AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution](https://arxiv.org/abs/2609.29204) | arXiv | [Code](https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA) |
| 2026/09 | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | arXiv | [Project](https://darwin-agent.github.io/HarnessPAI) |
| 2026/09 | [Learning and Transferring Closed-Loop Robot Software](https://arxiv.org/abs/2609.19906) | arXiv | — |
| 2026/09 | [RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394) | arXiv | — |
| 2026/08 | [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227) | arXiv | — |
| 2026/08 | [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | arXiv | — |
| 2026/08 | [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](https://arxiv.org/abs/2608.09410) | arXiv | — |
| 2026/08 | [You Don't Need To Stay in The Loop: An Agentic Robotics Loop for Robot-Policy Improvement](https://arxiv.org/abs/2608.07555) | arXiv | — |
| 2026/08 | [Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) | arXiv | [Project](https://air-embodied-brain.github.io/zetta) · [Code](https://github.com/air-embodied-brain/Zetta-Embodiment) |
| 2026/07 | [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) | arXiv | — |
| 2026/06 | [RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458) | arXiv | [Project](https://rho-robotics.github.io) |
| 2026/06 | [SPINE: Bridging the Cyber-Physical Gap with Agentic AI](https://arxiv.org/abs/2607.13049) | arXiv | — |
| 2026/04 | [ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents](https://arxiv.org/abs/2604.10096) | arXiv | [Code](https://github.com/amap-cvlab/ABot-Claw) |
| 2026/03 | [Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation](https://arxiv.org/abs/2603.04466) | arXiv | — |

<!-- END AUTO-GENERATED PAPER LIST -->

<!-- ## Citation -->

<!-- The survey's final publication identifier and BibTeX citation are pending. Please use the official citation once released. -->

<!-- Replace this notice with the author-confirmed survey BibTeX upon release. -->

## Contributing

Paper suggestions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and submission details.
