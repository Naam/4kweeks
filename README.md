# 4000 Weeks Poster Generator

This Python project generates vertical timeline posters representing an individual's life in weeks (up to 4000 weeks, roughly 76 years). Each week is represented by a small square, with specific life events highlighted in custom colors and labeled next to the corresponding row.

## What It Does

- Visualizes 4000 weeks of a person's life.
- Highlights past weeks in black.
- Allows life events (birth, marriage, etc.) to be annotated with colored squares and labels.
- Aligns the grid to start from the actual week of birth.
- Reads multiple people's configurations from a single YAML file and outputs one image per person.

---

## How to Use

### 1. Clone the repository

```bash
git clone git@github.com:Naam/4kweeks.git
cd 4kweeks
```

### 2. Create a Python virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```plain
matplotlib
pyyaml
```

### 4. Create your configuration file

Name it `people.yaml` and place it in the same directory. Here's the structure:

```yaml
john_doe:
  - birthdate: "1982-02-02"
  - events:
      "2000-02-02": "Officially an adult"
      "2011-07-07": "Married"
      "2015-02-19": "Child is born"

jane_smith:
  - birthdate: "1985-01-01"
  - events:
      "2003-06-01": "Graduated high school"
      "2010-09-15": "First job"
```

Name and birthdate are mandatory to align the grid and generate the file.
Events are optional but great for milestones and major events.

### 5. Run the generator

```bash
python generator.py
```

Each person in the config file will get a corresponding PNG image like:

```plain
john_doe_4000_weeks.png
jane_smith_4000_weeks.png
```

---

## Customization

- The colors for events are currently set to red globally but can be customized per event with small code changes.
- You can easily tweak cell spacing, fonts, and figure size in `generator.py`.

---

## Credits

This project was inspired by the ideas presented in Oliver Burkeman's book _Four Thousand Weeks: Time Management for Mortals_ — particularly the concept of visualizing a human lifespan in weeks to bring clarity and intentionality to how we use our time.

Design inspiration was also drawn from similar week-grid visualizations found online, including [waitbutwhy.com](https://waitbutwhy.com/2014/05/life-weeks.html) and various open-source projects exploring this theme.

This implementation is an original work designed to be flexible, customizable, and friendly to non-technical users through YAML configuration.
