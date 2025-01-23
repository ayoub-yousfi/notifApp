# Sending Scheduled Emails with Brevo using GitHub Actions

This project automates the sending of daily Dua emails at specific times (morning, midday, and midnight) using the Brevo (formerly Sendinblue) API and GitHub Actions for scheduling. Below is a guide on how to set up and use this repository.

## Prerequisites

1. **Brevo Account**: Ensure you have a Brevo account and generate an API key.
2. **GitHub Repository**: Create a GitHub repository to host your project.
3. **Python Installed**: The script uses Python 3.10. Make sure all dependencies are specified in the repository.

## Configuration

### Python Script
The `script.py` file contains the logic for determining the appropriate Dua and sending it via email using the Brevo API. Key parts of the script include:

- **Dynamic Dua Selection**: Sends a different Dua based on the time of day (morning, midday, midnight).
- **Email Payload**: Configures the sender and recipient details for the email.
- **API Request**: Sends the email using Brevo's transactional email endpoint.

### Environment Variables
The script relies on the `BREVO_KEY` environment variable for authentication. This key must be securely stored in GitHub Secrets.

### GitHub Actions Workflow
The workflow file (`.github/workflows/template.yml`) automates the execution of the Python script at scheduled times. It uses the `schedule` event to trigger the script.

## Steps to Set Up

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Add the Python Script
Add the provided `script.py` file to the root of your repository. This script handles sending emails via the Brevo API.

### 3. Set Up GitHub Secrets
Store your Brevo API key in GitHub Secrets:
1. Go to your repository on GitHub.
2. Navigate to **Settings** > **Secrets and variables** > **Actions**.
3. Click **New repository secret**.
4. Add a secret with the name `BREVO_KEY` and your Brevo API key as the value.

### 4. Configure the Workflow
Add the following workflow file to `.github/workflows/template.yml`:

### 5. Commit and Push
Commit the changes to your repository:
```bash
git add .
git commit -m "Add email script and GitHub Actions workflow"
git push origin main
```

### 6. Verify Workflow
Go to the **Actions** tab in your GitHub repository to ensure the workflow runs successfully at the scheduled times.

## Testing
To test the workflow:
1. Trigger the GitHub Action manually using the **Run workflow** button in the Actions tab.
2. Verify that the email is sent by checking the recipient's inbox and reviewing the logs in the Actions tab.

## Notes
- Ensure the sender email address used in the script is authorized in your Brevo account.
- Customize the Dua messages and email details as needed.
- You may notice that the schedule type isn't as precise as expected, but don't worry—it's not your fault. This is a limitation of GitHub Actions.

## Troubleshooting
- If the workflow fails, check the logs in the Actions tab for error messages.
- Ensure the `BREVO_KEY` is correctly set and has sufficient permissions for sending emails.
- Verify that all Python dependencies are installed successfully in the workflow.
