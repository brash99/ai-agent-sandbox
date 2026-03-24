# AI Agent Sandbox

A small Python sandbox for learning how AI agents work.

## Purpose

This repo is for experimenting with:
- model calls
- tool use
- web search
- custom function tools
- logging and inspection
- small evaluation workflows

The goal is not to build a giant autonomous system. The goal is to build small, understandable agent patterns and learn how they behave.

## Current version

### v0.1
A simple research-style agent that:
- accepts a user question
- decides whether to use tools
- can use web search
- can use a custom math tool
- logs full responses to JSON files

## Project structure

```text
ai-agent-sandbox/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   ├── prompts.py
│   ├── run_agent.py
│   └── tools.py
├── logs/
├── examples/
└── tests/
