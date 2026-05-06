def export_sideboard_guide(df, archetypes, file_name="sideboard_guide.txt"):
    sections = []

    for archetype in archetypes:
        in_cards = []
        out_cards = []

        for _, row in df.iterrows():
            card = row["Card"]

            value = row.get(archetype, "")

            if isinstance(value, str):
                value = value.strip()

            if value in ["+1", "+2", "+3", "+4"]:
                in_cards.append(f"{value} {card}")

            elif value in ["-1", "-2", "-3", "-4"]:
                out_cards.append(f"{value} {card}")

        section = []
        section.append(f"=== {archetype.upper()} ===\n")

        section.append("IN:")
        section.extend(in_cards if in_cards else ["(none)"])

        section.append("\nOUT:")
        section.extend(out_cards if out_cards else ["(none)"])

        sections.append("\n".join(section))

    output = "\n\n".join(sections)

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ Sideboard guide généré : {file_name}")