"""
File: utils_sandra_otubushin.py

Purpose: Reusable header/tagline module for analytics projects.

Description:
A short, first-week module to demonstrate key skills:
- declare basic variables (bool, int, str, list)
- compose a reusable f-string "tagline" (a formatted-string header block)
- expose a function named get_tagline() that can be imported into other modules
- run this file as a script via main() using the if __name__ == '__main__' pattern

Author: Sandra Otubushin
"""

# Standard library
import statistics

# External packages
import loguru
import pyttsx3  # type: ignore

# ---------------- Logger ----------------
logger = loguru.logger
logger.add(
    "project.log",
    level="INFO",
    rotation="100 KB",
    backtrace=False,
    diagnose=False,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
)
logger.info("Logger loaded.")

# ---------------- Globals ----------------
is_accepting_clients: bool = True
offers_remote_workshops: bool = True
is_hiring: bool = False

current_year: int = 2025
year_started: int = 2020
number_of_employees: int = 25

author: str = "Sandra Otubushin"
organization: str = "Sandra Analytics"
motto: str = "Excellence. Stewardship. Impact."
location: str = "Dallas, TX"

services: list[str] = ["Data Analysis", "Machine Learning", "Business Intelligence"]
satisfaction_scores: list[float] = [4.8, 4.6, 4.9, 5.0, 4.7]
office_locations: list[str] = ["Dallas, TX", "Houston, TX", "Austin, TX", "Chicago, IL"]

years_active: int = current_year - year_started
min_score: float = min(satisfaction_scores)
max_score: float = max(satisfaction_scores)
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)

mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

tagline: str = f"""
**********************************************************
{organization} — Project Header
**********************************************************
Author:                     {author}
Motto:                      {motto}
Primary Location:           {location}
Years Active:               {years_active} (since {year_started})
Accepting New Clients?:     {is_accepting_clients}
Currently Hiring?:          {is_hiring}
Remote Workshops?:          {offers_remote_workshops}
Employees:                  {number_of_employees}
Services ({count_of_services}):         {services}
Office Locations ({count_of_locations}): {office_locations}
Client Satisfaction Scores ({count_of_scores}): {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
     Standard Deviation:    {stdev_score:.2f}
**********************************************************
"""

def get_tagline() -> str:
    """Return the reusable tagline string."""
    return tagline

def read_tagline_aloud() -> None:
    """Use text-to-speech to read the tagline aloud."""
    engine = pyttsx3.init()
    if engine is not None:
        engine.say(tagline)
        engine.runAndWait()

def main() -> None:
    """Entry point when running as a script."""
    loguru.logger.info("STARTING main()..")
    loguru.logger.info("Tagline:\n" + get_tagline())
    try:
        # read_tagline_aloud()  # Uncomment for audio
        pass
    except KeyboardInterrupt:
        logger.info("Speech interrupted by user (Ctrl+C).")
    except Exception as ex:
        logger.warning(f"Text-to-speech skipped: {ex}")
    loguru.logger.info("END main()...")

if __name__ == "__main__":
    main()
