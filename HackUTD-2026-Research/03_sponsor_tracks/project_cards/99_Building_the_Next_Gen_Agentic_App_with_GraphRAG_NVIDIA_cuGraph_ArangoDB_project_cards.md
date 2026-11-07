# Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB): project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2025

### AgentBIM  (2025)

- **Prizes:** Honorable Mention [unknown]  (tier: sponsor_winner)
- **Pitch:** Natural-language agent that answers questions about building (BIM) models by translating them to AQL over an ArangoDB graph built from parsed IFC files.
- **Problem / user:** Exploring BIM data needs repeated back-and-forth and expert tooling; users want to ask plain-English questions about building elements and relationships. / architects, engineers and construction teams working with BIM models
- **Domain / idea type:** other + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; frontend Gradio; backend LangChain; LangGraph; IfcOpenShell; NetworkX; db ArangoDB; hosting 
- **Tech/APIs:** ArangoDB (graph store for IFC building data) (database, core, sponsor); LangChain ArangoGraphQAChain (framework, core); LangGraph (framework, supporting); IfcOpenShell / IFC (framework, core); NetworkX (framework, supporting); Gradio (framework, supporting)
- **Sponsor APIs:** ArangoDB | fit: Stored parsed IFC building data as an ArangoDB graph and used LangChain's ArangoGraphQAChain for text-to-AQL querying, targeting the GraphRAG agentic-app challenge; no cuGraph or NVIDIA tooling is mentioned.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Solo build; IFC files parsed with IfcOpenShell into a NetworkX graph then stored in ArangoDB; uses LangChain ArangoGraphQAChain with a Gradio front end; single screenshot; no NVIDIA/cuGraph use stated in the writeup.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; demo_video_url (iframe not readable); domain_primary; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/agentbim) | [GitHub](https://github.com/tewodros18/arangodb-hack)

### AskStreets: Querying and Visualizing Street Networks  (2025)

