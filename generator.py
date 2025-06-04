import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import yaml

# Parameters
weeks_per_year = 52
total_weeks = 4000
current_date = datetime.now()

def load_people_events(yaml_file):
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)

people = load_people_events("people.yaml")

for person, attributes in people.items():
    birth_date = datetime.fromisoformat(attributes[0]['birthdate'])
    events = attributes[1]['events']

    event_map = {}
    event_color = "red"
    for date_str, label in events.items():
        event_date = datetime.fromisoformat(date_str)
        week_index = (event_date - birth_date).days // 7
        if 0 <= week_index < total_weeks:
            event_map[week_index] = label

    # Calculate lived weeks
    weeks_lived = (current_date - birth_date).days // 7
    total_years = total_weeks // weeks_per_year

    # Grid and layout settings
    cell_spacing = 1.6
    square_size = 1

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 90))

    # Draw the grid
    birth_week_offset = birth_date.timetuple().tm_yday // 7

    for year in range(total_years):
        for week in range(weeks_per_year):
            idx = year * weeks_per_year + week

            if year == 0 and week < birth_week_offset:
                continue

            if idx >= total_weeks:
                break

            if idx in event_map:
                facecolor = event_color
            else:
                facecolor = 'black' if idx < weeks_lived else 'white'

            x = week * cell_spacing
            y = -year * cell_spacing
            rect = patches.Rectangle((x, y), square_size, -square_size,
                                     facecolor=facecolor, edgecolor=facecolor if facecolor != 'white' else 'black', linewidth=1.2)
            ax.add_patch(rect)
            if idx in event_map:
                row_center_x = weeks_per_year * cell_spacing + 2  # consistent offset beyond last column
                ax.text(row_center_x, y - 0.6, event_map[idx].upper(), fontsize=6, va='center', color='black', fontweight='bold')

    # Configure display
    ax.set_xlim(0, weeks_per_year * cell_spacing)
    ax.set_ylim(-total_years * cell_spacing, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Add legend with visual square
    legend_x, legend_y = 0, 3
    legend_box = patches.Rectangle((legend_x, legend_y), square_size, -square_size,
                                   facecolor='white', edgecolor='black', linewidth=1.2)
    ax.add_patch(legend_box)
    ax.text(legend_x + 1.5, legend_y - 0.5, "= 1 week", fontsize=16, va='center')

    # Save output
    person_name_safe = person.replace(" ", "_")
    output_path = f"{person_name_safe}_{total_weeks}_weeks.png"
    plt.savefig(output_path, bbox_inches='tight', dpi=300)