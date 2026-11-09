import express from "express";
import cors from "cors";
import authRoutes from "./routes/authRoutes.js";
import resumeRoutes from "./routes/resumeRoutes.js";

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("ResumeIQ API is running");
});

app.use("/api/auth", authRoutes);
app.use("/api/resumes", resumeRoutes);

export default app;