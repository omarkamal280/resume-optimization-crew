#!/usr/bin/env python
import sys
import warnings

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://jobs.siemens.com/careers?query=LLM&location=New%20Cairo%20City%2C%20Cairo%20Governorate%2C%20Egypt&pid=563156122872988&domain=siemens.com&sort_by=relevance&utm_source=j_c_global',
        'company_name': 'Siemens'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
