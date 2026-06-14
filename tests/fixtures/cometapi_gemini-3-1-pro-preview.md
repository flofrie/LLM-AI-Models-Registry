[Kimi K2.7 Code is now on CometAPI — Kimi's most intelligent coding model to date, reliably follows instructions in long contexts and completes programming tasks with a higher success rate. Try it now](https://www.cometapi.com/models/moonshotai/kimi-k2-7-code/)

[Schema](https://apidoc.cometapi.com/chat.md)

Copy Page

Google

# Gemini 3.1 Pro

Input:$1.6/M

Output:$9.6/M

Gemini 3.1 Pro is the next generation in the Gemini series of models, a suite of highly-capable, natively multimodal, reasoning models. Gemini 3 Pro is now Google’s most advanced model for complex tasks, and can comprehend vast datasets, challenging problems from different information sources, including text, audio, images, video, and entire code repositories

Text

New

Commercial Use

Playground

Overview

Features

Pricing

API

Versions

## Playground for Gemini 3.1 Pro

Explore Gemini 3.1 Pro's Playground — an interactive environment to test models, run queries in real time. Try prompts, adjust parameters, and iterate instantly to accelerate development and validate use cases.

Chat

JSON

![](https://lf3-static.bytednsdoc.com/obj/eden-cn/ptlz_zlp/ljhwZthlaukjlkulzlp/docs-icon.png)

Hello

![](https://resource.cometapi.com/logo.svg)

Hello, how can I help you?

Login to chat with Gemini 3.1 Pro

1. [Technical specifications — Gemini 3.1 Pro](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#technical-specifications--gemini-31-pro)
2. [What is Gemini 3.1 Pro ?](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#what-is-gemini-31-pro-)
3. [Main Features of Gemini 3.1 Pro](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#main-features-of-gemini-31-pro)
1. [Multimodal Integration](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#multimodal-integration)
2. [Extended Context Window](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#extended-context-window)
3. [Sparse Mixture-of-Experts (MoE) Scaling](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#sparse-mixture-of-experts-moe-scaling)
4. [Advanced Reasoning / Planning](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#advanced-reasoning--planning)
4. [Supposed benchmarks:](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#supposed-benchmarks)
5. [Representative enterprise use cases](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#representative-enterprise-use-cases)
6. [How to access Gemini 3.1 Pro API](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#how-to-access-gemini-31-pro-api)
1. [Step 1: Sign Up for API Key](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#step-1-sign-up-for-api-key)
2. [Step 3: Retrieve and Verify Results](https://www.cometapi.com/models/google/gemini-3-1-pro-preview/#step-3-retrieve-and-verify-results)

## Technical specifications — Gemini 3.1 Pro

| Item | gemini-3-pro (public summary) |
| --- | --- |
| Provider | Google |
| Canonical model id | gemini-3-pro (public preview) |
| Input types | Text, Image, Video, Audio, PDF |
| Output types | Text (natural language, structured outputs, function-call payloads) |
| Input token limit (context) | 1,048,576 tokens |
| Output token limit | 65,536 tokens |
| Function-calling / tool use | Supported (function calling, structured outputs, tool integrations) |
| Multimodality | Full multimodal support (images, video, audio, documents) |
| Code execution & agentic flows | Supported (agent mode, code assist, tool orchestration) |
| Knowledge cutoff | January 2025 |

## What is Gemini 3.1 Pro ?

Gemini 3.1 Pro is Google’s publicly flagship in the Gemini 3 family, positioned as a state-of-the-art multimodal reasoning model with advanced agentic and developer tooling. The model emphasizes high-capacity context handling (over **1M token** inputs), broad media support (images, video, audio, PDF), and deep integrations for tool use, function calling, and code-centric workflows (e.g., Gemini Code Assist and agent modes).

Gemini 3 Pro is presented by Google as optimized for both interactive developer experiences (low-latency coding and agent workflows) and high-fidelity multimodal understanding (interpreting and reasoning across mixed media inputs).

## Main Features of Gemini 3.1 Pro

Gemini-3.1 Pro (via its Preview) introduces the following features:

### Multimodal Integration

Processes inputs across:

- Natural language
- Images
- Speech/audio
- Video

with a unified token representation for cross-modal reasoning.

### Extended Context Window

An exceptionally large context capacity of up to ~1 million tokens enables handling of:

- Long documents
- Multidocument synthesis
- Codebases and transcripts.

This surpasses many competing models that typically support ~32 K–262 K tokens.

### Sparse Mixture-of-Experts (MoE) Scaling

Sparse MoE routing allows _scaling internal model capacity_ without proportional compute costs, improving reasoning at scale.

### Advanced Reasoning / Planning

Innovations like chain-of-thought training, reinforcement learning from human feedback, and specialized benchmarks make it strong on logical and mathematical tasks.

## Supposed benchmarks:

AIME 2025: 100% (with code execution)

SWE-Bench Verified: 83.9%

ARC-AGI-2: 71.8%

LiveCodeBench Pro: 2844 Elo

Terminal-Bench 2.0: 63.5%

MMMLU: 93.6%

## Representative enterprise use cases

- **End-to-end media pipelines:** Ingest video, transcript, and images to produce synchronized summaries, metadata, and structured insight at scale.
- **Large-scale code generation and review:** Use in IDEs and CI pipelines to auto-generate code, refactor multi-file projects, and produce test suggestions across large codebases.
- **Agentic automation:** Coordinate multi-tool agents that interact with cloud services, orchestration systems, and internal APIs using structured function calls.
- **Research & content production:** Draft long-form content (reports, books) that combine text and embedded multimedia with internal cross-references preserved.

## How to access Gemini 3.1 Pro API

### Step 1: Sign Up for API Key

Log in to cometapi.com. If you are not our user yet, please register first. Sign into your [CometAPI console](https://api.cometapi.com/console/token). Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

Step 2: Send Requests to Gemini 3.1 Pro API

Select the “ **`gemini-3.1-pro`**” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account. base url is [Gemini Generating Content](https://apidoc.cometapi.com/gemini-generating-content) and [Chat](https://apidoc.cometapi.com/chat).

Insert your question or request into the content field—this is what the model will respond to . Process the API response to get the generated answer.

### Step 3: Retrieve and Verify Results

Process the API response to get the generated answer. After processing, the API responds with the task status and output data.

**See also** [**Gemini 3 Pro API**](https://www.cometapi.com/gemini-3-pro-api/)

### FAQ

#### Can the Gemini 3.1 Pro API handle 1,048,576‑token documents?

Yes. The Gemini 3.1 Pro supports a context window of up to 1,048,576 tokens and can produce outputs up to 65,536 tokens, enabling single‑session reasoning over very large documents or codebases.

#### What input modalities does Gemini 3.1 Pro accept through the API?

Gemini 3.1 Pro Preview accepts text, images, video, audio, and PDF inputs and can reason across these modalities in a single session.

#### Does Gemini 3.1 Pro support function calling, structured outputs, and agentic tool use?

Yes. The API supports function calling, JSON‑constrained structured outputs, search grounding, and agentic/tool execution patterns (including code execution hooks in supported environments).

#### Is Gemini 3.1 Pro production‑ready?

Exercise caution: it is a public preview release (launched Nov 18, 2025). Validate API contracts, quotas, and behavior for your workloads and sandbox agentic or code‑execution features before wide production rollout.

#### What is Gemini 3.1 Pro Preview's knowledge cutoff date?

The documented knowledge cutoff for Gemini 3 Pro Preview is January 2025.

## Features for Gemini 3.1 Pro

Explore the key features of Gemini 3.1 Pro, designed to enhance performance and usability. Discover how these capabilities can benefit your projects and improve user experience.

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

## Pricing for Gemini 3.1 Pro

Explore competitive pricing for Gemini 3.1 Pro, designed to fit various budgets and usage needs. Our flexible plans ensure you only pay for what you use, making it easy to scale as your requirements grow. Discover how Gemini 3.1 Pro can enhance your projects while keeping costs manageable.

| Comet Price (USD / M Tokens) | Official Price (USD / M Tokens) | Discount |
| --- | --- | --- |
| Input:$1.6/M<br>Output:$9.6/M | Input:$2/M<br>Output:$12/M | -20% |

## Sample code and API for Gemini 3.1 Pro

Access comprehensive sample code and API resources for Gemini 3.1 Pro to streamline your integration process. Our detailed documentation provides step-by-step guidance, helping you leverage the full potential of Gemini 3.1 Pro in your projects.

POST

[/v1/chat/completions](https://apidoc.cometapi.com/chat)

Copy

Python

JavaScript

Curl

```python
from google import genai
import os

# Get your CometAPI key from https://www.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

client = genai.Client(
    http_options={"api_version": "v1beta", "base_url": BASE_URL},
    api_key=COMETAPI_KEY,
)

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### Python Code Example

```
from google import genai
import os

# Get your CometAPI key from https://www.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

client = genai.Client(
    http_options={"api_version": "v1beta", "base_url": BASE_URL},
    api_key=COMETAPI_KEY,
)

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript Code Example

```
// Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
const api_key = process.env.COMETAPI_KEY || "<YOUR_COMETAPI_KEY>";
const base_url = "https://api.cometapi.com/v1beta";
const model = "gemini-3.1-pro-preview";
const operator = "generateContent";

async function main() {
  const response = await fetch(`${base_url}/models/${model}:${operator}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: api_key,
    },
    body: JSON.stringify({
      contents: [\
        {\
          parts: [{ text: "Explain how AI works in a few words" }],\
        },\
      ],
    }),
  });

  const data = await response.json();
  console.log(data.candidates[0].content.parts[0].text);
}

await main();
```

### Curl Code Example

```
curl "https://api.cometapi.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "Authorization: $COMETAPI_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a few words"\
          }\
        ]\
      }\
    ]
  }'
```

## Versions of Gemini 3.1 Pro

The reason Gemini 3.1 Pro has multiple snapshots may include potential factors such as variations in output after updates requiring older snapshots for consistency, providing developers a transition period for adaptation and migration, and different snapshots corresponding to global or regional endpoints to optimize user experience. For detailed differences between versions, please refer to the official documentation.

| version |
| --- |
| gemini-3.1-pro-preview-all |
| gemini-3.1-pro-preview |
| gemini-3.1-pro-preview-thinking |

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

[![Cancel Your AI Subscriptions and Pay Only for What Your Product Actually Uses](https://resource.cometapi.com/Pay-as-you-go%20.webp)\\
\\
Jun 12, 2026\\
\\
**Cancel Your AI Subscriptions and Pay Only for What Your Product Actually Uses** Per-unit billing, not per-month. Cost is calculated per token (text models), per second (video models), per minute (audio models), or per generation (image models). Your bill at the end of the month is the sum of what you actually used, with no flat fee on top.](https://www.cometapi.com/cancel-your-ai-subscriptions-and-pay-only-for-what-your-product-actually-uses/) [![GPT-5.5 vs Claude Sonnet 4.6 vs Gemini 3.1 Pro: What No Benchmark Tells You](https://resource.cometapi.com/image-1781251897896.jpeg)\\
\\
Jun 12, 2026\\
\\
gemini-3-1-pro\\
\\
gpt-5-5\\
\\
**GPT-5.5 vs Claude Sonnet 4.6 vs Gemini 3.1 Pro: What No Benchmark Tells You** Three concrete prompts be sent to GPT-5.5, Claude Sonnet 4.6, and Gemini 3.1 Pro through the same OpenAI-compatible endpoint, with the same temperature settings and no extra prompting.](https://www.cometapi.com/gpt-5-5-vs-claude-sonnet-4-6-vs-gemini-3-1-pro-what-no-benchmark-tells-you/) [![How to Update Gemini CLI to the Latest Version: Complete Guide, New Features & Pro Tips](https://resource.cometapi.com/How%20to%20Update%20Gemini%20CLI.webp)\\
\\
Jun 7, 2026\\
\\
gemini-cli\\
\\
**How to Update Gemini CLI to the Latest Version: Complete Guide, New Features & Pro Tips** Learn exactly how to update Gemini CLI with step-by-step instructions, latest changelog highlights from v0.40.0, troubleshooting tips, and why pairing it with CometAPI delivers faster, cheaper Gemini-powered workflows. Master terminal AI in minutes.](https://www.cometapi.com/how-to-update-gemini-cli/) [![Function Calling in the OpenAI API: What It Actually Does and How to Use It Right](https://resource.cometapi.com/Function%20Calling%20in%20the%20OpenAI%20API.webp)\\
\\
Apr 20, 2026\\
\\
open-ai\\
\\
tech\\
\\
**Function Calling in the OpenAI API: What It Actually Does and How to Use It Right** Master OpenAI Function Calling: move beyond prompt engineering to structured orchestration. Learn strict schema enforcement, security best practices, and agentic workflows. Standardize tool calling across GPT, Claude, and Gemini with CometAPI.](https://www.cometapi.com/function-calling-in-the-openai-api/) [![Best Chatgpt Model for Math in 2026](https://resource.cometapi.com/chatgpt.jpg)\\
\\
Apr 7, 2026\\
\\
chat-gpt\\
\\
**Best Chatgpt Model for Math in 2026** The best ChatGPT model for math in 2026 is \*\*GPT-5.4 Pro\*\* (high/xhigh reasoning mode). It achieves 100% on AIME 2025, 98.1% on MATH Level 5, and 50% on FrontierMath — leading Claude Opus 4.6 (40.7% FrontierMath) and Gemini 3.1 Pro (95.1% MATH but trails on competition math). For developers, access it cheapest via CometAPI pay-as-you-go.](https://www.cometapi.com/best-chatgpt-model-for-math-in-2026/)