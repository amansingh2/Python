class SystemMonitor:
    def load_activity(self):
        return """Get the events from a source, to be processed."""

    def identify_events(self):
        """Parse the source raw data into events (domain objects)."""

    def stream_events(self):
        """Send the parsed events to an external agent."""

print((SystemMonitor().load_activity()))