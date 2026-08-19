# Standard Operating Procedures & Annotation Guidelines

## 1. Project Scope
This document outlines the labeling specifications and quality rules applied across Natural Language Processing (NLP), Computer Vision, Audio, and Video tasks in Label Studio.

## 2. Modality Rules & Taxonomy

### A. Named Entity Recognition (NER)
* `Person`: Label full names of individuals (e.g., *Daniel Okafor*, *Sarah Johnson*). Do not include job titles or honorifics.
* `Organization`: Label business and corporate entities (e.g., *NovaTech Solutions*).
* `Time`: Label explicit time references (e.g., *10:30 AM*).
* **Rule:** Do not highlight trailing punctuation or whitespace.

### B. Computer Vision (Semantic & Instance Segmentation)
* `Car`: Polygon mask covering vehicle frames.
* `Person`: Precise polygon outlines for pedestrians and riders.
* `Bike`: Outline motorized and manual two-wheelers distinctly from riders.
* `Road` / `Sky` / `Bushes` / `Sign Post`: Polygon region segmentation for full environmental scenes.
* **Occlusion Rule:** If an object is more than 40% hidden by vegetation or other obstacles, label only visible pixel regions.

### C. Audio & Video Annotation
* **Audio Segmentation:** Mark exact frame boundaries where speech begins and ends; transcribe verbatim.
* **Video Tracking:** Maintain consistent Object IDs across sequential video frames for moving targets.

## 3. Quality Assurance
* Target agreement threshold: **>95%**.
* Borderline or ambiguous cases flagged with low confidence scores for secondary audit.
*
