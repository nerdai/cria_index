## Project Structure

```
├── README.md
├── cria-index-core
│   ├── README.md
│   ├── cria_index
│   │   └── core
│   │       └── __init__.py
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
├── cria-index-integrations
│   ├── llms
│   │   ├── cria-index-llms-huggingface
│   │   │   ├── README.md
│   │   │   ├── cria_index
│   │   │   │   └── llms
│   │   │   │       └── huggingface
│   │   │   │           └── __init__.py
│   │   │   ├── pyproject.toml
│   │   │   └── tests
│   │   │       └── __init__.py
│   │   └── cria-index-llms-openai
│   │       ├── README.md
│   │       ├── cria_index
│   │       │   └── llms
│   │       │       └── openai
│   │       │           └── __init__.py
│   │       ├── pyproject.toml
│   │       └── tests
│   │           └── __init__.py
│   └── vector-stores
│       ├── cria-index-vector-stores-elasticsearch
│       │   ├── README.md
│       │   ├── cria_index
│       │   │   └── vector_stores
│       │   │       └── elasticsearch
│       │   │           └── __init__.py
│       │   ├── pyproject.toml
│       │   └── tests
│       │       └── __init__.py
│       └── cria-index-vector-stores-qdrant
│           ├── README.md
│           ├── cria_index
│           │   └── vector_stores
│           │       └── qdrant
│           │           └── __init__.py
│           ├── pyproject.toml
│           └── tests
│               └── __init__.py
└── cria-index-plugins
    ├── datasets
    ├── loaders
    │   ├── cria-index-loader-plugin-gmail
    │   │   ├── README.md
    │   │   ├── cria_index_loader_plugin_gmail
    │   │   │   └── __init__.py
    │   │   ├── pyproject.toml
    │   │   └── tests
    │   │       └── __init__.py
    │   └── cria-index-loader-plugin-notion
    │       ├── README.md
    │       ├── cria_index_loader_plugin_notion
    │       │   └── __init__.py
    │       ├── pyproject.toml
    │       └── tests
    │           └── __init__.py
    ├── packs
    │   ├── cria-index-pack-plugin-rag-evaluator
    │   │   ├── README.md
    │   │   ├── cria_index_pack_plugin_rag_evaluator
    │   │   │   └── __init__.py
    │   │   ├── pyproject.toml
    │   │   └── tests
    │   │       └── __init__.py
    │   └── cria-index-pack-plugin-resume-screener
    │       ├── README.md
    │       ├── cria_index_pack_plugin_resume_screener
    │       │   └── __init__.py
    │       ├── pyproject.toml
    │       └── tests
    │           └── __init__.py
    └── tools
        ├── cria-index-tool-plugin-arxiv
        │   ├── README.md
        │   ├── cria_index_tool_plugin_arxiv
        │   │   └── __init__.py
        │   ├── pyproject.toml
        │   └── tests
        │       └── __init__.py
        └── cria-index-tool-plugin-gmail
            ├── README.md
            ├── cria_index_tool_plugin_gmail
            │   └── __init__.py
            ├── pyproject.toml
            └── tests
                └── __init__.py
```