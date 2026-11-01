# Feature Brief: Autókölcsönző Rendszer [Fast-Path Brief]

**Status:** Approved  
**Author:** CASE | Package Creator  
**Date:** 2026-04-19  
**Approved by:** Czétényi Kristóf I62GFT
**Approval date:** 2026-04-19
**Brief ID:** FB-001

---

## Summary

Design and implement a simple car rental system in Python using object-oriented principles. The system allows users to rent a car for a day, cancel an existing rental, and list all active rentals. The application is a university graded project requiring a clean OOP class hierarchy, non-public attributes with accessors, input validation, error handling, a simple CLI interface, and pre-loaded seed data on startup.

---

## Problem Statement

A university OOP assignment requires a fully functional, self-contained Python car rental application. The assignment defines the class structure, required operations, and delivery constraints (public GitHub repository, Neptun submission, elevator pitch video). The student must deliver a working, runnable project that demonstrates OOP concepts including abstraction, encapsulation, inheritance, and error handling.

---

## User Persona

| Persona | Role | Relationship to Feature |
|---|---|---|
| Student / Developer | Implements and submits the project | Author and owner of the codebase |
| Course Instructor | Evaluates the submission by cloning and running it | Executor — runs the project from a fresh clone |
| End User (simulated) | Operates the CLI to rent, cancel, and list cars | Actor — interacts with the running application |

---

## Business Outcome

- A runnable Python application that passes the instructor's clone-and-run test.
- Demonstrates correct OOP principles: abstraction, encapsulation, inheritance.
- Submitted successfully by the deadline via Neptun with a public GitHub repository link.

> **Note:** These are success metrics (business observables). Acceptance criteria are defined by the Analyst in the PRD.

---

## Priority and Context

- **Priority:** High
- **Urgency:** Updated deadline — **2026-12-06 23:59:59**
- **Business context:** University graded assignment — "Kötelező project feladat" submitted via Neptun. Final grade depends on successful delivery and public GitHub submission.

---

## Functional Requirements

The following describe **what the system must be capable of** — not how or where it is implemented.

1. The system must define an abstract base class `Auto` with attributes for licence plate number (`rendszám`), type (`típus`), and daily rental rate (`bérleti díj`).
2. The system must provide a `Személyautó` (passenger car) subclass of `Auto` with the following specific attributes: passenger count (`utas_szam`), transmission type (`váltó`: manual/automatic), luggage compartment size (`csomagtartó_méret`), range (`hatótáv`).
3. The system must provide a `Teherautó` (truck) subclass of `Auto` with the following specific attributes: passenger count (`utas_szam`), weight limit (`teherbírás`), speed limit (`sebesség_korlát`), range (`hatótáv`).
4. The system must define an `Autókölcsönző` (rental company) class that holds a collection of cars and a company name attribute.
5. The system must define a `Bérlés` (rental) class that associates a specific car with a rental date (one day).
6. The system must allow a user to rent an available car for a specified date, and return the computed rental price.
7. The system must allow a user to cancel an existing rental.
8. The system must allow a user to list all current active rentals.
9. All class attributes must be non-public where possible; public getter and setter methods must be provided where access is required.
10. The system must apply input validation: verify that the chosen car is available for the requested date, and that the date is valid.
11. The system must ensure that only existing rentals can be cancelled.
12. The system must handle errors gracefully (invalid input, unavailable car, non-existent rental) and provide meaningful feedback to the user.
13. On startup, the system must pre-load one rental company instance containing 3 cars and 4 pre-existing rentals, so the user receives a ready-to-use system.
14. The system must provide an interactive CLI interface exposing three operations: rent a car, cancel a rental, list rentals. The interaction style must be a numbered menu (e.g., 1. Rent, 2. Cancel, 3. List, 0. Exit) using only the Python standard library — no third-party packages. The application must run from a fresh `git clone` with no additional installs.

---

## Non-Functional Requirements

1. The application must be implemented entirely in Python.
2. The project must be executable from a fresh `git clone` without any `pip install` or additional setup — the Python standard library only. No third-party packages are permitted.
3. The repository must be public on GitHub.
4. The codebase must demonstrate OOP principles: abstraction (abstract base class), encapsulation (non-public attributes), inheritance (subclasses of `Auto`).
5. Error handling must prevent the application from crashing on invalid or unexpected user input.

---

## Delivery Increments

| Increment | Scope | Description |
|---|---|---|
| **MVP 1** | Class hierarchy | Define `Auto` (abstract), `Személyautó`, `Teherautó`, `Bérlés`, `Autókölcsönző` with non-public attributes and accessors |
| **MVP 2** | Core operations | Implement rent, cancel, and list-rentals logic with validation and error handling |
| **MVP 3** | CLI + seed data | Build the CLI interface and pre-load the startup dataset (1 company, 3 cars, 4 rentals) |
| **MVP 4** | Delivery prep | Verify public GitHub repo, confirm clone-and-run, create `NEPTUNKOD.docx`, upload the elevator-pitch video to GitHub |

---

## Known Future Extensions

| Extension | Notes |
|---|---|
| Multi-day rentals | Currently scoped to single-day only — date range support is a known potential extension |
| Persistence (file/DB) | Seed data is in-memory only — future versions may require saving state |
| Web or GUI interface | CLI-only now; a richer interface could be added later |

---

## Known Constraints

- Language: Python only.
- Rental duration: one day per rental (fixed scope).
- Submission: public GitHub repository + `NEPTUNKOD.docx` file uploaded to Neptun.
- Updated deadline communicated: **2026-12-06 23:59:59**.
- Verifiability: the instructor will clone the repo and run it in PyCharm — it must start without errors.
- Video: a 2–3 minute elevator pitch video demonstrating the running project is required and must be uploaded to GitHub.

---

## Out of Scope

- Database or file-based persistence.
- User authentication or multi-user support.
- Web, desktop GUI, or API interface.
- Multi-day or date-range rentals.
- Payment processing.
- Fleet management beyond the 3 pre-loaded cars.

---

## Open Questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | What is the student's Neptun code? (Required for `NEPTUNKOD.docx`) | Student | **Closed** — `I62GFT` |
| 2 | Are there specific attributes defined for `Személyautó` and `Teherautó` beyond the base class? | Student | **Closed** — See FR-2 and FR-3 |
| 3 | Should the CLI use numbered menus or another interaction style? | Student | **Closed** — Arrow-key navigable menu preferred; numbered menu as fallback |

## Confirmed Answers

- **Neptun code:** `I62GFT` → `NEPTUNKOD.docx` must contain the public GitHub repository URL.
- **`Személyautó` attributes:** passenger count, transmission (manual/automatic), luggage compartment size, range.
- **`Teherautó` attributes:** passenger count, weight limit, speed limit, range.
- **CLI style:** Numbered menu only (`1/2/3/0`). No third-party libraries — standard library exclusively. Must run from a fresh clone without any `pip install`.
