import mongoose from "mongoose";

const resumeSchema = new mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },

    title: {
      type: String,
      required: true,
      trim: true,
    },

    personalInfo: {
      fullName: String,
      email: String,
      phone: String,
      location: String,
      summary: String,
    },

    skills: [
      {
        type: String,
        trim: true,
      },
    ],

    education: [
      {
        school: String,
        degree: String,
        startYear: String,
        endYear: String,
      },
    ],

    experience: [
      {
        company: String,
        position: String,
        startDate: String,
        endDate: String,
        description: String,
      },
    ],
  },
  {
    timestamps: true,
  }
);

const Resume = mongoose.model("Resume", resumeSchema);

export default Resume;