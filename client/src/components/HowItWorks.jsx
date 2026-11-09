import {
  Upload,
  ScanSearch,
  FileCheck2,
} from "lucide-react";

function HowItWorks() {

  const steps = [
    {
      icon: <Upload size={40} />,
      title: "Upload Resume",
      desc: "Upload your resume in PDF format.",
    },
    {
      icon: <ScanSearch size={40} />,
      title: "AI Analysis",
      desc: "Our AI scans your resume for ATS compatibility.",
    },
    {
      icon: <FileCheck2 size={40} />,
      title: "Improve Resume",
      desc: "Receive suggestions to improve your resume instantly.",
    },
  ];

  return (
    <section className="bg-slate-900 py-24">

      <div className="max-w-7xl mx-auto px-6">

        <h2 className="text-4xl font-bold text-center text-white">
          How ResumeIQ Works
        </h2>

        <div className="grid md:grid-cols-3 gap-8 mt-16">

          {steps.map((step, index) => (

            <div
              key={index}
              className="bg-slate-800 rounded-2xl p-8 text-center hover:scale-105 transition"
            >

              <div className="text-cyan-400 flex justify-center">
                {step.icon}
              </div>

              <h3 className="text-2xl text-white font-semibold mt-6">
                {step.title}
              </h3>

              <p className="text-slate-400 mt-4">
                {step.desc}
              </p>

            </div>

          ))}

        </div>

      </div>

    </section>
  );
}

export default HowItWorks;
