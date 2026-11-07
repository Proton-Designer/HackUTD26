# Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) — 2025 (6 projects)

### AgentBIM
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Honorable Mention

**What it is:** Gradio-based agent that answers plain-English questions about a building (BIM) model. IFC files are parsed with IfcOpenShell into a graph in ArangoDB, and a LangChain chain translates questions into AQL queries.
**Problem / user:** People working with BIM data who must go through slow, repetitive exchanges to explore a building model.

**Features**
- IFC to graph — IfcOpenShell parses IFC files and NetworkX transforms them into a graph stored in ArangoDB. *[claimed]*
- Natural-language to AQL — LangChain ArangoGraphQAChain turns a question into an AQL query over elements, relationships and spatial properties. *[claimed]*
- Gradio front end — User types questions and gets text or visual results. *[claimed]*
- Intent recognition, richer visualization, more IFC properties — Listed future work. *[planned]*

**Flow:** Enter question in Gradio → Chain generates AQL → Query runs on ArangoDB → Text or visual answer returned

**Prompt:** Build an agent that answers natural-language questions over graph data: load a dataset into NetworkX and ArangoDB, route simple queries to AQL and complex ones to cuGraph analytics, with hybrids earning extra credit; judged on innovation, functionality, technical excellence, usability and documentation.
**Fit (implied):** Uses ArangoDB graph plus NL-to-AQL agent; page does not mention cuGraph or hybrid routing, so only the AQL half of the brief is addressed.  *(targeted: Honorable Mention)*
**Sponsor tools:** ArangoDB (Graph store and AQL queries for the building model, core)
**AI:** LLM (unnamed) via LangChain ArangoGraphQAChain generates AQL from questions; LangGraph listed in tags.
**Architecture:** IFC files to IfcOpenShell parsing to NetworkX graph to ArangoDB; Gradio UI sends questions to a LangChain QA chain that runs AQL.
**Novelty:** Applies graph-QA to construction BIM/IFC data, an uncommon domain for this challenge.
**Scope:** small · working: Page claims a working system but lists no demo or video; repo could not be cloned for inspection. · polish: Text-only writeup; no screenshots described.
**Gaps:** Repo clone failed; No demo; LLM unnamed
Sources: https://devpost.com/software/agentbim, sponsor_prompts_NVIDIA.jsonl

---

### AskStreets: Querying and Visualizing Street Networks
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Second Place [2nd]

**What it is:** Jupyter-based LangGraph ReAct agent that answers natural-language questions about street networks by downloading OpenStreetMap graphs with OSMnx, storing them in ArangoDB, and calling text-to-AQL, text-to-OSMnx, geocoder and Folium map tools, with an optional cuGraph GPU notebook.
**Problem / user:** City planners, architects and business owners who want street-network analysis (accessibility, distances, busy intersections) without writing graph code.

**Features**
- Agent with four tools — ReAct agent chooses between text-to-AQL, text-to-OSMnx/NetworkX code, geocoder and map visualizer. *[shown_working]*
- Street graph persistence — OSMnx graphs and OSM features stored in ArangoDB. *[shown_working]*
- GPU graph algorithms — Notebook uses RAPIDS and NVIDIA cuGraph for accelerated analysis. *[shown_working]*
- Map output — Folium maps plot points and results. *[shown_working]*
- Cross-source queries — AQL combines street graph, OSM features and health-facility data. *[shown_working]*

**Flow:** Set up ArangoDB and credentials → Open notebook → Call query_street_network with a question → Agent runs tools → Receive text answer or map

