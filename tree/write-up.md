# Write-up: Daily Reflection Tree Assignment

## Problem Understanding

The assignment required building a deterministic Daily Reflection Tool for employees.

This is not a chatbot and not an LLM-based system.

The goal is to create a structured reflection framework where:

- users answer fixed-choice questions
- every answer leads to predefined branches
- same input always gives same output
- no runtime AI generation happens

This makes the system predictable, safe, and psychologically consistent.

The tool is designed to encourage reflection, not advice.

---

## Psychological Framework Used

The tree is based on 3 required psychological axes:

### 1. Victim vs Victor (Locus of Control)

This measures whether a person responds to challenges with ownership or external blame.

People with an internal locus of control focus on actions they can improve.

People with an external locus of control focus more on circumstances and other people.

This axis helps identify responsibility mindset.

---

### 2. Contribution vs Entitlement

This checks whether the user focuses more on contribution or expectations.

Contribution mindset asks:

“What did I give today?”

Entitlement mindset asks:

“What should I have received?”

This helps evaluate maturity in work relationships.

---

### 3. Self-Centric vs Others-Centric

This measures awareness of others during stress and challenge.

It helps identify whether a person thinks only about personal discomfort or also considers team, customer, and collective outcomes.

This is important for leadership and emotional maturity.

---

## Design Decisions

I chose fixed-option multiple-choice questions instead of open text because:

- deterministic systems require predictable branching
- fixed options reduce ambiguity
- easier to audit and explain
- no hallucination risk
- no dependency on external AI systems

Reflection nodes were added after each axis instead of only at the end.

This improves user engagement and creates immediate psychological feedback.

Bridge nodes were added to make the experience feel natural and progressive instead of abrupt.

A final summary node gives closure to the session.

---

## Why JSON Format

JSON was chosen because:

- easy to read
- easy to maintain
- easy to connect with Python
- scalable for future expansion
- supports clear node-based architecture

This also makes Part B implementation simpler.

---

## Part B Implementation

The Python CLI agent loads the JSON tree and runs the reflection session.

It:

- starts from the START node
- displays questions
- accepts user choice
- moves to the next node
- shows reflection messages
- reaches summary and end node

No LLM calls are used.

Only deterministic branching logic is used.

This follows the assignment rules strictly.

---

## How AI Was Used Carefully

AI was used only as a support tool for:

- refining question wording
- improving structure clarity
- checking JSON formatting
- improving documentation quality

AI was not used to replace thinking.

I manually verified:

- psychological alignment
- deterministic branching
- assignment compliance
- removal of non-deterministic behavior

This prevented hallucination and ensured correctness.

I also rejected suggestions that introduced open-ended responses because they violated assignment rules.

This helped maintain guardrails against AI misuse.

---

## Future Improvements

If given more time, I would improve:

- deeper branching with 25+ advanced nodes
- scoring system across all three axes
- downloadable daily reflection reports
- dashboard for weekly pattern tracking
- manager-level anonymized team reflection insights

This would make the system more useful for long-term workplace culture improvement.

---

## Final Thought

The purpose of this system is not to judge employees.

It is to create awareness.

Reflection improves behavior only when people can clearly see their own patterns.

This tool helps create that awareness using structure, consistency, and psychological design.
