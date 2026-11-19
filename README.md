# AI Interview Coach

An AI-powered interview coach built with Python and OpenAI. The application generates interview questions for experienced iOS developers, evaluates their answers, and provides structured scores and feedback.

This was my first AI application, built to gain hands-on experience with object-oriented programming (OOP), LLM integration, prompt engineering, and structured AI responses.

## Overview

AI Interview Coach simulates a technical interview through a command-line interface.

The application asks an interview question, accepts an answer from the candidate, and evaluates the response using an OpenAI language model. Each answer receives a clarity score, a correctness score, reasoning behind the evaluation, and feedback for the candidate.

The interview continues until the candidate chooses to exit.

## Features

- **AI-generated interview questions:** Generates short interview questions for experienced iOS developers using a predefined system prompt.
- **Question history:** Tracks previously asked questions during the session and includes them in subsequent prompts to discourage repetition.
- **Automated answer evaluation:** Evaluates candidate answers using an LLM.
- **Structured scoring:** Produces clarity and correctness scores on a scale of 1 to 5, along with reasoning and feedback.
- **OpenAI tool calling:** Uses a defined function tool to request structured evaluation data from the model.
- **Data validation:** Uses Pydantic to define the expected evaluation structure and enforce score boundaries.
- **API connection validation:** Checks OpenAI API connectivity during application startup.
- **Logging:** Writes application logs to a file and displays them in the terminal.
- **Environment-based configuration:** Loads the OpenAI API key from a local `.env` file.
- **Python project management:** Uses `uv` to manage the project environment, dependencies, and execution.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Application development |
| OpenAI API | Interview question generation and answer evaluation |
| GPT-4o mini | Language model used for the interview workflow |
| OpenAI Python SDK | API client and chat completion requests |
| Pydantic | Data modelling, JSON schema generation, and validation |
| python-dotenv | Loading environment variables |
| uv | Dependency and project management |
| Git and GitHub | Version control and source code hosting |

## Project Structure

```text
ai_interview_coach/
├── src/
│   └── ai_interview_coach/
│       ├── main.py
│       ├── openai_service.py
│       ├── interview_session.py
│       ├── scoring_tool.py
│       └── answer_score.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

The `logs/` directory and `app.log` file are created automatically when the application starts.

### Module Responsibilities

#### `main.py`

The main entry point of the application.

- Configures application logging.
- Loads environment variables.
- Initializes the OpenAI service.
- Validates the API connection.
- Runs the interactive interview loop.
- Collects candidate answers and displays evaluation results.

#### `openai_service.py`

Contains the `OpenAIService` class, which manages OpenAI client initialization and API connection validation.

It checks whether the API key is configured and validates connectivity by requesting the available model list.

#### `interview_session.py`

Contains the `InterviewSession` class, which manages the interview workflow.

Its responsibilities include generating interview questions, tracking previously asked questions, submitting answers for evaluation, and validating the resulting scores.

#### `scoring_tool.py`

Contains the `ScoringTool` class, which defines the OpenAI function-calling tool used to request a structured evaluation of candidate answers.

It uses the schema generated from the `AnswerScore` model.

#### `answer_score.py`

Contains the `AnswerScore` Pydantic model, which defines the expected evaluation fields and validates the clarity and correctness scores.

## How It Works

The application follows this workflow:

1. Loads environment variables from the `.env` file.
2. Configures logging and initializes the OpenAI client.
3. Validates the OpenAI API connection.
4. Generates an interview question based on the predefined system prompt.
5. Displays the question and accepts the candidate's answer.
6. Sends the question and answer to the LLM for evaluation.
7. Requests structured evaluation data through OpenAI function calling.
8. Validates the evaluation using the `AnswerScore` model.
9. Displays the scores, reasoning, and feedback.
10. Asks whether the candidate wants to continue the interview.

Enter `Y` to continue to another question. Any other response exits the application.

## Answer Evaluation

Each answer is evaluated using four fields.

| Field | Description |
|---|---|
| `reasoning` | Explains the reasoning behind the assigned scores, with a maximum of three sentences specified in the schema description |
| `clarity` | Rates how clearly the answer is expressed, from 1 to 5 |
| `correctness` | Rates the technical correctness of the answer, from 1 to 5 |
| `feedback` | Provides feedback on the candidate's answer, with a maximum of three sentences specified in the schema description |

The `AnswerScore` model uses Pydantic field constraints to enforce the valid score range.

The model's JSON schema is used to define the parameters of the scoring tool, keeping the expected evaluation structure consistent with the application's data model.

## Object-Oriented Programming

The application is organized into classes with separate responsibilities rather than placing the entire implementation in a single Python script.

The primary classes are:

- **`OpenAIService`:** Encapsulates OpenAI client initialization and API connection validation.
- **`InterviewSession`:** Manages the interview workflow, prompts, and question history.
- **`ScoringTool`:** Defines the tool schema used for structured answer evaluation.
- **`AnswerScore`:** Models and validates the evaluation data.

This separation demonstrates how OOP can help organize an AI application into distinct components with clearly defined responsibilities.

## Getting Started

### Prerequisites

Before running the application, ensure that you have:

- Python 3.13 or later.
- `uv` installed.
- An OpenAI API key with access to the configured model.

Install `uv` by following the official [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### 1. Clone the Repository

```bash
git clone https://github.com/saching11/ai_interview_coach.git
cd ai_interview_coach
```

### 2. Install Dependencies

Run the following command from the project root:

```bash
uv sync
```

This installs the project dependencies and prepares the Python environment using the project's configuration and lockfile.

### 3. Configure the API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your actual OpenAI API key.

The application loads the variable using `python-dotenv`.

**Important:** Keep your API key private. Do not commit your `.env` file to GitHub.

### 4. Run the Application

Execute the registered command from the project root:

```bash
uv run ai-interview-coach
```

The application validates the API connection before starting the interview.

## Example Interaction

The following is an illustrative example. Actual interview questions, scores, and feedback depend on the model's responses.

```text
Starting AI Interview Coach

What is the difference between a struct and a class in Swift?

Enter your answer
[Your answer here]

Answer check:
reasoning='The answer explains the main distinction...'
clarity=4
correctness=5
feedback='Good explanation. Consider discussing value and reference semantics...'

Do you want to continue
Y

[The next interview question is generated]
```

## Logging

The application creates a `logs/` directory and writes logs to:

```text
logs/app.log
```

Logs are also displayed in the terminal.

The logging configuration captures application events, including startup, OpenAI client initialization, API connection validation, and failures encountered during application setup.

## Scope and Limitations

- The application uses a command-line interface and does not include a web or mobile frontend.
- The interview prompt is predefined for experienced iOS developers.
- Question history is maintained in memory during the running session.
- Interview evaluations depend on the language model's responses.
- The application does not persist interview results between sessions.

## Project Status

**Completed ✅**

This was my first AI application, built to gain practical experience integrating an LLM into a Python application using object-oriented programming.

Through this project, I gained hands-on experience with:

- Integrating an external LLM API into a Python application.
- Writing system prompts for an AI-powered workflow.
- Using OpenAI function calling to request structured responses.
- Defining and validating data models with Pydantic.
- Separating application responsibilities using OOP.
- Managing Python dependencies and project execution with `uv`.
- Handling environment variables, API connectivity, and application logging.

The project represents my first completed step toward building practical AI-powered applications.

## Author

**Sachin Gotal**

GitHub: [@saching11](https://github.com/saching11)

Repository: [AI Interview Coach](https://github.com/saching11/ai_interview_coach)