**Prompt:** Build an agent that answers natural-language questions over graph data: load a dataset into NetworkX and ArangoDB, route simple queries to AQL and complex ones to cuGraph analytics, with hybrids earning extra credit; judged on innovation, functionality, technical excellence, usability and documentation.
**Fit (explicit):** Combines AQL tool and graph-algorithm tool on ArangoDB with a GPU cuGraph notebook, matching the simple-vs-complex routing idea; the README names the hackathon.  *(targeted: Second Place [2nd])*
**Sponsor tools:** ArangoDB (Persist street graphs and collections; AQL queries, core); NVIDIA cuGraph/RAPIDS (GPU-accelerated graph algorithms in GPU notebook, core)
**AI:** LangGraph ReAct agent calling LLM-backed tools (text-to-AQL, text-to-OSMnx code generation, geocoding); OpenAI listed in tags, prompts iteratively tuned.
**Architecture:** OSMnx fetches OSM data into NetworkX and ArangoDB; a LangGraph ReAct agent dispatches to tools; results rendered as text or Folium maps; cuGraph accelerates algorithms on GPU.
**Novelty:** Lets the LLM write executable OSMnx/NetworkX analysis code in addition to AQL; solo build with GPU and CPU notebook variants.
**Scope:** small · working: Notebook with fully answered sample queries and a YouTube demo; repo is only 11 files, mostly notebooks. · polish: README with setup, Docker command, citation; no UI beyond notebook.
**Claims:** Tools accurately interpret queries and pick correct geographic attributes
**Gaps:** No accuracy metrics; Video not watched
Sources: https://devpost.com/software/askstreets-querying-and-visualizing-street-networks, evidence/sponsor-building-the-next-gen-agentic-app-with-graphrag-nvidia-cugra-2025-askstreets-querying-and-visualizing-street-networks.json, sponsor_prompts_NVIDIA.jsonl

---

### Data Engineer's Buddy
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Honorable Mention

**What it is:** Agent for data engineering that stores table dependencies and refresh metadata in ArangoDB, then answers operations questions: upstream/downstream impact, refresh scheduling with propagated delays, and lineage, with generated visualizations including dependencies parsed from SQL code.
**Problem / user:** Data engineering teams at large organizations running data across many databases, where tracking lineage and refresh timing is costly.

**Features**
- Dependency and lineage tracking — Relationships between data structures kept as an ArangoDB graph; agent traverses upstream and downstream. *[shown_working]*
- Refresh scheduling with upstream delay — Metadata collections hold refresh details; agent computes delays propagated from upstream. *[shown_working]*
- Impact analysis — Agent assesses effect of a data-model change on dependents. *[claimed]*
- SQL dependency extraction — Dependencies derived from SQL code and visualized. *[shown_working]*
- Graph analytics — NetworkX and cuGraph for parsing and insight extraction. *[claimed]*

**Flow:** Ask the agent a data-operations question → Agent queries the ArangoDB graph and metadata → Receive analysis plus upstream, schedule or SQL-dependency visualization

**Prompt:** Build an agent that answers natural-language questions over graph data: load a dataset into NetworkX and ArangoDB, route simple queries to AQL and complex ones to cuGraph analytics, with hybrids earning extra credit; judged on innovation, functionality, technical excellence, usability and documentation.
**Fit (explicit):** Graph-backed agent on ArangoDB with NetworkX and cuGraph for enterprise lineage; page names both and the hackathon explicitly.  *(targeted: Honorable Mention)*
**Sponsor tools:** ArangoDB (Graph of data-structure dependencies and metadata collections, core); NVIDIA cuGraph (Graph analytics for insights, supporting)
**AI:** OpenAI-based agent built with LangChain and LangGraph reads graph and metadata through tools to answer lineage and scheduling questions with minimal prompting.
**Architecture:** Python LangGraph agent over ArangoDB (graph plus collections); NetworkX/cuGraph analytics; visualization outputs.
**Novelty:** Applies GraphRAG-style agent to data-pipeline operations rather than documents; computes upstream-propagated refresh delays.
**Scope:** small · working: YouTube demo and three screenshots; GitHub repo evidence shows a single file. · polish: Brief writeup; little documentation in the repo.
**Claims:** Agent identifies dependencies and implications with minimal prompting
**Gaps:** Repo has one file; Video not watched; Code not inspected
Sources: https://devpost.com/software/trial-kjzbys, evidence/sponsor-building-the-next-gen-agentic-app-with-graphrag-nvidia-cugra-2025-data-engineer-s-buddy.json, sponsor_prompts_NVIDIA.jsonl

---

### GDELT Open Intelligence Agent
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** First Place [1st]

**What it is:** Natural-language agent over the GDELT global-events knowledge graph in ArangoDB. A ReWOO plan-and-execute LLM agent picks among AQL, full-text, vector, geospatial and cuGraph analytics tools, asks for human confirmation before writes, and shows results in Streamlit with Plotly graphs.
**Problem / user:** Analysts and non-technical users who want to explore geopolitical event data without stitching separate tools together.

