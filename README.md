# Prompt Evaluation Lab: Measuring LLM Quality, Cost, and Latency

A practical AI engineering project to evaluate prompting strategies, measure their performance, and determine which approach delivers the best trade-off between accuracy, latency, and cost.

## Overview

What happens when the cost of an LLM-powered feature triples, but nobody can prove whether the additional spending has improved its output quality?

This project investigates that problem by benchmarking multiple prompting strategies against a dataset of 120 tasks spanning arithmetic reasoning, classification, information extraction, and open-ended judgment.

The goal is to move beyond intuition when choosing a prompting strategy. Instead of assuming that more sophisticated prompting produces better results, this project measures the actual impact of each approach and identifies where its additional cost is justified.

The final outcome is a data-driven recommendation for selecting prompting strategies across different task categories, including a cost projection for **100,000 requests per month**.

## Business Problem

LLM-powered applications often use increasingly sophisticated prompting techniques to improve response quality. However, these techniques can introduce additional token consumption, latency, and inference costs.

Without systematic evaluation, it is difficult to answer questions such as:

- Does Chain-of-Thought prompting actually improve accuracy for the tasks that matter?
- Is Self-Consistency worth the extra cost of generating multiple responses?
- Does Tree-of-Thought reasoning provide enough improvement to justify its overhead?
- Which prompting strategy offers the best balance between quality, latency, and cost?
- What would each strategy cost at 100,000 requests per month?

This project builds an evaluation pipeline to answer these questions using measured results rather than assumptions.

## Project Objectives

- Establish a baseline for LLM performance using a consistent evaluation harness.
- Implement and compare multiple prompting strategies across four task families.
- Measure token consumption, estimated API cost, response accuracy, and latency.
- Validate structured LLM outputs using Pydantic.
- Evaluate deterministic tasks using exact-match grading and open-ended tasks using an LLM-as-judge.
- Analyze failure patterns to understand where each strategy succeeds or fails.
- Calculate cost per 100 tasks and the cost per additional correct answer.
- Identify the quality-cost trade-off and recommend a suitable strategy for each task family.
- Extrapolate measured costs to a production workload of 100,000 requests per month.

## Prompting Strategies

| Strategy | Description | Primary Evaluation Goal |
|---|---|---|
| Baseline | A straightforward prompt without additional reasoning techniques | Establish a reference for quality, latency, and cost |
| Chain-of-Thought (CoT) | Encourages the model to work through a task using a structured reasoning approach | Measure improvements on reasoning-intensive tasks |
| Self-Consistency | Generates multiple candidate responses and selects an answer through majority voting | Determine whether repeated sampling improves answer reliability |
| Tree-of-Thought (ToT) | Explores a shallow tree of candidate reasoning paths before selecting an answer | Measure whether exploring alternatives improves task performance |

Each strategy is evaluated against the same benchmark wherever applicable. Model versions, parameters, and other relevant settings should be kept consistent to support a fair comparison.

## Evaluation Methodology

### 1. Benchmark Dataset

Use a benchmark of 120 tasks covering four task families:

- **Arithmetic reasoning:** Problems requiring numerical reasoning and correct calculations.
- **Classification:** Assigning an input to the appropriate category.
- **Information extraction:** Extracting specific information from unstructured inputs.
- **Open-ended judgment:** Evaluating responses that require qualitative assessment.

Results are tracked by task family so that improvements on one type of task do not hide regressions on another.

### 2. Evaluation Harness

Build a reusable Python evaluation pipeline that runs the same benchmark across the different prompting strategies.

The harness captures relevant information for each execution, including:

- Task identifier and task family
- Prompting strategy and model configuration
- Model response and parsed output
- Input and output token counts
- Estimated API cost
- Execution latency
- Grading result and error details

This makes it possible to compare strategies consistently and investigate individual failures.

### 3. Structured Output Validation

Use **Pydantic** to define and validate expected response schemas.

Schema validation helps detect malformed responses, missing fields, invalid data types, and other output-formatting problems. Invalid responses are recorded as evaluation outcomes rather than silently accepted.

### 4. Automated Grading

Use two complementary evaluation methods:

**Exact-match grading**

For tasks with deterministic answers, compare the model output against the expected answer using a task-appropriate normalization and comparison procedure.

**LLM-as-judge**

For open-ended tasks, use a separate evaluation prompt to assess responses against explicit grading criteria. Validate the judge's output, record its reasoning or evidence where appropriate, and test the judging process against manually reviewed examples to identify inconsistent evaluations.

These approaches provide a consistent way to evaluate both deterministic and qualitative tasks while making their limitations visible.

### 5. Cost and Performance Analysis

Aggregate the benchmark results to calculate:

- Accuracy by prompting strategy and task family
- Total and average token consumption
- Estimated cost per 100 tasks
- Average and percentile latency, where sufficient measurements are available
- Cost per additional correct answer
- Projected monthly cost at 100,000 requests

Monthly estimates should state their assumptions, including the expected distribution of task types, model pricing, and whether repeated model calls are included.

### 6. Quality-Cost Trade-off

Plot a Pareto frontier comparing accuracy against cost.

A strategy is Pareto-dominated when another strategy achieves at least as much accuracy for no greater cost, with a strict improvement in at least one of those dimensions.

This analysis helps identify the strategies that offer competitive quality-cost trade-offs instead of simply selecting the most accurate or least expensive option.

## Key Performance Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures how often the model produces an acceptable answer |
| Token usage | Measures prompt and response token consumption |
| Estimated cost | Quantifies the expected inference expense |
| Latency | Measures the time needed to produce a response |
| Cost per 100 tasks | Enables direct comparison of evaluation costs |
| Cost per additional correct answer | Measures the incremental expense associated with improved accuracy |
| Monthly projected cost | Estimates the financial impact at 100,000 requests |
| Failure distribution | Reveals common errors and task-specific weaknesses |

For the cost-per-additional-correct-answer metric, compare each strategy with the baseline:

**Incremental cost per additional correct answer**

`(Strategy cost - Baseline cost) / (Strategy correct answers - Baseline correct answers)`

This metric is meaningful when the strategy produces more correct answers than the baseline. If it does not, report the result separately rather than forcing a misleading value.

## Technology Stack

- **Python:** Evaluation orchestration and experiment logic
- **OpenAI API / Anthropic API:** LLM inference, depending on the configured provider
- **tiktoken:** Token counting for supported tokenization schemes
- **Pydantic:** Structured output schemas and validation
- **Pandas:** Benchmark results, aggregation, and analysis
- **Matplotlib / Seaborn:** Accuracy-cost comparisons and visualizations
- **JSONL:** Benchmark inputs and experiment records
- **Git & GitHub:** Version control and project documentation

Token counts and prices should be calculated using the appropriate model-specific configuration. Actual billing can differ from estimates, so projected costs should be treated as estimates rather than invoices.

## Expected Deliverables

The project produces the following artifacts:

1. **Evaluation harness:** A repeatable pipeline for executing and grading benchmark tasks.
2. **Comparative results:** A structured dataset containing output quality, token usage, latency, and cost.
3. **Accuracy versus cost visualization:** A Pareto frontier comparing prompting strategies.
4. **Failure taxonomy:** A categorized analysis of common errors, invalid outputs, and task-specific failure patterns.
5. **Production cost projection:** An estimate of the cost of serving 100,000 requests per month.
6. **Shipping recommendation:** A documented recommendation for each task family, supported by measured performance and explicit cost assumptions.

## Results and Findings

> Results will be added after the benchmark has been executed and validated.

### Strategy Comparison

| Strategy | Accuracy | Cost per 100 Tasks | Avg. Latency | Monthly Cost Projection |
|---|---:|---:|---:|---:|
| Baseline | TBD | TBD | TBD | TBD |
| Chain-of-Thought | TBD | TBD | TBD | TBD |
| Self-Consistency | TBD | TBD | TBD | TBD |
| Tree-of-Thought | TBD | TBD | TBD | TBD |

### Task-Level Recommendations

| Task Family | Recommended Strategy | Reason |
|---|---|---|
| Arithmetic reasoning | TBD | Based on measured accuracy, failure patterns, and incremental cost |
| Classification | TBD | Based on measured accuracy, latency, and cost |
| Information extraction | TBD | Based on schema validity, extraction accuracy, and cost |
| Open-ended judgment | TBD | Based on judge scores, qualitative review, and cost |

Replace these placeholders with actual results. Recommendations should follow the measured evidence, even when the baseline turns out to be the best option for a particular task.

## What This Project Demonstrates

This project demonstrates practical skills in:

- LLM application evaluation and benchmarking
- Prompt engineering and strategy comparison
- API integration and token-based cost estimation
- Structured output generation and validation
- Automated testing and quality assessment
- Data analysis and visualization
- Failure analysis and evidence-based decision-making
- Production cost modeling and technical recommendations

The focus is not simply on making an LLM produce better answers. It is on determining **when an improvement is worth paying for** and making that decision measurable.

## Future Improvements

- Evaluate additional models and compare their quality-cost trade-offs.
- Add repeated runs and confidence intervals to account for model variability.
- Expand the benchmark with more representative production tasks.
- Calibrate the LLM judge against human-reviewed samples.
- Introduce experiment versioning and regression checks for prompt changes.
- Build a lightweight dashboard to explore results by task family, model, and strategy.

## Project Status

In progress.

Final findings, visualizations, and production recommendations will be documented after the evaluation pipeline has been implemented and the benchmark results have been reviewed.
