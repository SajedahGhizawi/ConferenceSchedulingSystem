from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# (Replace with your database connection and models)
sessions = [  # Sample data (replace with database interaction)
    {"title": "Machine Learning for Beginners", "time": "10:00 AM - 11:00 AM", "speaker": "John Doe"},
    {"title": "Building Scalable Web Applications", "time": "11:30 AM - 1:00 PM", "speaker": "Jane Smith"},
    {"title": "Deep Dive into Cybersecurity", "time": "2:00 PM - 3:00 PM", "speaker": "Michael Lee"},
]

@app.route("/")
def index():
    return render_template("index.html", sessions=sessions)

@app.route("/add_session", methods=["POST"])  # Example form submission route
def add_session():
    # Extract data from form (replace with actual form data access)
    title = request.form.get("title")
    time_slot = request.form.get("timeSlot")
    speaker = request.form.get("speaker")

    # (Implement validation and database interaction here)
    # Add the new session to your data store (e.g., database)

    # Update sessions list for rendering (temporary, replace with actual retrieval)
    sessions.append({"title": title, "time": time_slot, "speaker": speaker})

    return render_template("index.html", sessions=sessions)

@app.route("/export_sessions", methods=["GET"])
def export_sessions():
  """Exports the current list of sessions in JSON format."""
  return jsonify(sessions)

if __name__ == "__main__":
    app.run(debug=True)