**Features**
- Dynamic tool selection — ReWOO planner chooses among AQL, FTS, vector, geospatial and cuGraph tools per query. *[claimed]*
- Multi-mode search — ArangoSearch full-text ranking, semantic vector search and geospatial lookup on event descriptions. *[claimed]*
- GPU graph analytics — cuGraph computes network centralities on large spatiotemporal graphs. *[claimed]*
- Human-in-the-loop writes — Updates and deletes need user confirmation. *[claimed]*
- Conversation memory — Stores prior queries and decisions across turns. *[claimed]*
- Plotly and Streamlit UI — Interactive graph of events, actors and locations. *[claimed]*

**Flow:** Type a question about global events → Agent plans tools → Executes plan, confirming any write → Streamlit shows answer and Plotly graph → Follow-up uses memory

**Prompt:** Build an agent that answers natural-language questions over graph data: load a dataset into NetworkX and ArangoDB, route simple queries to AQL and complex ones to cuGraph analytics, with hybrids earning extra credit; judged on innovation, functionality, technical excellence, usability and documentation.
**Fit (explicit):** Covers the hybrid brief: AQL for simple lookups, cuGraph for heavy analytics, with an agent routing between them; the writeup stresses CPU infeasibility above 100k nodes.  *(targeted: First Place [1st])*
**Sponsor tools:** ArangoDB (GDELT graph store with AQL, ArangoSearch, vector and geospatial indexes, core); NVIDIA cuGraph (GPU-accelerated centralities and graph analytics, core)
**AI:** LangChain/LangGraph ReWOO agent (OpenAI models) that plans all tool calls up front; tested ReAct and plan-and-execute first and rejected them for cost and traceability.
**Architecture:** Streamlit UI over a LangGraph ReWOO agent; tools hit ArangoDB (AQL, FTS, vector, geo) and cuGraph/NetworkX; memory store; Plotly rendering; main artifact is a notebook.
**Novelty:** Combines four search modes plus GPU analytics under one planner with explicit pattern comparison and human approval for destructive operations.
**Scope:** small · working: Demo video and a notebook submission; repo is 9 files and ~1.7k LOC; no live link. · polish: Streamlit UI and Plotly visuals; README is one line.
**Claims:** CPU is infeasible beyond 100k nodes and edges; cuGraph scales well
**Gaps:** No benchmarks; Video not watched; README minimal
Sources: https://devpost.com/software/gdelt-open-intelligence-agent, evidence/sponsor-building-the-next-gen-agentic-app-with-graphrag-nvidia-cugra-2025-gdelt-open-intelligence-agent.json, sponsor_prompts_NVIDIA.jsonl

---

### Neuthera - Drug discovery toolkit
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Third Place [3rd]

**What it is:** A modular starter toolkit that chains a generative molecule model, docking, binding-affinity prediction and embedding similarity search, backed by an ArangoDB biomedical knowledge graph and a GraphRAG layer. Ships as a notebook plus Streamlit app.
**Problem / user:** Researchers facing slow, costly drug discovery where generative and in-silico models run in isolation; wants one extensible pipeline for new molecules and drug repurposing.

**Features**
- De novo molecule generation for a target protein — TamGen transformer proposes compounds, which are docked on the protein before being returned; screenshot shows generations for one PDB target. *[shown_working]*
- Binding-affinity prediction — DeepPurpose scores drug-target binding for generated compounds without lab work. *[claimed]*
- Biomedical knowledge graph in ArangoDB — 15+ datasets (BioSNAP, DrugBank, ChEMBL, PDB) mapped into genes, proteins, diseases, drugs and structures. *[claimed]*
- Vector similarity search over drugs — chemBERTa embeddings and Morgan fingerprints with Tanimoto similarity, optional ArangoDB vector index, FAISS. *[claimed]*
- GraphRAG reasoning with GPT-4o — LangChain agent retrieves from the graph to answer biomedical questions; authors say it works about three quarters of the time. *[claimed]*
- Interactive Streamlit app — Run start notebook for preprocessing, then launch app.py. *[claimed]*
- Feedback loop, diffusion, GNN repurposing, richer UI — Listed as future roadmap. *[planned]*

**Flow:** Start ArangoDB via docker compose → Create conda env and install requirements, add Gemini key to .env → Run start.ipynb to preprocess and load data → Launch the Streamlit app → Choose a target protein and generate/score candidate compounds → Query the knowledge graph or chat via GraphRAG

