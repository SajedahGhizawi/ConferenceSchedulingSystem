// Get references to DOM elements
const scheduleList = document.getElementById('schedule-list');
const dataForm = document.getElementById('data-form'); // Assuming your form has this ID
const exportButton = document.getElementById('export-sessions-btn');

// (Optional) Function to add a new session (replace with your form submission logic)
function addNewSession(formData) {
  // ... (existing code for adding a new session)
}

// (Optional) Attach event listener to form submission (replace with your logic)
if (dataForm) {
  dataForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const formData = new FormData(dataForm); // Assuming form uses FormData
    addNewSession(formData);
    // Clear form after submission (optional)
    dataForm.reset();
  });
}

// Add event listener to export button (optional for this approach)
if (exportButton) {
  exportButton.addEventListener('click', async () => {
    try {
      const response = await fetch('/export_sessions');
      if (!response.ok) {
        throw new Error(`Error exporting sessions: ${response.statusText}`);
      }
      const data = await response.json();
      console.log('Sessions exported successfully:', data);
      // Display success message to user (optional)
      alert('Sessions exported successfully! The data is available for download or use in your Gurobi code.');
    } catch (error) {
      console.error('Error exporting sessions:', error);
      // Display error message to user (optional)
      alert('Error exporting sessions. Please try again later.');
    }
  });
}
