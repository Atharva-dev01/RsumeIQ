import express from "express";
import { protect } from "../middleware/authMiddleware.js";
import {
  createResume,
  getMyResumes,
  getResumeById,
  updateResume,
  deleteResume,
} from "../controllers/resumeController.js";

const router = express.Router();

router.use(protect);

router.route("/")
  .post(createResume)
  .get(getMyResumes);

router.route("/:id")
  .get(getResumeById)
  .put(updateResume)
  .delete(deleteResume);

export default router;