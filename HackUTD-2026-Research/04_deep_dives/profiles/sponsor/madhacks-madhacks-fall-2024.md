# MadHacks — MadHacks Fall 2024 (1 projects)

### TaskChain
*MadHacks MadHacks Fall 2024 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner [Capital One] How Will You Reimagine Banking?

**What it is:** A blockchain accountability task manager: users create tasks with deadlines and stake ETH, which is returned on time completion or sent to a chosen charity if the deadline passes. Solidity contracts are deployed on Base Sepolia; the React frontend was not fully wired to them at submission.
**Problem / user:** Students who lack motivation to finish assignments; turns procrastination into a financial incentive with a charity outcome.

**Features**
- Stake ETH on a personal task with a deadline — TaskManager contract stores task name, description, due date and escrowed ETH *[claimed]*
- Refund on completion, charity payout on miss — Completing before the due date returns the stake; a missed deadline forfeits it to a chosen charity *[claimed]*
- Per-user contract via factory — TaskManagerFactory contract creates a TaskManager for each new user and records addresses *[shown_working]*
- MetaMask wallet connection and task slides UI — React frontend connects wallet, adds tasks, keeps a task log in session storage *[shown_working]*
- Due-date detection backend — Node/Express API with MongoDB watches for passed deadlines *[claimed]*
- Canvas account linking — Import assignments from Canvas *[planned]*

**Flow:** Connect MetaMask wallet → Add a task with deadline and ETH stake → View tasks in the slide-style interface → Mark task complete before deadline to recover ETH → If deadline passes, stake goes to charity

**Prompt:** Capital One's MadHacks prize 'How Will You Reimagine Banking?': use creativity and technical skill to build a tool for any finance-related need.
**Fit (implied):** Treats money staking as a commitment device for productivity; finance angle is crypto escrow rather than banking APIs. Page does not state the link to the prompt.  *(targeted: Capital One: How Will You Reimagine Banking?)*
**AI:** none
**Architecture:** React frontend with MetaMask and thirdweb talks to Solidity TaskManager/TaskManagerFactory contracts on Base Sepolia; Node/Express backend with MongoDB handles wallet logic and deadline detection.
**Novelty:** Combines a commitment-device staking model with charity forfeiture on-chain; contracts built by a team new to large Solidity projects.
**Scope:** small · working: Contracts deployed on Base Sepolia with explorer links and a demo video; page admits frontend-to-contract integration was unfinished. · polish: Slide-style task UI shown in screenshots; no live site.
**Claims:** First time building large-scale smart contracts | Frontend integration not completed within the time limit
**Gaps:** repo clone failed in evidence extraction (repo named my-website); demo video on Drive not viewable
Sources: https://devpost.com/software/taskchain

---

