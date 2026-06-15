from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import markdown
import os

load_dotenv()

app = Flask(__name__)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/")
def home():
    return render_template("agent.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.form["message"]

    prompt = f"""
You are NayePankh AI Career & Volunteer Agent.

Answer in markdown format.

Use the following structure:

## Summary

## Detailed Explanation

## Key Points

## Real World Examples

## Next Steps

Question:
{message}
"""

    try:

        response = model.generate_content(prompt)

        formatted_response = markdown.markdown(
            response.text
        )

        return render_template(
            "agent.html",
            user_message=message,
            ai_response=formatted_response
        )

    except Exception as e:

        return render_template(
            "agent.html",
            ai_response=f"Error: {str(e)}"
        )


@app.route("/internship", methods=["POST"])
def internship():

    prompt = """
You are an Internship Advisor.

Answer in markdown format.

Use:

## Recommended Internships

## Why These Match

## Skills Required

## Career Benefits

## Next Steps
"""

    try:

        response = model.generate_content(prompt)

        formatted_response = markdown.markdown(
            response.text
        )

        return render_template(
            "agent.html",
            ai_response=formatted_response
        )

    except Exception as e:

        return render_template(
            "agent.html",
            ai_response=f"Error: {str(e)}"
        )


@app.route("/volunteer", methods=["POST"])
def volunteer():

    prompt = """
You are a Volunteer Coordinator.

Answer in markdown format.

Use:

## Volunteer Opportunities

## Responsibilities

## Benefits

## Skills You Will Learn

## Next Steps
"""

    try:

        response = model.generate_content(prompt)

        formatted_response = markdown.markdown(
            response.text
        )

        return render_template(
            "agent.html",
            ai_response=formatted_response
        )

    except Exception as e:

        return render_template(
            "agent.html",
            ai_response=f"Error: {str(e)}"
        )


@app.route("/roadmap", methods=["POST"])
def roadmap():

    prompt = """
Create a roadmap to become an AI Engineer.

Answer in markdown format.

Use:

## Goal

## Skills Required

## Learning Plan

## Projects

## Career Opportunities
"""

    try:

        response = model.generate_content(prompt)

        formatted_response = markdown.markdown(
            response.text
        )

        return render_template(
            "agent.html",
            ai_response=formatted_response
        )

    except Exception as e:

        return render_template(
            "agent.html",
            ai_response=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)