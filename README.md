# Project Structure

## Core

```bash
cria-index-core
├── README.md
├── VERSION
├── cria_index
│   └── core
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-310.pyc
│       ├── llama_packs
│       │   ├── __init__.py
│       │   └── base.py
│       ├── llms
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-310.pyc
│       │   │   └── base.cpython-310.pyc
│       │   └── base.py
│       ├── readers
│       │   ├── __init__.py
│       │   └── base.py
│       ├── tools
│       │   ├── __init__.py
│       │   └── base.py
│       └── vector_stores
│           ├── __init__.py
│           ├── __pycache__
│           │   ├── __init__.cpython-310.pyc
│           │   └── base.cpython-310.pyc
│           └── base.py
├── dist
│   ├── cria_core-0.1.0-py3-none-any.whl
│   ├── cria_core-0.1.0.tar.gz
│   ├── cria_core-0.1.1-py3-none-any.whl
│   └── cria_core-0.1.1.tar.gz
├── poetry.lock
├── pyproject.toml
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   └── test_classes.cpython-310-pytest-7.4.4.pyc
    └── test_classes.py
```

## Integrations

### LLMs

```bash
├── cria-index-llms-huggingface
│   ├── README.md
│   ├── cria_index
│   │   └── llms
│   │       └── huggingface
│   │           ├── __init__.py
│   │           ├── __pycache__
│   │           │   ├── __init__.cpython-310.pyc
│   │           │   └── base.cpython-310.pyc
│   │           └── base.py
│   ├── dist
│   │   ├── cria_llms_huggingface-0.1.0-py3-none-any.whl
│   │   └── cria_llms_huggingface-0.1.0.tar.gz
│   ├── examples
│   │   └── HuggingFaceLLM.ipynb
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_classes.cpython-310-pytest-7.4.4.pyc
│       └── test_classes.py
└── cria-index-llms-openai
    ├── README.md
    ├── cria_index
    │   └── llms
    │       └── openai
    │           ├── __init__.py
    │           ├── __pycache__
    │           │   ├── __init__.cpython-310.pyc
    │           │   └── base.cpython-310.pyc
    │           └── base.py
    ├── dist
    │   ├── cria_llms_openai-0.1.0-py3-none-any.whl
    │   └── cria_llms_openai-0.1.0.tar.gz
    ├── examples
    │   └── OpenAI.ipynb
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   └── test_classes.cpython-310-pytest-7.4.4.pyc
        └── test_classes.py
```

### Vector Stores

```bash
├── cria-index-vector-stores-elasticsearch
│   ├── README.md
│   ├── cria_index
│   │   └── vector_stores
│   │       └── elasticsearch
│   │           ├── __init__.py
│   │           ├── __pycache__
│   │           │   ├── __init__.cpython-310.pyc
│   │           │   └── base.cpython-310.pyc
│   │           └── base.py
│   ├── dist
│   │   ├── cria_vector_stores_elasticsearch-0.1.0-py3-none-any.whl
│   │   └── cria_vector_stores_elasticsearch-0.1.0.tar.gz
│   ├── examples
│   │   └── ElasticSearchVectorStore.ipynb
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       ├── __init__.py
│       └── test_classes.py
└── cria-index-vector-stores-qdrant
    ├── README.md
    ├── cria_index
    │   └── vector_stores
    │       └── qdrant
    │           ├── __init__.py
    │           ├── __pycache__
    │           │   ├── __init__.cpython-310.pyc
    │           │   └── base.cpython-310.pyc
    │           └── base.py
    ├── dist
    │   ├── cria_vector_stores_qdrant-0.1.0-py3-none-any.whl
    │   └── cria_vector_stores_qdrant-0.1.0.tar.gz
    ├── examples
    │   └── QdrantVectorStore.ipynb
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   └── test_classes.cpython-310-pytest-7.4.4.pyc
        └── test_classes.py
```

## Plugins

### Loaders 

