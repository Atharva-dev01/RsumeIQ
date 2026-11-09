# RsumeIQ
# 🚀 ResumeIQ – AI-Powered ATS Resume Analyzer

ResumeIQ is an AI-powered resume analysis platform designed to help job seekers improve their resumes and increase their chances of getting shortlisted by recruiters.

The platform aims to analyze resumes, evaluate ATS compatibility, identify missing skills and provide intelligent suggestions to make resumes more effective.

## 🎯 Project Objective

Many candidates struggle to create resumes that meet Applicant Tracking System (ATS) requirements.

ResumeIQ aims to solve this problem by providing an easy-to-use platform where users can upload their resumes and receive useful insights to improve their job applications.

## ✨ Key Features

- **Modern UI:** Clean, professional and responsive user interface.
- **Resume Upload:** Interface for uploading resumes in PDF format.
- **AI Resume Analysis:** Planned intelligent resume evaluation.
- **ATS Score:** Planned resume compatibility scoring.
- **Skill Gap Detection:** Identify missing skills based on job requirements.
- **Improvement Suggestions:** Provide recommendations for better resumes.
- **User Authentication:** Login and registration functionality planned.
- **Dashboard:** Central place to manage resume analysis and results.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React.js | Frontend development |
| Vite | Development and build tool |
| Tailwind CSS | UI styling |
| React Router DOM | Navigation |
| Node.js | Backend runtime |
| Express.js | Backend framework |
| MongoDB Atlas | Cloud database |
| Mongoose | Database management |
| JWT | Authentication |
| Bcrypt.js | Password hashing |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
ResumeIQ/
│
├── client/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   └── Footer.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── UploadResume.jsx
│   │   │   └── Result.jsx
│   │   │
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   └── package.json
│
├── server/
│   ├── config/
│   │   └── db.js
│   ├── app.js
│   ├── server.js
│   ├── .env
│   └── package.json
│
└── README.md
```

## ⚙️ Installation & Setup

Follow these steps to run ResumeIQ locally.

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd ResumeIQ
```

### 2. Setup Frontend

```bash
cd client
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

### 3. Setup Backend

Open another terminal:

```bash
cd server
npm install
```

Create a `.env` file inside the server folder:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

Start the backend:

```bash
npm run dev
```

Backend runs at:

```text
http://localhost:5000
```

### 4. Database Configuration

- Create a MongoDB Atlas account.
- Create a database user.
- Configure your network access.
- Add your MongoDB connection string to the server `.env` file.

**Important:** Never upload your `.env` file, database password or JWT secret to GitHub.

## 📸 Project Screenshots

Screenshots of the application will be added here as development progresses.

## 🚧 Development Status

ResumeIQ is currently under development.

- [x] Frontend project setup
- [x] React routing and navigation
- [x] Homepage UI
- [x] Navbar and footer
- [x] Feature sections and hero section
- [x] Backend project setup
- [ ] Complete MongoDB integration
- [ ] User authentication
- [ ] Resume upload functionality
- [ ] AI-powered resume analysis
- [ ] ATS scoring system
- [ ] Results dashboard

## 🔮 Future Improvements

- AI-powered resume evaluation.
- Job description and resume matching.
- Advanced ATS compatibility analysis.
- Missing keyword recommendations.
- Resume improvement suggestions.
- Downloadable analysis reports.

## 👨‍💻 Developer

**Atharva Mangesh Pawar**

B.Tech – Computer Science Engineering

GitHub: [Atharva-dev01](https://github.com/Atharva-dev01)

---

⭐ If you find this project interesting, consider giving it a star!

**ResumeIQ – Build Better Resumes. Create Better Opportunities.** 🚀