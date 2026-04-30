import matplotlib.pyplot as plt


def generate_flowchart(player_progress):
    """
    Generates a flowchart-like plot showing player progress over time.
    Args:
        player_progress (list of tuples): A list where each tuple contains (timestamp, progress_value).
    """
    # Unzip the list of player progress into two separate lists
    timestamps, progress_values = zip(*player_progress)

    # Create a figure and axis
    plt.figure(figsize=(10, 6))

    # Plot player progress over time
    plt.plot(timestamps, progress_values, marker='o')

    # Title and labels
    plt.title('Player Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Progress Value')
    plt.xticks(rotation=45)
    plt.grid()

    # Show the flowchart
    plt.tight_layout()
    plt.show()