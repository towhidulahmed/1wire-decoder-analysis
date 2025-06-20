# Forwarding-Attack on a Mechatronic Locking System

This repository contains the tools, scripts, and data used to analyze and decode communication from a mechatronic locking system based on the 1-Wire protocol. The work supports a Master's pre-thesis at the University of Rostock titled:

**"Forwarding-Attack on a Mechatronic Locking System"**  
Faculty of Computer Science and Electrical Engineering  
Work of: *Md Towhidul Ahmed* 
---

## Objectives

- Demonstrate the feasibility of forwarding attacks on a 1-Wire-based locking system.
- Analyze communication between the key and the lock to identify security flaws.
- Evaluate existing protective mechanisms.
- Provide risk assessments and suggest cryptographic countermeasures.

---

## What is a Forwarding Attack?

> A forwarding attack occurs when an adversary intercepts and relays (or alters) communication between two devices without their knowledge, typically exploiting weak communication protocols.

---

## Test Environment

- **Lock System**: ASSA ABLOY VERSO® CLIQ (Konrad Zuse Haus, Universität Rostock)
- **Key**: Embedded display, contact pins, system ID (`V1004261`)
- **Protocol**: 1-Wire (Master: Key, Slave: Lock)

---

## Tools Used

- PicoScope (Signal voltage testing)
- Logic Analyzer (Communication capture and decoding)
- Raspberry Pi (GPIO testing with 1-Wire module)
- Breadboard, jumper wires

---

## Communication Analysis Highlights

- **Signal decoding**: Binary decoding via pulse width (Write 1 ≈ 4.33µs, Write 0 ≈ 13.67µs)
- **System ID Exposed**: ASCII `V1004261` observed in plaintext
- **Key ID, Lock ID Detection**: Unique bytes in P1, P2, and P3 sequences
- **Sequence Similarity**: ~70–75% similarity even across time/key/lock changes
- **Dynamic Elements**: Sequences like `E0` and parts of `P5/P6` show high entropy (likely encryption or time-based tokens)
- **Static Elements**: Sequences `A0–A3`, `P4`, and `Q1–Q9` were constant



