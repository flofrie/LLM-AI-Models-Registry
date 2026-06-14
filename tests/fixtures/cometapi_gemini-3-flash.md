[Kimi K2.7 Code is now on CometAPI — Kimi's most intelligent coding model to date, reliably follows instructions in long contexts and completes programming tasks with a higher success rate. Try it now](https://www.cometapi.com/models/moonshotai/kimi-k2-7-code/)

[Schema](https://apidoc.cometapi.com/gemini-generating-content.md)

Copy Page

Gemini

# Gemini 3 Flash

100.00%

Input:$0.4/M

Output:$2.4/M

Context:1,048,576

Max Output:65.5k

Gemini 3 Flash is a lightweight, efficient multimodal large-scale model from Google tailored for real-world scenarios that require fast responses and low latency.

Text

New

Commercial Use

Playground

Overview

Features

Pricing

API

Versions

## Playground for Gemini 3 Flash

Explore Gemini 3 Flash's Playground — an interactive environment to test models, run queries in real time. Try prompts, adjust parameters, and iterate instantly to accelerate development and validate use cases.

Chat

JSON

![](https://lf3-static.bytednsdoc.com/obj/eden-cn/ptlz_zlp/ljhwZthlaukjlkulzlp/docs-icon.png)

Hello

![](https://resource.cometapi.com/logo.svg)

Hello, how can I help you?

Login to chat with Gemini 3 Flash

1. [What is Gemini 3 flash](https://www.cometapi.com/models/google/gemini-3-flash/#what-is-gemini-3-flash)
2. [Main features :](https://www.cometapi.com/models/google/gemini-3-flash/#main-features-)
3. [How Gemini 3 Flash compares to other models](https://www.cometapi.com/models/google/gemini-3-flash/#how-gemini-3-flash-compares-to-other-models-)
4. [Practical use cases (where Flash wins)](https://www.cometapi.com/models/google/gemini-3-flash/#practical-use-cases-where-flash-wins)
5. [How to access Gemini 3 flash API](https://www.cometapi.com/models/google/gemini-3-flash/#how-to-access-gemini-3-flash-api)
1. [Step 1: Sign Up for API Key](https://www.cometapi.com/models/google/gemini-3-flash/#step-1-sign-up-for-api-key)
2. [Step 3: Retrieve and Verify Results](https://www.cometapi.com/models/google/gemini-3-flash/#step-3-retrieve-and-verify-results)

## What is Gemini 3 flash

“Gemini 3 Flash” is the Flas h/fast member of the Gemini-3 family: a lighter, lower-latency, cost-efficient variant of Google’s Gemini-3 models intended for high-throughput, real-time and scale-sensitive applications. A variant of the Gemini API model family that lets developers call a low-latency, cost-optimized Gemini 3 style model over CometAPI's API (same API surface as other Gemini models). It exposes the same multimodal inputs and structured output tools but prioritizes inference speed and throughput.

## Main features :

- **Low latency / high throughput:** tuned for fast responses and cost efficiency (Flash design point).
- **Multimodal input support:** text, images, video snippets and audio in many Flash variants (API model entries list supported input types per variant).
- **Function calling & structured outputs:** JSON/structured output enforcement for integration with tools and agents.
- **Agent/Tooling support:** integrates with Google Search grounding, function/tool calling, and agent frameworks in the Gemini ecosystem.

## How Gemini 3 Flash compares to other models

- **Versus Gemini-3 Pro (same family):** Flash = speed/cost optimized; Pro = higher reasoning, multimodal fidelity, and Deep Think. Choose Flash for real-time UIs; Pro for accuracy-sensitive tasks.
- **Versus previous Gemini (2.5 Flash):** Gemini-3 family improves reasoning and multimodal performance; Flash design point continues to target price/performance. If you currently use 2.5 Flash, Gemini-3 Fast/Flash is intended to give better quality at similar latency/cost.

## Practical use cases (where Flash wins)

- **Realtime chatbots & voice agents:** low latency for conversational UIs and streaming audio applications.
- **Customer support & high-volume summarization:** cost-efficient summarization of long transcripts at scale.
- **Edge or embedded inference where response time matters:** use flash/lite style variants for tight SLAs.
- **Mass document parsing / ingestion pipelines:** Flash for indexing and pre-processing; escalate to Pro for high-value extraction/analysis.
- **Realtime code assistants / IDE plugins:** fast code completions with lower billing cost (validate with Pro for complex refactors).

## How to access Gemini 3 flash API

### Step 1: Sign Up for API Key

Log in to cometapi.com. If you are not our user yet, please register first. Sign into your [CometAPI console](https://api.cometapi.com/console/token). Get the access credential API key of the interface. Click “Add Token” at the API token in the personal center, get the token key: sk-xxxxx and submit.

Step 2: Send Requests to Gemini 3 flash API

Select the “ **`gemini-3-flash`**” endpoint to send the API request and set the request body. The request method and request body are obtained from our website API doc. Our website also provides Apifox test for your convenience. Replace <YOUR\_API\_KEY> with your actual CometAPI key from your account. base url is [Gemini Generating Content](https://apidoc.cometapi.com/gemini-generating-content) and [Chat](https://apidoc.cometapi.com/chat).

Insert your question or request into the content field—this is what the model will respond to . Process the API response to get the generated answer.

### Step 3: Retrieve and Verify Results

Process the API response to get the generated answer. After processing, the API responds with the task status and output data.

**See also** [**Gemini 3 Pro Preview API**](https://www.cometapi.com/gemini-3-pro-api/)

### FAQ

#### How does Gemini 3 Flash deliver Pro-level intelligence at Flash pricing?

Gemini 3 Flash is Google's most balanced model, offering frontier-level reasoning capabilities at $0.50/$3 per million tokens—approximately 4x cheaper than Gemini 3 Pro while maintaining comparable intelligence for most tasks.

#### What thinking levels does Gemini 3 Flash support?

Gemini 3 Flash supports four thinking levels: minimal (near-zero latency), low, medium, and high—giving developers granular control over the reasoning depth vs. speed tradeoff that Gemini 3 Pro doesn't offer.

#### Does Gemini 3 Flash have a free tier in the API?

Yes, Gemini 3 Flash (gemini-3-flash-preview) has a free tier in the Gemini API, unlike Gemini 3 Pro which currently requires paid usage for API access.

#### What are Thought Signatures and why are they required for Gemini 3 Flash?

Thought Signatures are encrypted representations of the model's internal reasoning that must be circulated back in multi-turn conversations—required even at minimal thinking level for Gemini 3 Flash to maintain reasoning context and enable function calling.

#### Can Gemini 3 Flash combine structured outputs with Google Search grounding?

Yes, Gemini 3 Flash uniquely supports combining structured outputs (JSON schema) with built-in tools like Google Search, URL Context, and Code Execution in the same request—enabling grounded, type-safe responses.

#### How does media\_resolution affect Gemini 3 Flash performance?

The media\_resolution parameter controls token usage per image/video frame: low (280 tokens), medium (560), high (1120), or ultra\_high for images. For video, low and medium are both capped at 70 tokens per frame to optimize context usage.

#### What tools does Gemini 3 Flash support?

Gemini 3 Flash supports Google Search, File Search, Code Execution, URL Context, and standard function calling. However, Google Maps grounding and Computer Use are not yet supported in Gemini 3 models.

## Features for Gemini 3 Flash

Explore the key features of Gemini 3 Flash, designed to enhance performance and usability. Discover how these capabilities can benefit your projects and improve user experience.

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

## Pricing for Gemini 3 Flash

Explore competitive pricing for Gemini 3 Flash, designed to fit various budgets and usage needs. Our flexible plans ensure you only pay for what you use, making it easy to scale as your requirements grow. Discover how Gemini 3 Flash can enhance your projects while keeping costs manageable.

### Correction: gemini-3-flash variants (same price across variants)

| Model family | Variant (model name) | Input price (USD / 1M tokens) | Output price (USD / 1M tokens) |
| --- | --- | --- | --- |
| gemini-3-flash | gemini-3-flash | $0.40 | $2.40 |
| gemini-3-flash | gemini-3-flash-preview | $0.40 | $2.40 |
| gemini-3-flash | gemini-3-flash-all | $0.40 | $2.40 |
| gemini-3-flash | gemini-3-flash-thinking | $0.40 | $2.40 |
| gemini-3-flash | gemini-3-flash-preview-thinking | $0.40 | $2.40 |

## Sample code and API for Gemini 3 Flash

Gemini 3 Flash is a text-only large language model (LLM) exposed through CometAPI’s hosted API (and mirrored by vendor inference layers). The API supports standard chat/completion patterns, streaming responses, function/tool invocation, structured JSON output, and several “thinking” modes designed for agent-style workflows (interleaved / preserved / turn-level thinking).

POST

[/v1beta/models/{model}:{operator}](https://apidoc.cometapi.com/)

POST

[/v1/chat/completions](https://apidoc.cometapi.com/)

Copy

Python

JavaScript

Curl

```python
from google import genai
import os

# Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

client = genai.Client(
    http_options={"api_version": "v1beta", "base_url": BASE_URL},
    api_key=COMETAPI_KEY,
)

response = client.models.generate_content(
    model="gemini-3-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### Python Code Example

```
from google import genai
import os

# Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
COMETAPI_KEY = os.environ.get("COMETAPI_KEY") or "<YOUR_COMETAPI_KEY>"
BASE_URL = "https://api.cometapi.com"

client = genai.Client(
    http_options={"api_version": "v1beta", "base_url": BASE_URL},
    api_key=COMETAPI_KEY,
)

response = client.models.generate_content(
    model="gemini-3-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript Code Example

```
// Get your CometAPI key from https://api.cometapi.com/console/token, and paste it here
const api_key = process.env.COMETAPI_KEY;
const base_url = "https://api.cometapi.com/v1beta";
const model = "gemini-3-flash";
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
#!/bin/bash

curl "https://api.cometapi.com/v1beta/models/gemini-3-flash:generateContent" \
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

## Versions of Gemini 3 Flash

The reason Gemini 3 Flash has multiple snapshots may include potential factors such as variations in output after updates requiring older snapshots for consistency, providing developers a transition period for adaptation and migration, and different snapshots corresponding to global or regional endpoints to optimize user experience. For detailed differences between versions, please refer to the official documentation.

| Model id | Description | Availability | Request |
| --- | --- | --- | --- |
| gemini-3-flash-all | The technology used is unofficial and the generation is unstable but Direct Internet etc， [Chat](https://apidoc.cometapi.com/chat "Chat") format | ✅ | [Chat](https://apidoc.cometapi.com/chat "Chat") format |
| **gemini-3-flash** | Automatically points to the latest model | ✅ | [Gemini Generating Content](https://apidoc.cometapi.com/gemini-generating-content "Gemini  Generating Content") |
| gemini-3-flash-preview | Official Preview | ✅ | [Gemini Generating Content](https://apidoc.cometapi.com/gemini-generating-content "Gemini  Generating Content") |

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

[![Google Shopping Guide: How Google AI Helps Consumers Shop Better](https://resource.cometapi.com/Google%20Shopping%20Guide%20How%20Google%20AI%20Helps%20Consumers%20Shop%20Better.webp)\\
\\
Feb 21, 2026\\
\\
google\\
\\
**Google Shopping Guide: How Google AI Helps Consumers Shop Better** Google’s push to fold generative AI into the shopping experience has shifted what “search + buy” looks like. Over the last 18 months the company has layered Gemini-powered AI, a re-built Shopping experience, agentic checkout standards and merchant tools that let AI act — within limits — on shoppers’ behalf. For consumers that means conversational discovery, personalized briefs, virtual try-ons, price-tracking and, increasingly, the option for AI to complete purchases; for retailers it means new integrations, richer product data demands, and attention to privacy and payment protocols.](https://www.cometapi.com/how-google-ai-helps-consumers-shop-better/) [![Google Gemini 3.5(Snow Bunny) Leaked: All you need to know ](https://resource.cometapi.com/Gemini-3.5-pro.jpg)\\
\\
Jan 30, 2026\\
\\
gemini-3-5\\
\\
**Google Gemini 3.5(Snow Bunny) Leaked: All you need to know** Google is quietly testing a new internal iteration of its Gemini family — reported variously as “Gemini 3.5” and by the intriguing internal codename “Snow Bunny.” Codenamed "Snow Bunny," this internal checkpoint has reportedly shattered existing benchmarks, demonstrating an unprecedented ability to generate entire software applications—up to 3,000 lines of functional code—in a single prompt.](https://www.cometapi.com/google-gemini-3-5snow-bunny-leaked/) [![Openclaw(Moltbot /Clawdbot) : Setup Guide+ API hosting Tutorial](https://resource.cometapi.com/Moltbot.webp)\\
\\
Jan 29, 2026\\
\\
clawdbot\\
\\
**Openclaw(Moltbot /Clawdbot) : Setup Guide+ API hosting Tutorial** Moltbot — previously known to the internet as Clawdbot — erupted onto timelines in late January 2026 as a do-it-yourself, agentic personal assistant that actually executes tasks on your behalf: clearing inboxes, running commands, searching local files, and answering through your chat app of choice (Telegram, WhatsApp, Discord, iMessage, etc.).](https://www.cometapi.com/moltbot-clawdbot--setup-guide-api-hosting-tutorial/) [![How to “Vibe Coding” a Tiny Mobile App as beginner](https://resource.cometapi.com/How%20to%20%E2%80%9CVibe%20Coding%E2%80%9D%20a%20Tiny%20Mobile%20App%20as%20beginner%20.webp)\\
\\
Jan 28, 2026\\
\\
vibe-coding\\
\\
**How to “Vibe Coding” a Tiny Mobile App as beginner** Vibe Coding a tiny mobile app as a beginner is all about momentum and feel: start with a very small idea (like a counter or simple to-do app), pick an easy framework or tool (Codex, Cursor etc.), build something that runs as fast as possible without worrying about clean code, then tweak the UI and interactions by feel while testing on your phone. When you get stuck, search or ask AI instead of overthinking, and once it works and feels good, stop and ship it. The goal is flow and confidence, not perfection.](https://www.cometapi.com/how-to-%E2%80%9Cvibe-coding%E2%80%9D-a-tiny-mobile-app-as-beginner/) [![Shopping on Google: How do you use Google’s AI shopping as Merchants](https://resource.cometapi.com/How%20do%20you%20use%20Google's%20Al.webp)\\
\\
Jan 24, 2026\\
\\
gemini-3-flash\\
\\
gemini-3-pro-preview\\
\\
**Shopping on Google: How do you use Google’s AI shopping as Merchants** Google has reworked its shopping experience around generative AI and the Gemini family of models. For consumers, the shift promises conversational product discovery, AI-generated comparison briefs, and — where available — automated “agentic” checkout that can buy on your behalf when preconditions are met. For merchants and developers, the new surface combines two sets of APIs (shopping / merchant APIs and Google’s GenAI / Gemini APIs) and requires updated feed practices, privacy controls, and technical integration.](https://www.cometapi.com/shopping-on-google-how-do-you-use-googlee28099s-ai-shopping-as-merchants/)