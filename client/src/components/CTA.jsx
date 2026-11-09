import { ArrowRight } from "lucide-react";

function CTA() {
  return (
    <section className="bg-slate-950 py-24">

      <div className="max-w-4xl mx-auto text-center px-6">

        <h2 className="text-5xl font-bold text-white">
          Ready to Improve Your Resume?
        </h2>

        <p className="text-slate-400 mt-6 text-lg">
          Upload your resume and get AI-powered insights in seconds.
        </p>

        <button className="mt-10 bg-blue-600 hover:bg-cyan-500 transition px-8 py-4 rounded-xl text-white font-semibold flex items-center gap-2 mx-auto">
          Get Started
          <ArrowRight size={20}/>
        </button>

      </div>

    </section>
  );
}

export default CTA;