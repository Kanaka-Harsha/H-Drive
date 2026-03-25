# HS3 (H-Drive) 🚀
**A Secure, Serverless Cloud Storage Solution**

HS3 is a high-performance personal cloud storage application. It leverages a serverless architecture to provide seamless file management, including secure uploads, deletions, and metadata tracking.

## 🏗️ Architecture
The project is split into two main components:
* **Frontend:** A modern, reactive UI built with [Vite](https://vitejs.dev/).
* **Backend:** Serverless logic powered by [AWS Lambda](https://aws.amazon.com/lambda/) (Python) and [Amazon S3](https://aws.amazon.com/s3/).

## ✨ Key Features
* **Secure Authentication:** Managed via `userLogin.py`.
* **File Management:** Upload and delete files directly to/from S3.
* **Metadata Tracking:** Automatic metadata handling via specialized Lambda functions.
* **Automated Deployment:** Includes a `deploy.sh` script for rapid iteration.

## 🛠️ Tech Stack
* **Frontend:** JavaScript, Vite, CSS
* **Backend:** Python 3.x, Boto3 (AWS SDK)
* **Cloud:** AWS Lambda, S3, API Gateway

## 🚀 Getting Started

### Prerequisites
* Node.js (v18+)
* AWS CLI configured with appropriate permissions

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Kanaka-Harsha/HS3.git](https://github.com/Kanaka-Harsha/HS3.git)
   cd HS3
