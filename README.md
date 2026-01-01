# HumanExo_MoCap_AnyBody

**Author:** Jeevan Jayasuriya  

---

## Overview

This repository contains an **AnyBody Modeling System** project for simulating a
**human–exoskeleton system** driven by **motion capture (BVH) data** with a
**Python-in-the-loop assistive torque controller**.

The model integrates a MoCap-driven human scaffold with an exoskeleton concept,
where **assistive joint torque is computed externally in Python** and applied
at each simulation step during inverse dynamics.

The focus of this work is on **assistive control and human–exoskeleton interaction**,
not on a specific task (e.g., box lifting). The underlying MoCap scaffold is reused
purely as a modeling framework.

---

## Repository Structure

```
HumanExo_MoCap_AnyBody/
├── ExoConcept_HumanMoCap.main.any   # Main AnyBody entry point
├── Changes.any                     # Assistive torque logic and Python hooks
├── Input/                          # Nodes, connections, interactions, force definitions
├── CAD/                            # Exoskeleton geometry and assembly (.any)
├── BVH-files/                      # Motion capture data (BVH)
│   ├── S01_T01.bvh
│   ├── S01_T02.bvh
│   └── ...
├── write_value.py                  # Python helper for exporting values
├── assistive_torque.py             # Python assistive torque controller
└── README_exo.md
```

---

## Key Files

### AnyBody
- **ExoConcept_HumanMoCap.main.any**  
  Main model file that loads the MoCap-driven human model, integrates the
  exoskeleton, and applies assistive torque.

- **Changes.any**  
  Defines the assistive control logic, including Python function calls and
  mapping of assistive torque to joints.

- **Input/**  
  Human–exoskeleton attachment definitions, interactions, and force elements.

- **CAD/**  
  Exoskeleton kinematic and geometric definitions.

### Python
- **write_value.py**  
  Called from AnyBody to write scalar simulation values (e.g., force signals)
  to text files at each simulation step.

- **assistive_torque.py**  
  Computes assistive torque based on the simulation step and sensor-like values,
  and returns the torque to AnyBody.

### Motion Capture
- **BVH-files/**  
  Contains BVH motion capture files used to prescribe human kinematics. These
  files can be replaced with user-specific MoCap data following the same format.

---

## Control and Data Flow

At each simulation step:

1. BVH files prescribe full-body human motion.
2. AnyBody performs inverse dynamics.
3. Selected internal forces are written to files via `write_value.py`.
4. `assistive_torque.py` reads these values and computes an assistive torque.
5. The returned torque is applied to the exoskeleton joint.

This forms a **Python-in-the-loop assistive control architecture**.

---

## Requirements

- AnyBody Modeling System
- AnyBody Managed Model Repository (AMMR)
- Python compatible with AnyBody Python hooks
- File I/O permissions enabled for Python–AnyBody communication

---

## Running the Model

1. Open **AnyBody Modeling System**.
2. Load `ExoConcept_HumanMoCap.main.any`.
3. Ensure valid BVH files are present in `BVH-files/`.
4. Run the **InverseDynamicStudy**.

---

## Notes

- The MoCap scaffold is reused solely as a modeling framework.
- Assistive torque is computed externally in Python and applied dynamically.
- File-based communication is used for clarity and prototyping.

---

## License

Released under the **MIT License**.
