# Cybersecurity Analysis Tool

## Project Overview
The Cybersecurity Analysis Tool is a Python-based project designed to analyze log files for potential security incidents such as failed login attempts, unauthorized access, and suspicious error messages.

This project demonstrates secure development practices using GitHub for version control and Freshworks for issue tracking.

---

## Project Structure

- main → Stable production branch
- development → Integration branch
- feature/* → Individual feature development branches

Example feature branches:
- feature/log-analysis
- feature/vulnerability-scan

---

## Requirements

- Python 3.x
- Git

---

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/YOUR_USERNAME/cybersecurity-analysis-tool.git

2. Navigate into the project folder:

   cd /c/Assignment5/cybersecurity-analysis-tool

---

## Running the Log Analysis Script

Ensure you have a log file (example: sample.log) in the project directory.

Run:

   python log_analysis.py

The script will:
- Detect suspicious log entries
- Identify failed login attempts
- Count repeated login attempts by IP address

---

## Version Control Workflow

1. Create a feature branch from main
2. Make changes
3. Commit with descriptive messages
4. Push to remote repository
5. Create a Pull Request for review

All commits reference Freshworks issue numbers when applicable.

---

## Security Guidelines

- No sensitive credentials should be committed.
- All features must be developed in isolated branches.
- Pull requests are required before merging.
- Commit messages must be clear and descriptive.
- Error handling must be implemented for reliability.
