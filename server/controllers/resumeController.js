import Resume from "../models/Resume.js";

export const createResume = async (req, res) => {
  try {
    const { title, personalInfo, skills, education, experience } = req.body;

    if (!title) {
      return res.status(400).json({
        message: "Resume title is required",
      });
    }

    const resume = await Resume.create({
      user: req.user._id,
      title,
      personalInfo,
      skills,
      education,
      experience,
    });

    res.status(201).json({
      message: "Resume created successfully",
      resume,
    });
  } catch (error) {
    res.status(500).json({
      message: "Could not create resume",
      error: error.message,
    });
  }
};

export const getMyResumes = async (req, res) => {
  try {
    const resumes = await Resume.find({
      user: req.user._id,
    }).sort({ createdAt: -1 });

    res.status(200).json({
      resumes,
    });
  } catch (error) {
    res.status(500).json({
      message: "Could not get resumes",
      error: error.message,
    });
  }
};

export const getResumeById = async (req, res) => {
  try {
    const resume = await Resume.findOne({
      _id: req.params.id,
      user: req.user._id,
    });

    if (!resume) {
      return res.status(404).json({
        message: "Resume not found",
      });
    }

    res.status(200).json({
      resume,
    });
  } catch (error) {
    res.status(500).json({
      message: "Could not get resume",
      error: error.message,
    });
  }
};

export const updateResume = async (req, res) => {
  try {
    const resume = await Resume.findOne({
      _id: req.params.id,
      user: req.user._id,
    });

    if (!resume) {
      return res.status(404).json({
        message: "Resume not found",
      });
    }

    const { title, personalInfo, skills, education, experience } = req.body;

    if (title !== undefined) resume.title = title;
    if (personalInfo !== undefined) resume.personalInfo = personalInfo;
    if (skills !== undefined) resume.skills = skills;
    if (education !== undefined) resume.education = education;
    if (experience !== undefined) resume.experience = experience;

    const updatedResume = await resume.save();

    res.status(200).json({
      message: "Resume updated successfully",
      resume: updatedResume,
    });
  } catch (error) {
    res.status(500).json({
      message: "Could not update resume",
      error: error.message,
    });
  }
};

export const deleteResume = async (req, res) => {
  try {
    const resume = await Resume.findOne({
      _id: req.params.id,
      user: req.user._id,
    });

    if (!resume) {
      return res.status(404).json({
        message: "Resume not found",
      });
    }

    await resume.deleteOne();

    res.status(200).json({
      message: "Resume deleted successfully",
    });
  } catch (error) {
    res.status(500).json({
      message: "Could not delete resume",
      error: error.message,
    });
  }
};