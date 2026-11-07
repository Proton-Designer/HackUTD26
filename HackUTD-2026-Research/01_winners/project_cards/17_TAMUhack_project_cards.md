# TAMUhack: project cards (33 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## TAMUhack 2025

### Aviateur  (TAMUhack 2025)

- **Prizes:** Second Place for American Airlines Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** iOS 3D-scanning app lets airline ground crews capture aircraft defects and upload them to a web platform where remote engineers pre-diagnose problems.
- **Problem / user:** Aircraft maintenance issues cause long delays when engineers must travel on site without knowing the fault. / airline ground crews and maintenance engineers
- **Domain / idea type:** mobility_transport + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** mobile_ios; web / False / False
- **Stack:** langs Swift; JavaScript; frontend Next.js; backend Express.js; db ; hosting 
- **Tech/APIs:** RealityKit / Swift (framework, core); Express.js (framework, core); Next.js (framework, core); American Airlines flight data APIs (data_source, supporting, sponsor)
- **Sponsor APIs:** American Airlines flight data APIs | fit: Server pulls American Airlines flight data and maintains fleet history for engineers reviewing scans.
- **Repo:** public, commits 74 (before/in/after event: 0/74/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 12, writeup medium, impact claims False
- **Notes:** Swift/RealityKit 3D scans from iPhone served via Express to a Next.js viewer rendering 3D models; team had no prior Swift experience.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/aviateur) | [GitHub](https://github.com/lryanle/aviateur)

### Coinvo  (TAMUhack 2025)

- **Prizes:** Second Place for PIMCO Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** Finance web app combining a real-time stock ticker, watchlist and an OpenAI-powered assistant that answers market questions.
- **Problem / user:** Many financial tools overwhelm people; they want clear, actionable insight and context on market data. / casual investors
- **Domain / idea type:** fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; Streamlit; backend Flask; Python; db ; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); Flask (framework, core); Stock data APIs (data_source, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Team states it is the first fully functional website each member built; watchlist persistence described as local storage or database.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; stock data API names not given; streamlit vs flask usage
- **Links:** [Devpost](https://devpost.com/software/coinvo)

### DJ Bestie  (TAMUhack 2025)

- **Prizes:** Third Overall Software Hack [3rd]  (tier: overall_top3)
- **Pitch:** Animated AI DJ companion that chats hands-free, reads the listener's facial expressions and body language, and curates Spotify playlists to match mood.
- **Problem / user:** People want music discovery that responds to mood and feels like a friend rather than a static playlist. / music listeners
- **Domain / idea type:** entertainment_games + creative_media / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat; vision; rag_or_search; recommendation; speech_or_voice
- **Stack:** langs JavaScript; Python; TypeScript; frontend Next.js; React; Unity WebGL; Tailwind CSS; backend Python; WebSockets; db MongoDB; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); DeepFace (ai_model, core); PyTorch (framework, supporting); TensorFlow/Keras (framework, supporting); Spotify API (data_source, core); Unity (framework, core); MongoDB (database, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 46 (before/in/after event: 0/45/1), README thin
- **Demo/writeup:** video True, live none, screenshots 2, writeup medium, impact claims False
- **Notes:** Combines real-time computer-vision emotion detection (DeepFace/Keras) with a RAG backend over Spotify data and a Unity WebGL animated character embedded in React.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; speech_or_voice (hands-free talk stated; tech not named)
- **Links:** [Devpost](https://devpost.com/software/dj-bestie) | [GitHub](https://github.com/suryajasper/AI-DJ)

### DreamDrive  (TAMUhack 2025)

- **Prizes:** Second Place for Toyota Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** Two-minute questionnaire that matches shoppers to a Toyota model based on budget, fuel economy, seating and tech preferences.
- **Problem / user:** Choosing among Toyota's wide lineup is overwhelming, especially for first-time buyers. / Toyota car shoppers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; SQL; frontend Next.js; backend Next.js; Drizzle; db PostgreSQL; hosting AWS
- **Tech/APIs:** Next.js (framework, core); PostgreSQL (database, core); Drizzle ORM (framework, supporting); AWS (cloud, supporting, sponsor)
- **Sponsor APIs:** AWS | fit: Recommends Toyota models from a custom questionnaire-matching algorithm; no Toyota API cited.
- **Repo:** public, commits 46 (before/in/after event: 0/45/1), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup medium, impact claims False (Says early testers reported high satisfaction; no numbers.)
- **Notes:** Next.js app with Drizzle ORM on PostgreSQL deployed to AWS; team compiled its own vehicle feature dataset by scraping and migrating to the database.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; AWS is_sponsor
- **Links:** [Devpost](https://devpost.com/software/dreamdrive) | [GitHub](https://github.com/jacksors/tamuhack-25)

### DrumRoller  (TAMUhack 2025)

- **Prizes:** Third Overall Hardware Hack [3rd]  (tier: overall_top3)
- **Pitch:** Portable servo-driven dice tower that rolls a chosen number of dice at the push of a button and returns them to a cup.
- **Problem / user:** Rolling many dice is tedious and physically hard for some tabletop gamers. / tabletop gamers, players with limited hand mobility
- **Domain / idea type:** entertainment_games + accessibility / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs C++; frontend ; backend Arduino (Atmega 2560); db ; hosting 
- **Tech/APIs:** Atmega 2560 / Arduino (hardware_part, core); Servo motors (hardware_part, core); IR line sensor (hardware_part, core); SOLIDWORKS / 3D printing (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 7 (before/in/after event: 0/7/0), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Rotating drum mechanism designed with mechanism synthesis; 3D-printed in SOLIDWORKS, Atmega 2560 control, three modes, and four sensor types tried before an IR line sensor worked.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/drumroller) | [GitHub](https://github.com/Brett797/DrumRoller-AutomaticDiceTower)

### EcoFy  (TAMUhack 2025)

- **Prizes:** First Place for Amazon Web Services Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Sustainability app with receipt-upload ESG tracking, resources to plan and learn, and cash-back style incentives meant to counter greenwashing.
- **Problem / user:** Companies overstate environmental efforts, and consumers lack easy ways to track and be rewarded for sustainable habits. / consumers and bank customers
- **Domain / idea type:** sustainability_climate + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; llm_chat
- **Stack:** langs JavaScript; frontend Next.js; React; backend ; db ; hosting AWS
- **Tech/APIs:** AWS Rekognition (cloud, core, sponsor); AWS S3 (cloud, supporting, sponsor); OpenAI API (ai_model, core); Open Food Facts API (data_source, supporting); Next.js (framework, core)
- **Sponsor APIs:** AWS Rekognition; AWS S3 | fit: Used AWS Rekognition and S3 for receipt image processing and storage in the ESG tracker; Bedrock access failed.
- **Repo:** public, commits 14 (before/in/after event: 0/14/0), README none
- **Demo/writeup:** video True, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Receipt photos are analysed with AWS Rekognition and stored in S3, with Open Food Facts data; team could not get AWS Bedrock access and used the OpenAI API instead.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; AWS is_sponsor
- **Links:** [Devpost](https://devpost.com/software/ecofy-5oalq2) | [GitHub](https://github.com/scs03/newTamuHacks)

### Ember  (TAMUhack 2025)

- **Prizes:** Second Place for Arm Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** Dashboard that educates on natural-disaster hazards and shows region-level data such as property damage and drought, motivated by the California fires.
- **Problem / user:** People affected or potentially affected by wildfires need accessible information about hazards and regional impacts. / residents of fire-prone regions
- **Domain / idea type:** sustainability_climate + safety_security / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; frontend React; Plotly; backend Flask; Python; db ; hosting 
- **Tech/APIs:** Google Gemini API (ai_model, supporting); Plotly (framework, core); Flask (framework, core); React (framework, core); Arm-based server (hardware_part, token, sponsor)
- **Sponsor APIs:** Arm | fit: REST API for graph data ran on an Arm-based laptop (local host).
- **Repo:** public, commits 54 (before/in/after event: 0/53/1), README thin
- **Demo/writeup:** video True, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Planned a click-to-select interactive map but shipped a simpler version; REST API was served from an Arm-based Mac and Gemini generated insights from the data.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; Arm is_sponsor
- **Links:** [Devpost](https://devpost.com/software/ember-guqk6r) | [GitHub](https://github.com/amasud7/laFire)

### FindAir  (TAMUhack 2025)

- **Prizes:** First Place for American Airlines Challenge [1st]; Best Use of Gen AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Lost-item system where cleaning crews photograph and voice-log items; an LLM writes descriptions and passengers get emailed with QR codes and shipping options.
- **Problem / user:** Airline lost-and-found lacks tracking and communication, so passengers rarely recover items left on planes. / airline cleaning crews and passengers
- **Domain / idea type:** mobility_transport + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice
- **Stack:** langs JavaScript; frontend Next.js; Tailwind CSS; backend Node.js; db ; hosting Vercel
- **Tech/APIs:** American Airlines API (data_source, core, sponsor); Groq LLaMA 3.3 (ai_model, core); Cloudinary (other, supporting); Vercel (cloud, supporting); Next.js (framework, core)
- **Sponsor APIs:** American Airlines API | fit: Employees verify flight numbers through the American Airlines API and the system maps seats to passenger contacts for notification.
- **Repo:** public, commits 127 (before/in/after event: 0/127/0), README solid
- **Demo/writeup:** video True, live none, screenshots 14, writeup long, impact claims True (Cites 30-40% item recovery rates at major airports like London Gatwick as the benchmark to beat.)
- **Notes:** Employee phone flow combines camera capture, voice seat entry with privacy toggle, Groq-hosted LLaMA 3.3 captions, Cloudinary storage and QR claim scanning; 15 gallery items including architecture diagram.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; speech_or_voice tech not named
- **Links:** [Devpost](https://devpost.com/software/afinda) | [GitHub](https://github.com/david-roh/tamuhack25)

### FinSim  (TAMUhack 2025)

- **Prizes:** First Place for PIMCO Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Stock-market simulator where users build a virtual portfolio and watch its value evolve with live and historical price data.
- **Problem / user:** Financial education is hard to make hands-on; learners want to see how investment choices and real events affect value. / students learning investing
- **Domain / idea type:** fintech_finance + education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs Python; JavaScript; HTML; frontend React; HTML; JavaScript; backend Flask; Python; db ; hosting 
- **Tech/APIs:** Flask (framework, core); React (framework, core); Web-scraped stock data (data_source, core)
- **Sponsor APIs:**  | fit: Educational portfolio simulator matching the finance sponsor's theme; no PIMCO data or API named.
- **Repo:** public, commits 2 (before/in/after event: 0/0/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Live simulation relies on scraped real-time stock data; planned extension lets users spend portfolio value on assets like cars and houses.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/finsim-d2j8be) | [GitHub](https://github.com/sahisagiraju/finsim)

### FireGrid.ai  (TAMUhack 2025)

- **Prizes:** First Place for Arm Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Arduino and Raspberry Pi sensor node tracking temperature, humidity and soil moisture with a Next.js dashboard, LLM Q&A and push alerts for wildfire risk.
- **Problem / user:** California wildfires cause major losses and insurers pull coverage; people lack local environmental data to anticipate fire risk. / homeowners and wildfire-prone communities
- **Domain / idea type:** sustainability_climate + safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat
- **Stack:** langs Python; JavaScript; frontend Next.js; React; backend Python; db MongoDB; hosting 
- **Tech/APIs:** Arduino (hardware_part, core); Raspberry Pi (hardware_part, core); MongoDB (database, core); OpenAI API (ai_model, supporting); Next.js (framework, core)
- **Sponsor APIs:**  | fit: Arm-based Raspberry Pi acts as the edge device collecting sensor data from an Arduino and uploading it to the cloud.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Sensor data goes Arduino to Raspberry Pi to MongoDB; dashboard graphs update live with an OpenAI chatbot over the metrics and phone push alerts over a temperature threshold; Cloudflare Workers plan dropped.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; Arm challenge fit inferred
- **Links:** [Devpost](https://devpost.com/software/firegrid-ai)

### flock  (TAMUhack 2025)

- **Prizes:** Second Overall Software Hack [2nd]  (tier: overall_top3)
- **Pitch:** Web app that, after a flight delay or cancellation, offers one-day itinerary planning, hotel vouchers redeemable with airline points, and car rentals.
- **Problem / user:** About 20% of US flights are delayed or cancelled and reimbursement or rebooking involves a lot of back and forth. / airline passengers with disrupted flights
- **Domain / idea type:** mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs TypeScript; frontend Next.js; Tailwind CSS; backend Next.js API routes; Prisma; NextAuth.js; db PostgreSQL; hosting AWS RDS
- **Tech/APIs:** American Airlines Flight Engine API (data_source, core, sponsor); OpenAI API (ai_model, supporting); Google Maps/Places API (maps_geo, supporting); AWS RDS (cloud, supporting, sponsor); PostgreSQL (database, core); Prisma (framework, supporting); NextAuth.js (auth, supporting); Next.js (framework, core)
- **Sponsor APIs:** American Airlines Flight Engine API; AWS RDS
- **Repo:** public, commits 127 (before/in/after event: 0/120/7), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup long, impact claims True (States roughly 20% of US flights are delayed or cancelled.)
- **Notes:** Uses American Airlines Flight Engine API for flight and rewards data; car rental listings were scraped from Turo because no free rate API existed; Google sign-in and AWS RDS Postgres.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; AWS is_sponsor
- **Links:** [Devpost](https://devpost.com/software/flock-ayxf75) | [GitHub](https://github.com/peterphann/tamuhack25)

### Garage  (TAMUhack 2025)

- **Prizes:** Third Place for Toyota Challenge [3rd]  (tier: sponsor_winner)
- **Pitch:** Toyota configurator that lets shoppers customize a 3D car on the web, send it to a Meta VR headset, walk around it and test drive.
- **Problem / user:** Online car configurators fail to convey the true feel of the vehicle before purchase. / car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / creative_tool
- **Platforms / hardware / AI:** web; hardware; other / True / False
- **Stack:** langs C#; TypeScript; frontend React; Three.js; Tailwind CSS; backend ; db ; hosting 
- **Tech/APIs:** Unity 6 / Meta XR SDK (framework, core); Blender (other, supporting); Three.js (framework, core); React (framework, supporting); Meta Quest headset (hardware_part, core); Toyota car database (data_source, supporting, sponsor)
- **Sponsor APIs:** Toyota car database | fit: Recreates Toyota's online shopping page with 3D and VR models and pulls model, cost and option data from the supplied Toyota database.
- **Repo:** public, commits 33 (before/in/after event: 0/33/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Unity VR app built from scratch with Meta XR SDK and C# for configurator and driving; React/Three.js web front end; only one headset for the team; uses the provided Toyota car database.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; headset model assumed Meta Quest from SDK name
- **Links:** [Devpost](https://devpost.com/software/garage-8vlb9e) | [GitHub](https://github.com/timothytsai1/Garage-hackathon-2025)

### Hi-5  (TAMUhack 2025)

- **Prizes:** First Overall Hardware Hack [1st]  (tier: overall_top3)
- **Pitch:** Voice-controlled assistive glove using servo-driven elastic strings to open and close fingers for people with limited hand mobility.
- **Problem / user:** Stroke, neurological conditions, arthritis or paralysis limit hand movement and make rehabilitation and daily tasks hard. / people with limited hand mobility, rehab patients
- **Domain / idea type:** health_wellness + accessibility / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / False
- **Stack:** langs Python; JavaScript; frontend React; backend Raspberry Pi 5; Arduino Uno; db Firebase Realtime Database; hosting 
- **Tech/APIs:** Arduino Uno (hardware_part, core); Raspberry Pi 5 (hardware_part, core); Servo motors and driver (hardware_part, core); Firebase Realtime Database (database, core); React (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup medium, impact claims False
- **Notes:** Elastic strings sewn into a glove pulled by servos via Arduino; commands flow from a React UI through Firebase Realtime Database to a Raspberry Pi 5, then serial to Arduino.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; ai_used (voice commands use an NLP library; judged not AI)
- **Links:** [Devpost](https://devpost.com/software/hi-5-lng2ha)

### Kaizen  (TAMUhack 2025)

- **Prizes:** First Place for Toyota Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Car-shopping helper that scrapes Toyota specs and reviews, ranks vehicles with user-weighted scores, and uses an LLM to summarize review sentiment.
- **Problem / user:** Modern cars have 100+ features to compare, making it hard to choose a Toyota that fits personal priorities. / car shoppers
- **Domain / idea type:** retail_consumer + mobility_transport / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; frontend Next.js; Tailwind CSS; Figma; backend Flask; LangChain; Selenium; BeautifulSoup; db PostgreSQL; hosting Docker
- **Tech/APIs:** OpenAI API (ai_model, core); LangChain (framework, core); Arize Phoenix (other, supporting); Guardrails (framework, supporting); PostgreSQL (database, core); Selenium/BeautifulSoup (data_source, core)
- **Sponsor APIs:**  | fit: Built a Toyota-vehicle comparison tool using scraped Toyota images and specs; the writeup frames the name after Toyota's kaizen philosophy.
- **Repo:** public, commits 196 (before/in/after event: 0/196/0), README thin
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims False
- **Notes:** Writeup details LLM observability: LangChain retrieval with Arize Phoenix tracing, custom hallucination and correctness evals, and Guardrails; data scraped with Selenium from three sites and stored in Postgres in Docker.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; Arize is_sponsor
- **Links:** [Devpost](https://devpost.com/software/kaizen-ri9yp2) | [GitHub](https://github.com/zanbowie138/TAMUHack25)

### NimbusNews: AI-Powered Weather Storytelling  (TAMUhack 2025)

- **Prizes:** Second Place for Amazon Web Services Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** Pipeline that turns weather charts into TV-style video reports using vision-LLM chart analysis, text summaries, synthetic narration and a lip-synced AI anchor.
- **Problem / user:** Meteorologists spend hours manually interpreting charts and turning them into public communication. / meteorologists and weather broadcasters
- **Domain / idea type:** sustainability_climate + creative_media / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; llm_chat; speech_or_voice; generative_media; agent_or_tool_use
- **Stack:** langs Python; frontend Streamlit; backend Flask; Python; db ; hosting AWS S3; Cloudflare
- **Tech/APIs:** AWS Bedrock (cloud, core, sponsor); AWS S3 (cloud, core, sponsor); Llama 3.2 Vision (ai_model, core); Llama 3.1 70B (ai_model, core); Deepgram Aura (ai_model, core); Wav2Lip (ai_model, core); Cloudflare Workers AI (cloud, core)
- **Sponsor APIs:** AWS Bedrock; AWS S3 | fit: Runs Llama models through AWS Bedrock (alongside Cloudflare) and stores generated video and audio outputs in S3 for the dashboard.
- **Repo:** public, commits 35 (before/in/after event: 0/35/0), README solid
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Claims 150x faster processing of NOAA 500 hPa charts than manual analysis and 'first-to-market' status.)
- **Notes:** Chains four AI systems (vision, summarisation, TTS, Wav2Lip); the team patched a deprecated Wav2Lip fork, ran it behind Flask, and switched between Cloudflare Workers AI and AWS Bedrock.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; AWS is_sponsor; impact claim self-reported
- **Links:** [Devpost](https://devpost.com/software/nimbusnews-ai-powered-weather-storytelling) | [GitHub](https://github.com/reddheeraj/WeatherMan ; https://github.com/Psylence0609/Wav2LipModern)

### Smart Plant Pot  (TAMUhack 2025)

- **Prizes:** Second Overall Hardware Hack [2nd]  (tier: overall_top3)
- **Pitch:** Purely analog circuit that senses soil moisture, lights an LED and runs a pump motor when the plant is dry, with no microcontroller or code.
- **Problem / user:** Small farmers and plant growers need simple automatic watering that is cheap and easy to build. / botanists, small-scale farmers
- **Domain / idea type:** sustainability_climate / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / False
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Op-amps and analog ICs (hardware_part, core); Transistors, resistors, capacitors (hardware_part, core); Gear/actuator motor (hardware_part, core)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Built only from op-amps, transistors, analog ICs and passives on a breadboard; a geared motor and soda-can parts stood in for a real water pump.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/smart-plant-pot-1ykih9)

### TalkTuahAirline  (TAMUhack 2025)

- **Prizes:** First Overall Software Hack [1st]; Third Place for American Airlines Challenge [3rd]  (tier: overall_top3)
- **Pitch:** Multilingual AI phone assistant for airline passengers that handles airport navigation, TSA questions, flight status and negotiates seat swaps by calling other passengers.
- **Problem / user:** Airports are stressful and tasks like seat swaps are awkward; travelers want a proactive assistant reachable without an app. / airline passengers
- **Domain / idea type:** mobility_transport + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs JavaScript; frontend React; Tailwind CSS; backend Node.js; db ; hosting 
- **Tech/APIs:** Retell AI (ai_model, core); OpenAI GPT (ai_model, core); Twilio (telecom, core); ElevenLabs (ai_model, core); React (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:**  | fit: Built around an American Airlines passenger scenario using the author's real flight data; the page does not show use of the sponsor's Flight Engine API.
- **Repo:** public, commits 14 (before/in/after event: 0/13/1), README solid
- **Demo/writeup:** video True, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** Voice agent built on Retell wrapping GPT, Twilio calls and ElevenLabs voices; the solo author used their own upcoming American Airlines flight as test data; TSA rules were mock APIs.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note depth
- **Links:** [Devpost](https://devpost.com/software/talktuahairline) | [GitHub](https://github.com/IbrahimKhanGH/TAMUhack3)

### Vision Learning  (TAMUhack 2025)

- **Prizes:** Third Place for Amazon Web Services Challenge [3rd]  (tier: sponsor_winner)
- **Pitch:** Interview-practice tool that scores confidence, knowledge and eye contact using facial analysis and gives personalized spoken feedback.
- **Problem / user:** Professional development resources are generic and lack personalized feedback for interview preparation. / job seekers and early-career professionals
- **Domain / idea type:** education + productivity_workplace / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; speech_or_voice; llm_chat
- **Stack:** langs Python; JavaScript; HTML; CSS; frontend HTML; CSS; JavaScript; backend Flask; Python; db ; hosting 
- **Tech/APIs:** AWS Rekognition (cloud, core, sponsor); AWS Polly (cloud, core, sponsor); OpenAI (ai_model, supporting); OpenCV (framework, supporting); Flask (framework, core)
- **Sponsor APIs:** AWS Rekognition; AWS Polly | fit: Used AWS Polly for voice synthesis and Rekognition for facial analysis of interview practice.
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README thin
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Combines AWS Rekognition and OpenCV for eye contact and expression analysis with Polly voice synthesis; plans Transcribe next.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; AWS is_sponsor; how OpenAI is used
- **Links:** [Devpost](https://devpost.com/software/vision-learning) | [GitHub](https://github.com/MuditUpadhyay04/TAMUHack)


## TAMUhack 2026

### AIsle0  (TAMUhack 2026)

- **Prizes:** First Place for American Airlines Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Flight-number-based coordination platform for airline ground and flight crews, with shared inspection checklists, live task status and AI hazard tagging.
- **Problem / user:** Crews working the same aircraft turnaround lack a shared flight-specific channel, causing miscoordination and delays. / airline ground and flight crews
- **Domain / idea type:** productivity_workplace + mobility_transport / automation_or_agent
- **Platforms / hardware / AI:** web; mobile_cross / False / llm_chat; vision
- **Stack:** langs TypeScript; JavaScript; frontend React; Vite; React Native; Expo; backend Supabase Edge Functions; Render; db Supabase PostgreSQL; hosting Render
- **Tech/APIs:** Supabase (database, core); OpenAI (ai_model, supporting); React Native / Expo (framework, core); React (framework, core); Vite (framework, supporting); American Airlines data (Workday shifts) (data_source, unclear, sponsor)
- **Sponsor APIs:**  | fit: Targets the American Airlines challenge with an airline crew coordination tool; screenshots mention shifts scraped from Workday via an AA API, not described in text.
- **Repo:** public, commits 30 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims False
- **Notes:** Web (React/Vite) and mobile (React Native/Expo) clients synced via Supabase realtime; screenshots show shifts scraped from Workday, a 3D plane model and an AI hazard audit log.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/idk-yet-8ba2hz) | [GitHub](https://github.com/sarvesh-tech/tamuhack26)

### Aria: The Multimodal AI Kiosk  (TAMUhack 2026)

- **Prizes:** Second Place for American Airlines Challenge [2nd]; [MLH] Best Use of Vultr [unknown]  (tier: sponsor_winner)
- **Pitch:** Voice-first airport kiosk with a 3D audio-reactive avatar, face or QR login, RAG answers, flight info, maps and rebooking.
- **Problem / user:** Touchscreen airport kiosks are unhygienic, awkward with luggage and impersonal. / airport passengers
- **Domain / idea type:** mobility_transport + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; speech_or_voice; vision
- **Stack:** langs Python; TypeScript; frontend React; Vite; Three.js; TanStack Router; TanStack Query; backend FastAPI; LangGraph; WebSockets; db MongoDB Atlas Vector Search; hosting Vultr
- **Tech/APIs:** Vultr Serverless Inference (cloud, core, sponsor); Kimi-K2-Instruct (ai_model, core); LangGraph (framework, core); ElevenLabs (ai_model, core); MongoDB Atlas Vector Search (database, core, sponsor); DeepFace (ai_model, core); Three.js (framework, supporting); Figma (other, token)
- **Sponsor APIs:** Vultr; MongoDB Atlas | fit: Uses Vultr Serverless Inference to run the Kimi-K2 model powering the agent.
- **Repo:** public, commits 120 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 17, writeup long, impact claims False
- **Notes:** LangGraph agent on Vultr serverless inference (Kimi-K2), ElevenLabs TTS with aligned text reveal, DeepFace login against MongoDB vector index, Three.js 20,000-particle FFT-driven sphere.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/aria-the-multimodal-ai-kiosk) | [GitHub](https://github.com/luvadlamudi/TAMUHack26)

### Autonomous Surgical Light  (TAMUhack 2026)

- **Prizes:** Second Overall Hardware Hack [2nd]  (tier: overall_top3)
- **Pitch:** Hands-free surgical spotlight that tracks the surgeon's head pose with computer vision and pans/tilts servos to illuminate where they look.
- **Problem / user:** Surgeons cannot touch light handles without breaking sterility, and headlamps are non-sterile; manual adjustments interrupt flow. / surgeons and operating room staff
- **Domain / idea type:** health_wellness / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / vision
- **Stack:** langs Python; JavaScript; C++; frontend React; backend Flask; Socket.IO; db ; hosting GitHub Pages
- **Tech/APIs:** MediaPipe Face Landmarker (ai_model, core); OpenCV (framework, core); Arduino Nano 33 BLE (hardware_part, core); MG995 servos (hardware_part, core); Web Serial / Web Bluetooth (framework, core); Flask (framework, supporting); React (framework, supporting); Socket.IO (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 8, writeup long, impact claims True (Cites surgeon eye-strain complaints (25-50%) and an adjustment every 7.5 minutes.)
- **Notes:** Pan/tilt rig with 3D-printed base, Arduino Nano 33 BLE plus Uno for the LED ring; browser bridges Python tracking to Arduino via Web Serial and Web Bluetooth; smoothing and deadband filters.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/autonomous-surgical-light)

### CarBaba  (TAMUhack 2026)

- **Prizes:** Second Place for Toyota Challenge [2nd]  (tier: sponsor_winner)
- **Pitch:** AI car search and recommender with user-weighted preferences, a voice-enabled chatbot, 3D car models and a two-car comparison mode.
- **Problem / user:** Existing car sites hide options behind marketing and force endless scrolling and asking others for opinions. / car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation; speech_or_voice
- **Stack:** langs JavaScript; Python; frontend React; Vite; backend FastAPI; db MongoDB Atlas; hosting Google Cloud VM; Vercel
- **Tech/APIs:** Gemini API (ai_model, core); ElevenLabs (ai_model, supporting); MongoDB Atlas (database, core); Google Cloud (cloud, supporting); FastAPI (framework, core)
- **Sponsor APIs:**  | fit: Car comparison and recommendation experience for the Toyota challenge; no Toyota API stated.
- **Repo:** public, commits 34 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup medium, impact claims False
- **Notes:** Users set weights on preferences; scraped car data and 3D models from external sites; Gemini chatbot with ElevenLabs speech in/out; backend on a GCP VM.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/carbaba) | [GitHub](https://github.com/exa2022/FINAL_HACK26)

### Celcii PixiPen  (TAMUhack 2026)

- **Prizes:** Third Overall Hardware Hack [3rd]  (tier: overall_top3)
- **Pitch:** A pen that lets users write in the air, built around an ESP32 and custom PCB.
- **Problem / user:** Page gives no problem statement; only a one-line tagline about writing in the air. / unknown
- **Domain / idea type:** creative_media / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / None
- **Stack:** langs C++; Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Custom PCB (hardware_part, core); Arduino IDE (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup short, impact claims False
- **Notes:** Almost no written description; page has a tagline, two images of the pen interior and a demo video. Built With lists ESP32, Arduino IDE, C++, PCB, Python.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; one_line_pitch; problem_statement; target_user; domain_primary; platforms; ai_used; event_start; event_end
- **Links:** [Devpost](https://devpost.com/software/pixipen)

### Cinder Control  (TAMUhack 2026)

- **Prizes:** Second Place for NorthMark Compute & Cloud Challenge [2nd]; Best Solo Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Dashboard predicting wildfire spread up to 96 hours with a cellular automata model, flagging affected infrastructure and routes, controllable by voice.
- **Problem / user:** People and responders often lack accessible, intuitive tools to understand how a wildfire will spread and what it will reach. / first responders and residents near wildfires
- **Domain / idea type:** safety_security + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; backend FastAPI; db ; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); ElevenLabs (ai_model, supporting); Mapbox (maps_geo, core); Overpass OpenStreetMap (data_source, core); NOAA NWS (data_source, supporting); Gemini (ai_model, token)
- **Sponsor APIs:**  | fit: Uses a parallelized simulation framed as HPC-ready; page does not name sponsor-provided compute.
- **Repo:** public, commits 18 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Solo build; parallelized Python cellular automata simulation; OpenAI parses voice/natural-language parameters and ElevenLabs narrates; Mapbox, Overpass and NOAA NWS data feed the map.
- **Team size:** 1 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/fsim) | [GitHub](https://github.com/Tarunls/fire-sim)

### Constellation  (TAMUhack 2026)

- **Prizes:** First Place for NorthMark Compute & Cloud Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** Web AI-native IDE for HPC that turns parallel workloads into a visual execution graph, with an agent that builds and debugs workflows and deploys to AWS Batch.
- **Problem / user:** Using HPC requires terminal skills and scheduler knowledge that block researchers without a CS background. / researchers new to HPC
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend Next.js; React; Monaco; reagraph; Zustand; backend NextAuth; db Firebase; hosting Railway; AWS
- **Tech/APIs:** AWS Batch (cloud, core, sponsor); AWS EC2 (cloud, core, sponsor); AWS S3 (cloud, supporting, sponsor); Gemini (ai_model, core); Firebase (database, supporting); Monaco Editor (framework, supporting); reagraph (framework, supporting)
- **Sponsor APIs:** AWS | fit: Deploys user workflows to real AWS Batch clusters for the compute and cloud challenge, with a local fallback for small files.
- **Repo:** public, commits 140 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup medium, impact claims False
- **Notes:** Real cluster deployment on AWS Batch/EC2 with dynamic scaling, plus local run mode; graph editor (reagraph) with Monaco code and CSV editing; contributor blurbs on page describe individual roles.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/constellation-qcb483) | [GitHub](https://github.com/aathul-raj/constellation)

### cortex  (TAMUhack 2026)

- **Prizes:** First Overall Software Hack [1st]  (tier: overall_top3)
- **Pitch:** Travel app combining iOS object and baggage tracking with computer vision, Solana on-chain bag records, and a fast ElevenLabs/Gemini airline voice agent.
- **Problem / user:** Travelers lose items in airports, wait at baggage claim, and find airline voice assistants slow and robotic. / airline travelers
- **Domain / idea type:** mobility_transport + ai_agents_infra / new_category
- **Platforms / hardware / AI:** mobile_ios; web / False / vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Swift; JavaScript; frontend Next.js; React; Three.js; backend Node.js; WebSockets; OpenCV; db MongoDB Atlas; hosting Vultr
- **Tech/APIs:** Gemini 2.0 Flash (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); Solana (other, core, sponsor); Auth0 (auth, supporting, sponsor); MongoDB Atlas (database, supporting, sponsor); Vultr GPU VMs (cloud, core, sponsor); ARKit/Vision/CoreML (framework, core); OpenCV (framework, core); Gaussian splatting (other, core)
- **Sponsor APIs:** Gemini; ElevenLabs; Solana; Auth0; MongoDB Atlas; Vultr
- **Repo:** public, commits 84 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup long, impact claims True (Claims airlines lose over $2 billion a year to lost luggage and fraudulent claims.)
- **Notes:** Four features: AirTag-free item tracking via ARKit/CoreML, bag detection with OpenCV, Solana-tracked bag fees and refunds, voice agent; 3D Gaussian splat terminal scans processed on Vultr GPU VMs.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; is_sponsor flags (MLH partners assumed); event dates
- **Links:** [Devpost](https://devpost.com/software/cortex-67ueyq) | [GitHub](https://github.com/ryunzz/cortex ; https://github.com/premiumfriedrice/CortexiOSApp)

### Haggle  (TAMUhack 2026)

- **Prizes:** Third Overall Software Hack [3rd]  (tier: overall_top3)
- **Pitch:** Negotiation trainer where a voice AI opponent adapts its tactics to the user's stress, read from iPhone-camera heart and breathing signals.
- **Problem / user:** Most people never negotiate salary, and those who do often crack under psychological pressure. / salary and deal negotiators, students
- **Domain / idea type:** education + fintech_finance / new_category
- **Platforms / hardware / AI:** web; mobile_ios / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs TypeScript; Swift; frontend Next.js; React; Tailwind CSS; Recharts; SwiftUI; backend Node.js; Socket.IO; db ; hosting Railway
- **Tech/APIs:** Google Gemini 2.5 Flash (ai_model, core, sponsor); ElevenLabs Conversational AI (ai_model, core, sponsor); Presage SmartSpectra SDK (other, core, sponsor); Socket.IO (framework, core); Railway (cloud, supporting)
- **Sponsor APIs:** Gemini; ElevenLabs; Presage SmartSpectra
- **Repo:** public, commits 26 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims True (Cites 78% of people never negotiating salary and a $5,000 raise compounding to $200,000+ lifetime.)
- **Notes:** Presage SmartSpectra SDK on a SwiftUI iOS app streams vitals via Socket.IO to Next.js; stress score injected into ElevenLabs/Gemini every 2 seconds; a reveal page logs exactly what context the AI received.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; is_sponsor flags (MLH partners assumed); event dates
- **Links:** [Devpost](https://devpost.com/software/haggle-admqhc) | [GitHub](https://github.com/rtalla1/tamuhack26)

### HPC Runner  (TAMUhack 2026)

- **Prizes:** Second Overall Software Hack [2nd]  (tier: overall_top3)
- **Pitch:** Web interface and MCP server for submitting jobs to a SLURM cluster, with Gemini detecting entry points and estimating resources from uploaded code.
- **Problem / user:** Researchers and students need large-scale computation but are blocked by schedulers, scripts and cluster complexity. / researchers, students, AI agents
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; other / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend React; Next.js; backend Flask; SLURM; MCP; db MongoDB; hosting 
- **Tech/APIs:** Gemini (ai_model, core, sponsor); SLURM (other, core); MCP server (framework, core); Auth0 (auth, supporting, sponsor); MongoDB (database, supporting, sponsor); Flask (framework, core)
- **Sponsor APIs:** Gemini; Auth0; MongoDB
- **Repo:** public, commits 46 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 3, writeup long, impact claims False
- **Notes:** Multi-stage LLM pipeline with schema validation and confidence scores feeds deterministic resource calculation; custom Python API built over SLURM; tested on MNIST, weather prediction and blackjack runs.
- **Team size:** 4 | **Confidence:** medium | unverified: ui_polish; is_sponsor flags (MLH partners assumed); event dates
- **Links:** [Devpost](https://devpost.com/software/slurmglue) | [GitHub](https://github.com/Shlok-Bhakta/HPC-Runner)

### MediBot  (TAMUhack 2026)

- **Prizes:** First Overall Hardware Hack [1st]  (tier: overall_top3)
- **Pitch:** Emergency first-aid robot: camera detects falls and classifies injuries, a robotic arm hands over the right supplies, and a voice agent talks the user through treatment.
- **Problem / user:** Panic during medical emergencies keeps bystanders from acting effectively before professionals arrive. / bystanders in medical emergencies
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware / True / vision; speech_or_voice; llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend LiveKit Agents; db ; hosting 
- **Tech/APIs:** OpenAI GPT-4 Vision (ai_model, core); Google Gemini (ai_model, core, sponsor); ElevenLabs (ai_model, core, sponsor); Deepgram (ai_model, supporting); Groq Llama 3.3 70B (ai_model, supporting); LiveKit Agents (framework, core); Raspberry Pi + CSI camera (hardware_part, core); Robotic arm (LeRobot) (hardware_part, core); Roboflow (other, supporting)
- **Sponsor APIs:** ElevenLabs; Gemini
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Raspberry Pi with CSI camera builds a voxel map for fall detection; vision models classify injuries; LeRobot-style arm retrieves supplies; LiveKit agent with Deepgram, ElevenLabs and Groq Llama 3.3 for voice.
- **Team size:** 2 | **Confidence:** medium | unverified: ui_polish; is_sponsor flags (MLH partners assumed); event dates; writeup truncated on page
- **Links:** [Devpost](https://devpost.com/software/medibot-as2980)

### PocketPlay  (TAMUhack 2026)

- **Prizes:** Third Place for NorthMark Compute & Cloud Challenge [3rd]; Best Beginner Hack (Software) [unknown]  (tier: sponsor_winner)
- **Pitch:** Football play simulator using an ML model to estimate success rates for offensive/defensive schemes, with coach and NFL modes, an AI agent and a 3D POV view.
- **Problem / user:** Football play analysis has natural variance suited to simulation, but detailed formation data is paywalled. / coaches, fans and analysts
- **Domain / idea type:** entertainment_games + other / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; agent_or_tool_use
- **Stack:** langs Python; TypeScript; frontend Next.js; React; backend ; db ; hosting 
- **Tech/APIs:** Auth0 (auth, supporting); Gemini / Google API (ai_model, supporting); nflfastR (data_source, core); Madden 26 dataset (data_source, core); Cursor (other, token)
- **Sponsor APIs:**  | fit: Framed as HPC-style simulation for the compute challenge; page does not name sponsor-provided compute.
- **Repo:** public, commits 15 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims False
- **Notes:** Trained on nflfastR data with Madden 26 player ratings for NFL mode; simulates thousands of matchups for win probability; Auth0 login; agent feedback via Google API; built with Cursor.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/pocketplay) | [GitHub](https://github.com/Rishbhu/tamuhack26)

### RideIQ  (TAMUhack 2026)

- **Prizes:** First Place for Toyota Challenge [1st]  (tier: sponsor_winner)
- **Pitch:** AI car marketplace using vector embeddings of listings and natural-language queries for semantic search and recommendations.
- **Problem / user:** Car shopping with rigid filters and keyword search is overwhelming and does not capture buyer intent. / car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / rag_or_search; recommendation
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; backend Supabase; db PostgreSQL; pgvector; hosting 
- **Tech/APIs:** Supabase (database, core); pgvector (database, core); Text embeddings (ai_model, core); Next.js (framework, supporting)
- **Sponsor APIs:**  | fit: Builds a car-buying experience for the Toyota challenge; no Toyota API or data use stated on the page.
- **Repo:** public, commits 7 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 5, writeup medium, impact claims False
- **Notes:** Short writeup; semantic search via pgvector in Supabase; screenshots show compare view and charts. A stray Zoom link is listed in Try it out (not a demo).
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/rideiq) | [GitHub](https://github.com/joshuaraja1/HackTamu2026)

### Stowed  (TAMUhack 2026)

- **Prizes:** Third Place for American Airlines Challenge [3rd]  (tier: sponsor_winner)
- **Pitch:** Web app that matches lost luggage by AI image similarity and predicts when a flight's overhead bins will fill based on logged carry-ons.
- **Problem / user:** Travelers face lost bags without tags and surprise gate-checks when overhead bins fill. / air travelers
- **Domain / idea type:** mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / vision; rag_or_search
- **Stack:** langs TypeScript; frontend Next.js; React; Tailwind CSS; backend Prisma; db ; hosting Vercel
- **Tech/APIs:** OpenAI API (ai_model, core); Aviation API (data_source, supporting); Prisma (framework, supporting); Next.js (framework, core); Antigravity (other, supporting); Canva (other, token)
- **Sponsor APIs:**  | fit: Addresses airline passenger baggage and boarding pain points for the American Airlines challenge; page does not name a sponsor API.
- **Repo:** public, commits 173 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Team of first-time hackers; visual luggage fingerprinting via OpenAI API plus an aviation API for flight tracking; Antigravity AI used to write backend logic.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/stowed) | [GitHub](https://github.com/joshuale2007/STOWED-TAMUHACK-2026)

### Treat Me To A Toyota  (TAMUhack 2026)

- **Prizes:** Third Place for Toyota Challenge [3rd]  (tier: sponsor_winner)
- **Pitch:** Voice AI car-shopping assistant that asks follow-up questions and updates a live image carousel of cars matching the stated preferences.
- **Problem / user:** Car shoppers should not have to type every preference or click through rigid filters. / car buyers
- **Domain / idea type:** retail_consumer + mobility_transport / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; frontend Next.js; Tailwind CSS; backend ; db PostgreSQL; Supabase; hosting Vercel
- **Tech/APIs:** Claude Opus 4.5 (ai_model, core); Vapi (ai_model, core); Groq (ai_model, supporting); Supabase (database, core); Cursor (other, token)
- **Sponsor APIs:**  | fit: Conversational car-finding experience for the Toyota challenge; no Toyota API use stated.
- **Repo:** public, commits 32 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup medium, impact claims False
- **Notes:** Claude Opus 4.5 with tool calls generating SQL against Postgres; Vapi voice agent loads car images into a carousel as preferences emerge; screenshots include a payment form.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/toyota-truefit) | [GitHub](https://github.com/Lukeyp43/TamuHack-2026-Dream-Team)
