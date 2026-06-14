[Kimi K2.7 Code is now on CometAPI — Kimi's most intelligent coding model to date, reliably follows instructions in long contexts and completes programming tasks with a higher success rate. Try it now](https://www.cometapi.com/models/moonshotai/kimi-k2-7-code/)

[Schema](https://apidoc.cometapi.com/anthropic-messages.md)

Copy Page

Claude

# Claude Sonnet 4.6

100.00%

Input:$2.4/M

Output:$12/M

Claude Sonnet 4.6 is our most capable Sonnet model yet. It’s a full upgrade of the model’s skills across coding, computer use, long-context reasoning, agent planning, knowledge work, and design. Sonnet 4.6 also features a 1M token context window in beta.

Text

New

Commercial Use

Playground

Overview

Features

Pricing

API

Versions

## Playground for Claude Sonnet 4.6

Explore Claude Sonnet 4.6's Playground — an interactive environment to test models, run queries in real time. Try prompts, adjust parameters, and iterate instantly to accelerate development and validate use cases.

Chat

JSON

![](https://lf3-static.bytednsdoc.com/obj/eden-cn/ptlz_zlp/ljhwZthlaukjlkulzlp/docs-icon.png)

Hello

![](https://resource.cometapi.com/logo.svg)

Hello, how can I help you?

Login to chat with Claude Sonnet 4.6

1. [Technical specifications — Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#technical-specifications--claude-sonnet-46)
2. [What Is Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#what-is-claude-sonnet-46)
3. [Main Features of Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#main-features-of-claude-sonnet-46)
4. [Benchmark Performance of Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#benchmark-performance-of-claude-sonnet-46)
5. [Claude Sonnet 4.6 vs Other Claude Models](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#claude-sonnet-46-vs-other-claude-models)
6. [Limitations of Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#limitations-of-claude-sonnet-46)
7. [Representative Use Cases of Claude Sonnet 4.6](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#representative-use-cases-of-claude-sonnet-46)
8. [How to access and use Claude Sonnet 4.6 API](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#how-to-access-and-use-claude-sonnet-46-api)
1. [Step 1: Sign Up for API Key](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#step-1-sign-up-for-api-key)
2. [Step 2: Send Requests to claude-sonnet-4-6 API](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#step-2-send-requests-toclaude-sonnet-4-6api)
3. [Step 3: Retrieve and Verify Results](https://www.cometapi.com/models/anthropic/claude-sonnet-4-6/#step-3-retrieve-and-verify-results)

## Technical specifications — Claude Sonnet 4.6

| Item | Claude Sonnet 4.6 (public summary) |
| --- | --- |
| Provider | Anthropic |
| Model family | Sonnet (Claude v4.x family) — Sonnet 4.6 variant |
| Model id (canonical) | claude-sonnet-4-6 |
| Input types | Text (primary). Limited/secondary support for structured tool/JSON I/O. Not positioned as a primary image-generation model. |
| Output types | Text (natural language, structured JSON, code, and tool-call payloads) |
| Context window | ~200,000 tokens (approx.) — designed for multi-document and long-session coherence |
| Function-calling / tool use | Yes — structured tool invocation, JSON-constrained outputs, agent-style orchestration supported |
| Multimodality | Limited — Sonnet is focused on text and structured tool integration; not optimized for image generation. |
| Release note highlights | Stability/improvements in long-context reasoning, lower-latency Sonnet variant tuned for speed–accuracy tradeoffs, improved instruction adherence. |

## What Is Claude Sonnet 4.6

Claude Sonnet 4.6 is the latest evolution of Anthropic’s **Sonnet** model line, designed to deliver **near-Opus performance at a more accessible price point**. It upgrades Sonnet from its earlier 4.5 iteration, bringing stronger instruction following, vastly expanded context support, improved coding and computer use skills, and broader multi-step reasoning abilities — all while maintaining pricing parity with Sonnet 4.5.

Unlike Opus models, which are flagship and optimized for heavy agentic workloads, Sonnet 4.6 targets developers and general knowledge work where broad capability and cost-effectiveness matter.

## Main Features of Claude Sonnet 4.6

- **1M Token Context Window (Beta):** Sonnet 4.6 supports up to **one million tokens** of context in beta — roughly enough to ingest entire codebases, stacks of legal contracts, or multiple academic papers in a single request.
- **Improved Coding Performance:** Compared with Sonnet 4.5, Sonnet 4.6 shows significant gains in real-world developer tasks and benchmarks like SWE-Bench Verified (~79.6% score reported), making it suitable for complex coding tasks.
- **Enhanced Computer Use:** New levels of competency in tasks involving operating software (spreadsheets, multi-step web form workflows, etc.) approaching human-level performance on OSWorld-Verified tests.
- **Adaptive Thinking:** The model incorporates enhanced reasoning strategies and can dynamically allocate internal computation to tackle complex problems step by step.
- **Stronger Instruction Following:** Users report more consistency and precision in following detailed requests, with fewer hallucinations and better task completion.
- **Safety & Prompt Injection Resistance:** Anthropic has improved robustness over Sonnet 4.5 in resisting prompt injection attacks and similar vulnerabilities.

## Benchmark Performance of Claude Sonnet 4.6

| Evaluation | Claude Sonnet 4.6 (approx.) | Notes |
| --- | --- | --- |
| SWE-Bench Verified | ~79.6% | Strong coding performance close to Opus-class. |
| OSWorld-Verified (Computer Use) | ~72.5% | Near human-level task performance; powerful for workflows. |
| ARC-AGI-2 | ~60.4% | Reflects broad reasoning strength. |

As a mid-tier model, Sonnet 4.6 narrows the performance gap with Opus models significantly, making it suitable for many tasks previously reserved for flagship class.

## Claude Sonnet 4.6 vs Other Claude Models

| Model | Best For | Key Differences |
| --- | --- | --- |
| Claude Sonnet 4.6 | Balanced coding, reasoning, large contexts | Massive context window beta, cost-efficient, strong for workflow tasks. |
| Claude Sonnet 4.5 | Mid-tier general tasks | Lower benchmarks, smaller context window before 4.6. |
| Claude Opus 4.6 | Deep reasoning & agentic coding | Stronger raw reasoning and agent capabilities; pricier. |

Compared to Sonnet 4.5, the 4.6 release boosts contextual understanding and performance on office-style tasks; compared to Opus models, Sonnet sits slightly below in flagship reasoning power but often closer than expected in coding and general task benchmarks.

* * *

## Limitations of Claude Sonnet 4.6

- **Beta Context Window:** The 1M token context is currently in beta — adoption and stability may vary depending on API usage and plan.
- **Latency & Cost:** Handling very large contexts increases computational cost and may introduce higher latency on API calls relative to smaller contexts.
- **Benchmark Granularity:** While strong in reported tests, Sonnet may lag a bit behind Opus on the most complex reasoning or multidisciplinary benchmarks.

## Representative Use Cases of Claude Sonnet 4.6

1. **Large Codebase Assistance:** Ideal for ingesting and reasoning about entire software systems, refactorings, or cross-file dependencies.
2. **Document & Research Synthesis:** Useful for long-document analysis where context extends beyond typical limits.
3. **Workflow Automation:** Solving multi-step computer tasks, such as spreadsheets and form automation.
4. **General Knowledge Work:** Suitable for knowledge workers needing reliable instruction following and reasoning without the cost of flagship models.

## How to access and use Claude Sonnet 4.6 API

### Step 1: Sign Up for API Key

Log in to cometapi.com. If you are not our user yet, please register first. Sign into your [CometAPI console](https://api.cometapi.com/console/token). Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

### Step 2: Send Requests to `claude-sonnet-4-6` API

Select the “ **`claude-opus-4-6`**” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account. **Where to call it:** [Anthropic Messages](https://apidoc.cometapi.com/anthropic-messages) format and [Chat](https://apidoc.cometapi.com/chat) format.

Insert your question or request into the content field—this is what the model will respond to . Process the API response to get the generated answer.

### Step 3: Retrieve and Verify Results

Process the API response to get the generated answer. After processing, the API responds with the task status and output data.

### FAQ

#### How large is the context window in the Claude Sonnet 4.6 API?

Claude Sonnet 4.6 supports a 1,000,000-token context window in beta, allowing developers to process entire codebases, contracts, or research datasets within a single request.

#### How does Claude Sonnet 4.6 compare with Claude Opus 4.6?

Sonnet 4.6 is a mid-tier model designed to deliver near-Opus performance at lower cost, while Opus 4.6 remains Anthropic’s flagship model for the most complex reasoning and research tasks.

#### Can Claude Sonnet 4.6 handle large software engineering projects?

Yes. Sonnet 4.6 performs strongly on software engineering benchmarks such as SWE-Bench Verified, achieving around 79.6%, making it well suited for repository-scale coding and debugging.

#### What new capabilities were added in Claude Sonnet 4.6 compared with Sonnet 4.5?

Sonnet 4.6 introduces a 1M token context window, improved coding accuracy, better instruction following, and stronger computer-use capabilities across software environments.

#### Is Claude Sonnet 4.6 suitable for agent workflows and automation?

Yes. The model supports tool calling, web search, and programmatic workflows, making it effective for building AI agents that perform multi-step tasks.

#### Which platforms support the Claude Sonnet 4.6 API?

Claude Sonnet 4.6 is available through CometAPI’s API .

## Features for Claude Sonnet 4.6

Explore the key features of Claude Sonnet 4.6, designed to enhance performance and usability. Discover how these capabilities can benefit your projects and improve user experience.

TEXT

text-to-text

pdf-to-text

image-to-text

speech-to-text

video-to-text

IMAGE

text-to-image

image-editing

VIDEO

text-to-video

image-to-video

video-editing

AUDIO

text-to-speech

speech-to-text

video-to-audio

## Pricing for Claude Sonnet 4.6

Explore competitive pricing for Claude Sonnet 4.6, designed to fit various budgets and usage needs. Our flexible plans ensure you only pay for what you use, making it easy to scale as your requirements grow. Discover how Claude Sonnet 4.6 can enhance your projects while keeping costs manageable.

| Comet Price (USD / M Tokens) | Official Price (USD / M Tokens) | Discount |
| --- | --- | --- |
| Input:$2.4/M<br>Output:$12/M | Input:$3/M<br>Output:$15/M | -20% |

## Sample code and API for Claude Sonnet 4.6

Access comprehensive sample code and API resources for Claude Sonnet 4.6 to streamline your integration process. Our detailed documentation provides step-by-step guidance, helping you leverage the full potential of Claude Sonnet 4.6 in your projects.

POST

[/v1/messages](https://apidoc.cometapi.com/anthropic-messages)

POST

[/v1/chat/completions](https://apidoc.cometapi.com/chat)

Copy

Python

JavaScript

Curl

```python
import anthropic
import os

# Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

message = anthropic.Anthropic(
    base_url=BASE_URL,
    api_key=COMETAPI_KEY,
)
messages = message.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(messages.content[0].text)
```

### Python Code Example

```
import anthropic
import os

# Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

message = anthropic.Anthropic(
    base_url=BASE_URL,
    api_key=COMETAPI_KEY,
)
messages = message.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(messages.content[0].text)
```

### JavaScript Code Example

```
import Anthropic from "@anthropic-ai/sdk";

// Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
const api_key = process.env.COMETAPI_KEY || "<YOUR_COMETAPI_KEY>";
const base_url = "https://api.cometapi.com";

const anthropic = new Anthropic({
  apiKey: api_key,
  baseURL: base_url,
});

const message = await anthropic.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude" }],
});
console.log(message.content[0].text);
```

### Curl Code Example

```
curl https://api.cometapi.com/v1/messages \
     --header "Authorization: $COMETAPI_KEY" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [\
        {"role": "user", "content": "Hello, Claude"}\
    ]
}'
```

## Versions of Claude Sonnet 4.6

The reason Claude Sonnet 4.6 has multiple snapshots may include potential factors such as variations in output after updates requiring older snapshots for consistency, providing developers a transition period for adaptation and migration, and different snapshots corresponding to global or regional endpoints to optimize user experience. For detailed differences between versions, please refer to the official documentation.

| version |
| --- |
| claude-sonnet-4-6 |
| claude-sonnet-4-6-thinking |

## More Models

[![Claude Opus 4.8](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2Fimage-1780019515442.jpeg&w=3840&q=75)\\
\\
Claude\\
\\
**Claude Opus 4.8**\\
\\
Input:$4/M\\
\\
Output:$20/M](https://www.cometapi.com/models/anthropic/claude-opus-4-8/) [![Gemini 3.5 Flash](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2Fimage-1779242267140.jpeg&w=3840&q=75)\\
\\
Google\\
\\
**Gemini 3.5 Flash**\\
\\
Input:$1.2/M\\
\\
Output:$7.2/M](https://www.cometapi.com/models/google/gemini-3-5-flash/) [![Gemini 3.1 Pro](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2F31cf8d0a-8d53-42ab-9c78-601a744532f4.png&w=3840&q=75)\\
\\
Google\\
\\
**Gemini 3.1 Pro**\\
\\
Input:$1.6/M\\
\\
Output:$9.6/M](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/) [![Kimi K2.7 Code](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2Fimage-1781274928307.jpeg&w=3840&q=75)\\
\\
MoonshotAI\\
\\
**Kimi K2.7 Code**\\
\\
Input:$0.76/M\\
\\
Output:$3.19998/M](https://www.cometapi.com/models/moonshotai/kimi-k2-7-code/) [![Claude Mythos 5](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2Fimage-1781058007347.jpeg&w=3840&q=75)\\
\\
Claude\\
\\
**Claude Mythos 5**\\
\\
Coming soon\\
\\
Input:$8/M\\
\\
Output:$40/M](https://www.cometapi.com/models/anthropic/claude-mythos-5/) [![Claude Opus 4.7](https://www.cometapi.com/_next/image/?url=https%3A%2F%2Fresource.cometapi.com%2Fs7.png&w=3840&q=75)\\
\\
Claude\\
\\
**Claude Opus 4.7**\\
\\
Input:$4/M\\
\\
Output:$20/M](https://www.cometapi.com/models/anthropic/claude-opus-4-7/)

## Related Blog

[![What Is Auto Compact in Claude Code](https://resource.cometapi.com/auto%20compact%20in%20claude%20code.webp)\\
\\
May 30, 2026\\
\\
claude-code\\
\\
**What Is Auto Compact in Claude Code** Auto Compact in Claude Code is Anthropic’s intelligent context management feature that automatically summarizes and compresses long conversation histories when approaching the ~200k token context window limit. It analyzes key decisions, code changes, and project state, replaces older messages with a concise summary, and lets you continue coding seamlessly—preventing crashes, token waste, and context loss in extended development sessions. Since version 2.0.64 (early 2026), compaction is near-instant, with manual \`/compact\` commands and configurable API options for power users.](https://www.cometapi.com/what-is-auto-compact-in-claude-code/) [![Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026](https://resource.cometapi.com/Cutting%20LLM%20API%20Costs%20in%20Half.webp)\\
\\
May 20, 2026\\
\\
**Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026** How to route LLM API traffic to cheap and flagship models in production: cascade pattern, cost math, failure modes, and a step-by-step migration playbook.](https://www.cometapi.com/cutting-llm-api-costs-in-half-a-model-routing-guide-for-production-workloads-in-2026/) [![The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4](https://resource.cometapi.com/image-1779333673645.jpeg)\\
\\
May 20, 2026\\
\\
gemini-3-5-flash\\
\\
gpt-5-5\\
\\
**The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4** Compare 2026 LLM API pricing for GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash , and DeepSeek V4. Worked example shows what 100M tokens/month actually costs.](https://www.cometapi.com/2026-llm-api-pricing-comparison-gpt-5-5-claude-gemini/) [![How to Completely Remove Claude Code: Step-by-Step Uninstall Guide + Best Alternatives](https://resource.cometapi.com/How%20to%20Completely%20Remove%20Claude%20Code.webp)\\
\\
May 8, 2026\\
\\
claude-code\\
\\
**How to Completely Remove Claude Code: Step-by-Step Uninstall Guide + Best Alternatives** Learn how to fully uninstall Claude Code from macOS, Windows, and Linux, remove leftover files, configs, and watermarks. Plus, latest Anthropic news, risks of AI-generated code, and why developers are switching to CometAPI for reliable multi-model access.](https://www.cometapi.com/how-to-remove-claude-code/) [![Claude 4.6/4.7 vs. GPT-5.4/5.5: A Comprehensive Comparison of ](https://resource.cometapi.com/Claude%204.7%20vs%20GPT-5.5.webp)\\
\\
May 7, 2026\\
\\
gpt-5-5\\
\\
claude-opus-4-7\\
\\
**Claude 4.6/4.7 vs. GPT-5.4/5.5: A Comprehensive Comparison of** A detailed 2026 comparison of Claude Claude 4.6/4.7 vs ChatGPT GPT-5.4/5.5 covering the latest model updates, benchmark data, pricing, context windows, use cases, and a practical verdict for writers, developers, and businesses.](https://www.cometapi.com/claude-4-6-4-7-vs-gpt-5-4-5-5/)