- **Prizes:** Second Place [2nd]  (tier: sponsor_winner)
- **Pitch:** LangGraph ReAct agent that answers natural-language questions about city street networks using OSMnx data in ArangoDB, GPU-backed graph algorithms and Folium map output.
- **Problem / user:** Planners and business owners want street-network insights like service accessibility and routed distances without writing long graph algorithms. / city planners, architects and business owners
- **Domain / idea type:** mobility_transport + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** other / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; frontend Jupyter Notebook; Folium; backend LangChain; LangGraph; OSMnx; NetworkX; RAPIDS/cuGraph; db ArangoDB; hosting local Docker
- **Tech/APIs:** ArangoDB (street graphs and OSM features, AQL) (database, core, sponsor); NVIDIA GPU / RAPIDS (cuGraph) acceleration (framework, supporting, sponsor); LangGraph ReAct agent (framework, core); OpenAI (ai_model, core); OSMnx / OpenStreetMap (data_source, core); NetworkX (framework, supporting)
- **Sponsor APIs:** ArangoDB; NVIDIA CUDA/RAPIDS (cuGraph, GPU graph algorithms) | fit: Loaded OpenStreetMap street graphs into ArangoDB, queried them via a text-to-AQL tool and ran GPU-backed graph algorithms through RAPIDS in the GPU notebook, targeting the GraphRAG plus cuGraph agentic-app challenge.
- **Repo:** public, commits 25 (before/in/after event: 0/23/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Delivered as a Jupyter notebook, not an app UI; four tools (text-to-AQL, text-to-OSMnx code, geocoder, map visualizer); GPU notebook variant uses RAPIDS; health-facility data overlaid; joined hackathon late; 19 gallery images.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; platforms; domain_primary
- **Links:** [Devpost](https://devpost.com/software/askstreets-querying-and-visualizing-street-networks) | [GitHub](https://github.com/msradam/askstreets)

### Data Engineer's Buddy  (2025)

- **Prizes:** Honorable Mention [unknown]  (tier: sponsor_winner)
- **Pitch:** Agent that stores data-lineage and refresh metadata in ArangoDB and answers questions on upstream/downstream dependencies, refresh scheduling and change impact, with visualizations.
- **Problem / user:** Enterprise data spread over many databases makes cataloging, lineage tracking and data operations costly and slow for data engineering teams. / enterprise data engineers
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** other / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; frontend ; backend LangChain; LangGraph; NetworkX; db ArangoDB; hosting 
- **Tech/APIs:** ArangoDB (lineage graph and metadata collections) (database, core, sponsor); NetworkX (framework, core); cuGraph (mentioned as usable by agents) (framework, token, sponsor); LangGraph (framework, core); LangChain (framework, supporting); OpenAI API (ai_model, core)
- **Sponsor APIs:** ArangoDB; NVIDIA cuGraph (mentioned only) | fit: Modeled SQL object dependencies as an ArangoDB graph with metadata collections and had a LangGraph agent traverse it for lineage and scheduling, targeting the agentic GraphRAG challenge; cuGraph is only mentioned as a library option.
- **Repo:** public, commits 3 (before/in/after event: 0/3/0), README none
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Solo build; SQL object relationships kept as an Arango graph and refresh details as collections; agent computes refresh delays and impact analysis; writeup says NetworkX and cuGraph can be used by agents but names only NetworkX in built-with.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; platforms
- **Links:** [Devpost](https://devpost.com/software/trial-kjzbys) | [GitHub](https://github.com/HrishikeshP-01/DEBy-Project)

### GDELT Open Intelligence Agent  (2025)

- **Prizes:** First Place [1st]  (tier: sponsor_winner)
- **Pitch:** ReWOO-style agent that answers natural-language questions on GDELT global events via AQL, full-text and vector search, and cuGraph-accelerated graph analytics, shown in Streamlit.
- **Problem / user:** Analysts need to explore a huge geopolitical events dataset in real time without hand-writing database queries or slow CPU graph algorithms. / analysts studying geopolitical events
- **Domain / idea type:** ai_agents_infra + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs Python; frontend Streamlit; Plotly; backend LangChain; LangGraph; NetworkX; cuGraph; db ArangoDB; hosting 
- **Tech/APIs:** ArangoDB (AQL, ArangoSearch, geospatial, vector index) (database, core, sponsor); NVIDIA cuGraph (via nx-cugraph style GPU analytics) (framework, core, sponsor); LangGraph (ReWOO agent) (framework, core); OpenAI (ai_model, core); GDELT dataset (data_source, core); NetworkX (framework, supporting); Streamlit (framework, supporting)
- **Sponsor APIs:** ArangoDB; NVIDIA cuGraph | fit: Combined ArangoDB AQL, full-text, geospatial and vector search with cuGraph-accelerated spatiotemporal graph analytics inside one ReWOO agent over GDELT, directly targeting the GraphRAG plus cuGraph challenge.
- **Repo:** public, commits 19 (before/in/after event: 0/19/0), README thin
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Plan-and-execute ReWOO orchestration with human confirmation before updates or deletes, conversation memory, and ArangoSearch full-text, geospatial and vector search; Plotly graph view; notes cuGraph needed for graphs over 100k nodes; one screenshot.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; tech_items.cuGraph name (built-with lists cugraph only)
- **Links:** [Devpost](https://devpost.com/software/gdelt-open-intelligence-agent) | [GitHub](https://github.com/QasimKhan5x/GDELT-AQL-NetworkX-Agent)

### Neuthera - Drug discovery toolkit  (2025)

- **Prizes:** Third Place [3rd]  (tier: sponsor_winner)
- **Pitch:** Modular agentic drug-discovery toolkit combining generative molecule models, binding prediction and an ArangoDB biomedical knowledge graph with GraphRAG retrieval.
- **Problem / user:** Drug discovery is slow and costly, and generative, scoring and knowledge tools are not integrated into one end-to-end candidate pipeline. / drug discovery researchers
- **Domain / idea type:** health_wellness + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** other / False / llm_chat; agent_or_tool_use; rag_or_search; predictive_ml; generative_media
- **Stack:** langs Python; frontend ; backend TamGen; DeepPurpose; ChemBERTa; RDKit; FAISS; LangChain; PyTorch; db ArangoDB; hosting 
- **Tech/APIs:** ArangoDB (biomedical knowledge graph) (database, core, sponsor); GraphRAG (framework, core, sponsor); TamGen (ai_model, core); DeepPurpose (ai_model, core); ChemBERTa embeddings (ai_model, core); GPT-4o (ai_model, supporting); FAISS (framework, supporting); nx-arangodb (tried, discarded) (framework, token, sponsor)
- **Sponsor APIs:** ArangoDB; GraphRAG | fit: Built an ArangoDB knowledge graph of genes, proteins, diseases and drugs with a GraphRAG layer over it for the drug-discovery agent, targeting the GraphRAG challenge; cuGraph is not used and nx-arangodb was dropped.
- **Repo:** public, commits 48 (before/in/after event: 0/23/25), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Cites 20-year drug timelines, 20M+ and 120M+ SMILES training sets, 15+ datasets, millions of generated compounds and about 75 percent success.)
- **Notes:** Merges 15+ biomedical datasets (DrugBank, ChEMBL, BioSNAP, PDB) into a graph; TamGen rewritten to run without CUDA; nx-arangodb discarded as incompatible; GPT-4o use kept minimal; authors say it works about 75 percent of the time.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; platforms; domain_primary
- **Links:** [Devpost](https://devpost.com/software/neuthera-drug-discovery-platform) | [GitHub](https://github.com/Redomic/NeuThera-Drug-Discovery-Toolkit)

### Scopium  (2025)

- **Prizes:** Public Choice [unknown]  (tier: sponsor_winner)
- **Pitch:** Chatbot for talking to a codebase: source code is chunked into a graph of functions, classes and files in ArangoDB and queried conversationally.
- **Problem / user:** Understanding and debugging large unfamiliar codebases and open-source libraries is overwhelming for developers. / software developers
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; frontend React; backend Flask; LangChain; NetworkX; db ArangoDB; hosting 
- **Tech/APIs:** ArangoDB (code graph storage and retrieval) (database, core, sponsor); Mistral (ai_model, core); LangChain (framework, supporting); NetworkX (framework, supporting); Flask (framework, supporting); React (framework, supporting)
- **Sponsor APIs:** ArangoDB | fit: Stored a codebase as a graph in ArangoDB and retrieved from it for LLM chat, targeting the GraphRAG agentic-app challenge; no cuGraph or NVIDIA tooling is mentioned; prize was Public Choice.
- **Repo:** public, commits 4 (before/in/after event: 0/4/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Code components as graph nodes with dependency edges; Flask and React app with Mistral and LangChain; page is sparse on technical detail and shows one screenshot; awarded the Public Choice prize.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/scopium-lna7ro) | [GitHub](https://github.com/AdityaS8804/scopium)
