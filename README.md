# Daily Reflection Tree

A deterministic end-of-day reflection system implemented as a structured decision tree.

This project encodes psychological reflection into a **fully deterministic, auditable flow** — not a chatbot.

---

## 🔑 Key Idea

The system guides users through three sequential axes:

1. **Locus of Control** (Victim ↔ Victor)  
2. **Contribution vs Entitlement**  
3. **Radius of Concern** (Self ↔ Others)

Each interaction:
- Uses fixed options (no free text)
- Follows deterministic branching
- Produces consistent outcomes for identical inputs

---

## 📂 Repository Structure


/tree/
reflection-tree.tsv # Core decision tree (primary deliverable)
tree-diagram.md # Visual flow of the tree

/agent/
run.py # CLI-based deterministic agent

/transcripts/ # (Optional) Sample runs
write-up.md # Design rationale
README.md


---

## 🌳 How the Tree Works

Each node contains:

- `id` → Unique identifier  
- `type` → start | question | decision | reflection | bridge | summary | end  
- `text` → What the user sees  
- `options` → Fixed choices (for question nodes)  
- `target` → Next node (for routing)  
- `signal` → Updates psychological state  

The system tracks signals across axes:

- axis1 → internal / external  
- axis2 → contribution / entitlement  
- axis3 → self / team / wide  

Final output is based on **dominant signals**, not AI inference.

---

## ▶️ Running the Agent (Part B)

A simple CLI agent is included to execute the tree.

### Steps

```bash
cd agent
python run.py
