# Junction — Junction 2025 (1 projects)

### WAVELET
*Junction Junction 2025 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Main prize (exact prize name not stated by source)

**What it is:** Real-time GPU simulation of radio-frequency electromagnetic waves, solving Maxwell's equations on a grid in pure C++ and OpenGL compute shaders. Demonstrated on a Hong Kong city model with adjustable transmitters showing interference, absorption and dead zones.
**Problem / user:** Visualizing how radio signals propagate through an urban model for the Sensofusion/Radiocity challenge; users are network planners or anyone studying signal coverage.

**Features**
- Maxwell-equation wave simulation — time-stepped EM field solved on a grid in compute shaders, giving wave-forms through any loaded model *[shown_working]*
- Hong Kong map scenario — radio waves propagate, interfere and get absorbed by city geometry *[shown_working]*
- Hot-spot and dead-zone display — shows where signal concentrates or barely arrives *[shown_working]*
- Adjustable transmitter nodes — per-node frequency and placement editable at runtime *[shown_working]*
- ImGui control overlay — wave color, simulation speed, intensity and detail adjustable *[shown_working]*
- Dynamic adaptive grid — grid refines when transmitters are added to limit performance cost *[claimed]*
- Culling and parallel optimizations — GPU culling and parallelism for performance *[claimed]*
- Side prototypes — shooting stars in 3D cubes, heat-map slices *[claimed]*

**Flow:** Launch the C++/OpenGL app with the city model → Place or edit transmitter nodes and frequencies → Watch waves propagate in real time → Tune speed, intensity, detail and colors in the ImGui overlay

**Prompt:** not public / not found
**Fit (explicit):** README says it won the Sensofusion track for Radiocity and the whole hackathon; it visualizes radio propagation over a Hong Kong map, matching the challenge's apparent domain. Official track text not found.  *(targeted: Sensofusion track for Radiocity, Junction 2025 main prize)*
**AI:** none
**Architecture:** Single C++ OpenGL application with GLSL compute shaders for the field solver, ImGui UI overlay, adaptive grid, model loader; vendored external dependencies.
**Novelty:** First-principles physics solver rather than a ray-tracing approximation, with no engine or framework dependencies; large GPU-programming focus.
**Scope:** large · working: README embeds a demo video and live-simulation screenshots; about 63k estimated lines including vendored libraries. · polish: Interactive UI controls and multiple prototypes; no tests or docs.
**Claims:** Won the Sensofusion/Radiocity track and the entire hackathon (per README) | Dynamic grid keeps performance impact minimal
**Gaps:** no Devpost page; track prompt text not found; no build instructions
Sources: evidence/junction-junction-2025-wavelet.json (README)

---