**Prompt:** Build an agent answering natural-language questions over graph data using NetworkX and ArangoDB, routing simple queries to AQL and complex analytics to cuGraph, with hybrids earning extra credit.
**Fit (implied):** Uses ArangoDB as a drug/gene/disease graph with GraphRAG retrieval for an LLM agent; cuGraph is not used and nx-arangodb was dropped, so the analytics-routing part is absent.  *(targeted: Third Place)*
**Sponsor tools:** ArangoDB (graph store of biomedical entities plus experimental vector index, core); GraphRAG (graph-augmented retrieval for LLM answers, supporting); NVIDIA cuGraph (not used, token)
**AI:** Pretrained TamGen for molecule generation, chemBERTa for embeddings, DeepPurpose for affinity, GPT-4o via LangChain for GraphRAG question answering; no fine-tuning.
**Architecture:** Dockerized ArangoDB holds the merged knowledge graph and vectors; Python modules wrap TamGen, DockBox docking, DeepPurpose and chemBERTa; a LangChain GraphRAG agent and Streamlit front end sit on top, driven by a setup notebook.
**Novelty:** Stitches several research models plus a 15-dataset graph into one pipeline; rewrote TamGen to run without CUDA. Unusually large vendored code base for a hackathon.
**Scope:** large · working: Repo with vendored TamGen, Streamlit app, setup notebook and Docker file; generation screenshot; no demo video or benchmarks. · polish: Detailed README and roadmap, but install is admittedly fragile and no live demo.
**Claims:** Combines 15+ biomedical datasets into one graph | GraphRAG works roughly 75% of the time | Can generate millions of compounds with virtual ADMET profiling
**Gaps:** no video or demo; no benchmark results
Sources: https://devpost.com/software/neuthera-drug-discovery-platform, https://github.com/Redomic/NeuThera-Drug-Discovery-Toolkit, https://arangodbhackathon.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### Scopium
*Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB) 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Public Choice

**What it is:** A multi-chat web app where a developer searches GitHub for any public repo, connects it, and chats with it. The code is chunked into a graph of functions, classes and files in ArangoDB/NetworkX and queried through Mistral.
**Problem / user:** Developers trying to understand large codebases or unfamiliar open-source libraries and trace bugs or dependencies.

**Features**
- GitHub repo search and connect — Built-in access lets the user pick any public repository to load. *[claimed]*
- Code-to-graph conversion — Codebase is chunked into nodes with relationship edges, built dynamically per repo; a notebook walks through the process. *[claimed]*
- Per-repo chat sessions — Each repository gets its own chat; histories cached locally and survive reload. *[claimed]*
- GraphRAG codebase Q&A — Mistral answers using graph retrieval for dependencies, error tracing and navigation. *[claimed]*

**Flow:** Search for a public GitHub repo → Connect it so the graph is built → Open a dedicated chat for that repo → Ask questions about the code → Return later to cached chat history

**Prompt:** Build an agent answering natural-language questions over graph data using NetworkX and ArangoDB, routing simple queries to AQL and complex analytics to cuGraph; hybrids earn extra credit.
**Fit (implied):** Uses ArangoDB plus NetworkX for a code graph and LLM chat over it; no cuGraph or query routing is described. Prize was audience-voted.  *(targeted: Public Choice)*
**Sponsor tools:** ArangoDB (storing code graph nodes and edges, core); NetworkX (graph modelling, supporting); NVIDIA cuGraph (not mentioned; README only recommends CUDA machine, token)
**AI:** Mistral AI via LangChain answers questions over graph-retrieved code chunks; CUDA recommended for embedding or model work.
**Architecture:** React/Tailwind/shadcn front end talks to a Flask server that fetches GitHub repos, builds the ArangoDB/NetworkX graph and runs the Mistral GraphRAG chain.
**Novelty:** Treats an arbitrary repo as a graph on the fly and wraps it in a per-repo multi-chat UI instead of a single fixed dataset.
**Scope:** small · working: About 4k lines across Frontend and Backend plus an explanatory notebook; no demo video or live link. · polish: Modern UI stack and run instructions; 87 Devpost likes; no tests.
**Claims:** Handles any public GitHub repository | Chat history persists across reloads
**Gaps:** no video or live demo
Sources: https://devpost.com/software/scopium-lna7ro, https://github.com/AdityaS8804/scopium (evidence README), https://arangodbhackathon.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

