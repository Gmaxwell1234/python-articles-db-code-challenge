# python-articles-db-code-challenge
# Overview
A Python system modeling relationships between Authors, Articles, and Magazines using SQLite with:

-Proper database schema (1-to-many and many-to-many relationships)
-Raw SQL queries in Python classes
-Transaction handling
-Test coverage
# Setup
Install dependencies:
pip install pytest sqlite3
Initialize database:
python scripts/setup_db.py
# Run tests:
pytest
# Key Features
Class Key Methods

Author articles(), magazines(), add_article(), topic_areas()

Magazine articles(), contributors(), article_titles(), contributing_authors()

Article Relationship methods to connect authors and magazines

# Database Schema
See lib/db/schema.sql for:

Table definitions

Foreign key constraints

Performance indexes

# Testing
Run all tests:

pytest tests/