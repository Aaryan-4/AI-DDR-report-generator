import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
You are a building inspection expert.

Generate a Detailed Diagnostic Report (DDR).

Inspection Report Data:
{inspection_text}

Thermal Report Data:
{thermal_text}

Structure the report as:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
7. Missing Information

Rules:
- Do not invent facts
- If data missing write 'Not Available'
- Use clear client-friendly language
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content