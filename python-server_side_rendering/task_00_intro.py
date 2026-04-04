# task_00_intro.py

def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing values with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders in template
        personalized = template.replace("{name}", name)
        personalized = personalized.replace("{event_title}", event_title)
        personalized = personalized.replace("{event_date}", event_date)
        personalized = personalized.replace("{event_location}", event_location)

        # Write output file
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