```bash
├── cria-index-plugin-loader-gmail
│   ├── README.md
│   ├── cria_index
│   │   └── plugins
│   │       └── loaders
│   │           └── gmail
│   │               ├── __init__.py
│   │               ├── __pycache__
│   │               │   ├── __init__.cpython-310.pyc
│   │               │   └── base.cpython-310.pyc
│   │               └── base.py
│   ├── dist
│   │   ├── cria_plugin_loader_gmail-0.1.0-py3-none-any.whl
│   │   └── cria_plugin_loader_gmail-0.1.0.tar.gz
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_classes.cpython-310-pytest-7.4.4.pyc
│       └── test_classes.py
└── cria-index-plugin-loader-notion
    ├── README.md
    ├── cria_index
    │   └── plugins
    │       └── loaders
    │           └── notion
    │               ├── __init__.py
    │               ├── __pycache__
    │               │   ├── __init__.cpython-310.pyc
    │               │   └── base.cpython-310.pyc
    │               └── base.py
    ├── dist
    │   ├── cria_plugin_loader_notion-0.1.0-py3-none-any.whl
    │   └── cria_plugin_loader_notion-0.1.0.tar.gz
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   └── test_classes.cpython-310-pytest-7.4.4.pyc
        └── test_classes.py
```

### Tools

```bash
├── cria-index-plugin-tool-arxiv
│   ├── README.md
│   ├── cria_index
│   │   └── plugins
│   │       └── tools
│   │           └── arxiv
│   │               ├── __init__.py
│   │               ├── __pycache__
│   │               │   ├── __init__.cpython-310.pyc
│   │               │   └── base.cpython-310.pyc
│   │               └── base.py
│   ├── dist
│   │   ├── cria_index_tool_plugin_arxiv-0.1.0-py3-none-any.whl
│   │   └── cria_index_tool_plugin_arxiv-0.1.0.tar.gz
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_classes.cpython-310-pytest-7.4.4.pyc
│       └── test_classes.py
└── cria-index-plugin-tool-gmail
    ├── README.md
    ├── cria_index
    │   └── plugins
    │       └── tools
    │           └── gmail
    │               ├── __init__.py
    │               ├── __pycache__
    │               │   ├── __init__.cpython-310.pyc
    │               │   └── base.cpython-310.pyc
    │               └── base.py
    ├── dist
    │   ├── cria_index_tool_plugin_gmail-0.1.0-py3-none-any.whl
    │   └── cria_index_tool_plugin_gmail-0.1.0.tar.gz
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   └── test_classes.cpython-310-pytest-7.4.4.pyc
        └── test_classes.py
```

### Packs

```
├── cria-index-plugin-pack-rag-evaluator
│   ├── README.md
│   ├── cria_index
│   │   └── plugins
│   │       └── packs
│   │           └── rag_evaluator
│   │               ├── __init__.py
│   │               ├── __pycache__
│   │               │   ├── __init__.cpython-310.pyc
│   │               │   └── base.cpython-310.pyc
│   │               └── base.py
│   ├── dist
│   │   ├── cria_plugin_pack_rag_evaluator-0.1.0-py3-none-any.whl
│   │   └── cria_plugin_pack_rag_evaluator-0.1.0.tar.gz
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_classes.cpython-310-pytest-7.4.4.pyc
│       └── test_classes.py
└── cria-index-plugin-pack-resume-screener
    ├── README.md
    ├── cria_index
    │   └── plugins
    │       └── packs
    │           └── resume_screener
    │               ├── __init__.py
    │               └── base.py
    ├── dist
    │   ├── cria_index_plugin_pack_resume_screener-0.1.0-py3-none-any.whl
    │   └── cria_index_plugin_pack_resume_screener-0.1.0.tar.gz
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        └── test_classes.py
```

## Experimental

```bash
├── README.md
├── cria_index
│   └── experimental
│       ├── __init__.py
│       └── experimental_feature.py
├── dist
│   ├── cria_index_experimental-0.1.0-py3-none-any.whl
│   └── cria_index_experimental-0.1.0.tar.gz
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py
```