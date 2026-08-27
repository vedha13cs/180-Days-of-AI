# ✦ DAY 12 — TRAIN / TEST SPLIT ✦

<div align="center">

## 🧪 Can My Model Predict Unseen Data?

**180 DAYS OF AI • DAY 12 / 180**

*Training a model is only half the job. Testing it is where we learn how well it generalizes.*

</div>

---

## 🌱 Today's Focus

On Day 11, I learned **Linear Regression**.

Today, I learned how to divide a dataset into:

- 🧠 Training Data
- 🧪 Testing Data

This helps us evaluate how well a Machine Learning model performs on data it has **not seen during training**.

---

## 🧠 Train vs Test

A dataset can be divided like this:

```text
                DATASET
                   │
          ┌────────┴────────┐
          ↓                 ↓
    🧠 TRAINING          🧪 TESTING
       DATA                 DATA
          │                 │
          ↓                 ↓
     Learn Patterns     Evaluate Model
