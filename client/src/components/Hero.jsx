import { ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

function Hero() {
  return (
    <section className="relative min-h-[90vh] flex items-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white overflow-hidden">

      {/* Background Glow */}
      <div className="absolute top-20 left-10 w-72 h-72 bg-blue-600/20 rounded-full blur-3xl"></div>
      <div className="absolute bottom-20 right-10 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl"></div>

      <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center relative z-10">

        {/* Left Side */}
        <motion.div
          initial={{ opacity: 0, y: 60 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >

          {/* Badge */}
          <div className="inline-flex items-center gap-2 bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 px-4 py-2 rounded-full text-sm mb-6">
            🚀 Trusted by 10,000+ Students
          </div>

          {/* Small Heading */}
          <p className="text-cyan-400 font-semibold uppercase tracking-widest">
            AI Powered Resume Analyzer
          </p>

          {/* Main Heading */}
          <h1 className="text-5xl md:text-7xl font-extrabold mt-6 leading-tight">
            Land More
            <span className="text-cyan-400"> Interviews </span>
            with AI
          </h1>

          {/* Description */}
          <p className="text-slate-400 mt-8 text-lg leading-8 max-w-xl">
            Analyse your resume, improve your ATS score,
            identify missing skills, and receive AI-powered
            suggestions to increase your interview chances.
          </p>

          {/* Buttons */}
          <div className="flex flex-wrap gap-5 mt-10">

            <button className="bg-gradient-to-r from-blue-600 to-cyan-500 px-8 py-4 rounded-xl font-semibold flex items-center gap-2 shadow-lg hover:shadow-cyan-500/40 hover:scale-105 transition-all duration-300">

              Upload Resume

              <ArrowRight size={20} />

            </button>

            <button className="border border-slate-700 hover:border-cyan-400 px-8 py-4 rounded-xl transition duration-300 hover:bg-slate-800">
              Learn More
            </button>

          </div>

        </motion.div>

        {/* Right Side Card */}
        <motion.div
          initial={{ opacity: 0, x: 80 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 1 }}
          className="flex justify-center"
        >

          <div className="bg-slate-900 border border-slate-700 rounded-3xl p-8 w-full max-w-md shadow-2xl">

            <h2 className="text-2xl font-bold mb-6">
              Resume Report
            </h2>

            <div className="space-y-5">

              <div className="flex justify-between">
                <span>ATS Score</span>
                <span className="text-green-400 font-bold">
                  92%
                </span>
              </div>

              <div className="w-full bg-slate-700 rounded-full h-3">
                <div className="bg-gradient-to-r from-blue-500 to-cyan-400 h-3 rounded-full w-[92%]"></div>
              </div>

              <div className="flex justify-between">
                <span>Grammar</span>
                <span className="text-green-400">
                  Excellent
                </span>
              </div>

              <div className="flex justify-between">
                <span>Formatting</span>
                <span className="text-yellow-400">
                  Good
                </span>
              </div>

              <div className="flex justify-between">
                <span>Keywords</span>
                <span className="text-cyan-400">
                  18 Found
                </span>
              </div>

              <div className="flex justify-between">
                <span>Missing Skills</span>
                <span className="text-red-400">
                  3
                </span>
              </div>

            </div>

          </div>

        </motion.div>

      </div>

    </section>
  );
}

export default Hero;