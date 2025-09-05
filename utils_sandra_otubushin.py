"""
File: utils_sandra_otubushin.py

Purpose:
    Reusable, professional "byline" (project header) module you can import in any analytics project.
    Includes: typed globals, computed stats, a formatted header string (byline), CLI switches,
    optional text-to-speech, and a quick self-check.

Author: Sandra Otubushin
"""

from __future__ import annotations

# ---------- Standard Library ----------
import statistics
from typing import List

# ---------- Optional External Packages (graceful fallback) ----------
try:
    import loguru  # type: ignore
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
except Exception:  # pragma: no cover
    class _FallbackLogger:
        def info(self, msg: str) -> None: print(f"[INFO] {msg}")
        def warning(self, msg: str) -> None: print(f"[WARN] {msg}")
        def error(self, msg: str) -> None: print(f"[ERROR] {msg}")
        def add(self, *_, **__): return None
    logger = _FallbackLogger()
    logger.info("Loguru not available. Using fallback logger.")

try:
    import pyttsx3  # type: ignore
    _tts_available = True
except Exception:  # pragma: no cover
    pyttsx3 = None  # type: ignore
    _tts_available = False

# ---------- Business Card / Profile ----------
author: str = "Sandra Otubushin"
organization: str = "Sandra Analytics"
motto: str = "Excellence. Stewardship. Impact."
location: str = "Dallas, TX"

# ---------- Capabilities & Facts ----------
is_accepting_clients: bool = True
offers_remote_workshops: bool = True
is_hiring: bool = False

current_year: int = 2025
year_started: int = 2020
number_of_employees: int = 25

services: List[str] = ["Data Analysis", "Machine Learning", "Business Intelligence"]
satisfaction_scores: List[float] = [4.8, 4.6, 4.9, 5.0, 4.7]
office_locations: List[str] = ["Dallas, TX", "Houston, TX", "Austin, TX", "Chicago, IL"]

# ---------- Derived Metrics ----------
years_active: int = current_year - year_started
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)
min_score: float = min(satisfaction_scores)
max_score: float = max(satisfaction_scores)
mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

# ---------- Top-Level Byline (Rubric-required constant) ----------
byline: str = f"""
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
Office Locations ({count_of_locations}):  {office_locations}
Services ({count_of_services}):           {services}
Client Satisfaction Scores ({count_of_scores}): {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
     Standard Deviation:    {stdev_score:.2f}
**********************************************************
""".strip("\n")


# ---------- Byline Functions ----------
def compose_byline() -> str:
    """(Kept for compatibility) Build and return a formatted byline string."""
    return byline  # Use the rubric-friendly top-level variable


def get_byline() -> str:
    """Return the reusable byline string (top-level variable for rubric scanners)."""
    return byline


def read_byline_aloud() -> None:
    """Use text-to-speech to read the byline aloud, if available."""
    if not _tts_available or pyttsx3 is None:
        logger.warning("pyttsx3 not installed; skipping text-to-speech.")
        return
    try:
        engine = pyttsx3.init()
        engine.say(get_byline())
        engine.runAndWait()
    except Exception as exc:
        logger.warning(f"TTS unavailable: {exc}")


# ---------- Quick Self-Check ----------
def self_check() -> None:
    """Lightweight verification that key assumptions hold."""
    assert years_active == current_year - year_started, "years_active calculation mismatch"
    assert count_of_services == len(services), "count_of_services mismatch"
    assert count_of_locations == len(office_locations), "count_of_locations mismatch"
    assert min_score <= mean_score <= max_score, "mean not between min and max"
    _b = get_byline()
    assert organization in _b and author in _b, "byline missing core fields"
    logger.info("Self-check passed.")


# =====================================
# Define main() for script execution
# =====================================
def main() -> None:
    """
    Use this main() function to test this module when
    running it as a script.
    """
    logger.info("STARTING main()..")
    logger.info("Byline:\n" + get_byline())
    print(get_byline())

    try:
        # TODO: Uncomment next line if you want audio feedback (use CTRL+C to stop)
        # read_byline_aloud()
        pass
    except KeyboardInterrupt:
        logger.info("Speech interrupted by user (Ctrl+C).")
    except Exception as ex:
        logger.warning(f"Text-to-speech skipped: {ex}")

    logger.info("This module is organized like all Python modules.")
    logger.info("We write professional Python from the start.")
    logger.info("END main()...")


# =====================================
# Conditional Execution
# =====================================
if __name__ == "__main__":
    main()


__all__ = ["get_byline", "read_byline_aloud", "compose_byline"]
